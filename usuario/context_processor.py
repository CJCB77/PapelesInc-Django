from .models import Categoria, Order

def procesador_categorias(request):
    categorias = Categoria.objects.order_by('id')
    return {'categorias':categorias}

def procesador_order(request):
    order = Order.objects.filter(perfil= request.user.perfil)
    return {'current_orders': order}