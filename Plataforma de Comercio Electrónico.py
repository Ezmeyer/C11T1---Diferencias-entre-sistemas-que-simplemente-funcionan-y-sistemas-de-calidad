# ==============================
# ECOMMERCE SIMPLE
# ==============================

# Productos disponibles
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 800, "stock": 5, "categoria": "Tecnologia"},
    {"id": 2, "nombre": "Mouse", "precio": 20, "stock": 10, "categoria": "Tecnologia"},
    {"id": 3, "nombre": "Teclado", "precio": 50, "stock": 7, "categoria": "Tecnologia"}
]

usuarios = []
pedidos = []
carrito = []


# ------------------------------
# Registro de usuario
# ------------------------------
def registrar_usuario(nombre, email):
    usuarios.append({"nombre": nombre, "email": email})


# ------------------------------
# Mostrar productos
# ------------------------------
def mostrar_productos():
    for p in productos:
        print(p["id"], p["nombre"], "$", p["precio"], "Stock:", p["stock"])


# ------------------------------
# Buscar productos
# ------------------------------
def buscar_producto(texto):
    for p in productos:
        if texto.lower() in p["nombre"].lower():
            print(p["id"], p["nombre"], "$", p["precio"])


# ------------------------------
# Carrito de compras
# ------------------------------
def agregar_al_carrito(producto_id):
    carrito.append(producto_id)


# ------------------------------
# Procesar compra
# ------------------------------
def comprar(usuario):
    total = 0

    for idp in carrito:
        for p in productos:
            if p["id"] == idp:
                if p["stock"] <= 0:
                    print("Producto sin stock:", p["nombre"])
                    return
                total += p["precio"]

    # Descontar inventario
    for idp in carrito:
        for p in productos:
            if p["id"] == idp:
                p["stock"] -= 1

    pedidos.append({
        "usuario": usuario,
        "productos": carrito.copy(),
        "total": total
    })

    carrito.clear()
    print("Compra realizada. Total:", total)


# ------------------------------
# Ver pedidos
# ------------------------------
def ver_pedidos():
    for p in pedidos:
        print("Usuario:", p["usuario"])
        print("Total:", p["total"])
        print("Productos:", p["productos"])
        print("-----")


# ------------------------------
# MENÚ PRINCIPAL
# ------------------------------
def main():
    usuario_actual = "Invitado"

    while True:
        print("\n1. Registrar usuario")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Agregar al carrito")
        print("5. Comprar")
        print("6. Ver pedidos")
        print("7. Salir")

        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            registrar_usuario(nombre, email)
            usuario_actual = nombre

        elif op == "2":
            mostrar_productos()

        elif op == "3":
            texto = input("Buscar: ")
            buscar_producto(texto)

        elif op == "4":
            idp = int(input("ID producto: "))
            agregar_al_carrito(idp)

        elif op == "5":
            comprar(usuario_actual)

        elif op == "6":
            ver_pedidos()

        elif op == "7":
            break


if __name__ == "__main__":
    main()