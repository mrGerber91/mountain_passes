from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'submitData', views.PerevalAddedViewSet)

urlpatterns = [
    path('submitData/', views.submit_data, name='submit_data'),
    path('submitData/<int:id>/', views.get_single_data, name='get_single_data'),
    path('submitData/<int:id>/', views.edit_data, name='edit_data'),
    path('submitData/', views.get_user_data, name='get_user_data'),
    path('', include(router.urls)),
]