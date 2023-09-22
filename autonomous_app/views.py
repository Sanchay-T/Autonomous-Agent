from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse, JsonResponse , FileResponse
import random
from .ai import Chat
from .config import default_config
import os
from .models import *
import re
import hashlib
from django.core.files.uploadedfile import InMemoryUploadedFile

from .pdf2markdown import convert_and_save

from .utils import *
from .ingest import ingest_and_log_data
import json

from .html2markdown import url_to_doc

email = "example@example.com"

from dotenv import load_dotenv

load_dotenv(".env")

from autonomous_app.chat import conversation_initiate, conversation_continue , summary_request

conversation_stack = conversation_initiate()


# open_api_key = 
# print("Openai key " , os.getenv("OPENAI_API_KEY"))


# Create your views here.

def landing(request):
    return render(request , "landing.html")

def bard(request):
    return render(request , "bard_chat.html")

@xframe_options_exempt
def gpt_chat(request , cb_key):
    return render(request , "chat.html" , context={'cb_key' : cb_key})


def email_data_post(request):

    if request.method == "POST":

        email = request.POST.get('email' , '')


        unique_key = hashlib.sha256(email.encode()).hexdigest()

        if(Business.objects.filter(email = email).exists()):
            business = Business.objects.get(email = email)
            request.session['anonymous_id'] = business.id
            print("\nEmail already exists\n")
            return JsonResponse({'message': "Email already exists" , 'user_id' : business.id})

        business = Business.objects.create(email = email , key = unique_key)

        print("Setting session")
        request.session['anonymous_id'] = business.id


        print("\n\n\nEmail: " , email)

        # generate key ans save in models 



        return JsonResponse({'message': "Email successfully generated." , 'user_id' : business.id})
    



def generate_business_data(request):

    context = None

    if request.session.get('anonymous_id'):


        print("Present...")

        context = {'user_id' : request.session.get('anonymous_id')}


    return render(request , "generate_business_data.html" , context=context)


responses = [
    "Thank you for your message. Our team will get back to you soon.",
    "Your message has been received. We'll respond shortly.",
    "We appreciate your feedback. Our team will review it.",
    "Your input has been noted. Expect a reply from us soon.",
]


chat = Chat(config=default_config)

@csrf_exempt
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

def url_data_post(request):

    if request.method == "POST":
        url = request.POST.get('url', '')
        op = False
        if url:
            try:
                op = url_to_doc(url)
            except Exception as e:
                print(e)

            if op:
                return JsonResponse({'message': "URL Scraped Successfully."})
            else:
                return JsonResponse({'message': "Not a Valid URL."} , status=400)
            
        



def business_data_post(request):

    end = False
    if request.method == 'POST':
        query = request.POST.get('user_id', '')
        question = request.POST.get('message', '')
        end_of_talk = request.POST.get('end_of_talk', '')
        start_of_talk = request.POST.get('start_of_talk', '')


        if start_of_talk:
            busi_chat_hist = BusinessChatHistory(business_id = query)
            if busi_chat_hist and busi_chat_hist.chat_history:
                request.session['business_chat_history'] = json.loads(busi_chat_hist.chat_history)
            else:
                request.session['business_chat_history'] = conversation_stack

            
        prev_chat_history = request.session.get('business_chat_history', [])

        # list_of_dicts = [tuple(item) for item in prev_chat_history]
        # print("\n\nPrev chat history: " , list_of_tuples)
        # print("\n\n")

        # bot_response = "Thank you for your message. Our team will get back to you soon."
        bot_response_ , updated_chat_history = conversation_continue(conversation=prev_chat_history , user_input=question)

        request.session['business_chat_history'] = updated_chat_history



        match = re.search(r'Prompt:\s*', bot_response_)

        # Search for the pattern in the example text
        print("\n\n\nBot response: " , bot_response_)
        print("\n\n\n")


        
        pattern = r'Prompt:\s*(.*)'
        match = re.search(pattern, bot_response_, re.DOTALL)
     

        if match:
            end = True
            extracted_text = match.group(1).strip()
            print(extracted_text)  
            busi_chat_hist = BusinessChatHistory(business_id = query)
            busi_chat_hist.chat_history = json.dumps(updated_chat_history)
            busi_chat_hist.save()


            new_prompt = extracted_text + "\n\n" + "CONTEXT\\n{context}\\n================\\nGiven the context information and not prior knowledge, answer the question."
            # save in chat_prompt.json 
            prompt_json = {"system_template": new_prompt, "human_template": "{question}\\n================\\nFinal Answer in Markdown:"}

            # open chat_prompt.json and add the prompt
            chat_prompt_path = os.path.join("autonomous_app", "chat_prompt.json")
            with open(chat_prompt_path, "w") as f:
                # i want to write to this file 
                f.write(json.dumps(prompt_json))

            f.close()

            busi_summary = BusinessSummary(business_id = query)
            busi_summary.summary = extracted_text
            busi_summary.save()

            request.session['business_chat_history'] = conversation_stack

            request.session.modified = True


            # say ression to update 




        print("\n\n\nBot history: " , updated_chat_history)
        print("\n\n")

        # bot_response = random.choice(responses)

        return JsonResponse({'message': bot_response_ , 'end_of_talk' : end})

    return JsonResponse({'message': 'Invalid request'}, status=400)



def file_upload(request):

    if request.method == "POST":

        user_id = request.POST.get('user_id', '')

        file = request.FILES.get('file')

        print("\n\n\n Uploaded File: " , file)


        # file_content = file.read()




        # try:
        #     convert_and_save(temp_file_path , user_id)
        #     return JsonResponse({'message': "File uploaded successfully."})
        # except:
        #     return JsonResponse({'message': "Error in uploading file."} , status=400)
        

        if isinstance(file, InMemoryUploadedFile):
            # File is stored in memory
            # save file to disk
            file_path = "autonomous_app/static/autonomous_app/files/" + file.name
            with open(file_path, 'wb') as f:
                f.write(file.read())
            # Handle it here
            try:
                # Use file_content as needed
                convert_and_save(file_path=file_path, id_= user_id)
                return JsonResponse({'message': "File uploaded successfully."})
            except:
                return JsonResponse({'message': "Error in uploading file."}, status=400)
        else:
            # File is stored on disk
            try:
                temp_file_path = file.temporary_file_path()
                convert_and_save(temp_file_path, user_id)
                return JsonResponse({'message': "File uploaded successfully."})
            except:
                return JsonResponse({'message': "Error in uploading file."}, status=400)

        # file_path = "autonomous_app/static/autonomous_app/files/" + file_name

        # with open(file_path , "wb") as f:
        #     f.write(file_content)

        # Return the uploaded file as a response
        # response = FileResponse(open(file_path, 'rb'), content_type=file_type)
        # response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)
        # return response
        # return JsonResponse({'message': "File uploaded successfully." , 'file_path' : file_path})





from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_chatbot(request):
    businessId = request.POST.get('businessId', '')
    unique_cb_key = generate_unique_key()

    BusinessChatbot(business_id = businessId , chatbot_key = unique_cb_key , chatbot_name = f"Test{unique_cb_key[:4]}").save()


    print("Before ingest")
    try:
        ingest_and_log_data()
        return JsonResponse({'message': "Chatbot created successfully." , 'chatbot_key' : unique_cb_key})
    except Exception as e:
        print(e)
        return JsonResponse({'message': "Error in creating chatbot." , 'chatbot_key' : unique_cb_key} , status=400)

