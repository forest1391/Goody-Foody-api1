from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Report
from api.models import Post

from utils.decorators import user_login_required

@api_view()

def get_all_reports(request):
    reports=Report.objects.all()
    # print(books)
    return Response({
        'success':True,
        'data': [
            {
                'report_id':report.report_id,
                'account': report.account.pk,
                'title': report.title,
                'content': report.content,
                'report_type_id': report.report_type_id,
                'object_id': report.object_id,

            }
        for report in reports
        ]

    })


@api_view(['POST'])
def add_report(request):
    data = request.data
    # try:
    Report.objects.create(account=data['account'], title=data['title'], content=data['content'], time=data['time'])

    # except:
    #     return Response({'success': False, "message": '新增失敗'}, status=status.HTTP_400_BAD_REQUEST)
    #
    # return Response({'success': True, 'message': '新增成功'})

