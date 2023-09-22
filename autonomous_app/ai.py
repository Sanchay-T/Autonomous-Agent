import os
from types import SimpleNamespace

import gradio as gr
import wandb
from .chain import get_answer, load_chain, load_vector_store
from .ingest import load_documents , chunk_documents

from dotenv import load_dotenv

doc_dir = os.path.join("documents" , "iteration_1")


load_dotenv(".env")



class Chat:
    """A chatbot interface that persists the vectorstore and chain between calls."""

    def __init__(
        self,
        config: SimpleNamespace,
    ):
        """Initialize the chatbot.
        Args:
            config (SimpleNamespace): The configuration.
        """
        self.config = config
        self.wandb_run = wandb.init(
            project=self.config.project,
            entity=self.config.entity,
            job_type=self.config.job_type,
            config=self.config,
        )
        self.vector_store = None
        self.chain = None

    def __call__(
        self,
        question: str,
        history: list[tuple[str, str]] | None = None,
        openai_api_key: str = None,
    ):
        """
        Args:
            question (str): The question to answer.
            history (list[tuple[str, str]] | None, optional): The chat history. Defaults to None.
            openai_api_key (str, optional): The OpenAI API key. Defaults to None.
        Returns:
            list[tuple[str, str]], list[tuple[str, str]]: The chat history before and after the question is answered.
        """
        if openai_api_key is not None:
            openai_key = openai_api_key
        elif os.getenv("OPENAI_API_KEY"):
            openai_key = os.getenv("OPENAI_API_KEY")
        else:
            raise ValueError(
                "Please provide your OpenAI API key as an argument or set the OPENAI_API_KEY environment variable"
            )

        if self.vector_store is None:

            docs = load_documents(doc_dir)
            # print("AI DOCS " , docs)
            chunks = chunk_documents(docs, chunk_size=600, chunk_overlap=200)

            self.vector_store = load_vector_store(chunks)
            
        if self.chain is None:
            self.chain = load_chain(self.vector_store, openai_api_key=openai_key)

        history = history or []
        question = question.lower()
        response = get_answer(
            chain=self.chain,
            question=question,
            chat_history=history,
        )

        final_res = f"Answer:\t{response}"
        history.append((question, final_res))
        return response, history