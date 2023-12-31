from django.contrib import admin
from django.urls import path, include
from website import urls
import debug_toolbar

urlpatterns = [
    path("__reload__/",
	include("django_browser_reload.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
