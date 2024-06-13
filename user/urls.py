from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login),
    path('get', views.get_user),
    path('logout', views.logout),
    path('get_magic_code', views.get_magic_code),
    path('set_login/<str:magic_code>/<str:device_id>/<str:device_type>', views.set_login),
    path('get_login', views.get_login),
    path('del_login', views.del_login),
    path('user_list',views.user_list_view,name='user_list')
]
