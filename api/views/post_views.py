from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu
from api.models import Post,Account
from utils.decorators import user_login_required
from django.shortcuts import render


# from .forms import UploadModelForm


@api_view()
# @user_login_required
def get_all_posts(request):
    posts = Post.objects.all()
    # print(books)
    return Response({
        'success': True,
        'data': [
            {
                'post_id':post.post_id,
                'account': post.account.pk,
                'title': post.title,
                'content': post.content,
                'post_time': post.post_time,
            }
            for post in posts
        ]

    })


@api_view(['POST'])
def add_post(request):
    data = request.data
    try:
        account=Account.objects.get(pk=data['account'])
        Post.objects.create(account=account,title=data['title'], content=data['content'])

    except:
        return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '新增成功'})




# @api_view()
# def get_a_post(request):
#     data = request.data
#
#     post_id = data.get('post_id')
#     posts = Post.objects.filter(post_id=post_id)
#     if not posts.exists():
#         return Response({'success': False, 'message': '沒有此貼文'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'account': post.account,
#                 'title': post.title,
#                 'content': post.content,
#                 'post_time': post.post_time,
#             }
#             for post in posts
#         ]
#     })

@api_view()
def get_post(request,pk):
    # data = request.query_params
    # pk = data.get('post_id')
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({

        'success': True,
        'data': {
            'post_id':post.post_id,
            'account': post.account.pk,
            'title': post.title,
            'content': post.content,
            'post_time': post.post_time,
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
