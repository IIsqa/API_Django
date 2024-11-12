from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet, EmployeeViewSet
from .views import UserRegisterView,example_view


router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('logout/', TokenRefreshView.as_view(), name='token_refresh'),  # Uncomment for JWT authentication
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('example/', example_view, name='example')
]