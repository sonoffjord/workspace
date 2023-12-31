from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('board.urls')),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]
