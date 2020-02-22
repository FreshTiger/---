from django.urls import path, re_path
from. import views

app_name="Home"
urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'HotGoods/', views.HotGoods,name="HotGoods"),
    path(r'notice/', views.notice,name="notice"),
    path(r'comment/', views.comment,name="comment"),
    path(r'register/',views.register,name='register'),
    re_path(r'^goods/(?P<goodsID>[0-9]+)$',views.goods,name='goods'),
    path(r'cart/',views.cart,name='cart'),
    path(r'logOut/',views.logOut,name='logOut'),
    path(r'buy/',views.buy,name='buy'),
    path(r'search/',views.search,name='search')
]

