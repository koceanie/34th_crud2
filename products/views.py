from datetime import date
from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from products.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        dog = Dog.objects.create(
            owner = owner,
            name = data['dog'],
            age = data['dogage']
        )
        return JsonResponse({'message':'created'}, status = 201)
