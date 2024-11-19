"""
URL configuration for mahalaxmi project.

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
from mahalaxmi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userlogin, name='userlogin'),
    path('index', views.index, name='index'),

    path('branch', views.branch, name='branch'),
    path('branch_view', views.branch_view, name='branch_view'),


    path('employee_reg', views.employee_reg, name='employee_reg'),
    path('employee_certificate/<str:employee_id>/', views.employee_certificate, name='employee_certificate'),
    path('emp_home', views.emp_home, name='emp_home'),
    path('employee_view', views.employee_view, name='employee_view'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),


    path('customer', views.customer, name='customer'),
    path('check_mobile/', views.check_mobile, name='check_mobile'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('edit_customer/edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),  # Route for editing a customer
    path('edit_customer/remove/<int:customer_id>/', views.remove_customer, name='remove_customer'),

    path('add_dealer', views.add_dealer, name='add_dealer'),
    path('dealer_view', views.dealer_view, name='dealer_view'),
    path('edit_dealer/edit/<int:dealer_id>/', views.edit_dealer, name='edit_dealer'),
    path('remove_dealer/remove/<int:dealer_id>/', views.remove_dealer, name='remove_dealer'),

    path('add_item', views.add_item, name='add_item'),
    path('item_view', views.item_view, name='item_view'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('Item_view_stock', views.Item_view_stock, name='Item_view_stock'),


    path('customer_booking', views.customer_booking, name='customer_booking'),
    path('get_customer_details', views.get_customer_details, name='get_customer_details'),
    path('get_items_by_branch/', views.get_items_by_branch, name='get_items_by_branch'),
    path('customer_booking_view', views.customer_booking_view, name='customer_booking_view'),
    path('receipt/<str:receipt>/', views.receipt, name='receipt'),

    path('customer_balance', views.customer_balance, name='customer_balance'),
    path('save_customer_balance', views.save_customer_balance, name='save_customer_balance'),
    path('get_customer_items', views.get_customer_items, name='get_customer_items'),
    path('transfer_item', views.transfer_item, name='transfer_item'),

    path('get_customer_details/', views.get_customer_details, name='get_customer_details'),
    path('check_duplicate_contact/', views.check_duplicate_contact, name='check_duplicate_contact'),
    path('get_item_details/', views.get_item_details, name='get_item_details'),

    path('sale/', views.sale, name='sale'),
    path('get-total-amount/',views. get_total_amount, name='get_total_amount'),


    # Add this
    # For AJAX request


    # Route for removing a customer
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
