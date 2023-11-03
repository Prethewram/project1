from django.urls import path
from Myapp import views


urlpatterns = [
    path('mypage/',views.mypage,name="mypage"),
    path('addcat/',views.category,name='addcat'),
    path('savedata/',views.savedata,name='savedata'),
    path('display/',views.disdata,name='display'),
    path('editcat/<int:dataid>',views.editcat,name='editcat'),
    path('deletecat/<int:dataid>',views.deletecat,name='deletecat'),
    path('updatedata/<int:dataid>',views.updatedata,name='updatedata'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('savepro/',views.saveproduct,name='savepro'),
    path('dispro/',views.displayproduct,name='dispro'),
    path('editpro/<int:dataid>/',views.editproduct,name='editpro'),
    path('deletepro/<int:dataid>/',views.deleteproduct,name='deletepro'),
    path('updatepro/<int:dataid>/',views.updateproduct,name='updatepro'),
    path('adminlog/',views.adminlogin,name='adminlog'),
    path('admlog/',views.admlog,name='admlog'),
    path('logout/',views.adminlogout,name='logout'),
    path('displaycontact/',views.displaycontact,name='displaycontact'),

]