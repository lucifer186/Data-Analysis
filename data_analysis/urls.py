from django.contrib import admin
from django.urls import path, include
from data_analysis import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'data_analysis'  # Define the namespace
urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('analyze', views.analyze, name='analyze'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
