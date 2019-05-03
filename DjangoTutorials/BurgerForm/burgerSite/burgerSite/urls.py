from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('burger/', include('burgerForm.urls')),
    path('admin/', admin.site.urls),
]
