from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('pt/<str:pk>',views.pt,name='pt')
]