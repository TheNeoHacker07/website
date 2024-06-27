from django.urls import path
from .views import *


urlpatterns=[
    path('create_cabinet/',CreateCabinet.as_view()),
    path('retrieve_cabinet/<slug:slug>/',RetrieveCabinet.as_view()),
    path('list_cabinet/',ListCabinet.as_view()),

]



