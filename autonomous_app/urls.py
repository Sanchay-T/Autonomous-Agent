"""
URL configuration for autonomous project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.landing , name = "base"),
    path("bard/", views.bard , name = "bard"),
    path("chat/<str:cb_key>/", views.gpt_chat , name = "chat"),
    path('bot-response/', views.bot_response, name='bot_response'),
    path('business-data-post/', views.business_data_post, name='business_data_post'),
    path('email_data_post/', views.email_data_post, name='email_data_post'),
    path('generate-business-data/', views.generate_business_data, name='generate_business_data'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('create_chatbot/', views.create_chatbot, name='create_chatbot'),
    path('url_data_post/', views.url_data_post, name='url_data_post'),

]


urlpatterns += urlpatterns + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
