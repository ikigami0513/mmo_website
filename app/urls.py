from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='app_index'),
    path('register/', UserRegister.as_view(), name='app_register'),
    path('logout/', UserLogout.as_view(), name='app_logout'),
    path('login/', UserLogin.as_view(), name='app_login'),
    path('password/forgot', ForgotPassword.as_view(), name='app_forgot_password'),
    path('encyclopedie/<str:type>/', Encyclopedie.as_view(), name='app_encyclopedie'),
    path('api/encyclopedie/search/', FilterEncyclopedie.as_view(), name='app_encyclopedie_search'),
    path('player/create/', CreatePlayer.as_view(), name='app_player_create'),
    path('player/list/', ListPlayer.as_view(), name='app_player_list'),
    path('player/delete/<int:id>', DeletePlayer.as_view(), name='app_player_delete'),
    path('player/update/<int:id>', UpdatePlayer.as_view(), name='app_player_update'),
    path('equipements/<str:type_e>/', Equipements.as_view(), name='app_equipements_get')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
