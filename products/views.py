from datetime import date
from itertools import product
import re
from unittest import result
from urllib import request
from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View
import products

from products.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        owner = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        
        return JsonResponse({'message':'SUCCESS'}, status = 201)


    def get(self, request):
        result=[]
        owners = Owner.objects.all()

        for owner in owners :
            dogs = list(Dog.objects.filter(owner=owner.id).values('name','age'))
            result.append(
                {
                    'name' : owner.name,
                    'age' : owner.age,
                    'email' : owner.email,
                    'dogs' : [{
                        'name' : dog.name,
                        'age' : dog.age,
                    } for dog in owner.dog_set.all()
                    ]
                }
            )
        return JsonResponse({'result':result}, status = 200)

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)

        owner = Owner.objects.get(name=data['owner'])

        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = owner.id
        )
        return JsonResponse({"message" : "SUCCESS"}, status = 201)


    def get(self, request):
        result = []
        dogs = Dog.objects.all()

        for dog in dogs:
            result.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner' : dog.owner.name
                }
            )
        return JsonResponse({"result" : result}, status=200)
