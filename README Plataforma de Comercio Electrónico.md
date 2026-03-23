🛒 E-commerce Simple en Python

Este proyecto es una implementación básica de un sistema de comercio electrónico en consola utilizando Python. Permite gestionar productos, usuarios, carrito de compras y pedidos.

🚀 Funcionalidades

El sistema incluye las siguientes características:

👤 Registro de usuarios
📦 Visualización de productos disponibles
🔍 Búsqueda de productos por nombre
🛒 Carrito de compras
💳 Procesamiento de compras
📜 Historial de pedidos
🧠 Estructura del Sistema
📦 Productos

Los productos están definidos como una lista de diccionarios con la siguiente información:

id: Identificador único
nombre: Nombre del producto
precio: Precio en dólares
stock: Cantidad disponible
categoria: Categoría del producto
👤 Usuarios

Los usuarios se almacenan en una lista simple con:

Nombre
Email
🛒 Carrito

El carrito guarda los IDs de los productos que el usuario desea comprar.

📜 Pedidos

Cada pedido contiene:

Usuario que realizó la compra
Lista de productos comprados
Total de la compra
⚙️ Funciones Principales
registrar_usuario(nombre, email)

Registra un nuevo usuario en el sistema.

mostrar_productos()

Muestra todos los productos disponibles con su precio y stock.

buscar_producto(texto)

Permite buscar productos por nombre (búsqueda parcial).

agregar_al_carrito(producto_id)

Agrega un producto al carrito mediante su ID.

comprar(usuario)

Procesa la compra:

Verifica stock
Calcula el total
Descuenta inventario
Registra el pedido
ver_pedidos()

Muestra todos los pedidos realizados.

▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
🖥️ Menú del sistema

El programa funciona mediante un menú interactivo:

1. Registrar usuario
2. Ver productos
3. Buscar producto
4. Agregar al carrito
5. Comprar
6. Ver pedidos
7. Salir
📌 Ejemplo de uso
Opción: 1
Nombre: Juan
Email: juan@email.com

Opción: 2
1 Laptop $ 800 Stock: 5

Opción: 4
ID producto: 1

Opción: 5
Compra realizada. Total: 800
⚠️ Limitaciones

Este proyecto es una versión simplificada y tiene algunas limitaciones:

❌ No hay persistencia de datos (todo se pierde al cerrar el programa)
❌ No hay validación avanzada de entradas
❌ No maneja múltiples usuarios simultáneamente
❌ El carrito es global (no por usuario)
🛠️ Posibles mejoras
💾 Guardar datos en archivos o base de datos
🔐 Sistema de autenticación (login)
🛒 Carrito independiente por usuario
📊 Reportes de ventas
🌐 Interfaz web con Flask o Django
