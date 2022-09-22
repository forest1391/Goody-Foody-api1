from django.urls import path

from api.views.book_review_views import *

from api.views.book_review_views import get_all_reviews, get_review

app_name = 'book_review'

urlpatterns = [
    path('all/', get_all_reviews),
    path('post/', get_all_posts),
    path('add/', add_post),
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]