from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views, view1
from .api_views import CustomLoginView,ProtectedView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # ✅ This is the missing piece
    path('setsession/',view1.set_session,name='set_session'),
    path('getsession/', view1.get_session, name='get_session'),
    path('delsession/', view1.delete_key, name='del_session'),
     path('visitcounter/', view1.visit_counter, name='visit_counter'),

]
urlpatterns += [
    path('api/token/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/',ProtectedView.as_view(),name='protected_api'),
]
