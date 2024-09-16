from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'), # In case you create a separate page
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]