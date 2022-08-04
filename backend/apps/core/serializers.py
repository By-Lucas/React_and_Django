from django.contrib.auth.models import User, Group
from .models import List, Item
from rest_framework import serializers


class ItempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name',  'done'] #'list', 'url'

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItempSerializer(many=True) #Mostrar items na lista
    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']
