from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Menu, Tags
from api.models import Post

from utils.decorators import user_login_required

@api_view()

def get_all_tags(request):
    tags=Tags.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'tag_name':tag.tag_name,

            }
        for tag in tags
        ]

    })

@api_view(['POST'])
def add_tag(request):
    data = request.data
    try:
        Tags.objects.create(tag_name=data['tag_name'],tag_type_id=data['tag_type_id'])

    except:
        return Response({'success':False, "message":'新增失敗'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'success':True, 'message':'新增成功'})