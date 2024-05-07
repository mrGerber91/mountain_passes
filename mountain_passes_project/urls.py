from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic import RedirectView

router = routers.DefaultRouter()

urlpatterns = [
    path('', RedirectView.as_view(url='/api/submitData/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('mountain_passes.urls')),
]
