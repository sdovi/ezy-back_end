from .models import Info,Orders
from rest_framework import generics
from .serializer import UsersSerializers,usersbot

class Infopost(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = UsersSerializers


class Info_get_post_path(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = UsersSerializers

class Zakaz_get(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = usersbot
