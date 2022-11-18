from django.urls import path

from api.views.comment_views import *


app_name = 'comment_test'

urlpatterns = [
    path('all/', all_review),
    path('add/', add_review),
    path('delete/', delete_review),
    # path('edit/',edit_review),
]
