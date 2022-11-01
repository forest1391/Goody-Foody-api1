from django.urls import path

from api.views.post_views import *

from api.views.menu_views import get_all_menus,get_restaurant_menu,add_menu

app_name = 'menu'

urlpatterns = [

    path('all/', get_all_menus),
    path('restaurant_menu/<int:get_restaurant_id>/', get_restaurant_menu),
    path('add/', add_menu),
    # path('detail/', get_a_post),
    # path('add/', add_post),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]