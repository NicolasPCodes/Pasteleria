from django.urls import path
from . import views


app_name = 'pasteleria_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'lista-productos/',
        views.ListProductsClient.as_view(),
        name='product_all'
    ),
    path(
        'ver-producto/<pk>/',
        views.ProductoDetailView.as_view(),
        name='producto_detalle'
    ),
    path(
        'contacto/',
        views.ContactoView.as_view(),
        name='contacto'
    ),
]