from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .sitemaps import PostSitemap, CategorySitemap
from django.contrib.sitemaps.views import sitemap



# Sitemap configuration
sitemaps = {
    "posts": PostSitemap,
    "categories": CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
