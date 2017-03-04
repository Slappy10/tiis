from django.conf.urls import url, include
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(frontend_urls)),
    url(r'', include('blog.urls')),
]
 