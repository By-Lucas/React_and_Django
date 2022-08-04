from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet
from django.contrib import admin
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet, basename='list')
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Fazer um post e gerar um token para o usuario(Precisa informar usuario e senha no bady)
    #http://127.0.0.1:8000/api-token-auth/
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
]
