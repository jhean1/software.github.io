
import time

print("Bienvenido al menu")
time.sleep(1)
print("seleccione la opción que desea realizar")
print("1. Agregar")
print("2. Modificar")
print("3. Eliminar")
print("4. Mostrar")
print("5. salir del programa")
x=int(input(""))

if x==1:
    print("seleccionaste agregar")
elif x==2:
    print("seleccionaste modificar")
elif x==3:
    print("seleccionaste eliminar")
elif x==4:
    print("seleccinaste mostrar")
else:
    print("saliste del programa")
    exit()







