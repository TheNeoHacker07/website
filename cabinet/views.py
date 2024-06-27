from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from .models import UserCabinet
from .serializer import UserCabinetSerializer

class ListCabinet(ListAPIView):
    queryset=UserCabinet.objects.all()
    serializer_class=UserCabinetSerializer



class RetrieveCabinet(RetrieveAPIView):
    queryset=UserCabinet.objects.all()
    serializer_class=UserCabinetSerializer
    lookup_field='slug'



class CreateCabinet(CreateAPIView):
    queryset=UserCabinet.objects.all()
    serializer_class=UserCabinetSerializer



    






