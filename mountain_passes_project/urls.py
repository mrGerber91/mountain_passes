from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic import RedirectView
from swagger import schema_view
from mountain_passes import views as mountain_passes_views

router = routers.DefaultRouter()

# Конфигурация URL-адресов приложения
urlpatterns = [
    path('', RedirectView.as_view(url='/api/submitData/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('mountain_passes.urls')),
    path('submitData/', mountain_passes_views.submit_data, name='submit_data'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

