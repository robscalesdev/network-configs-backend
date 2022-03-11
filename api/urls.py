from django.urls import path
from .views.mango_views import MangosView, MangoDetailView
from .views.network_views import NetworksView, NetworkDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('mangos/', MangosView.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetailView.as_view(), name='mango_detail'),
    path('networks/', NetworksView.as_view(), name='networks'),
    path('networks/<int:pk>/', NetworkDetailView.as_view(), name='network_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
