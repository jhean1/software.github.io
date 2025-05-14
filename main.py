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

def submenu():
    clear_screen()
    print(Fore.GREEN + "Registro de Producción".center(80))
    referencia = input(Fore.CYAN + "Ingrese la referencia: ")
    talla = input(Fore.CYAN + "Ingrese la talla: ")
    descripcion = input(Fore.CYAN + "Ingrese la descripción: ")
    try:
        costo_produccion = float(input(Fore.CYAN + "Ingrese el costo de producción: "))
        porcentaje_utilidad = float(input(Fore.CYAN + "Ingrese el porcentaje de utilidad: "))
        precio_venta = float(input(Fore.CYAN + "Ingrese el precio de venta: "))
        saldo_inicial = int(input(Fore.CYAN + "Ingrese el saldo inicial: "))
        entrada = int(input(Fore.CYAN + "Ingrese las entradas: "))
        salida = int(input(Fore.CYAN + "Ingrese las salidas: "))
    except ValueError:
        print(Fore.RED + "Error: Por favor ingrese valores numéricos válidos.".center(80))
        time.sleep(3)
        return

    saldo_final = saldo_inicial + entrada - salida

    # Guardar en inventario
    inventario.append({
        "referencia": referencia,
        "talla": talla,
        "descripcion": descripcion,
        "costo_produccion": costo_produccion,
        "precio_venta": precio_venta,
        "saldo_final": saldo_final
    })

    # Guardar en historial
    historial.append({
        "tipo": "producción",
        "referencia": referencia,
        "talla": talla,
        "descripcion": descripcion,
        "costo_produccion": costo_produccion,
        "precio_venta": precio_venta,
        "saldo_final": saldo_final
    })

    print(Fore.GREEN + f"Saldo final calculado: {saldo_final}".center(80))
    time.sleep(3)

def guardar():
    clear_screen()
    print(Fore.BLUE + "Registro de Cliente".center(80))
    cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ")
    nombre_completo = input(Fore.CYAN + "Ingrese el nombre completo: ")
    telefono = input(Fore.CYAN + "Ingrese el teléfono: ")
    try:
        valor_comprado = float(input(Fore.CYAN + "Ingrese el valor comprado: "))
    except ValueError:
        print(Fore.RED + "Error: Por favor ingrese un valor numérico válido.".center(80))
        time.sleep(3)
        return

    # Guardar en clientes
    clientes.append({
        "id": cliente_id,
        "nombre": nombre_completo,
        "telefono": telefono,
        "valor_comprado": valor_comprado
    })

    # Guardar en historial
    historial.append({
        "tipo": "cliente",
        "id": cliente_id,
        "nombre": nombre_completo,
        "telefono": telefono,
        "valor_comprado": valor_comprado
    })

    print(Fore.BLUE + f"Cliente registrado: {nombre_completo} (ID: {cliente_id})".center(80))
    time.sleep(3)

def compra():
    clear_screen()
    print(Fore.RED + "Transacciones".center(80))
    print(Fore.YELLOW + "1. Compra".center(80))
    print(Fore.YELLOW + "2. Venta".center(80))
    try:
        opcion_transaccion = int(input(Fore.CYAN + "Seleccione una opción: "))
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.".center(80))
        time.sleep(3)
        return

    if opcion_transaccion == 1:
        # Compra
        referencia = input(Fore.CYAN + "Ingrese la referencia: ")
        talla = input(Fore.CYAN + "Ingrese la talla: ")
        try:
            cantidad = int(input(Fore.CYAN + "Ingrese la cantidad: "))
        except ValueError:
            print(Fore.RED + "Cantidad inválida.".center(80))
            time.sleep(3)
            return

        # Guardar en historial
        historial.append({
            "tipo": "compra",
            "referencia": referencia,
            "talla": talla,
            "cantidad": cantidad
        })

        print(Fore.GREEN + "Compra registrada correctamente.".center(80))
        time.sleep(3)

    elif opcion_transaccion == 2:
        # Venta
        cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ")
        referencia = input(Fore.CYAN + "Ingrese la referencia: ")
        talla = input(Fore.CYAN + "Ingrese la talla: ")
        try:
            unidades = int(input(Fore.CYAN + "Ingrese el número de unidades: "))
            valor_a_pagar = float(input(Fore.CYAN + "Ingrese el valor a pagar: "))
        except ValueError:
            print(Fore.RED + "Valores inválidos.".center(80))
            time.sleep(3)
            return

        # Guardar en historial
        historial.append({
            "tipo": "venta",
            "cliente_id": cliente_id,
            "referencia": referencia,
            "talla": talla,
            "unidades": unidades,
            "valor_a_pagar": valor_a_pagar
        })

        print(Fore.GREEN + "Venta registrada correctamente.".center(80))
        time.sleep(3)
    else:
        print(Fore.RED + "Opción inválida.".center(80))
        time.sleep(3)

def mostrar_historial():
    clear_screen()
    print(Fore.MAGENTA + "Historial de Inventario".center(80))
    if not historial:
        print(Fore.WHITE + "No hay registros en el historial.".center(80))
    else:
        for item in historial:
            print(Fore.WHITE + str(item).center(80))
    input(Fore.CYAN + "\nPresione Enter para continuar...")

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
