from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
