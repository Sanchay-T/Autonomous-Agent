import json
import logging
import pathlib
from typing import List, Tuple
from langchain.text_splitter import CharacterTextSplitter
import langchain
import wandb
from langchain.cache import SQLiteCache
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import TextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings


langchain.llm_cache = SQLiteCache(database_path="llm_cache.db")
logger = logging.getLogger(__name__)
api_key = "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"

def ingest_data(docs_dir:str, chunk_size:int, chunk_overlap:int, vector_store_path:str, wandb_project:str, prompt_file:str):
    
    # Load the documents
    documents = load_documents(docs_dir)
    
    # Split the documents into chunks
    chunked_documents = chunk_documents(documents, chunk_size, chunk_overlap)
    
    # Create the vector store with the chunked documents
    vector_store = create_vector_store(chunked_documents, vector_store_path)
    return documents, vector_store

def load_documents(data_dir:str) -> List[Document]:
    md_files = list(map(str, pathlib.Path(data_dir).glob("*.md")))
    documents = [
        TextLoader(file_path=file_path , encoding="utf8").load()[0] for file_path in md_files
    ]    
    return documents

def chunk_documents(
    documents: List[Document], chunk_size: int = 500, chunk_overlap=0
) -> List[Document]:
    """Split documents into chunks

    Args:
        documents (List[Document]): A list of documents to split into chunks
        chunk_size (int, optional): The size of each chunk. Defaults to 500.
        chunk_overlap (int, optional): The number of tokens to overlap between chunks. Defaults to 0.

    Returns:
        List[Document]: A list of chunked documents.
    """
    markdown_text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    split_documents = markdown_text_splitter.split_documents(documents)
    return split_documents

def create_vector_store(documents, vector_store_path:str) -> Chroma:

    model_name = "BAAI/bge-small-en"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings_function = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    user_vector_store_path = os.path.join(vector_store_base_path, user_key)


    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings_function,
        persist_directory=vector_store_path
    )
    vector_store.persist()
    return vector_store

def log_prompt(prompt:dict, run:wandb.run , unique_user_key):
    prompt_artifact = wandb.Artifact(name="chat_prompt", type="prompt")
    with prompt_artifact.new_file("prompt.json") as f:
        f.write(json.dumps(prompt))
    run.log_artifact(prompt_artifact)

def log_dataset(documents:List[Document], run:wandb.run , unique_user_key):
    document_artifact = wandb.Artifact(name="documentation_dataset", type="dataset")
    with document_artifact.new_file("document.json") as f:
        for document in documents:
            f.write(document.json() + "\n")
    run.log_artifact(document_artifact)

def log_index(vector_store_dir:str, run:wandb.run , unique_user_key):
    index_artifact = wandb.Artifact(name="vector_store", type="search_index")
    index_artifact.add_dir(vector_store_dir)
    run.log_artifact(index_artifact)
    

def ingest_and_log_data(
        unique_user_key: str,
        docs_dir: str = "/Users/ayusi/OneDrive/Desktop/Hackathon-Projects/Autonomous Agent/autonomous_app/documents",
        chunk_size: int = 600,
        chunk_overlap: int = 200,
        vector_store_path: str = "/Users/ayusi/OneDrive/Desktop/Hackathon-Projects/Autonomous Agent/autonomous_app/vector_store",
        prompt_file_path: str = "/Users/ayusi/OneDrive/Desktop/Hackathon-Projects/Autonomous Agent/autonomous_app/chat_prompt.json",
        wandb_project: str = "AI Agents Hackathon",
    ):
    """
    Ingest documentation data, create a vector store, and log artifacts to W&B.
    Designed to be used within a Django context.
    """
    run = wandb.init(project=wandb_project)  # Move the wandb initialization to this function

    # Ingest data
    documents, vector_store = ingest_data(
        docs_dir=docs_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        vector_store_path=vector_store_path,
        wandb_project=wandb_project,
        prompt_file=prompt_file_path
    )

    # Log data to wandb
    log_dataset(documents, run , unique_user_key=unique_user_key)
    log_index(vector_store_path, run , unique_user_key=unique_user_key)
    
    with open(prompt_file_path, 'r') as f:
        prompt_data = json.load(f)
    log_prompt(prompt_data, run , unique_user_key=unique_user_key)

    # Finish the wandb run
    run.finish()

if __name__ == "__main__":
    # Call the function only when this module is run as a script
    ingest_and_log_data("ayushi")
