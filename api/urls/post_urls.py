from django.urls import path

from api.views.post_views import *

from api.views.post_views import get_all_posts, add_post

app_name = 'post'

urlpatterns = [

    path('all/', get_all_posts),
    path('add/', add_post),
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]