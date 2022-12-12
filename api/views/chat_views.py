from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Chat, Account
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
                'account':chat.account.pk,
                'b_account': chat.b_account,
                'content': chat.content,
                'time': chat.time,

            }
        for chat in chats
        ]
    })

@api_view(['POST'])
def add_chat(request):
    data = request.data
    try:
        account=Account.objects.get(pk=data['account'])
        Chat.objects.create(account=account, b_account=data['b_account'], content=data['content'], time=data['time'])

    except:
        return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '新增成功'})

@api_view()
def chat_and_add(request):
    data = request.data
    chats = Chat.objects.all()
    now = datetime.now()
    hms = now.strftime("%H:%M:%S")
    try:
        account = Account.objects.get(pk=data['account'])
        Chat.objects.create(account=account, b_account=data['b_account'], content=data['content'], time=hms)

    except:
        return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    # return Response({'success': True, 'message': '新增成功'})
    return Response({
        'success':True,
        'data': [
            {
                'chat_id':chat.chat_id,
                'account':chat.account.pk,
                'b_account': chat.b_account,
                'content': chat.content,
                'time': chat.time,

            }
        for chat in chats
        ]
    })

