
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views
urlpatterns = [
    path('projects/',views.projects,name='projects'),
    path('languages/',views.languages,name='languages'),
    path('', views.index,name='index')
   
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)