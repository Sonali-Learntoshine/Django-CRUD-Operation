from django.conf.urls.static import static
from django.contrib.auth import settings
from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('<int:id>/', views.profile, name='profile'),
    path('', views.View_user.as_view(), name='users'),
    path('add/', views.add_student, name='add_student'),
    path('del/<int:id>/', views.del_student, name='del_student'),
    path('update/<int:id>/', views.update, name='update'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
