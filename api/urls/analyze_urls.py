from django.urls import path

from api.views.tag_views import *

from api.views.analyze_views import get_all_eatings, add_eating, get_meal_eating,add_menu_item,today_meal_eating

app_name = 'analyze'

urlpatterns = [
    path('all/', get_all_eatings),
    path('add/', add_eating),
    path('add_menu_item/', add_menu_item),
    path('meal/<int:type_id>/', get_meal_eating),
    path('today_meal/<int:type_id>/', today_meal_eating),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]