from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home),
    path("user_likes",views.likes,name='likes'),
    path("<slug:card_id>/add",views.like,name='add'),
    path("sign_up",views.sign_up,name="signUp"),
    path("logout",views.logoutt,name="logout"),
    path("add_card",views.add_card,name="addCard"),
    path('<int:pk>/update',views.Update.as_view(), name="update"),
    path("login",views.sign_in),
]