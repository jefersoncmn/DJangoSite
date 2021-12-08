from django import urls
from django.http import request
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('nft/<int:my_id>/', views.nft_view)
]

urlpatterns += staticfiles_urlpatterns()
