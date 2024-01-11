from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('local/', views.PackageListView.as_view(), name='local'),
    path('add/', views.AddLocalPackageView.as_view(), name='add'),
    path('', views.index, name='index'),
    path('', views.detail, name='detail'),
    path('export/', views.export_packages, name='export'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]