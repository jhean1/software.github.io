from colorama import Fore, Style, init
import time

# Inicializar colorama
init(autoreset=True)

while True:
    print(Fore.CYAN + 'BIENVENIDO AL MENU'.center(50, '='))
    time.sleep(1)
    print(Fore.YELLOW + "Seleccione la opción que desea realizar:")
    print(Fore.GREEN + "1. Agregar")
    print(Fore.BLUE + "2. Modificar")
    print(Fore.RED + "3. Eliminar")
    print(Fore.MAGENTA + "4. Mostrar")
    print(Fore.WHITE + "5. Salir del programa")
    
    try:
        x = int(input(Fore.CYAN + "Ingrese su opción: "))
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.")
        continue

    if x == 1:
        print(Fore.GREEN + "Seleccionaste agregar")
    elif x == 2:
        print(Fore.BLUE + "Seleccionaste modificar")
    elif x == 3:
        print(Fore.RED + "Seleccionaste eliminar")
    elif x == 4:
        print(Fore.MAGENTA + "Seleccionaste mostrar")
    elif x == 5:
        print(Fore.WHITE + "Saliste del programa")
        exit()
    else:
        print(Fore.RED + "Opción no válida, intenta de nuevo.")
    
    print(Style.DIM + ''.center(50, '='))





