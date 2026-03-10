# vamos a hacer un programa q nos diga el sueldo a recibir
# de un empleado, si gana menos de 2.000.000 de pesos le vamos a dar
# un subsidio de 200.000 pesos 
"""
sueldo = int(input("Ingrese el sueldo del empleado: "))

if sueldo < 2000000:
    print("Si se cumplio la condicion")
    sueldo += 200000 # esto es igual a "sueldo = sueldo + 200000"
else:
    print("No se cumplio la condicion")

print(f"El sueldo del Empleado es {sueldo}")
"""
# ---------------------------------------------------------------------------------------------------#

# Escribir un programa en python q le solicite al usuario su edad y determine si es mayor de edad o no 
# Si es mayor o igual a 18 eres mayor de edad de lo contrario eres menor de edad
"""
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
"""
# ---------------------------------------------------------------------------------------------------#

# de cero a 5 primera infancia 
# de 6 a 12 infancia
# de 13 a 17 adolescencia
# mayor o igual a 18 adultez
"""
edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 5:
    print("Primera Infancia")
elif edad >= 6 and edad <=12:
    print("Infancia")
elif edad >= 13 and edad <=17:
    print("Adolescencia")
else:
    print("Adultez")


edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("edad no valida")
elif edad <= 5:
    print("Primera Infancia")
elif edad <=12:
    print("Infancia")
elif edad <=17:
    print("Adolescencia")
else:
    print("Adultez")
"""
# ---------------------------------------------------------------------------------------------------#

# hacer que pida los numeros del 1 al 7 y escriba el dia de la semana segun corresponda el numero 
"""
dia = int(input("Ingrese un numero del 1 al 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Numero Invalido")
"""
# ---------------------------------------------------------------------------------------------------#

# match
"""
dia = int(input("Ingrese un numero del 1 al 7: "))

match dia:
    case 1: # en caso de que el "1" o la entrada sea cadena de caracteres en texto solo ponerlo entre comillas 
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _: # Este es para los valores q no estan dentro de las opciones 
        print("Numero no Valido") 
"""
# ---------------------------------------------------------------------------------------------------#

# Preguntar al usuario un animal (gato perro o pez)
# gato miau
# perro guau
# pez blub
"""
animal = input("Ingrese un un animal (gato perro o pez): ")

match animal:
    case "perro":
        print("Guau")
    case "gato":
        print("Miau")
    case "pez":
        print("Blob")
    case _:
        print("Dato Invalido")
  """      
# ---------------------------------------------------------------------------------------------------#
