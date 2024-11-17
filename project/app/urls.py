from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.logIn,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('change_password/',views.change_password,name='change_password')
    ,path('change_password_without_old_password/',views.set_password,name='Change_Password_Without_Old_Password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('add_album/',views.add_album,name='add_album'),
    path('add_musician/',views.add_musician,name='add_musician'),
    path('edit_album/<int:id>',views.edit_album,name='edit_album'),
    path('delete_album/<int:id>',views.delete_album,name='delete_album'),
    path('edit_albums/',views.edit_albums,name='edit_albums')
]