from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'), # In case you create a separate page
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('add_record/', views.add_record, name='add_record'),
    path('edit_record/<int:id>', views.edit_record, name='edit_record'),
    path('delete/<int:id>', views.delete_record, name='delete'),

    path('record/<int:id>', views.customer_record, name='record'),
    
]