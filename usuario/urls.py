from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

    #Pagina principal
    path('',views.IndexView.as_view(), name='index'),
    path('categoria/<int:id_categoria>', views.producto_por_categoria, name="categoria"),
    path('acerca_de_nosotros',views.about, name='about'),
    path('detalles_de_producto/<int:id_producto>',views.detalles_producto , name='detalles'),

    #Urls de la cuenta
    path('login',views.LoginUser.as_view(), name='login'),
    path('logout',views.LogoutUser.as_view(), name='logout'),
    path('register',views.register, name='register'),
    path('perfil',views.profile, name='profile'),
    path('editar_usuario',views.editar_usuario, name='editar'),
    
    #Carrito de compra
    path('cart',views.cart, name='cart'),
    path('delete_item/<int:order_item_id>',views.delete_item, name='delete'),
    path('add_item/<int:producto_id>',views.add_item, name='add'),
    path('add_item_qty/<int:order_item_id>',views.add_qty, name='add_qty'),
    path('sub_item_qty/<int:order_item_id>',views.sub_qty, name='sub_qty'),
    path('checkout',views.checkout, name='checkout'),

]
