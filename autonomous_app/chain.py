"""This module contains functions for loading a ConversationalRetrievalChain"""

import logging

import wandb
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma , Qdrant
from langchain.embeddings import OpenAIEmbeddings
from .prompts import load_chat_prompt
import os
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings

load_dotenv(".env")

url="https://c48daa38-a7a7-4c89-9cd9-718a1461e4ae.us-east-1-0.aws.cloud.qdrant.io:6333"
# url = "https://fa1dffb4-23bf-4b57-8cc2-730c85ead277.us-east-1-0.aws.cloud.qdrant.io:6333"
api_key_q = "2N5Wlg_y2xwgtJu0Iq5T5uHyesdewC3Vy-VX31YAq-laiQO1tCxAkg"

api_key = os.getenv("OPENAI_API_KEY")
logger = logging.getLogger(__name__)
def load_vector_store(documents) -> Qdrant:

    embedding_function = OpenAIEmbeddings(openai_api_key=api_key)


    # user_vector_store_path = os.path.join(vector_store_path, user_key)


    # vector_store = Chroma.from_documents(
    #     documents=documents,
    #     embedding=embedding_function,
    #     persist_directory=vector_store_path,
    # )
    #
    # return vector_store

    vector_store = Qdrant.from_documents(
        documents=documents,
        embedding=embedding_function,
        url=url,
        prefer_grpc=False,
        api_key=api_key_q,
        force_recreate=True,
        collection_name="my_documents",
    )
    return vector_store







def load_chain(vector_store: Qdrant, openai_api_key: str):
    """Load a ConversationalQA chain from a config and a vector store
    Args:
        wandb_run (wandb.run): An active Weights & Biases run
        vector_store (Chroma): A Chroma vector store object
        openai_api_key (str): The OpenAI API key to use for embedding
    Returns:
        ConversationalRetrievalChain: A ConversationalRetrievalChain object
    """

    retriever = vector_store.as_retriever(search_type="mmr")
    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model_name='gpt-3.5-turbo-16k-0613',
        temperature=0,
    )
    chat_prompt_dir = os.path.join("autonomous_app", "chat_prompt.json")
    print("Chat prompt dir " , chat_prompt_dir)
    qa_prompt = load_chat_prompt(chat_prompt_dir)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
        return_source_documents=True,
    )
    return qa_chain


def get_answer(
    chain: ConversationalRetrievalChain,
    question: str,
    chat_history: list[tuple[str, str]],
):
    """Get an answer from a ConversationalRetrievalChain
    Args:
        chain (ConversationalRetrievalChain): A ConversationalRetrievalChain object
        question (str): The question to ask
        chat_history (list[tuple[str, str]]): A list of tuples of (question, answer)
    Returns:
        str: The answer to the question
    """
    result = chain(
        inputs={"question": question, "chat_history": chat_history},
        return_only_outputs=True,
    )
    response = result['answer']
    return response