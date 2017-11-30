import json
import login.services as services
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from query_db import update_db
from login.models import Credentials
from rest_framework import status
# Create your views here.

class Register(APIView):
    def post(self ,requests ,Format=None):
        req_body = json.loads(requests.body)
        val = services.register(req_body)
        return Response(val)


class Update(APIView):
    def post(self ,requests ,format=None):
        req_body = json.loads(requests.body)
        val = services.update(req_body)
        return Response()

class Delete(APIView):
    def delete(self,request,format=None):
        req_body = json.loads(request.body)
        services.deleteUser(req_body)
        return Response()

class ListAll(APIView):
    def get(self,request,format=None):
        lst= services.listAllUsers()
        return Response(lst)

class Login(APIView):
    def post(self, requests,format=None):
        req_str = json.loads(requests.body)
        a=services.login(req_str)
        return Response(a)



