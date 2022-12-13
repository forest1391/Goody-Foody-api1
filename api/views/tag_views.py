from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu, Tags, Restaurant
from api.models import Post

from utils.decorators import user_login_required


@api_view()
def get_all_tags(request):
    tags = Tags.objects.all()
    # print(books)
    return Response({
        'success': True,
        'data': [
            {
                'tag_id': tag.tag_id,
                'tag_name': tag.tag_name,

            }
            for tag in tags
        ]

    })


@api_view(['POST'])
def add_tag(request):
    data = request.data
    try:
        Tags.objects.create(tag_name=data['tag_name'], tag_type_id=data['tag_type_id'])

    except:
        return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success': True, 'message': '新增成功'})


@api_view()
def tag_search(request, pk):
    restaurants = Restaurant.objects.all().filter(tag_id=pk)
    posts = Post.objects.all().filter(tag_id=pk)
    # print(books)
    return Response({
        'success': True,
        'data1': [
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
            for restaurant in restaurants
        ],
        'data2':[
            {
                'post_id': post.post_id,
                'account': post.account.pk,
                'title': post.title,
                'content': post.content,
                # 'post_time': post.post_time,
                'image':post.post_photo,
            }
            for post in posts
        ]

    })
