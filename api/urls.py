from django.urls import path
from . import views
from rest_framework.routers import  DefaultRouter
from django.urls import include

router =   DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeesDetail.as_view()),

    #register for router url
    path('',include(router.urls))
]
