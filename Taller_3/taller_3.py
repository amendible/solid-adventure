CLIENTES_CSV = "clientes.csv"
PEDIDOS_CSV = "pedidos.csv"
VENTAS_CSV = "ventas.csv"

#Utilidades de archivo 
def archivo_existe(nombre):
    try:
        f = open(nombre, "r", encoding="utf-8")
        f.close()
        return True
    except:
        return False

def crear_si_no_existe(nombre, cabecera):
    if not archivo_existe(nombre):
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(cabecera + "\n")

def leer_lineas(nombre):
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            return f.readlines()
    except:
        return []

def escribir_lineas(nombre, lineas):
    with open(nombre, "w", encoding="utf-8") as f:
        for l in lineas:
            f.write(l)

def siguiente_id(nombre, campo_id):
    lineas = leer_lineas(nombre)
    if len(lineas) <= 1:
        return 1
    maxid = 0
    for i in range(1, len(lineas)):
        arr = lineas[i].strip().split(",")
        try:
            val = int(arr[0])
            if val > maxid:
                maxid = val
        except:
            pass
    return maxid + 1

#Inicialización 
def inicializar():
    crear_si_no_existe(CLIENTES_CSV, "id_cliente,nombre,apellido,telefono,activo")
    crear_si_no_existe(PEDIDOS_CSV, "id_pedido,id_cliente,producto,precio,cantidad,activo")
    crear_si_no_existe(VENTAS_CSV, "id_venta,id_cliente,producto,cantidad,precio_unitario,activo")

#Operaciones
def registrar_cliente():
    idc = str(siguiente_id(CLIENTES_CSV, "id_cliente"))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    linea = ",".join([idc, nombre, apellido, telefono, "1"]) + "\n"
    with open(CLIENTES_CSV, "a", encoding="utf-8") as f:
        f.write(linea)
    print("Cliente registrado con ID", idc)

def listar_clientes():
    lineas = leer_lineas(CLIENTES_CSV)
    if len(lineas) <= 1:
        print("No hay clientes.")
        return
    for i in range(len(lineas)):
        print(lineas[i].strip())

def eliminar_cliente():
    idc = input("ID de cliente a eliminar (lógico): ")
    lineas = leer_lineas(CLIENTES_CSV)
    nuevas = []
    for i in range(len(lineas)):
        if i == 0:
            nuevas.append(lineas[i])
        else:
            arr = lineas[i].strip().split(",")
            if arr[0] == idc:
                arr[4] = "0"
            nuevas.append(",".join(arr) + "\n")
    escribir_lineas(CLIENTES_CSV, nuevas)
    print("Cliente marcado como inactivo.")

def registrar_pedido():
    idp = str(siguiente_id(PEDIDOS_CSV, "id_pedido"))
    idc = input("ID cliente: ")
    producto = input("Producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    linea = ",".join([idp, idc, producto, precio, cantidad, "1"]) + "\n"
    with open(PEDIDOS_CSV, "a", encoding="utf-8") as f:
        f.write(linea)
    print("Pedido registrado con ID", idp)

def listar_pedidos_cliente():
    idc = input("ID cliente: ")
    lineas = leer_lineas(PEDIDOS_CSV)
    for i in range(1, len(lineas)):
        arr = lineas[i].strip().split(",")
        if arr[1] == idc:
            print(lineas[i].strip())

def guardar_venta():
    idv = str(siguiente_id(VENTAS_CSV, "id_venta"))
    idc = input("ID cliente: ")
    producto = input("Producto: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio unitario: ")
    linea = ",".join([idv, idc, producto, cantidad, precio, "1"]) + "\n"
    with open(VENTAS_CSV, "a", encoding="utf-8") as f:
        f.write(linea)
    print("Venta registrada con ID", idv)

def listar_ventas_cliente():
    nombre = input("Nombre del cliente: ").lower()
    # buscar id(s) de clientes con ese nombre
    clientes = leer_lineas(CLIENTES_CSV)
    ids = []
    for i in range(1, len(clientes)):
        arr = clientes[i].strip().split(",")
        if nombre in arr[1].lower() or nombre in arr[2].lower():
            ids.append(arr[0])
    if not ids:
        print("Cliente no encontrado.")
        return
    ventas = leer_lineas(VENTAS_CSV)
    total = 0.0
    for i in range(1, len(ventas)):
        arr = ventas[i].strip().split(",")
        if arr[1] in ids and arr[5] == "1":
            try:
                cant = float(arr[3])
                precio = float(arr[4])
                parcial = cant * precio
                total += parcial
            except:
                parcial = 0.0
            print("Venta:", arr[2], "x", arr[3], "=", parcial)
    print("Total:", total)

#Menú
def menu():
    inicializar()
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Registrar pedido")
        print("5. Listar pedidos de un cliente")
        print("6. Guardar venta")
        print("7. Listar ventas de un cliente")
        print("8. Salir")
        op = input("Opción: ")
        if op == "1":
            registrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            eliminar_cliente()
        elif op == "4":
            registrar_pedido()
        elif op == "5":
            listar_pedidos_cliente()
        elif op == "6":
            guardar_venta()
        elif op == "7":
            listar_ventas_cliente()
        elif op == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()