from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.models import Restaurant,Account

from utils.decorators import user_login_required

@api_view()
def get_all_restaurants(request):
    restaurants=Restaurant.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'restaurant_id':restaurant.restaurant_id,
                # 'account': restaurant.account,
                'name': restaurant.name,
                'address': restaurant.address,
                'phone': restaurant.phone,
                'business_hours': restaurant.business_hours,
                'resume': restaurant.resume,
                'license_id': restaurant.license_id,
                'lat': restaurant.lat,
                'lon': restaurant.lon,

            }
        for restaurant in restaurants
        ]

    })

# @api_view()
# def get_a_restaurant(request):
#     data=request.data
#
#     restaurant_id=data.get('restaurant_id')
#     restaurants = Restaurant.objects.filter(restaurant_id=restaurant_id)
#     if not restaurants.exists():
#         return Response({'success':False, 'message':'沒有此餐廳'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data':[
#             {
#                 'name': restaurant.name,
#                 'address': restaurant.address,
#                 'phone': restaurant.phone,
#                 'business_hours': restaurant.business_hours,
#                 'resume': restaurant.resume,
#             }
#             for restaurant in restaurants
#         ]
#     })

@api_view()
def get_a_restaurant(request,pk):
    # data = request.query_params
    # pk = data.get('post_id')
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({

        'success': True,
        'data': {
            'restaurant_id': restaurant.restaurant_id,
            # 'account': restaurant.account,
            'name': restaurant.name,
            'address': restaurant.address,
            'phone': restaurant.phone,
            'business_hours': restaurant.business_hours,
            'resume': restaurant.resume,
            'license_id': restaurant.license_id,
            'lat': restaurant.lat,
            'lon': restaurant.lon,
        }
    })

@api_view(['POST'])
def add_information(request):
    data = request.data
    # try:
    account=Account.objects.get(pk=data['account'])
    Restaurant.objects.create(account=account,name=data['name'], address=data['address'], phone=data['phone'],business_hours=data['business_hours'],resume=data['resume'],license_id=data['license_id'],lat=data['lat'],lon=data['lon'])

    # except:
    #     return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)
    #
    # return Response({'success': True, 'message': '新增成功'})

