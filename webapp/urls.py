from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home' ),
    path('logout/', views.logout_user, name='logout'),
    # path('register', views.register_user, name='register'),
    # path('create-cat/<str:category>', views.create_category, name='create-category'),
    path('category/', views.category_list, name='category-list'),
    path('products/', views.products_view, name='products-view'),
    path('products/<int:pk>/', views.product_view, name='product-view'),
    path('add-product/', views.add_product, name='add-product1'),
    path('exercise/', views.exercise_view, name='exercise-view'),
    path('create/', views.create_exercise, name='create_exercise'),
    path('create/category/', views.create_category, name='create_category'),
    path('create/product/', views.create_product, name='create_product'),
    
]
