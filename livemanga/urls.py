from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from livemanga import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mangaupload/',views.MangaUploadView.as_view()),
    path('',views.VideoListAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)