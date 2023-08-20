from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse, JsonResponse
import random
from .ai import Chat
from .config import default_config
import os

from dotenv import load_dotenv

load_dotenv(".env")


# open_api_key = 
# print("Openai key " , os.getenv("OPENAI_API_KEY"))


# Create your views here.

@xframe_options_exempt
def base(request):
    return render(request , "base.html")

def bard(request):
    return render(request , "bard_chat.html")

@xframe_options_exempt
def gpt_chat(request):
    return render(request , "chat.html")


responses = [
    "Thank you for your message. Our team will get back to you soon.",
    "Your message has been received. We'll respond shortly.",
    "We appreciate your feedback. Our team will review it.",
    "Your input has been noted. Expect a reply from us soon.",
]


chat = Chat(config=default_config)

def bot_response(request):
    if request.method == 'POST':
        query = request.POST.get('message', '')

        prev_chat_history = request.session.get('chat_history', [])


        list_of_tuples = [tuple(item) for item in prev_chat_history]
        print("\n\nPrev chat history: " , list_of_tuples)
        print("\n\n")

        # bot_response = "Thank you for your message. Our team will get back to you soon."
        bot_response_ , updated_chat_history = chat(question = query , history = list_of_tuples)

        request.session['chat_history'] = updated_chat_history

        print("\n\n\nBot history: " , updated_chat_history)
        print("\n\n")

        # bot_response = random.choice(responses)

        return JsonResponse({'message': bot_response_})

    return JsonResponse({'message': 'Invalid request'}, status=400)