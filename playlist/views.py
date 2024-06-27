from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import Playlist
from .serializer import PlaylistSerializer

class PlaylistListView(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class PlaylistDetail(generics.RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_field='slug'



class PlaylistDelete(generics.DestroyAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    lookup_field='slug'
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]


class PlaylistUpdate(generics.UpdateAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    lookup_field='slug'
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]

class PlaylistCreate(generics.CreateAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

