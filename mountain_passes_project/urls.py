from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mountain_passes import views as mountain_passes_views
from swagger import schema_view

router = routers.DefaultRouter()
router.register(r'api/submitData', mountain_passes_views.PerevalAddedViewSet, basename='submitData')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
