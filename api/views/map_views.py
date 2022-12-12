from math import sqrt

from api.models import LocView, Restaurant
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Restaurant

@api_view()
def get_map_restaurant(request, lat, lng):
    # data = request.query_params
    # pk = data.get('post_id')
    try:
        result = LocView.objects.get(lat=lat, lng=lng)

    except:
        return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({

        'success': True,
        'data': {
            'restaurant_id': result.restaurant,
            'account': result.account.pk,
            'name': result.name,
            'address': result.address,
            'business_hours': result.businesshours,
        }
    })

@api_view()
def maptest(request):
    # 傳資料到資料庫
    data = request.query_params
    lat = data.get('lat')
    lng = data.get('lng')
    # 拿資料出來
    # print(lat)
    results = LocView.objects.all().filter()
    # r = results.filter(lat=)


    # 傳資料到資料庫
    # try:
       # LocView.objects.create(lat=data['lat'], lng=data['lng'])
    # except:
    #     return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    # return Response({'success': True, 'message': '新增成功'})

    # 拿資料出來
    return Response({
        'success':True,
        'data': [
            {
                'restaurant_id': result.restaurant_id,
                'account': result.account,
                'name': result.name,
                'address': result.address,
                'business_hours': result.business_hours,

            }
        for result in results
        ]
    })

@api_view()
def location_restaurant(request):
    data = request.query_params
    userlat = float(data['userlat'])
    userlon = float(data['userlng'])
    restaurants = Restaurant.objects.all()

    # lat = restaurants.lat
    # lon = restaurants.lon

    res = []
    for r in restaurants:
        num = sqrt(((userlat - r.lat) ** 2) + ((userlon - r.lon) ** 2))
        print(type(num))
        print(num)
        if num < 0.002:
            res.append({
                'restaurant_id': r.restaurant_id,
                # 'account': restaurant.account,
                'name': r.name,
                'address': r.address,
                'phone': r.phone,
                'business_hours': r.business_hours,
                'resume': r.resume,
                'license_id': r.license_id,
                'lat': r.lat,
                'lon': r.lon,
            })
    return Response({
        'success':True,
        'data':res
    })



    '''for i in range(1, max(restaurants.restaurant_id)):
        if ((((userlat-i.lat)**2)-((userlon-i.lon)**2))**0.5) < 0.001:
            return Response({
                'success': True,
                'data': [
                    {
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
                    for restaurant in i
                ]

            })'''