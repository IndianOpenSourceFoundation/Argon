from django.urls import path

from .views import HomePageView

from django.contrib import admin


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    ]
