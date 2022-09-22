from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu
from api.models import Post
from utils.decorators import user_login_required
from django.shortcuts import render
# from .forms import UploadModelForm


# @api_view()
# @user_login_required
# def get_all_posts(request):
#     menus=Menu.objects.all()
#     # print(books)
#     return Response({
#         'success':True,
#         'data': [
#             {
#                 'menu_id':menu.pk,
#                 'restaurant_id':menu.restaurant_id,
#                 'name':menu.name,
#                 'price':menu.price,
#                 'kcal':menu.kcal,
#             }
#         for menu in menus
#         ]
#
#     })



@api_view()
# @user_login_required
def get_all_posts(request):
    posts=Post.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                    'post_id':post.pk,
                    'account':post.account,
                    'title':post.title,
                    'content':post.content,
                    'post_time':post.post_time,
            }
        for post in posts
        ]

    })

@api_view(['POST'])
def add_post(request):
    data = request.data
    try:
        Post.objects.create(post_id=data['post_id'],title=data['title'],content=data['content'])

    except:
        return Response({'success':False, "message":'新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success':True, 'message':'新增成功'})


# @api_view(['POST'])
# def index(request):
#     form = UploadModelForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'photos/index.html', context)
#


# @api_view()
# @user_login_required
# def get_all_posts(request, post=None):
#     posts=Post.objects.all()
#
#     return Response({
#         'success':True,
#         'data': [
#             {
#                 'post_id':post.pk,
#                 'account':post.account,
#                 'title':post.title,
#                 'content':post.content,
#                 'post_time':post.post_time,
#     }
#         ]
#
#     })

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