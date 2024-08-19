
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path("", include(("mailings.urls", "mailings"), namespace="mailings")),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
