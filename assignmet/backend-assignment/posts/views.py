from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def http_response(request):
    if request.method == "GET":
        return HttpResponse("Hello World!")


def index(request):
    if request.method=="POST":
        name=request.POST.get('name')

        data={
            'name':name
        }
        return render(request,'index.html', context=data)

    else:
        return render(request,'index.html')


# 어떤 요청이 날라오면 요청과 함께 index.html을 보여주라 

def json_response(request):
    if request.method=="GET":

        data={
            'name': 'gwangmin',
            'school' : 'CAU'
        }

        return JsonResponse(data=data)