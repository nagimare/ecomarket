from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InfoSerializer
from .models import Info


class InfoListAPIView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self, request):
        products = Info.objects.all()
        serializer = InfoSerializer(products, many=True)
        return Response(serializer.data)


class InfoCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)


class InfoDestroyApiView(APIView):


    def get_object(self, id):
        try:
            return Info.objects.get(id=id)
        except Info.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InfoUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return Info.objects.get(id=id)
        except Info.DoesNotExist:
            raise Http404

    def put(self, requests, id):
        post = self.get_object(id)
        serializer = InfoSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)