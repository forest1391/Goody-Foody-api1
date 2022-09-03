from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Account, Rank
from utils.decorators import user_login_required


@api_view(['POST'])
def login(request):
    data = request.data

    if 'user_id' in request.session:
        return  Response({'success':False, 'message': '您已經登入過'},status=status.HTTP_403_FORBIDDEN)

    try:
        user = Account.objects.get(pk=data['account'], password=data['password'], rank=data['btn_value'])
    except:
        return Response({'success': False,'message': '登入失敗'},status=status.HTTP_404_NOT_FOUND)

    # Account.objects.get(pk=data['id'], pwd=data['pwd'])
    request.session['user_id'] = user.account
    request.session.save()
    return Response({'success': True, 'message': '登入成功', 'sessionid': request.session.session_key})


@api_view(['POST'])
@user_login_required
def logout(request):
    request.session.flush()
    return Response({'success': True, 'message': '登出成功'})


@api_view(['POST'])
def register(request):
    data = request.data
    # if 'user_id' in request.session:
    #     return  Response({'success':False, 'message': '您已經登入過'},status=status.HTTP_403_FORBIDDEN)
    try:
        btn_value = Rank.objects.get(pk=data['btn_value'])

        Account.objects.create(account=data['account'], password=data['password'], rank=btn_value)
    except:
        return Response({'success': False, 'message': '註冊失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '註冊成功'})