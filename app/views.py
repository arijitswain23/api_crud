from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *

# Create your views here.
class ProductCrud(APIView):
    def get(self, request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS, many=True)
        return Response(PJD.data)
    
    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'message':'Product is Updated'})
        return Response({'Failed':'Product is not Updated'})
    
    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductSerializer(PO, data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})
        
    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductSerializer(PO, data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})
    
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({"delete":"Product is Deleted"})