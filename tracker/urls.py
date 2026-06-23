from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
    
    path('tenantadd/',views.tenant_form,name="tenantadd"),
    path('tenantlist/',views.tenant_list,name="tenant_list"),
    path("edit/<int:id>/",views.tenant_edit,name="tenant_edit"),
    path("delete/<int:id>/",views.tenant_delete,name="tenant_delete"),
    path('payment/',views.payment_form,name="payment_form"),
    path('paymentlist/',views.payment_list,name="payment_list"),
    path('paymentedit/<int:id>/',views.payment_edit,name="payment_edit"),
    path('paymentdelete/<int:id>/',views.payment_delete,name="payment_delete"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('',views.home,name="home"),
    
]

