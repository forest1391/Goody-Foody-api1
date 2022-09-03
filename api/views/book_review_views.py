from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu
from utils.decorators import user_login_required


@api_view()
@user_login_required
def get_all_reviews(request):
    menus=Menu.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'menu_id':menu.pk,
                'restaurant_id':menu.restaurant_id,
                'name':menu.name,
                'price':menu.price,
                'kcal':menu.kcal,
            }
        for menu in menus
        ]

    })

# @api_view()
# def get_all_reviews(request):
#     menu_tag=Menu.objects.all()
#     # print(books)
#     return Response({
#         'success':True,
#         'data': [
#             {
#                 'menu_id': menus.user.pk,
#                 'restaurant_id': menu_tag.user.pk,
#
#
#
#
#             }
#         for menus in Menu
#         ]
#
#     })







@api_view()
@user_login_required
def get_review(request, pk):
    try:
        menu=Menu.objects.get(pk=pk)
    except:
        return Response({'success':False,'message':'查無資料'},status=status.HTTP_404_NOT_FOUND)

    # print(books)
    return Response({
        'success': True,
        'data': {
            'menu_id':menu.menu_id.pk,
            'restaurant_id':menu.restaurant_id,
            'name':menu.name,
            'price':menu.title,
            'kcal':menu.comment,
        }

    })


# @api_view(['POST'])
# # @user_login_required
# def add_review(request):
#     data = request.data
#     try:
#         book.object.create(user_id=data['user_id'], name=data['name'],
#                        title=data['title'], comment=data['comment'])
#     except:
#         return Response({'success': False, 'messaage': '新增成功'}, status= status.HTTP_400_BAD_REQUEST)
#
#     return Response({'success': True, 'messaage': '新增成功'})


# @api_view(['POST'])
# def edit_reviews(request, pk):
#     data = request.data
#
#     menu = Menu.objects.filter(no=pk)
#
#     menu.update(name=data['name'],title=data['title'],comment=data['comment'])
#     return Response({'success': True, 'message': '編輯成功'})

