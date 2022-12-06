from django.urls import path
from . import views


""""
DefaultRouter class allows automatic routing of ALL URLS for all operations on object from DB
ViewSet is mapped with Router below in code. Finally urlpatterns gets populated
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]