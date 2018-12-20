# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView
import pymongo
from django.http import HttpResponse
from bson.json_util import dumps
import json
import django
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')
class getToken(TemplateView):
    def get(self, request, **kwargs):
        response = HttpResponse('{"csrf":"' + django.middleware.csrf.get_token(request)+ '"}',content_type='application/json; charset=utf-8')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
class setSite(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html') 
# method insert into mongodb
    def post(self,request,**kwargs):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb= myclient['mydb']
        mycol= mydb['tourism_data']
        if request.POST.get('submit'):
            myimg = request.FILES.getlist('myfiles')
            fs = FileSystemStorage()
            listImg = []
            for key,file in enumerate(myimg) :
                filename =  fs.save(file.name,file)
                listImg.append({'url':fs.url(filename),
                                'des': request.POST.getlist('desImg')[key],
                                  })
            data = {'place':request.POST.get('place'),
                    'des':request.POST.get('des'),
                    'img':listImg,
                    }
            mycol.insert_one(data)
            return render(request, 'index.html',)
        return render(request, 'index.html')
class getSite(TemplateView):
    # return all  data as json
    def get(self, request, **kwargs):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['mydb']
        mycol = mydb['tourism_data']
        info = mycol.find()
        response=HttpResponse(dumps(info), content_type='application/json; charset=utf-8')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response