from django.urls import path
from webapp import views

urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('productpage/',views.product_page,name='productpage'),
    path('singleprod/<int:prodid>/',views.single_product,name='singleprod'),
    path('filteredpro/<cat_name>/',views.filtered_product,name='filteredpro'),
    path('aboutpage/',views.aboutpage,name='aboutpage'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('savecontact/',views.savecontact,name='savecontact'),
    path('registration_page/',views.registration_page,name='registration_page'),
    path('registerdata/',views.registerdata,name='registerdata'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('cartpage/',views.cartpage,name='cartpage'),
    path('savecartpage/',views.savecartpage,name='savecartpage'),
    path('delete_pro/<int:dataid>/',views.delete_pro,name='delete_pro'),
    path('Checkout_page/',views.Checkout_page,name='Checkout_page'),
    path('checkoutsummary/',views.checkoutsummary,name='checkoutsummary'),

]