from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

def keyboard(request):
#카카오톡에 버튼 정보를 보내는 부분
    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘','내일']
    })


@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
#각 버튼에 대한 응답 내용 
    if datacontent == '오늘':
        today = "오늘 급식"


        return JsonResponse({
            'message': {
                'text' : today
            },
            'keyboard': {
                'type' : 'buttons',
                'buttons':['오늘','내일']

            }
        })

    elif datacontent == '내일':
        tomorrow ="내일 급식"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type':'buttons',
                'buttons':['오늘','내일']
            }
        })