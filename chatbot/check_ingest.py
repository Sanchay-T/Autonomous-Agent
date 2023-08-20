from ingest import *
import os



# Define your test parameters
docs_dir = "/Users/sanchaythalnerkar/Documents/AI Projects/SuperAGI/chatbot/documents"
vector_store_path = "/Users/sanchaythalnerkar/Documents/AI Projects/SuperAGI/chatbot/vector_store"
wandb_project = "AI Agents Hackathon"
prompt_file = "/Users/sanchaythalnerkar/Documents/AI Projects/SuperAGI/chatbot/chat_prompt.json"



documents, vector_store = ingest_data(docs_dir, vector_store_path, wandb_project, prompt_file)


# You can print or log the results to check them
print("Documents:", documents[0].page_content)
print("Vector store:", vector_store)