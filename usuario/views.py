from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfil, Producto, Categoria, OrderItem, Order
from django.views import generic
from .forms import CustomUserCreationForm, CustomLoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     productos = Producto.objects.order_by('id')
#     context = {'productos': productos}
#     return render(request, 'usuario/index.html', context)

class IndexView(generic.ListView):
    template_name = 'usuario/index.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.order_by('id')
    
def producto_por_categoria(request,id_categoria):
    categoria = get_object_or_404(Categoria, pk= id_categoria)
    productos = Producto.objects.filter(categoria_id=id_categoria)
    return render(request, 'usuario/categoria.html', {'productos':productos, 'categoria':categoria})

def detalles_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    categoria = Categoria.objects.get(pk=producto.categoria_id)
    return render(request, 'usuario/detalles_prod.html', {'producto':producto, 'categoria':categoria})

def about(request):
    return render(request, 'usuario/about.html')

class LoginUser(LoginView):
    template_name = "usuario/login.html"
    authentication_form = CustomLoginForm

class LogoutUser(LogoutView):
    pass

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            user = User.objects.get(username=request.POST.get("username"))
            perfil = Perfil(usuario=user, 
                            nombre=request.POST.get("nombre"),
                            apellido=request.POST.get("apellido"),
                            email=request.POST.get("correo"),
                            provincia=request.POST.get("provincia"),
                            ciudad=request.POST.get("ciudad"),
                            direccion=request.POST.get("direccion"),
                            celular=request.POST.get("celular"),
                            )
            perfil.save()
            messages.success(request, 'Te has registrado con exito')
            return redirect("/login")
        
        
    return render(request, 'usuario/register.html', {'form':form,})

def profile(request):
    return render(request, 'usuario/profile.html')

def editar_usuario(request):
    perfil = Perfil.objects.get(usuario_id = request.user.id)
    form = ProfileForm(instance=perfil)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=perfil)
        if form.is_valid:
            form.save()
            return redirect("/perfil")
    return render(request, 'usuario/editar.html', {'form':form})

def cart(request):  
    perfil = request.user.perfil
    order, created = Order.objects.get_or_create(perfil=perfil, orden_completada=False)
    items = order.orderitem_set.all()

    return render(request, 'usuario/cart.html', {'items':items, 'order':order} )

def delete_item(request, order_item_id):
    item = get_object_or_404(OrderItem, pk=order_item_id)
    item.delete()
    return redirect("/cart")


def add_item(request, producto_id):
    if request.user.is_authenticated:
        perfil = request.user.perfil
        producto = Producto.objects.get(pk=producto_id)
        order, created = Order.objects.get_or_create(perfil=perfil, orden_completada=False)
        order_item = OrderItem.objects.get_or_create(producto=producto, order=order)
        return redirect("/cart")
    else:
        messages.error(request, "Necesitas entrar a tu cuenta para agregar articulos")
        return redirect("/login")

def add_qty(request, order_item_id):
    item = get_object_or_404(OrderItem, pk=order_item_id)
    item.cantidad += 1
    item.save()
    return redirect("/cart")

def sub_qty(request, order_item_id):
    item = get_object_or_404(OrderItem, pk=order_item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
        
    return redirect("/cart")

def checkout(request):
    # order = Order.objects.get(perfil= )
    return render(request, 'usuario/checkout.html' )

    