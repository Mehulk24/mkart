from django.urls import path
from Mkart import views

urlpatterns = [
    path("",views.index,name='home'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.hlogin,name="login"),
    path('logout/',views.my_logout,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete-item/<int:product_id>/', views.remove_from_cart, name='delete_from_cart'),
    path('man-product/',views.man_product,name="man-product"),
    path('woman-product/',views.woman_product,name="woman-product"),
    path('kids-product/',views.kids_product,name="kids-product"),

]