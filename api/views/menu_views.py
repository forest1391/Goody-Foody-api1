from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu
from api.models import Post
from utils.decorators import user_login_required
from django.shortcuts import render


# from .forms import UploadModelForm


@api_view()
def get_all_menus(request):
    menus = Menu.objects.all()
    # print(books)
    return Response({
        'success': True,
        'data': [
            {
                'menu_id': menu.menu_id,
                'restaurant_id': menu.restaurant_id,
                'name': menu.name,
                'price': menu.price,
                'kcal': menu.kcal,
                'carbohydrate': menu.carbohydrate,
                'protein': menu.protein,
                'fat': menu.fat,

            }
            for menu in menus
        ]

    })

#
# @api_view()
# @user_login_required
# def get_review(request, pk):
#     try:
#         menu = Menu.objects.get(pk=pk)
#     except:
#         return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)
#
#     # print(books)
#     return Response({
#         'success': True,
#         'data': {
#             'menu_id': menu.menu_id.pk,
#             'restaurant_id': menu.restaurant_id,
#             'name': menu.name,
#             'price': menu.title,
#             'kcal': menu.comment,
#         }
#
#     })
