from django.contrib import admin
from django.urls import path
from .views import *
from .views import SignUpView

urlpatterns = [
    path('', home, name='home'),
    path('sale/', sale, name='sale'),
    path('game/<int:id>/', game, name='game'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
