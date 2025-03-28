from pydoc import resolve

from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.status import *
from rest_framework import status


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH", "DELETE"])
def movie_details(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
        response = {"success": True}
    except Exception as e:
        response["error"] = e
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        response["data"] = serializer
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializers.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=HTTP_400_BAD_REQUEST)
