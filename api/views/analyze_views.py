from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Eating


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
                'account': eating.account,
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
    try:
     Eating.objects.create(eat_id=data['eat_id'],account=data['account'],menu_id=data['menu_id'],eat_type_id=data['eat_type_id']
                           ,date=data['date'],kcal=data['kcal'],carbohydrate=data['carbohydrate'],protein=data['protein']
                           ,fat=data['fat'])

    except:
        return Response({'success':False, "message":'新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success':True, 'message':'新增成功'})

@api_view()
def get_meal_eating(request):
    data=request.data

    eat_type_id=data.get('eat_type_id')
    eatings = Eating.objects.filter(eat_type_id=eat_type_id)
    if not eatings.exists():
        return Response({'success':False, 'message':'沒有此飲食紀錄'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':[
            {
                'eat_id': eating.eat_id,
                'account': eating.account,
                'menu_id': eating.menu_id,
                'eat_type_id': eating.eat_type_id,
                'kcal': eating.kcal,
                'protein': eating.protein,
                'fat': eating.fat,
                'carbohydrate': eating.carbohydrate,
            }
            for eating in eatings
        ]
    })

