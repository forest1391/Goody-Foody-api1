from django.urls import path


from api.views.map_views import get_map_restaurant, maptest, location_restaurant

app_name = 'post'

urlpatterns = [

    path('location_restaurant/', location_restaurant),
    # path('maptest/', maptest ),


    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]