from django.urls import path

from api.views.tag_views import *

from api.views.chat_views import get_all_chats, add_chat, chat_and_add

app_name = 'chat'

urlpatterns = [
    path('all/', get_all_chats),
    path('add/', add_chat),
    path('chat/',chat_and_add),
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]