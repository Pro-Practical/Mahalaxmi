"""
URL configuration for Mahalaxmi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Maha_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('branch/', views.branch, name='branch'),
path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
path('admin_nav/', views.admin_nav, name='admin_nav'),
path('employee/', views.employee, name='employee'),
path('view_certificate/<int:id>/', views.view_certificate, name='view_certificate'),
path('emp_list/', views.emp_list, name='emp_list'),
path('edit_employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
path('emp_dashboard/', views.emp_dashboard, name='emp_dashboard'),

 path('branch_list/', views.branch_list, name='branch_list'),
 path('edit/<int:branch_id>/', views.edit_branch, name='edit_branch'),


path('add_item/', views.add_item, name='add_item'),
path('item_list/', views.item_list, name='item_list'),
path('item_view/', views.item_view, name='item_view'),

 path('stock/', views.stock_list, name='stock_list'),
path('transfer_item_list/', views.transfer_item_list, name='transfer_item_list'),

path('transfer_item/', views.item_view, name='transfer_item'),

path('customer/', views.customer, name='customer'),
path('check-contact', views.check_contact, name='check_contact'),

path('customer_list/', views.customer_list, name='customer_list'),
path('edit_customer/<int:id>', views.edit_customer, name='edit_customer'),

 path("dealer_create/", views.dealer_create, name="dealer_create"),
path("edit_dealer/<int:dealer_id>/edit/", views.edit_dealer, name="edit_dealer"),
path("dealer_list/", views.dealer_list, name="dealer_list"),
                  # For updating customer
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





