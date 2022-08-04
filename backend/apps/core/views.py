from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ItempSerializer, ListSerializer
from .models import List, Item


class ListViewSet(viewsets.ModelViewSet):
    #queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication] #proteger rotar com autenticacao via token
    #authentication.SessionAuthentication = para que eu tenha acesso a api se estiver autenticado

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItempSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication] #proteger rotar com autenticacao via token
    #authentication.SessionAuthentication = para que eu tenha acesso a api se estiver autenticado
