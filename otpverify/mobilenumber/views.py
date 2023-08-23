from django.shortcuts import render
from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt 
from rest_framework.response import Response
from .serializers import *
from .helprs import sent_otp_to_phone
from .models import User


# Create your views here.
@api_view(['POST'])
def sent_otp(request):
   data=request.data
   if data.get('phone_number') is None:
     return Response({
       'status':400,
       'key':'key phone_number is requried'
    })
   

   if data.get('password') is None:
     return Response({
       'status':400,
       'key':'key password is requried'
    })   
   
   user = User.objects.create(
            phone_number=data.get('phone_number'),
            otp=sent_otp_to_phone(data.get('phone_number'))
            )
   user.set_password=data.get('set_password')
   user.save()
   return Response({'status':200,'message':'otp sent'})


@api_view(['POST'])
def verify_otp(request):
   data=request.data
   if data.get('phone_number') is None:
     return Response({
       'status':400,
       'key':'key phone_number is requried'
    })
   

   if data.get('otp') is None:
     return Response({
       'status':400,
       'key':'key otp is requried'
    })  
   try:
      
      usr_obj=User.objects.get(phone_number=data.get('phone_number'))

   except Exception as e:
       return Response({
       'status':400,
       'key':'invalid otp'
    }) 
   
   if usr_obj.otp == data.get('otp'):
       usr_obj.is_verified=True
       usr_obj.save()
       return Response({
       'status':200,
       'key':'otp match'
    }) 
   return Response({
       'status':400,
       'key':'invalid otp'
    }) 

   
   
