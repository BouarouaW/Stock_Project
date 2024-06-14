from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom_auth.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('employe-panel/', include('employe_panel.urls')),

]
