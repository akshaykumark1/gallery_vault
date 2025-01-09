# gallery/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user_gallery', views.user_gallery, name='user_gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete/<pk>', views.delete, name='delete'),
    path('',views.login_user,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_g,name='logout_g'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
