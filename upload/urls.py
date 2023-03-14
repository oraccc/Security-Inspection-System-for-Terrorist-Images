from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/', views.uploadImg, name='upload'),
    path('upload2/', views.uploadImgPerson, name="upload2"),
    path('show/', views.showImg, name='show'),
    path('show2/', views.showImgPerson, name="show2"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

