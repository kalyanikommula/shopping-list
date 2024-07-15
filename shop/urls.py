from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('success/', views.success, name="success"),
    path('category/<slug:val>', views.categoryView.as_view(), name="category"),
    path('category-title/<val>', views.categoryTitle.as_view(), name="category-title"),  # noqa
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),  # noqa
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name="updateAddress"),  # noqa
    path('deleteAddress/<int:pk>', views.deleteAddress.as_view(), name="deleteAddress"),  # noqa
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.show_cart, name="showcart"),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
