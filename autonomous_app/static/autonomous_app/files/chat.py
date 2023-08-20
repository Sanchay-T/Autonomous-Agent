import openai

# Replace this with your OpenAI API key
openai.api_key = "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"
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

def get_summary():
    global conversation_summary
    return conversation_summary

if __name__ == "__main__":
    conversation_summary = main()

    # Use the conversation_summary in the next code
