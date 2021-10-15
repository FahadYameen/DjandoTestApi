from django.shortcuts import render
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from FactorAApplication.models import Post
from FactorAApplication.serializers import PostSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def posts(request):
    try:
        if request.method == 'GET':
            posts = Post.objects.order_by('-score')[:5]
            tutorials_serializer = PostSerializer(posts, many=True)
            return JsonResponse(tutorials_serializer.data, safe=False)
        elif request.method == 'POST': 
            post_data = JSONParser().parse(request)
            post_serializer = PostSerializer(data=post_data)
            if post_serializer.is_valid():
                post_serializer.save()
                return JsonResponse({"message" :"Data Created Succcessfully","data": post_serializer.data}, status=status.HTTP_201_CREATED) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse({"message":"Bad Request"})
    
