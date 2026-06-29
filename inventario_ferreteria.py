#Parcial 2 progrmaacion

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Carga inical de stock de herramientas")
    print("2. Visualización de inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualización de stock (Venta / Ingreso)")
    print("7. Salir")
    print("=====================================")


def nombre_existe(inventario, nombre):
    #Verifica si un nombre ya existe en el inventario (sin distinguir mayusculas ni espacios)
    nombre_limpio = nombre.strip().lower()
    for item in inventario:
        if item["herramienta"].strip().lower() == nombre_limpio:
            return True
    return False


def cargar_herramientas(inventario):
    #Opción 1: Carga inicial de herramientas. Solo se ejecuta si el inventario está vacio
    if len(inventario) > 0:
        print("Ya existen herramientas cargadas. Para agregar nuevos productos use la opción 5.")
        return inventario

    while True:
        try:
            cantidad = int(input("¿Cuántas herramientas desea cargar? "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número entero mayor que cero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    cargadas = 0
    while cargadas < cantidad:
        try:
            nombre = input(f"\nHerramienta {cargadas + 1} — Ingrese nombre: ")
            if nombre.strip() == "":
                raise ValueError("El nombre no puede estar vacío.")
            if nombre_existe(inventario, nombre):
                raise ValueError(f"Ya existe una herramienta con el nombre '{nombre.strip()}'.")

            stock = int(input(f"Ingrese stock inicial para '{nombre.strip()}': "))
            if stock < 0:
                raise ValueError("El stock inicial no puede ser negativo.")

            inventario.append({"herramienta": nombre.strip(), "cantidad": stock})
            cargadas += 1
            print(f"✔ '{nombre.strip()}' agregada con stock {stock}.")

        except ValueError as e:
            print(f"Error: {e}. Por favor reintente nuevamente")

    print(f"\nCarga completada. Se registraron {cantidad} herramienta(s).")
    return inventario


def mostrar_inventario(inventario):
    #Opción 2: Muestra todas las herramientas y su stock actual
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    print("\n========== INVENTARIO ==========")
    for i, item in enumerate(inventario, start=1):
        print(f"{i}. {item['herramienta']} — Stock: {item['cantidad']}")
    print("================================")


def consultar_stock(inventario):
    #Opción 3: Busca una herramienta por nombre y muestra su stock
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    nombre = input("Ingrese el nombre de la herramienta a consultar: ")
    nombre_limpio = nombre.strip().lower()

    for item in inventario:
        if item["herramienta"].strip().lower() == nombre_limpio:
            print(f"'{item['herramienta']}' — Stock disponible: {item['cantidad']} unidad(es).")
            return

    print(f"La herramienta '{nombre.strip()}' no se encuentra en el inventario")


def reporte_agotados(inventario):
    #Opción 4: Lista las herramientas con stock igual a cero
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    agotados = []
    for item in inventario:
        if item["cantidad"] == 0:
            agotados.append(item["herramienta"])

    if len(agotados) == 0:
        print("No hay productos agotados.")
    else:
        print("\n========== PRODUCTOS AGOTADOS ==========")
        for nombre in agotados:
            print(f"  - {nombre}")
        print("=========================================")


def alta_producto(inventario):
    #Opción 5: Agrega una única herramienta nueva al inventario
    try:
        nombre = input("Ingrese el nombre de la nueva herramienta: ")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if nombre_existe(inventario, nombre):
            raise ValueError(f"Ya existe una herramienta con el nombre '{nombre.strip()}'.")

        stock = int(input(f"Ingrese stock inicial para '{nombre.strip()}': "))
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        inventario.append({"herramienta": nombre.strip(), "cantidad": stock})
        print(f"✔ '{nombre.strip()}' agregada correctamente con stock {stock}.")

    except ValueError as e:
        print(f"Error: {e}. No se agregó el producto.")

    return inventario


def actualizar_stock(inventario):
    #Opción 6: Permite registrar una venta o un ingreso de mercaderia
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    nombre = input("Ingrese el nombre de la herramienta: ")
    nombre_limpio = nombre.strip().lower()

    indice = -1
    for i, item in enumerate(inventario):
        if item["herramienta"].strip().lower() == nombre_limpio:
            indice = i
            break

    if indice == -1:
        print(f"La herramienta '{nombre.strip()}' no se encuentra en el inventario")
        return

    print(f"\nHerramienta: {inventario[indice]['herramienta']} — Stock actual: {inventario[indice]['cantidad']}")
    print("Tipo de operación:")
    print("  1. Venta (disminuir stock)")
    print("  2. Ingreso (aumentar stock)")

    try:
        tipo = int(input("Seleccione una opción (1 o 2): "))
        if tipo not in (1, 2):
            raise ValueError("Opción inválida. Debe ingresar 1 o 2.")

        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero mayor que cero.")

        if tipo == 1:
            if inventario[indice]["cantidad"] - cantidad < 0:
                raise ValueError(
                    f"Stock insuficiente. Disponible: {inventario[indice]['cantidad']} unidad(es)."
                )
            inventario[indice]["cantidad"] -= cantidad
            print(f"✔ Venta registrada. Stock actualizado: {inventario[indice]['cantidad']} unidad(es).")
        else:
            inventario[indice]["cantidad"] += cantidad
            print(f"✔ Ingreso registrado. Stock actualizado: {inventario[indice]['cantidad']} unidad(es).")

    except ValueError as e:
        print(f"Error: {e}")

# Bloque principal del programa

inventario = []  
opcion = 0

while opcion != 7:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            inventario = cargar_herramientas(inventario)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            consultar_stock(inventario)
        elif opcion == 4:
            reporte_agotados(inventario)
        elif opcion == 5:
            inventario = alta_producto(inventario)
        elif opcion == 6:
            actualizar_stock(inventario)
        elif opcion == 7:
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            raise ValueError("La opción debe estar entre 1 y 7.")
    except ValueError:
        print("Opción inválida. Por favor ingrese un número entre 1 y 7.")
