from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('index',views.index,name="index"),
    path('show',views.show,name="show"),
    path('create',views.create,name="create"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('update/<str:pk>',views.update,name="update"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]


