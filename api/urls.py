from django.urls import path

from . import views

urlpatterns = [
    path('department/',views.DepartmentListCreate.as_view(), name='department_create'),
    path('department/<int:pk>/', views.DepartmentRetrieveUpdateDestory.as_view(), name='department_detail'),
    path('department/<str:name>/', views.DepartmentDetailView.as_view(), name='department_search'),
    path('position/', views.PositionListCreate.as_view(), name='position_create'),
    path('position/<int:pk>/', views.PositionRetrieveUpdateDestroy.as_view(), name='position_detail'),
    path('position/<str:name>/', views.PositionDetailView.as_view(), name='position_search'),
    path('employee/', views.EmployeeListCreate.as_view(), name='employee_create'),
]