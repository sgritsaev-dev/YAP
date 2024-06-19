
from django.contrib import admin
from django.urls import include, path

from anfisa_for_friends.views import test_rendering

urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
    path('test_rendering/', test_rendering),
]