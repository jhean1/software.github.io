from colorama import Fore, Style, init
import os
import time
import platform

# Inicializar colorama
init(autoreset=True)

# Variables para almacenar datos
inventario = []
clientes = []
historial = []

# Arte para menú proyecto
arte_ascii = """

 
  /$$$$$$  /$$       /$$      /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$   /$$       /$$$$$$$  /$$$$$$$$        /$$$$$$   /$$$$$$  /$$       /$$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$       
 /$$__  $$| $$      | $$$    /$$$ /$$__  $$ /$$__  $$| $$_____/| $$$ | $$      | $$__  $$| $$_____/       /$$__  $$ /$$__  $$| $$      |_____ $$  /$$__  $$| $$__  $$ /$$__  $$      
| $$  \ $$| $$      | $$$$  /$$$$| $$  \ $$| $$  \__/| $$      | $$$$| $$      | $$  \ $$| $$            | $$  \__/| $$  \ $$| $$           /$$/ | $$  \ $$| $$  \ $$| $$  \ $$      
| $$$$$$$$| $$      | $$ $$/$$ $$| $$$$$$$$| $$      | $$$$$   | $$ $$ $$      | $$  | $$| $$$$$         | $$      | $$$$$$$$| $$          /$$/  | $$$$$$$$| $$  | $$| $$  | $$      
| $$__  $$| $$      | $$  $$$| $$| $$__  $$| $$      | $$__/   | $$  $$$$      | $$  | $$| $$__/         | $$      | $$__  $$| $$         /$$/   | $$__  $$| $$  | $$| $$  | $$      
| $$  | $$| $$      | $$\  $ | $$| $$  | $$| $$    $$| $$      | $$\  $$$      | $$  | $$| $$            | $$    $$| $$  | $$| $$        /$$/    | $$  | $$| $$  | $$| $$  | $$      
| $$  | $$| $$$$$$$$| $$ \/  | $$| $$  | $$|  $$$$$$/| $$$$$$$$| $$ \  $$      | $$$$$$$/| $$$$$$$$      |  $$$$$$/| $$  | $$| $$$$$$$$ /$$$$$$$$| $$  | $$| $$$$$$$/|  $$$$$$/      
|__/  |__/|________/|__/     |__/|__/  |__/ \______/ |________/|__/  \__/      |_______/ |________/       \______/ |__/  |__/|________/|________/|__/  |__/|_______/  \______/       
                                                                                                                                                                                     
                                                                                                                                                                                     
                                                                                                                                                                                     
                                                       /$$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$$  /$$$$$$                                                                      
                                                      |__  $$__/ /$$__  $$| $$__  $$|_  $$_/|__  $$__/ /$$__  $$                                                                     
                                                         | $$   | $$  \ $$| $$  \ $$  | $$     | $$   | $$  \ $$                                                                     
                                                         | $$   | $$$$$$$$| $$$$$$$/  | $$     | $$   | $$$$$$$$                                                                     
                                                         | $$   | $$__  $$| $$____/   | $$     | $$   | $$__  $$                                                                     
                                                         | $$   | $$  | $$| $$        | $$     | $$   | $$  | $$                                                                     
                                                         | $$   | $$  | $$| $$       /$$$$$$   | $$   | $$  | $$                                                                     
                                                         |__/   |__/  |__/|__/      |______/   |__/   |__/  |__/                                                                     
                                                                                                                                                                                     
                                                                                                                                                                                     
                                                                                                                                                                                     

                                                                                                                                                                        
                                                                                                                                                                        
"""

print(Fore.GREEN + arte_ascii)
time.sleep(3.2)
print("Cargando programa.")
time.sleep(2)
print("Cargando programa. .")
time.sleep(2)
print("Cargando programa. . .")
time.sleep(2)
print("Carga completada!")
time.sleep(2)

def clear_screen():
    # Limpiar pantalla según sistema operativo
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def verificar_referencia_talla(referencia, talla):
    """Verifica si ya existe la combinación de referencia y talla"""
    for item in inventario:
        if item["referencia"] == referencia and item["talla"] == talla:
            return True
    return False

def calcular_precio_venta(porcentaje_utilidad, precio_base):
    """Calcula el precio de venta automáticamente"""
    return precio_base * (1 + porcentaje_utilidad / 100)

def submenu():
    while True:
        clear_screen()
        print(Fore.GREEN + "Registro de Producción".center(80))
        print(Fore.YELLOW + "0. Volver al menú principal".center(80))
        
        opcion = input(Fore.CYAN + "Presione Enter para continuar o 0 para volver: ")
        if opcion == "0":
            return
        
        referencia = input(Fore.CYAN + "Ingrese la referencia: ")
        if not referencia:
            print(Fore.RED + "La referencia no puede estar vacía.".center(80))
            time.sleep(2)
            continue
        
        # Solicitar talla sin restricciones
        talla = input(Fore.CYAN + "Ingrese la talla: ")
        if not talla:
            print(Fore.RED + "La talla no puede estar vacía.".center(80))
            time.sleep(2)
            continue
        
        # Verificar si la combinación de referencia y talla ya existe
        if verificar_referencia_talla(referencia, talla):
            print(Fore.RED + f"Ya existe un producto con referencia {referencia} y talla {talla}.".center(80))
            time.sleep(3)
            continue
        
        descripcion = input(Fore.CYAN + "Ingrese la descripción: ")
        
        try:
            precio_base = float(input(Fore.CYAN + "Ingrese el precio base: "))
            porcentaje_utilidad = float(input(Fore.CYAN + "Ingrese el porcentaje de utilidad: "))
            # Se eliminó la solicitud de saldo inicial
        except ValueError:
            print(Fore.RED + "Error: Por favor ingrese valores numéricos válidos.".center(80))
            time.sleep(3)
            continue
        
        # Calcular precio de venta automáticamente
        precio_venta = calcular_precio_venta(porcentaje_utilidad, precio_base)
        
        # Guardar en inventario (con saldo inicial 0)
        inventario.append({
            "referencia": referencia,
            "talla": talla,
            "descripcion": descripcion,
            "precio_base": precio_base,
            "porcentaje_utilidad": porcentaje_utilidad,
            "precio_venta": precio_venta,
            "saldo": 0  # El saldo inicial ahora es siempre 0
        })
        
        # Guardar en historial
        historial.append({
            "tipo": "producción",
            "referencia": referencia,
            "talla": talla,
            "descripcion": descripcion,
            "precio_base": precio_base,
            "porcentaje_utilidad": porcentaje_utilidad,
            "precio_venta": precio_venta,
            "saldo_inicial": 0  # El saldo inicial ahora es siempre 0
        })
        
        print(Fore.GREEN + f"Producto registrado correctamente.".center(80))
        print(Fore.GREEN + f"Precio de venta calculado: ${precio_venta:.2f}".center(80))
        time.sleep(3)

def guardar():
    while True:
        clear_screen()
        print(Fore.BLUE + "Registro de Cliente".center(80))
        print(Fore.YELLOW + "0. Volver al menú principal".center(80))
        
        opcion = input(Fore.CYAN + "Presione Enter para continuar o 0 para volver: ")
        if opcion == "0":
            return
        
        # Proceso de validación de ID cliente
        id_valido = False
        while not id_valido:
            cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ")
            if not cliente_id:
                print(Fore.RED + "El ID no puede estar vacío.".center(80))
                time.sleep(2)
                continue
                
            # Verificar si el ID ya existe
            id_existente = False
            for cliente in clientes:
                if cliente["id"] == cliente_id:
                    print(Fore.RED + f"Ya existe un cliente con ID {cliente_id}. Por favor ingrese otro ID.".center(80))
                    time.sleep(2)
                    id_existente = True
                    break
            
            if not id_existente:
                id_valido = True
        
        nombre_completo = input(Fore.CYAN + "Ingrese el nombre completo: ")
        telefono = input(Fore.CYAN + "Ingrese el teléfono: ")
        
        # Guardar en clientes
        clientes.append({
            "id": cliente_id,
            "nombre": nombre_completo,
            "telefono": telefono
        })
        
        # Guardar en historial
        historial.append({
            "tipo": "cliente",
            "id": cliente_id,
            "nombre": nombre_completo,
            "telefono": telefono
        })
        
        print(Fore.BLUE + f"Cliente registrado: {nombre_completo} (ID: {cliente_id})".center(80))
        time.sleep(3)

def buscar_producto(referencia, talla):
    """Busca un producto por referencia y talla"""
    for item in inventario:
        if item["referencia"] == referencia and item["talla"] == talla:
            return item
    return None

def compra():
    while True:
        clear_screen()
        print(Fore.RED + "Transacciones".center(80))
        print(Fore.YELLOW + "1. Compra (Entrada)".center(80))
        print(Fore.YELLOW + "2. Venta (Salida)".center(80))
        print(Fore.YELLOW + "0. Volver al menú principal".center(80))
        
        try:
            opcion_transaccion = input(Fore.CYAN + "Seleccione una opción: ")
            if opcion_transaccion == "0":
                return
            opcion_transaccion = int(opcion_transaccion)
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido.".center(80))
            time.sleep(3)
            continue
        
        if opcion_transaccion == 1:
            # Compra (Entrada)
            referencia = input(Fore.CYAN + "Ingrese la referencia: ")
            
            # Solicitar talla sin restricciones
            talla = input(Fore.CYAN + "Ingrese la talla: ")
            if not talla:
                print(Fore.RED + "La talla no puede estar vacía.".center(80))
                time.sleep(2)
                continue
            
            producto = buscar_producto(referencia, talla)
            if not producto:
                print(Fore.RED + f"No se encontró el producto con referencia {referencia} y talla {talla}.".center(80))
                print(Fore.YELLOW + "Primero debe registrar el producto en 'Registro de producción'.".center(80))
                time.sleep(3)
                continue
            
            try:
                cantidad = int(input(Fore.CYAN + "Ingrese la cantidad a comprar: "))
                if cantidad <= 0:
                    print(Fore.RED + "La cantidad debe ser mayor a cero.".center(80))
                    time.sleep(2)
                    continue
            except ValueError:
                print(Fore.RED + "Cantidad inválida.".center(80))
                time.sleep(3)
                continue
            
            # Actualizar saldo en inventario
            producto["saldo"] += cantidad
            
            # Guardar en historial
            historial.append({
                "tipo": "compra",
                "referencia": referencia,
                "talla": talla,
                "cantidad": cantidad,
                "nuevo_saldo": producto["saldo"]
            })
            
            print(Fore.GREEN + f"Compra registrada correctamente. Nuevo saldo: {producto['saldo']}".center(80))
            time.sleep(3)
        
        elif opcion_transaccion == 2:
            # Venta (Salida)
            cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ")
            
            # Verificar si el cliente existe
            cliente_encontrado = False
            for cliente in clientes:
                if cliente["id"] == cliente_id:
                    cliente_encontrado = True
                    break
            
            if not cliente_encontrado:
                print(Fore.RED + f"No se encontró el cliente con ID {cliente_id}.".center(80))
                time.sleep(3)
                continue
            
            referencia = input(Fore.CYAN + "Ingrese la referencia: ")
            
            # Solicitar talla sin restricciones
            talla = input(Fore.CYAN + "Ingrese la talla: ")
            if not talla:
                print(Fore.RED + "La talla no puede estar vacía.".center(80))
                time.sleep(2)
                continue
            
            producto = buscar_producto(referencia, talla)
            if not producto:
                print(Fore.RED + f"El producto con referencia {referencia} y talla {talla} no está disponible.".center(80))
                time.sleep(3)
                continue
            
            try:
                unidades = int(input(Fore.CYAN + "Ingrese el número de unidades: "))
                if unidades <= 0:
                    print(Fore.RED + "Las unidades deben ser mayores a cero.".center(80))
                    time.sleep(2)
                    continue
            except ValueError:
                print(Fore.RED + "Valor inválido.".center(80))
                time.sleep(3)
                continue
            
            # Verificar stock disponible
            if producto["saldo"] < unidades:
                print(Fore.RED + f"Stock insuficiente. Disponible: {producto['saldo']} unidades".center(80))
                time.sleep(3)
                continue
            
            # Calcular valor a pagar automáticamente
            valor_a_pagar = unidades * producto["precio_venta"]
            
            # Actualizar saldo en inventario
            producto["saldo"] -= unidades
            
            # Guardar en historial
            historial.append({
                "tipo": "venta",
                "cliente_id": cliente_id,
                "referencia": referencia,
                "talla": talla,
                "unidades": unidades,
                "valor_a_pagar": valor_a_pagar,
                "nuevo_saldo": producto["saldo"]
            })
            
            print(Fore.GREEN + "Venta registrada correctamente.".center(80))
            print(Fore.GREEN + f"Valor a pagar: ${valor_a_pagar:.2f}".center(80))
            print(Fore.GREEN + f"Nuevo saldo: {producto['saldo']} unidades".center(80))
            time.sleep(3)
        else:
            print(Fore.RED + "Opción inválida.".center(80))
            time.sleep(3)

def mostrar_historial():
    while True:
        clear_screen()
        print(Fore.MAGENTA + "Historial de Inventario".center(80))
        print(Fore.YELLOW + "0. Volver al menú principal".center(80))
        print(Fore.RED + "1. Limpiar historial".center(80))
        
        if not historial:
            print(Fore.WHITE + "No hay registros en el historial.".center(80))
        else:
            # Crear encabezado de la tabla
            print(Fore.CYAN + '+' + '-' * 78 + '+')
            print(Fore.CYAN + '| ' + 'TIPO'.ljust(10) + ' | ' + 'REFERENCIA'.ljust(10) + ' | ' + 'TALLA'.ljust(8) + ' | ' + 'DESCRIPCIÓN'.ljust(16) + ' | ' + 'DETALLES'.ljust(23) + ' |')
            print(Fore.CYAN + '+' + '-' * 78 + '+')
            
            # Mostrar cada registro en formato de tabla
            for item in historial:
                tipo = item.get('tipo', '').ljust(10)
                referencia = item.get('referencia', '').ljust(10)
                talla = item.get('talla', '').ljust(8)
                
                if item['tipo'] == 'producción':
                    descripcion = item.get('descripcion', '').ljust(16)
                    detalles = f"Precio: ${item.get('precio_venta', 0):.2f}".ljust(23)
                elif item['tipo'] == 'cliente':
                    descripcion = f"ID: {item.get('id', '')}".ljust(16)
                    detalles = f"Tel: {item.get('telefono', '')}".ljust(23)
                elif item['tipo'] == 'compra':
                    descripcion = "".ljust(16)
                    detalles = f"Cant: +{item.get('cantidad', 0)} → {item.get('nuevo_saldo', 0)}".ljust(23)
                elif item['tipo'] == 'venta':
                    descripcion = f"Clt: {item.get('cliente_id', '')}".ljust(16)
                    detalles = f"Unds: -{item.get('unidades', 0)} → {item.get('nuevo_saldo', 0)}".ljust(23)
                else:
                    descripcion = "".ljust(16)
                    detalles = "".ljust(23)
                
                print(Fore.WHITE + '| ' + tipo + ' | ' + referencia + ' | ' + talla + ' | ' + descripcion + ' | ' + detalles + ' |')
            
            print(Fore.CYAN + '+' + '-' * 78 + '+')
        
        opcion = input(Fore.CYAN + "\nSeleccione una opción (0: Volver, 1: Limpiar historial): ")
        
        if opcion == "0":
            return
        elif opcion == "1":
            # Solicitar confirmación antes de limpiar el historial
            confirmacion = input(Fore.RED + "\n¿Está seguro que desea eliminar todo el historial? (S/N): ").upper()
            if confirmacion == "S":
                historial.clear()  
                print(Fore.GREEN + "\nHistorial eliminado correctamente.".center(80))
                time.sleep(2)
            else:
                print(Fore.YELLOW + "\nOperación cancelada.".center(80))
                time.sleep(2)

def main():
    while True:
        clear_screen()

        # Crear marco decorativo superior
        print(Fore.CYAN + '+' + '=' * 80 + '+')
        print(Fore.CYAN + '|' + 'Desarrollo de software en python para la gestión de'.center(78) + '|')
        print(Fore.CYAN + '|' + ' inventario en la empresa calzado'.center(78) + '|')
        print(Fore.CYAN + '+' + '=' * 80 + '+')

        # Opciones del menú
        print(Fore.YELLOW + '|' + "Seleccione la opción que desea realizar:".center(78) + '|')
        print(Fore.GREEN + '|' + "1. Registro de producción".center(78) + '|')
        print(Fore.BLUE + '|' + "2. Registro de cliente".center(78) + '|')
        print(Fore.RED + '|' + "3. Transacciones".center(78) + '|')
        print(Fore.MAGENTA + '|' + "4. Historial de inventario".center(78) + '|')
        print(Fore.WHITE + '|' + "5. Salir del programa".center(78) + '|')
        print(Fore.CYAN + '+' + '=' * 80 + '+')

        try:
            x = int(input(Fore.CYAN + "Ingrese su opción: "))
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido.".center(80))
            time.sleep(2)
            continue

        if x == 5:
            print(Fore.WHITE + "Saliendo del programa...".center(80))
            time.sleep(2)
            break

        elif x == 1:
            submenu()

        elif x == 2:
            guardar()

        elif x == 3:
            compra()

        elif x == 4:
            mostrar_historial()

        else:
            print(Fore.RED + "Opción no válida, intente de nuevo.".center(80))
            time.sleep(2)

if __name__ == "__main__":
    main()
    