import cryptocode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Account, Rank
from utils.decorators import user_login_required

secret_key = 'asecretkey'


    # 加密
# def encrypt(password, password=data['password']):
#     global secret_key
#     str_encoded = cryptocode.encrypt(password, secret_key)
#     return str_encoded

    # 解密
# @api_view([''])
#  def decode(enpw, cryptocode=None):
#     str_decoded = cryptocode.decrypt(enpw, secret_key)
#      return str_decoded

# class Encoder():
#     # 加密
#     @staticmethod
#     def encrypt(pw):
#         global secret_key
#         str_encoded = cryptocode.encrypt(pw, secret_key)
#         return str_encoded
#
#     # 解密
#     @staticmethod
#     def decode(enpw):
#         global secret_key
#         str_decoded = cryptocode.decrypt(enpw, secret_key)
#         return str_decoded


@api_view(['POST'])
def login(request):
    data = request.data
    print(data['account'])
    if 'user_id' in request.session:
        return Response({'success':False, 'message': '您已經登入過'},status=status.HTTP_403_FORBIDDEN)

    # try:
        # btn_value = Rank.objects.get(pk=data['btn_value'])

    # 帳號不存在會跑到except，因為有response所以會直接結束程式
    try:
        user = Account.objects.get(pk=data['account'])
    except:
        return Response({'success': False, 'message': 'not exist'}, status=status.HTTP_404_NOT_FOUND)

    # 解密
    password = cryptocode.decrypt(user.password, '12345')

    # 資料表解密後的密碼是否跟使用者傳入的密碼相同
    if password == data['password'] and user.rank.pk == int(data['btn_value']):
        request.session['user_id'] = user.account
        request.session.save()
        return Response({'success': True, 'message': '登入成功', 'sessionid': request.session.session_key})
    else:
        return Response({'success': False, 'message': 'fail'}, status=status.HTTP_404_NOT_FOUND)

    # password = cryptocode.encrypt(data['password'], '12345')
    # print(password)
    # Account.objects.filter(data['password'], 'password')
    # password = cryptocode.decrypt(data['password'], '12345')
    # password = print(password)
    # user = Account.objects.get(pk=data['account'])
    # except:
    #     return Response({'success': False,'message': '登入失敗'},status=status.HTTP_404_NOT_FOUND)

    # Account.objects.get(pk=data['id'], pwd=data['pwd'])


@api_view(['POST'])
@user_login_required
def logout(request):
    request.session.flush()
    return Response({'success': True, 'message': '登出成功'})


@api_view(['POST'])
def register(request):
    data = request.data

    try:
        btn_value = Rank.objects.get(pk=data['btn_value'])
        password = cryptocode.encrypt(data['password'], '12345')
        # str_encoded = request.get(password=data['password'])
        Account.objects.create(pk=data['account'], password=password, rank=btn_value)

    except:
        return Response({'success': False,'message': '註冊失敗'},status=status.HTTP_404_NOT_FOUND)

    # Account.objects.get(pk=data['id'], pwd=data['pwd'])
    return Response({'success': True, 'message': '註冊成功'})
