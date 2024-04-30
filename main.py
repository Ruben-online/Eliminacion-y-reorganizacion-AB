from search_tree import *

raiz = None

while True:
    print("Menu principal")
    print("1. Insertar más productos")
    print("2. Mostrar los tres recorridos")
    print("3. Buscar un producto en específico")
    print("4. Reemplazar un producto en específico")
    print("5. Eliminar un producto")
    print("6. Mostrar los productos según el orden binario")
    print("7. Salir")

    main_menu = input("Ingrese una opción (1-7): ")

    if main_menu == "1":
        codigo = int(input("Ingrese el código del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nuevo_producto = Producto(codigo, nombre, descripcion, precio, cantidad)
        raiz = insertar_producto(raiz, nuevo_producto)
        print("Producto insertado correctamente.")

    elif main_menu == "2":
        print("Recorrido Preorden:")
        preorden(raiz)
        print("\nRecorrido Inorden:")
        inorden(raiz)
        print("\nRecorrido Postorden:")
        postorden(raiz)

    elif main_menu == "3":
        codigo_buscar = int(input("Ingrese el código del producto a buscar: "))
        producto_encontrado = buscar_producto(raiz, codigo_buscar)
        if producto_encontrado:
            print("Producto encontrado:")
            print("Código:", producto_encontrado.producto.codigo)
            print("Nombre:", producto_encontrado.producto.nombre)
            print("Descripción:", producto_encontrado.producto.descripcion)
            print("Precio:", producto_encontrado.producto.precio)
            print("Cantidad:", producto_encontrado.producto.cantidad)
        else:
            print("Producto no encontrado.")

    elif main_menu == "4":
        codigo_reemplazar = int(input("Ingrese el código del producto a reemplazar: "))
        producto_reemplazo = buscar_producto(raiz, codigo_reemplazar)
        if producto_reemplazo:
            codigo_nuevo = int(input("Ingrese el nuevo código del producto: "))
            nombre_nuevo = input("Ingrese el nuevo nombre del producto: ")
            descripcion_nueva = input("Ingrese la nueva descripción del producto: ")
            precio_nuevo = float(input("Ingrese el nuevo precio del producto: "))
            cantidad_nueva = int(input("Ingrese la nueva cantidad del producto: "))
            nuevo_producto = Producto(codigo_nuevo, nombre_nuevo, descripcion_nueva, precio_nuevo, cantidad_nueva)
            raiz = reemplazar_nodo(raiz, codigo_reemplazar, nuevo_producto)
            print("Producto reemplazado correctamente.")
        else:
            print("Producto no encontrado.")

    elif main_menu == "5":
        codigo_eliminar = int(input("Ingrese el código del producto a eliminar: "))
        raiz = eliminar_producto(raiz, codigo_eliminar)
        print("Producto eliminado correctamente.")

    elif main_menu == "6":
        print("Recorrido Inorden:")
        inorden(raiz)

    elif main_menu == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")

