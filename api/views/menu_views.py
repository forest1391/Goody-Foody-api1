from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.models import Menu
from api.models import Post,Account
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

@api_view()
def get_restaurant_menu(request, get_restaurant_id):
    data=request.data

    restaurant_id = get_restaurant_id
    restaurant_menus = Menu.objects.filter(restaurant_id=restaurant_id)
    if not restaurant_menus.exists():
        return Response({'success':False, 'message':'沒有菜單'}, status=status.HTTP_404_NOT_FOUND)
    return Response ({
        'success': True,
        'data' : [
            {
                'menu_id': menu.menu_id,
                'restaurant_id': menu.restaurant_id,
                'name': menu.name,
                'price': menu.price,
                'kcal': menu.kcal,
                'carbohydrate': menu.carbohydrate,
                'protein': menu.protein,
                'fat': menu.fat,
                'sodium':menu.sodium,
                'subname':menu.subname
            }
            for menu in restaurant_menus
        ]
    })

@api_view(['POST'])
def add_menu(request):
    data = request.data
    try:
        Menu.objects.create(restaurant_id=data['restaurant_id'], name=data['name'], price=data['price'], kcal=data['kcal'], carbohydrate=data['carbohydrate'], protein=data['protein'], fat=data['fat'], sodium=data['sodium'], subname=data['subname'])

    except:
        return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '新增成功'})

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
