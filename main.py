from colorama import Fore, Style, init
import os
import time

# Inicializar colorama
init(autoreset=True)

while True:
    # Limpiar la pantalla
    os.system('cls')  # En Windows, usa 'cls'. En Linux/Mac, sería 'clear'.

    # Crear marco decorativo superior
    print(Fore.CYAN + '+' + '=' * 48 + '+')
    print(Fore.CYAN + '|' + 'Desarrollo de software en python para la gestión de inventario en la empresa calzado'.center(48) + '|')
    print(Fore.CYAN + '+' + '=' * 48 + '+')

    # Opciones del menú
    print(Fore.YELLOW + '|' + "Seleccione la opción que desea realizar:".center(46) + '|')
    print(Fore.GREEN + '|' + "1. Ingreso de mercancia".center(46) + '|')
    print(Fore.BLUE + '|' + "2. Ingreso de clientes".center(46) + '|')
    print(Fore.RED + '|' + "3. Ingreso de ventas".center(46) + '|')
    print(Fore.MAGENTA + '|' + "4. Historial de inventario".center(46) + '|')
    print(Fore.WHITE + '|' + "5. Salir del programa".center(46) + '|')
    print(Fore.CYAN + '+' + '=' * 48 + '+')  # Línea decorativa inferior

    try:
        x = int(input(Fore.CYAN + "Ingrese su opción: ".center(50)))
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.".center(50))
        time.sleep(2)  # Pausa para que el usuario vea el mensaje
        continue

    # Respuesta según la opción seleccionada
    if x == 1:
        print(Fore.GREEN + "Seleccionaste ingreso de mercancia".center(50))
        time.sleep(2)  # Pausa de 2 segundos
    elif x == 2:
        print(Fore.BLUE + "Seleccionaste ingreso de clientes".center(50))
        time.sleep(2)  # Pausa de 2 segundos
    elif x == 3:
        print(Fore.RED + "Seleccionaste ingreso de ventas".center(50))
        time.sleep(2)  # Pausa de 2 segundos
    elif x == 4:
        print(Fore.MAGENTA + "Seleccionaste historial de inventario".center(50))
        time.sleep(2)  # Pausa de 2 segundos
    elif x == 5:
        print(Fore.WHITE + "Saliste del programa".center(50))
        time.sleep(2)  # Pausa antes de salir
        exit()
    else:
        print(Fore.RED + "Opción no válida, intenta de nuevo.".center(50))
        time.sleep(2)  # Pausa de 2 segundos
    
    # Separador entre iteraciones del menú
    print(Style.DIM + '+' + '=' * 48 + '+')
    time.sleep(2)  # Pausa antes de volver a mostrar el menú
