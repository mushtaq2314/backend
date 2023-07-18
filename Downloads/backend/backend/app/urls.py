from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'), 
    path('index',views.index,name='index'), 
    path('shirts',views.shirts,name='shirts'), 
    path('pants',views.pants,name='pants'), 
    path('kurtas',views.kurtas,name='kurtas'), 
    path('rental',views.rental,name='rental'), 
    path('shopnow',views.shopnow,name='shopnow'), 
    path('contact',views.contact,name='contact'), 
    path('customization_front',views.customization_front,name='customization_front'), 
    path('customization',views.customization,name='customization'), 
    path('customization2',views.customization2,name='customization2'), 
    path('individual_item_layout',views.individual_item_layout,name='individual_item_layout'), 
    path('individual_item_layout2',views.individual_item_layout2,name='individual_item_layout2'), 
    path('user',views.user,name='user'), 
    path('user2',views.user2,name='user2'), 
    path('buy',views.buy,name='buy'), 
    path('buy2',views.buy2,name='buy2'), 

    path('login',views.loginUser,name='login'),   
     path('signup',views.signupUser,name='signup'), 
    path('login2',views.loginUser2,name='login2'),   
     path('signup2',views.signupUser2,name='signup2'), 
]
