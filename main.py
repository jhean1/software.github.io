from colorama import Fore, Style, init
import os
import time

# Inicializar colorama
init(autoreset=True)

while True:
    # Limpiar la pantalla
    os.system('cls')  

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
        # Solicitar opción al usuario
        x = int(input(Fore.CYAN + "Ingrese su opción: ".center(80)))
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.".center(80))
        time.sleep(2)
        continue

    # Respuesta según la opción seleccionada
    if x == 1:
        # Submenú para Registro de Producción
        os.system('cls')
        print(Fore.GREEN + "Registro de Producción".center(80))
        referencia = input(Fore.CYAN + "Ingrese la referencia: ".center(80))
        talla = input(Fore.CYAN + "Ingrese la talla: ".center(80))
        costo_produccion = float(input(Fore.CYAN + "Ingrese el costo de producción: ".center(80)))
        porcentaje_utilidad = float(input(Fore.CYAN + "Ingrese el porcentaje de utilidad: ".center(80)))
        precio_venta = float(input(Fore.CYAN + "Ingrese el precio de venta: ".center(80)))
        saldo_inicial = int(input(Fore.CYAN + "Ingrese el saldo inicial: ".center(80)))
        entrada = int(input(Fore.CYAN + "Ingrese las entradas: ".center(80)))
        salida = int(input(Fore.CYAN + "Ingrese las salidas: ".center(80)))
        saldo_final = saldo_inicial + entrada - salida

        print(Fore.GREEN + f"Saldo final calculado: {saldo_final}".center(80))
        time.sleep(2)

    elif x == 2:
        # Submenú para Registro de Cliente
        os.system('cls')
        print(Fore.BLUE + "Registro de Cliente".center(80))
        cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ".center(80))
        nombre_completo = input(Fore.CYAN + "Ingrese el nombre completo: ".center(80))
        telefono = input(Fore.CYAN + "Ingrese el teléfono: ".center(80))
        valor_comprado = float(input(Fore.CYAN + "Ingrese el valor comprado: ".center(80)))

        print(Fore.BLUE + f"Cliente registrado: {nombre_completo} (ID: {cliente_id})".center(80))
        time.sleep(2)

    elif x == 3:
        print(Fore.RED + "Seleccionaste transacciones".center(80))
        time.sleep(2)

    elif x == 4:
        print(Fore.MAGENTA + "Seleccionaste historial de inventario".center(80))
        time.sleep(2)

    elif x == 5:
        print(Fore.WHITE + "Saliste del programa".center(80))
        time.sleep(2)
        exit()

    else:
        print(Fore.RED + "Opción no válida, intenta de nuevo.".center(80))
        time.sleep(2)

    # Separador entre iteraciones del menú
    print(Style.DIM + '+' + '=' * 80 + '+')
    time.sleep(2)
