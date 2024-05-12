from django.urls import path
from . import views

urlpatterns = [
    path('submitData/', views.submit_data, name='submit_data'),
    path('submitData/<int:id>/', views.get_single_data, name='get_single_data'),
    path('submitData/<int:id>/', views.edit_data, name='edit_data'),
    path('submitData/', views.get_user_data, name='get_user_data'),
]