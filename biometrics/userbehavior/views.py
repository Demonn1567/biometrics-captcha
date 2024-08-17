from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserBehavior
from .serializers import UserBehaviorSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin



# Create your views here.
class UserBehaviorView(APIView):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def post(self, request, *args, **kwargs):
        ip_address = self.get_client_ip(request)  
        request_data = request.data.copy()  
        request_data['ip_address'] = ip_address  

        serializer = UserBehaviorSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        user = UserBehavior.objects.all()
        serializer = UserBehaviorSerializer(user, many = True)
        return Response(serializer.data)
    
    def delete(self, request):
        id = request.data.get('id')
        
        try:
            user = UserBehavior.objects.get(id = id)
            user.delete()
            return Response({"message": "Data Deleted!"}, status = status.HTTP_204_NO_CONTENT)


        except:
            return Response("Invalid Id")
        
        
class GetUser(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = UserBehavior.objects.all()
    serializer_class = UserBehaviorSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

#only for getting a single user data
class GetSingleUser(GenericAPIView,UpdateModelMixin,RetrieveModelMixin, DestroyModelMixin):
    queryset= UserBehavior.objects.all()
    serializer_class = UserBehaviorSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
