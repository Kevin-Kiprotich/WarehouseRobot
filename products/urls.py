from django.urls import path
from . import views

urlpatterns=[
    path('check_store/',views.CheckStore.as_view(),name='check'),
    path('pick/',views.PickItem.as_view(),name='Pick'),
    path('store/',views.Store.as_view(),name='Store')
]