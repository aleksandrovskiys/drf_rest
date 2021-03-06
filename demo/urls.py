import store.api_views
import store.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("api/v1/products/", store.api_views.ProductList.as_view()),
    path("api/v1/products/new", store.api_views.ProductCreate.as_view()),
    path("api/v1/products/<int:id>/destroy", store.api_views.ProductDestroy.as_view()),
    path("api/v1/products_generic/<int:id>/", store.api_views.ProductRetrieveUpdateDestroy.as_view()),
    path("api/v1/products/<int:id>/stats", store.api_views.ProductStats.as_view()),
    path("admin/", admin.site.urls),
    path("products/<int:id>/", store.views.show, name="show-product"),
    path("cart/", store.views.cart, name="shopping-cart"),
    path("", store.views.index, name="list-products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
