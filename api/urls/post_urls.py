from django.urls import path

from api.views.post_views import *

from api.views.post_views import get_all_posts, add_post,get_post

app_name = 'post'

urlpatterns = [

    path('all/', get_all_posts),
    path('detail/', get_a_post),
    path('add/', add_post),
    path('test/', get_post),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]