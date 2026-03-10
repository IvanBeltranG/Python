"""
# "input" es para pedir por consola informacion del usuario 
# con "+ se puede concatenar texto"
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
suma = a + b
print("La suma de los numeros es:", suma)

------------------------------------------
nombre1 = input("Ingrese su nombre: ")
edad1 = input("Ingrese la edad: ")

print("Hola " + nombre1 + ", tienes " + edad1 + " años")
"""
# nombre1 = input("Ingrese su nombre: ")

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# suma = num1 + num2
# resta = num1 - num2
# mult = num1 * num2
# divi = float(f"{(num1 / num2):.3f}")       # f"{(num1 / num2):.3f}" este es el formato para controlar los decimales 
# mod = num1 % num2
# pot = num1 ** num2
# divEnt = num1 // num2

# print(f"Hola {nombre1} el resultado de la suma de {num1} y {num2} es igual a: {suma}")
# print(f"Hola {nombre1} el resultado de la resta de {num1} y {num2} es igual a: {resta}")
# print(f"Hola {nombre1} el resultado de la multiplicacion de {num1} y {num2} es igual a: {mult}")
# print(f"Hola {nombre1} el resultado de la division de {num1} y {num2} es igual a: {divi}")
# print(f"Hola {nombre1} el resultado de la division Entera de {num1} y {num2} es igual a: {divEnt}")
# print(f"Hola {nombre1} el resultado del modulo de {num1} y {num2} es igual a: {mod}")
# print(f"Hola {nombre1} el resultado de la potencia de {num1} y {num2} es igual a: {pot}")

"""
Escriba un programa en python que calcule el area de un circulo 
"""

# PI = 3.1416
# r = float(input("Ingrese el valor del Radio: "))
# a = float(f"{(PI*(r**2)):.3f}")

# print(f"El area del circulo es: {a}")

"""
Escriba un programa en python que calcule el area de un triangulo Rectangulo
"""

# base = float(input("Ingrese la Base: "))
# alt = float(input("Ingrese la Altura: "))
# at = float(f"{((base*alt)/2):.3f}")

# print(f"El area del Triangulo es: {at}")

"""
Vamos a calcular el valor a pagar a un empleado por su trabajo de la semana 
le vamos a preguntar al usuario cuantas horas trabajo el empleado y cuanto gana por hora 
al final le vammos a mostrar el valor a pagar al empleado por su trabajo de la semana 

"""
# ahora vamos a hacer el calculo de la nomina de los tres empleados 

valor_horas1 = int(input("Ingrese el valor por hora de su trabajo1: "))
horas_trabajadas1 = float(input("Ingrese cuantas horas trabajo a la semana: "))

valor_horas2 = int(input("Ingrese el valor por hora de su trabajo2: "))
horas_trabajadas2 = float(input("Ingrese cuantas horas trabajo a la semana: "))

valor_horas3 = int(input("Ingrese el valor por hora de su trabajo3: "))
horas_trabajadas3 = float(input("Ingrese cuantas horas trabajo a la semana: "))

valor_total1 = int(f"{(valor_horas1*horas_trabajadas1):.0f}")
valor_total2 = int(f"{(valor_horas2*horas_trabajadas2):.0f}")
valor_total3 = int(f"{(valor_horas3*horas_trabajadas3):.0f}")

valor_total = valor_total1+valor_total2+valor_total3

print(f"El valor total a pagar por la semana trabajo es: {valor_total}")

