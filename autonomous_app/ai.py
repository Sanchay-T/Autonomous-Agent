import os
from types import SimpleNamespace

import gradio as gr
import wandb
from .chain import get_answer, load_chain, load_vector_store

from dotenv import load_dotenv

load_dotenv(".env")


print("Openai key " , os.getenv("OPENAI_API_KEY"))

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
            self.vector_store = load_vector_store(
                wandb_run=self.wandb_run,
            )
            
        if self.chain is None:
            self.chain = load_chain(
                self.wandb_run, self.vector_store, openai_api_key=openai_key
            )

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