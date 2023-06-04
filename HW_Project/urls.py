from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from products.views import MainPageCBV, ProductCBV, ProductDetailCBV, product_create_view, review_create_view
from HW_Project import settings

from users.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('products/', ProductCBV.as_view()),
    path('products/create/', product_create_view),
    path('review/create/', review_create_view),
    path('products/<int:id>/', ProductDetailCBV.as_view()),
    path('users/login/', login_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


