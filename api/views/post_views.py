from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from api.models import Menu
from api.models import Post, Account,PostMsg
import json
from utils.decorators import user_login_required
from django.shortcuts import render
import time
import os


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
                'post_id': post.post_id,
                'account': post.account.pk,
                'title': post.title,
                'content': post.content,
                # 'post_time': post.post_time,
                'image':post.post_photo,
            }
            for post in posts
        ]

    })


@api_view(['POST'])
def add_post(request):
    data = request.data
    # 上傳圖片
    # fname = None
    # print("*******1")
    # print(request.FILES)
    # print(json.dumps(request.data['image']))

    # request.FILES['image']
        # if f.filename != '':
        #     # 改圖片檔名, 前面加入時間, 以免檔名與他人的圖檔同名
        #     pre = str(round(time.time() * 1000))
        #     fname = pre + '-' + f.filename
        #     f.save(os.path.join('./static/photo/', fname))
    # print("*******2")

    try:
        account = Account.objects.get(pk=data['account'])
        Post.objects.create(account=account, title=data['title'], content=data['content'], post_photo=data['image'])

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
def get_post(request, pk):
    # data = request.query_params
    # pk = data.get('post_id')
    # try:
    post = Post.objects.get(pk=pk)
    comments = PostMsg.objects.all().filter(post_id=pk)
    # comments = PostMsg.objects.all()
    # except:
    #     return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)
    return Response({

        'success': True,
        'data1': {
            'post_id': post.post_id,
            'account': post.account.pk,
            'title': post.title,
            'content': post.content,
            'post_time': post.post_time,
        }
        ,
        'data2': [
            {
                'account': comment.account.pk,
                'content': comment.content,
                'time': comment.time,
            }
            for comment in comments
        ]
    })

@api_view(['POST'])
def add_post_comment(request):
    data = request.data
    pk = data['post_id']
    # comments = PostMsg.objects.all().filter(post_id_id=pk)
    now = datetime.now()
    hms = now.strftime("%H:%M:%S")
    # try:
    account = Account.objects.get(pk=data['account'])
    PostMsg.objects.create(account=account, content=data['content'], time=hms, post_id=pk)

    # except:
    #     return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    # return Response({'success': True, 'message': '新增成功'})
    # return Response({
    #     'success':True,
    #     'data': [
    #         {
    #             'account':comment.account.pk,
    #             'content': comment.content,
    #             'time': comment.time,
    #         }
    #     for comment in comments
    #     ]
    # })

@api_view()
def test(request):

    posts = Post.objects.all().filter(post_photo__isnull=True)

    # for post in posts:
    #     post.post_photo = str(round(time.time() * 1000))
    #     post.save()

    data = request.query_params
    pk = data['pk']
    comments = PostMsg.objects.all().filter(post_id=pk)
    return Response({
        'success': True,
        'data': [
            {
                'content': comment.content,

            }
            for comment in comments
        ]
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
