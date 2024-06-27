from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from cabinet.views import RetrieveCabinet

urlpatterns=[
    path('registers/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('active/<str:email>/<str:activation_code>/',ActivationView.as_view(),name='activate'),
    
    path('cabinet_subs/<slug:slug>/',RetrieveCabinet.as_view()) 
]