from django.contrib import admin
from .models import Producto,Categoria,Perfil, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    list_display = ('username','is_staff','is_active')

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion de Venta', {'fields':['precio','stock']}),
        ('Informacion del Producto', {'fields':['nombre','descripcion','marca','imagen','categoria']}),
    ]

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','apellido','email','celular')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','orden_completada','perfil')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('producto','order','cantidad')
    list_filter = ('order',)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Producto, ProductAdmin)
admin.site.register(Categoria)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
