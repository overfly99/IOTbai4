from django.contrib import admin
from django.urls import path
from django.urls.conf import include 
from rest_framework.routers import DefaultRouter
from .models import *
from .views import *
router = DefaultRouter()
router.register('dropbox', DropBoxViewset, basename='dropbox')
urlpatterns = [
    path('dropbox/', include(router.urls)),
    path('dropbox/<int:pk>/', include(router.urls)),
    path('dropbox_api_view/',DropBoxAPIView.as_view(),name = 'dropbox_api_view'),
    path('dropbox_api_view/detail/<int:id>/', DropboxDetailAPIView.as_view(),name = 'detail')

]