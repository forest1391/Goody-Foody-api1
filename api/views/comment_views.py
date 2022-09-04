from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import RestaurantMsg
from utils.decorators import user_login_required


@api_view(['POST'])
@user_login_required
def add_review(request):
    data = request.data
    try:
        RestaurantMsg.objects.create(restaurant_msg_id=data['restaurant_msg_id'],account=data['account'], restaurant_id =data['restaurant_id '],content=data['content'],time=data['time'])
    except:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '新增成功'})


@api_view(['POST'])
@user_login_required
def delete_review(request):
    data = request.data
# <test>
    restaurant_msg_id = data.get('restaurant_msg_id')
# <test>
    account = data.get('account')
    restaurant_msg = RestaurantMsg.objects.filter(restaurant_msg_id=restaurant_msg_id,account=account)
    if not restaurant_msg.exists():
        return Response({'success': False, 'message': '沒有此留言'}, status=status.HTTP_404_NOT_FOUND)
    restaurant_msg.delete()
    return Response({'success': True, 'message': '刪除成功'})


@api_view()
@user_login_required
def all_review(request):
    data = request.query_params
    account = data.get('account')

    account = str(account).strip()
    restaurant_msgs = RestaurantMsg.objects.all()

    return Response({
        'success': True,
        'data': [
            {
            'restaurant_msg_id':restaurant_msg.restaurant_msg_id,
            'restaurant_id':restaurant_msg.restaurant_id,
            'account':restaurant_msg.account,
            'content':restaurant_msg.content,	   
            'time':restaurant_msg.time,
            }
            for restaurant_msg in restaurant_msgs
        ]
    })


@api_view()
def get_comment_reviews(request):
    # 注意：因使用GET，使用query_params
    data = request.query_params
    account = data.get('account')
    
    # 去除前後空白
    account= str(account).strip()

# 編輯留言

# @api_view(['POST'])
# @user_login_required
# def edit_review(request, pk):
#     data = request.data

#     account = data.get('account')
#     restaurant_msg = RestaurantMsg.objects.filter(restaurant_msg_id=restaurant_msg_id, account=account)
#     if not restaurant_msg.exists():
#         return Response({'success': False, 'message': '沒有此留言'}, status=status.HTTP_404_NOT_FOUND)

#     try:
#         restaurant_msg.update(restaurant_msg_id=data['restaurant_msg_id'],account=data['account'], restaurant_id =data['restaurant_id '],content=data['content'],time=data['time'])
#         return Response({'success': True, 'message': '編輯成功'})
#     except:
#         return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)

