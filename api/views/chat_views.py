from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu, Chat
from api.models import Post

from utils.decorators import user_login_required

@api_view()

def get_all_chats(request):
    chats=Chat.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'chat_id':chat.chat_id,
                'account':chat.account,
                'b_account': chat.b_account,
                'content': chat.content,
                'time': chat.time,

            }
        for chat in chats
        ]

    })

# @api_view(['POST'])
# def add_tag(request):
#     data = request.data
#     try:
#         Tags.objects.create(tag_id=data['tag_id'],tag_name=data['tag_name'],tag_type_id=data['tag_type_id'])
#
#     except:
#         return Response({'success':False, "message":'新增失敗'}, status=status.HTTP_400_BAD_REQUEST)
#
#     return Response({'success':True, 'message':'新增成功'})