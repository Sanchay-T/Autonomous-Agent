import openai
from dotenv import load_dotenv
import os

load_dotenv(".env")

# Replace this with your OpenAI API key
# openai.api_key = "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"
print(os.getenv("OPENAI_API_KEY"))
conversation_summary = None
def openai_chat_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=conversation,
    )
    return response.choices[0].message["content"]

def is_conversation_over(response):
    ending_phrases = ["thank you", "you're welcome", "glad I could help", "anything else", "all set", "no problem"]
    return any(phrase in response.lower() for phrase in ending_phrases)

def main():
    global conversation_summary
    conversation = [{
        "role": "system",
        "content": ("You are an advanced assistant with expertise in various fields. When responding to user queries, "
                    "present yourself as a professional expert in the field related to the query. Before providing a solution, "
                    "ask clarifying questions to ensure a complete understanding of the user's query and ask one question at a time, make conversations with the user. Engage in a meaningful "
                    "conversation by asking follow-up questions related to the user's query. Once you have a clear understanding "
                    "of the query, provide detailed answers, support, and clarifications. Maintain the context of the conversation, "
                    "and at the end, provide a concise summary suitable as a goal and prompt for another agent. Ensure "
                    "professionalism, clarity, and interactivity in all interactions.After the end of every responce ask anything that you can help with?")
    }]

    print("Hello! I'm here to help. We'll have a conversation, and I'll provide a summary once we're done.")
    while True:
        user_input = input("User: ")
        conversation.append({"role": "user", "content": user_input})
        response = openai_chat_response(conversation)
        conversation.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")
        if is_conversation_over(response):
            break

    summary_request = ("From the perspective of the user, kindly provide a succinct yet comprehensive summary of the "
                       "conversation. Be sure to accurately capture the primary queries, concerns, or issues raised "
                       "by the user. Identify any outstanding matters that may require further attention or "
                       "resolution. Offer well-considered recommendations for potential next steps or courses of "
                       "action that align with the user's needs. Ensure that the summary is both clear and "
                       "actionable, fostering a seamless transition for any subsequent discussions or engagements.")
    conversation.append({"role": "user", "content": summary_request})
    summary = openai_chat_response(conversation)
    print(f"\nSummary of the conversation:\n{summary}")
    conversation_summary = summary
    return summary


def conversation_initiate():
    conversation = [{
        "role": "system",
        "content": ("""
I want you to become my Expert Prompt Creator. Your goal is to help me craft the best possible prompt for my needs. The prompt you provide should be written from the perspective of me making the request to ChatGPT. Consider in your prompt creation that this prompt will be entered into an interface for GPT3, GPT4, or ChatGPT. The prompt will include instructions to write the output using my communication style.

The process is as follows:

You will generate the following sections:

Prompt:

In your second response, provide the best possible prompt according to my request and the answers I provided to your questions.
Summarize my prior messages to you and provide them as examples of my communication style.
You prompt output should contain the prefix `Prompt: ` followed by the prompt you created.

Questions:

In your first response, ask any questions pertaining to what additional information is needed from me to improve the prompt (up to two questions). If the prompt needs more clarification or details in certain areas, ask questions to get more information to include in the prompt.

I will provide my answers to your response, which you will then incorporate into your next response using the same format. However, you will ask questions only once. After that, you will generate a prompt based on the information available without asking further questions.

Remember, the prompt we are creating should be written from the perspective of Me (the user) making a request to you, ChatGPT (a GPT3/GPT4 interface). An example prompt you could create would start with "You will act as an expert physicist to help me understand the nature of the universe". Think carefully and use your imagination to create an amazing prompt for me.

Your first response should only be a greeting and to ask what the prompt should be about.
                    
At the end of every conversation add "If you have gif in the documentation then use that gif for explanation
""")
}]

    return conversation

def conversation_continue(conversation , user_input):
    conversation.append({"role": "user", "content": user_input})
    response = openai_chat_response(conversation)
    conversation.append({"role": "assistant", "content": response})
    print(f"Assistant: {response}")
    # if is_conversation_over(response):
        # todo
        # return response , conversation
        # pass
    return response , conversation


def summary_request(conversation):
    summary_request = ("From the perspective of the user, kindly provide a succinct yet comprehensive summary of the "
                       "conversation. Be sure to accurately capture the primary queries, concerns, or issues raised "
                       "by the user. Identify any outstanding matters that may require further attention or "
                       "resolution. Offer well-considered recommendations for potential next steps or courses of "
                       "action that align with the user's needs. Ensure that the summary is both clear and "
                       "actionable, fostering a seamless transition for any subsequent discussions or engagements.")
    conversation.append({"role": "user", "content": summary_request})
    summary = openai_chat_response(conversation)
    print(f"\nSummary of the conversation:\n{summary}")
    return summary


    # Use the conversation_summary in the next code
