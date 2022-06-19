from django.urls import path
from . import views
from .views import ClientLoginView, ClientRegister, EmployeeCreateView, EmployeeDetailView, EmployeeDeleteView, EmployeeUpdateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', ClientLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', ClientRegister.as_view(), name='register'),
    path('detail/<int:pk>', EmployeeDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', EmployeeDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', EmployeeUpdateView.as_view(), name='update'),

    path('', views.employees_list, name='list'),
    path('create-employee/', EmployeeCreateView.as_view(), name='create')
]

