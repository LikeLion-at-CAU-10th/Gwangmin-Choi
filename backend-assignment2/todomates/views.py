from django.shortcuts import get_object_or_404, render
from .models import*
import json
from django.http import JsonResponse
# Create your views here.
def create_category(requests):
    if requests.method=="POST":

        body=json.loads(requests.body.decode('utf-8'))

        new_category=Category.objects.create(
            title=body['title'],
            view_auth=body['view_auth'],
            color=body['color']
        )

        new_category_json={
            "id" : new_category.id,
            "title" : new_category.title,
            "view_auth": new_category.view_auth,
            "color": new_category.color,
            "pup_date":new_category.pup_date,
        }

        return JsonResponse({
            "status":200,
            "sycceess":True,
            "message":"생성성공",
            "data":new_category_json
        })
    return JsonResponse({
        "status":405,
        "success":False,
        "message":"method error",
        "data":None
         })




