from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WareHouseA, WareHouseB, WareHouseC

# Create your views here.
# class StoreInMain(APIView):
#     def post(self,request):
#         UID=request.data.get('UID')
#         Product_Name=models.CharField(max_length=15,null=False)
#         quantity=models.IntegerField(default=0, null=False)
#         Time_In=models.DateTimeField(auto_now=True,null=False)
#         Time_Out=models.DateTimeField(auto_now=False)
#         destination=models.CharField(max_length=5)
#         status=models.CharField(max_length=15,null=False,default="In Storage")
class CheckStore(APIView):
    def post(self,request):
        store=request.data.get('store')
        if store =='A':
            goods=WareHouseA.objects.values().all()
            good=goods[0]
            return Response({'UID':good.UID})
        elif store == 'B':
            goods=WareHouseB.objects.values().all()
            good=goods[0]
            return Response({'UID':good.UID})
        else:
            goods=WareHouseB.objects.values().all()
            good=goods[0]
            return Response({'UID':good.UID})

class PickItem(APIView):
    def post(self,request):
        UID=request.data.get('UID')
        

        good=WareHouseA.objects.get(UID=UID)
        good.status="In Transit"
        good.save()
        print(good.status)
        return Response({"UID":UID,"Success":True})
    
class Store(APIView):
    def post(self,request):
        UID=request.data.get('UID')
        store=request.data.get('store')

        good=WareHouseA.objects.get(UID=UID)
        good.status="Transported"
        good.save()

        if good.destination=='B':
            newgood=WareHouseB(UID=UID,Product_Name=good.Product_Name)
            newgood.save()
        elif good.destination=='C':
            newgood=WareHouseC(UID=UID,Product_Name=good.Product_Name)
            newgood.save()
        return Response({"UID":UID,"Success":True})
