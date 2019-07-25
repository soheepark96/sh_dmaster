"""d_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.board, name="board"),
    path('', views.board_create, name="board_create"),
    path('view/', views.board_view, name="board_view"),
    path('<int:pk>/', views.board, name="board"),
    path('update/<int:pk>', views.board_update, name="board_update"),
    path('delete/<int:pk>', views.board_delete, name="board_delete"),
]
