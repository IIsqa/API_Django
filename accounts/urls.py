# from django.urls import path
# from . import views


from django.urls import path
from . import views
from .views import MyTokenObtainPairView
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('api/token/',MyTokenObtainPairView.as_view, name='token_obtain_pair'),
]


# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
# ]
