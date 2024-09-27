from django.shortcuts import get_list_or_404, render, get_object_or_404
from .models import Producto, Categoria

# Diccionario que mapea categorías a sus imágenes
IMAGENES = {
    "gaseosas": {
        "1": "tienda/gaseosas/fanta.jpeg",
        "2": "tienda/gaseosas/coca_cola.jpeg",
        "3": "tienda/gaseosas/7up.jpeg"
    },
    "snacks": {
        "4": "tienda/snacks/cheetos.jpg",
        "5": "tienda/snacks/chizitos.jpg"
    },
    "galletas": {
        "6": "tienda/galletas/picaras.jpeg",
        "7": "tienda/galletas/coronita.jpg"
    },
    "chocolates": {
        "8": "tienda/chocolates/princesa.jpeg",
        "9": "tienda/chocolates/sublime.jpeg",
        "10": "tienda/chocolates/triangulo.jpg"
    }
}

def get_imagen_url(producto):
    categoria = producto.categoria.nombre.lower()
    producto_id = str(producto.id)
    return IMAGENES.get(categoria, {}).get(producto_id, '')

def index(request):
    product_list = Producto.objects.order_by('nombre')
    categorias = Categoria.objects.all()
    
    productos_con_imagenes = []
    for producto in product_list:
        productos_con_imagenes.append({
            'producto': producto,
            'imagen_url': get_imagen_url(producto)
        })
    
    context = {
        'productos_con_imagenes': productos_con_imagenes,
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    
    # Obtener la URL de la imagen del producto
    imagen_url = get_imagen_url(producto)
    
    context = {
        'producto': producto,
        'categorias': categorias,
        'imagen_url': imagen_url
    }
    return render(request, 'producto.html', context)

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    
    productos_con_imagenes = []
    for producto in productos:
        productos_con_imagenes.append({
            'producto': producto,
            'imagen_url': get_imagen_url(producto)
        })
    
    context = {
        'categoria': categoria,
        'productos_con_imagenes': productos_con_imagenes,
        'categorias': categorias,
    }
    return render(request, 'productos_por_categoria.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    
    # Obtener la URL de la imagen del producto
    imagen_url = get_imagen_url(producto)
    
    context = {
        'producto': producto,
        'categorias': categorias,
        'imagen_url': imagen_url
    }
    return render(request, 'detalle_producto.html', context)
