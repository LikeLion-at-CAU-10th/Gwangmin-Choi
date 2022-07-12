from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

def http_response(request):
    if request.method == "GET":
        #return HttpResponseNotFound("찾는 페이지가 없습니다.")
        return HttpResponse("Hello World!")

def json_response(request):
    if request.method == "GET":
        data = {
            'name' : 'gwangmin',
            'age' : 14,
            "phone": '0101'
        }
        return JsonResponse(data = data)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        context = {
            'name' : name
        }
        
        return render(request, 'index.html', context=context)

    else: # GET
        return render(request, 'index.html')
