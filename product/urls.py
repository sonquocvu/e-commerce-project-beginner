from django.urls import path

from product import views

urlpatterns = [
    path('products/search/', views.search),
    path('latest-products/', views.ProductViewList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductViewDetail.as_view()),
    path('category/<slug:category_slug>/', views.CategoryViewDetail.as_view())
]