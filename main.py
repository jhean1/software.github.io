from colorama import Fore, Style, init
import os
import time

# Inicializar colorama
init(autoreset=True)

# Variables para almacenar datos
inventario = []
clientes = []
historial = []

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
        descripcion = input(Fore.CYAN + "Ingrese la descripción: ".center(80))
        costo_produccion = float(input(Fore.CYAN + "Ingrese el costo de producción: ".center(80)))
        porcentaje_utilidad = float(input(Fore.CYAN + "Ingrese el porcentaje de utilidad: ".center(80)))
        precio_venta = float(input(Fore.CYAN + "Ingrese el precio de venta: ".center(80)))
        saldo_inicial = int(input(Fore.CYAN + "Ingrese el saldo inicial: ".center(80)))
        entrada = int(input(Fore.CYAN + "Ingrese las entradas: ".center(80)))
        salida = int(input(Fore.CYAN + "Ingrese las salidas: ".center(80)))
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

        print(Fore.GREEN + f"Saldo final calculado: {saldo_final}".center(80))
        time.sleep(5)

    elif x == 2:
        # Submenú para Registro de Cliente
        os.system('cls')
        print(Fore.BLUE + "Registro de Cliente".center(80))
        cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ".center(80))
        nombre_completo = input(Fore.CYAN + "Ingrese el nombre completo: ".center(80))
        telefono = input(Fore.CYAN + "Ingrese el teléfono: ".center(80))
        valor_comprado = float(input(Fore.CYAN + "Ingrese el valor comprado: ".center(80)))

        # Guardar en clientes
        clientes.append({
            "id": cliente_id,
            "nombre": nombre_completo,
            "telefono": telefono,
            "valor_comprado": valor_comprado
        })

        print(Fore.BLUE + f"Cliente registrado: {nombre_completo} (ID: {cliente_id})".center(80))
        time.sleep(5)

    elif x == 3:
        # Submenú para Transacciones
        os.system('cls')
        print(Fore.RED + "Transacciones".center(80))
        print(Fore.YELLOW + "1. Compra".center(80))
        print(Fore.YELLOW + "2. Venta".center(80))
        opcion_transaccion = int(input(Fore.CYAN + "Seleccione una opción: ".center(80)))

        if opcion_transaccion == 1:
            # Compra
            referencia = input(Fore.CYAN + "Ingrese la referencia: ".center(80))
            talla = input(Fore.CYAN + "Ingrese la talla: ".center(80))
            cantidad = int(input(Fore.CYAN + "Ingrese la cantidad: ".center(80)))

            # Guardar en historial
            historial.append({
                "tipo": "compra",
                "referencia": referencia,
                "talla": talla,
                "cantidad": cantidad
            })

            print(Fore.GREEN + "Compra registrada correctamente.".center(80))
            time.sleep(5)

        elif opcion_transaccion == 2:
            # Venta
            cliente_id = input(Fore.CYAN + "Ingrese el ID del cliente: ".center(80))
            referencia = input(Fore.CYAN + "Ingrese la referencia: ".center(80))
            talla = input(Fore.CYAN + "Ingrese la talla: ".center(80))
            unidades = int(input(Fore.CYAN + "Ingrese el número de unidades: ".center(80)))
            valor_a_pagar = float(input(Fore.CYAN + "Ingrese el valor a pagar: ".center(80)))

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
            time.sleep(5)

    elif x == 4:
        # Historial de Inventario
        os.system('cls')
        print(Fore.MAGENTA + "Historial de Inventario".center(80))
        for item in historial:
            print(Fore.WHITE + str(item).center(80))
        time.sleep(5)

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
