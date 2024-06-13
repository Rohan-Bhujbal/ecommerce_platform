from . import views
from django.urls import path, include

urlpatterns = [
    path('upload', views.upload_file),
    path('detail/<str:file_id>', views.get_file_detail),
    path('view/<str:type>/<str:id>', views.download_file),
]