from django.shortcuts import render
import joblib
import yaml , os , json
from .models import aissm
# Create your views here

def index(request):
    return render(request,'index.html')

def result(request):
    cls = joblib.load('../models/model.joblib')
    list = []
    list.append(int(request.GET['age']))
    list.append(int(request.GET['sex']))
    list.append(float(request.GET['bmi']))
    list.append(int(request.GET['children']))
    list.append(int(request.GET['smoker']))
    list.append(int(request.GET['region']))

    answer = cls.predict([list])

    b = aissm(age = int(request.GET['age']),
              sex = int(request.GET['sex']),
              bmi = float(request.GET['bmi']),
              children = int(request.GET['children']),
              smoker = int(request.GET['smoker']),
              region = int(request.GET['region']),
              charges = answer
              )
    b.save()

    return render(request,'index.html',{'answer':answer[0]})
