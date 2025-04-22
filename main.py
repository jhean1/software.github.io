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
    print(Fore.RED + '|' + "3. Transsacciónes".center(78) + '|')
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
        print(Fore.GREEN + "Seleccionaste registro de producción".center(80))
        time.sleep(2)
    elif x == 2:
        print(Fore.BLUE + "Seleccionaste registro de clientes".center(80))
        time.sleep(2)
    elif x == 3:
        print(Fore.RED + "Seleccionaste transsacciónes".center(80))
        time.sleep(2)
    elif x == 4:
        print(Fore.MAGENTA + "Seleccionaste historial de inventario".center(80))
        time.sleep(2)
    elif x == 5:
        print(Fore.WHITE + "Saliste del programa".center(80))
        time.sleep(2)
        exit()
    else:
        # Mensaje si la opción no es válida
        print(Fore.RED + "Opción no válida, intenta de nuevo.".center(80))
        time.sleep(2)

    # Separador entre iteraciones del menú
    print(Style.DIM + '+' + '=' * 80 + '+')
    time.sleep(2)
