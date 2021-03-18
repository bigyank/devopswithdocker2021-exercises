from django.urls import path
from . import views
aap_name = "accounts"
urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('searchpage/',views.SearchResultsView.as_view(), name = 'searchpage'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

    
    path("doctor/", views.doctor, name="doctor"),
    path("doctorprofile/<int:id>/", views.doctorprofile, name="doctorprofile"),
    path("ambulance/", views.ambulance, name="ambulance"),
    path('product/<int:id>/', views.product, name="product"), 
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("update_item/",views.updateItem, name= "update_item"),
    path("process_order/",views.processOrder, name= "process_order")


]