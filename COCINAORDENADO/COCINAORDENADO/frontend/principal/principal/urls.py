from django.contrib import admin
from django.urls import path
from cocina import views
urlpatterns = [

    path('', views.principal, name='principal'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('carrito/', views.carrito, name='carrito'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),
    path('signout/', views.signout, name='signout'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('footer', views.footer, name='footer'),
    path('head', views.head, name='head'),
    path('admin/', views.admin_panel, name='admin'),
    path('api/items/', views.manage_products, name='manage_products'),
    path('api/items/<int:product_id>/', views.manage_products, name='manage_product_detail'),

]