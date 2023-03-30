from django.contrib import admin
from django.urls import path, include
from store.forms import UserLoginForm
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

    path(
        'login/',
        views.LoginView.as_view(
            template_name="store/registration/login.html",
            authentication_form=UserLoginForm,
            ),
        name='login',
         ),
]
