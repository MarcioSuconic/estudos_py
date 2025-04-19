from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('logout_forcado/', views.logout_forcado, name="logout_forcado"),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
