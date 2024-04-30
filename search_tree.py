class Producto:
    def __init__(self, codigo, nombre, descripcion, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

class NodoProducto:
    def __init__(self, producto):
        self.producto = producto
        self.izquierda = None
        self.derecha = None

def insertar_producto(raiz, producto):
    if raiz is None:
        return NodoProducto(producto)
    else:
        if producto.codigo < raiz.producto.codigo:
            raiz.izquierda = insertar_producto(raiz.izquierda, producto)
        else:
            raiz.derecha = insertar_producto(raiz.derecha, producto)
    return raiz

def preorden(raiz):
    if raiz:
        print(raiz.producto.nombre)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

def inorden(raiz):
    if raiz:
        inorden(raiz.izquierda)
        print(raiz.producto.nombre)
        inorden(raiz.derecha)

def postorden(raiz):
    if raiz:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.producto.nombre)

def buscar_producto(raiz, codigo):
    if raiz is None or raiz.producto.codigo == codigo:
        return raiz
    if raiz.producto.codigo < codigo:
        return buscar_producto(raiz.derecha, codigo)
    return buscar_producto(raiz.izquierda, codigo)

def reemplazar_nodo(raiz, codigo, nuevo_producto):
    if raiz is None:
        return None
    if raiz.producto.codigo == codigo:
        raiz.producto = nuevo_producto
    elif raiz.producto.codigo < codigo:
        raiz.derecha = reemplazar_nodo(raiz.derecha, codigo, nuevo_producto)
    else:
        raiz.izquierda = reemplazar_nodo(raiz.izquierda, codigo, nuevo_producto)
    return raiz

def eliminar_producto(raiz, codigo):
    if raiz is None:
        return None
    if codigo < raiz.producto.codigo:
        raiz.izquierda = eliminar_producto(raiz.izquierda, codigo)
    elif codigo > raiz.producto.codigo:
        raiz.derecha = eliminar_producto(raiz.derecha, codigo)
    else:
        if raiz.izquierda is None:
            temp = raiz.derecha
            raiz = None
            return temp
        elif raiz.derecha is None:
            temp = raiz.izquierda
            raiz = None
            return temp
        temp = encontrar_minimo(raiz.derecha)
        raiz.producto = temp.producto
        raiz.derecha = eliminar_producto(raiz.derecha, temp.producto.codigo)
    return raiz

def encontrar_minimo(raiz):
    actual = raiz
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual

