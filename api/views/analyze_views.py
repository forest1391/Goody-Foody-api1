from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Eating, Account,Menu

from utils.decorators import user_login_required

# @api_view()
# def get_all_eatings(request):
#     data = request.data
#     account=data.get('account')
#     eatings=Eating.objects.all().filter(account=account,date=datetime.now())
#     # menu_name=Menu.objects.get(pk=eatings.menu_id)
#     # print(books)
#     return Response({
#         'success':True,
#         'data': [
#             {
#                 'eat_id':eating.eat_id,
#                 'account': eating.account.pk,
#                 'menu_id':eating.menu_id,
#                 # 'menu_name':menu_name,
#                 'menu_name':Menu.objects.get(menu_id=eating.menu_id).name,
#                 'eat_type_id': eating.eat_type_id,
#                 'kcal':eating.kcal,
#                 'protein':eating.protein,
#                 'fat':eating.fat,
#                 'carbohydrate':eating.carbohydrate,
#                 'date':eating.date,
#
#             }
#         for eating in eatings
#         ]
#     })
@api_view()
def get_all_eatings(request):
    #filter account date 使用者今日飲食加總
    data = request.data
    account=data.get('account')
    eatings=Eating.objects.all().filter(account=account,date=datetime.now())
    # menu_name=Menu.objects.get(pk=eatings.menu_id)
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'eat_id':eating.eat_id,
                'account': eating.account.pk,
                'menu_id':eating.menu_id,
                # 'menu_name':menu_name,
                'menu_name':Menu.objects.get(menu_id=eating.menu_id).name,
                'eat_type_id': eating.eat_type_id,
                'kcal':eating.kcal if eating.kcal is not None else "未填寫",
                'protein':eating.protein if eating.protein is not None else "未填寫",
                'fat':eating.fat if eating.fat is not None else "未填寫",
                'carbohydrate':eating.carbohydrate if eating.carbohydrate is not None else "未填寫",
                'date':eating.date,

            }
        for eating in eatings
        ]
    })

@api_view(['POST'])
def add_eating(request):
    data = request.data
    # try:
    account = Account.objects.get(pk=data['account'])
    Eating.objects.create(account=account,menu_id=data['menu_id'],eat_type_id=data['eat_type_id']
                           ,date=data['date'],kcal=data['kcal'],carbohydrate=data['carbohydrate'],protein=data['protein'],sodium=data['sodium']
                           ,fat=data['fat'])
    #
    # except:
    #     return Response({'success':False, "message":'新增失敗'}, status=status.HTTP_400_BAD_REQUEST)
    #
    # return Response({'success':True, 'message':'新增成功'})

@api_view()
def get_meal_eating(request, type_id):
  # 過濾account eat_type_id 使用者所有飲食紀錄
    data = request.data
    account = data.get('account')
    eatings = Eating.objects.filter(eat_type_id=type_id, account=account)
    # if not eatings.exists():
    #     return Response({'success':False, 'message':'沒有此飲食紀錄'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':[
            {
                'menu_id': eating.menu_id,
                'menu_name': Menu.objects.get(menu_id=eating.menu_id).name,
                # 'menu_name': Menu.objects.get(menu_id=eating.menu_id).name,
                # 'menu_name': Menu.objects.filter(pk=eating.menu_id).first().name, # eating.menu.name
                'kcal': eating.kcal,
                'protein': eating.protein,
                'fat': eating.fat,
                'carbohydrate': eating.carbohydrate,
            }
            for eating in eatings
        ]
    })

@api_view()
def today_meal_eating(request, type_id):
    # 過濾 date account eat_type_id 使用者今日飲食紀錄
    data = request.data
    account = data.get('account')
    eatings = Eating.objects.filter(eat_type_id=type_id,date=datetime.now(), account=account)
    # if not eatings.exists():
    #     return Response({'success':False, 'message':'沒有此飲食紀錄'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':[
            {
                'menu_id': eating.menu_id if eating.menu_id is not None else "未填寫",
                'menu_name': Menu.objects.get(menu_id=eating.menu_id).name,
                # 'menu_name': Menu.objects.filter(pk=eating.menu_id).first().name, # eating.menu.name
                'kcal': eating.kcal if eating.kcal is not None else "未填寫",
                'protein': eating.protein if eating.protein is not None else "未填寫",
                'fat': eating.fat if eating.fat is not None else "未填寫",
                'carbohydrate': eating.carbohydrate if eating.carbohydrate is not None else "未填寫",
            }
            for eating in eatings
        ]
    })

@api_view(['POST'])
def add_menu_item(request):
    data = request.data
    menu = Menu.objects.get(pk=data['menu_id'])

    try:
        account = Account.objects.get(pk=data['account'])
        Eating.objects.create(account=account , eat_type_id=data['eat_type_id'], menu_id=menu.menu_id, date=datetime.now()
                             , kcal=menu.kcal, carbohydrate=menu.carbohydrate, protein=menu.protein, fat=menu.fat)
    except:
        return Response({
            'success': True,
            'message': '新增失敗'
        })

    return Response({
        'success': True,
        'message':'新增成功'
    })


# objects.filter(..).orderby('-')
