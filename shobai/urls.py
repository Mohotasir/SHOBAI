from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="home"),
    # == Include the app's URLs ===
    # For development only
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
