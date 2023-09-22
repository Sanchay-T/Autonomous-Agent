from types import SimpleNamespace

LANGCHAIN_WANDB_TRACING = "true"

TEAM = None
PROJECT = "AI Agents Hackathon"
JOB_TYPE = "production"

default_config = SimpleNamespace(
    project=PROJECT,
    entity=TEAM,
    job_type=JOB_TYPE,
    chat_prompt_artifact="zestt/AI Agents Hackathon/chat_prompt:latest",
    chat_temperature=0,
    max_fallback_retries=1,
    model_name="gpt-3.5-turbo-16k",
    eval_model="gpt-3.5-turbo-16k",
    eval_artifact="zestt/AI Agents Hackathon/generated_examples:v0"
)

# vector_store_artifact="zestt/AI Agents Hackathon/vector_store:latest",