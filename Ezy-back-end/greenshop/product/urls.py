from django.urls import path
from .views import Infopost, Info_get_post_path, Zakaz_get
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('info/<int:pk>/', Info_get_post_path.as_view()),
    path('info/', Infopost.as_view()),
    path('accepting/', Zakaz_get.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)