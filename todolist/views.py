from django.shortcuts import render
from .models import(
    TasksModel
)
from .serializer import(
    TaskSerializer
)

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView


class TaskAdder(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]
    def get(self,request):
        obj = TasksModel.objects.filter(user=request.user.id)
        serializer= TaskSerializer(obj,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):
        print(request.data)
        request.data['user']=request.user.id
        print(request.data)
        obj = TaskSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                'status':'added'
            },status=201)
        return Response({
                'status':'failed',
                'message':obj.errors
            },status=400)


class TaskModifier(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self,request):
    
        try:
            obj = TasksModel.objects.filter(id=request.data['id'])
            obj.update(status=request.data['status'])
            return Response(status=202)
        except:
            return Response(status=404)


class TaskDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]
    def get(self,request,pk):
        
        try:
            obj = TasksModel.objects.filter(id=pk)
            obj.delete()
            return Response(status=203)
        except:
            return Response(status=404)
