from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Eating, Account,Menu

from utils.decorators import user_login_required

@api_view()

def get_all_eatings(request):
    eatings=Eating.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'eat_id':eating.eat_id,
                'account': eating.account.pk,
                'menu_id':eating.menu_id,
                'eat_type_id': eating.eat_type_id,
                'kcal':eating.kcal,
                'protein':eating.protein,
                'fat':eating.fat,
                'carbohydrate':eating.carbohydrate,




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
    data=request.data

    eat_type_id=type_id
    eatings = Eating.objects.filter(eat_type_id=eat_type_id)
    if not eatings.exists():
        return Response({'success':False, 'message':'沒有此飲食紀錄'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':[
            {
                'menu_id': eating.menu_id,
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
def add_menu_item(request,pk):
    # data = request.query_params
    # pk = data.get('post_id')
    # try:
    menu = Menu.objects.get(pk=pk)
    # except:
    #     return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({

        'success': True,
        'data': {
            'kcal':menu.kcal,
            'carbohydrate': menu.carbohydrate,
            'protein': menu.protein,
            'fat': menu.fat,

        }
    })

# objects.filter(..).orderby('-')
