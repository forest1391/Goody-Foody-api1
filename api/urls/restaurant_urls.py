from django.urls import path

from api.views.tag_views import *

from api.views.restaurant_views import get_all_restaurants, get_a_restaurant,add_information, search_restaurant

app_name = 'restaurant'

urlpatterns = [
    path('all/', get_all_restaurants),
    path('detail/<int:pk>/', get_a_restaurant),
    path('add/', add_information),
    path('search/', search_restaurant),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]