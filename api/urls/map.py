from django.urls import path

from api.views.comment_views import *

# from api.views.comment_views import add_review,delete_review,get_comment_reviews,all_review,edit_review

app_name = 'map_seach'

urlpatterns = [
    path('all/', all_review),
    path('seach/', add_review),
    # path('delete/', delete_review),
    # path('edit/',edit_review),
]