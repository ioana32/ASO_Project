from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views


""""
DefaultRouter class allows automatic routing of ALL URLS for all operations on object from DB
ViewSet is mapped with Router below in code. Finally urlpatterns gets populated
"""

urlpatterns = [

    # path('', views.signin, name='signin'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('',views.home, name='home'),  # new
    # path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]