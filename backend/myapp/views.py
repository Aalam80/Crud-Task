from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import json

# Create your views here.
@api_view(['POST'])
def create_task(request): 
    """
    Create a New Task.
    """  
    try:
        description =request.POST.get("description")
        title =request.POST.get("title")
        print(description,title)
        # json_body=json.loads(request.body)
        # print(json_body,'rtyui')
        # description = json_body["description"]
        # title = json_body['title']
        if len(description) <= 0 or len(title) <= 0 :
            return Response({'message':"Description and Title field is requred"},status=204)
        Task.objects.create(description=description,title=title)
        return Response({'message':'Task created successfully'}, status=200)
    except Exception as e:
        print(e,"ewewe")
        

        return Response({'message':'something went wrong'}, status=500)

@api_view(['POST'])
def update_task(request,id):
    """
    Update an existing Task.
    """
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"message": "Task not found"}, status=404)
    
    try:
        description=request.POST.get('description').strip()
        title=request.POST.get('title').strip()
        status=request.POST.get('status').strip()
        # json_body=json.loads(request.body)
        # description = json_body["description"].strip() if "description" in json_body else None
        # title = json_body['title'].strip() if "title" in json_body else None
        # status=json_body['status'].strip() if "status" in json_body else None
        # print(json_body,'jasoshs-msmsnnmnnmm,n',description,title,status)
        if description:
            print(description,'der')
            task.description = description
        if title:
            print(title,'title')
            task.title = title
        if status:
            print(status,'status')
            task.status=status
        task.save()
        return Response({'message':'Task updated successfully'}, status=200)


    except Exception as e:
       print(e,"ewewe")
       return Response({'message':'something went wrong'}, status=500)


@api_view(['Get']) 
def read_task(request):
    try:
        # Retrieve all tasks from the database
        tasks = Task.objects.all()
        # Serialize the tasks using TaskSerializer
        serializer = TaskSerializer(tasks, many=True)
        return Response({'message':'Task show successfully',"data":serializer.data}, status=200)
    except:
        return Response({'message':'something went wrong'}, status=500)



@api_view(['POST'])
def delete_task(request,id):
    """
    Update an existing Task.
    """
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({"message": "Task not found"}, status=404)
    
    try:
        # json_body=json.loads(request.body)
        Task.objects.filter(id=task.id).delete()
       
        return Response({'message':'Task deleted successfully'}, status=200)

    except Exception as e:
       print(e,"ewewe")
       return Response({'message':'something went wrong'}, status=500)



    