from colorama import Fore, Style, init
import time

# Inicializar colorama
init(autoreset=True)

while True:
    # Crear marco superior
    print(Fore.CYAN + '=' * 50)
    print(Fore.CYAN + 'BIENVENIDO AL MENU'.center(50))
    print(Fore.CYAN + '=' * 50)
    time.sleep(1)

    # Opciones del menú
    print(Fore.YELLOW + "Seleccione la opción que desea realizar:".center(50))
    print(Fore.GREEN + "1. Agregar".center(50))
    print(Fore.BLUE + "2. Modificar".center(50))
    print(Fore.RED + "3. Eliminar".center(50))
    print(Fore.MAGENTA + "4. Mostrar".center(50))
    print(Fore.WHITE + "5. Salir del programa".center(50))
    print(Fore.CYAN + '=' * 50)  # Línea decorativa inferior

    try:
        x = int(input(Fore.CYAN + "Ingrese su opción: ".center(50)))
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.".center(50))
        continue

    if x == 1:
        print(Fore.GREEN + "Seleccionaste agregar".center(50))
    elif x == 2:
        print(Fore.BLUE + "Seleccionaste modificar".center(50))
    elif x == 3:
        print(Fore.RED + "Seleccionaste eliminar".center(50))
    elif x == 4:
        print(Fore.MAGENTA + "Seleccionaste mostrar".center(50))
    elif x == 5:
        print(Fore.WHITE + "Saliste del programa".center(50))
        exit()
    else:
        print(Fore.RED + "Opción no válida, intenta de nuevo.".center(50))
    
    print(Style.DIM + '=' * 50)  # Línea decorativa para separar iteraciones