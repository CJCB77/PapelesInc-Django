from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    marca = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre

    def en_stock(self):
        return self.stock > 0
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    provincia = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    celular = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.usuario.username

class Order(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)
    fecha_del_pedido = models.DateTimeField(auto_now_add=True)
    orden_completada = models.BooleanField("completada",default="False")

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        cart_total = sum([item.get_total for item in order_items])
        return cart_total
    
    @property
    def get_cart_items_quantity(self):
        order_items = self.orderitem_set.all()
        total_quantity = sum([item.cantidad for item in order_items])
        return total_quantity

class OrderItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=1, null=True, blank=True)

    @property
    def get_total(self):
        total = self.cantidad * self.producto.precio
        return total
    def __str__(self):
        return self.producto.nombre
    





