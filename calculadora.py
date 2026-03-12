"""
Escribir un programa que pida al usuario dos numeros y muestre un 
menu de opciones, suma, resta, multiplicacion y division
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Divicion Entera
6. Potencia
7. Modulo
8. Salir 

"""
print("Para realizar las operaciones por favor:")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def division_entera(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a // b

def potencia(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: no se puede calcular módulo con cero"
    return a % b


while True:
    print("""
Calculadora
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division Entera
6. Potencia
7. Modulo
8. Salir
""")

    op = int(input("Ingrese la opcion que desea: "))

    if op == 8:
        print("Gracias por usar la Calculadora")
        break

    if op >= 1 and op <= 7:
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))

        if op == 1:
            print("Resultado:", suma(n1, n2))
        elif op == 2:
            print("Resultado:", resta(n1, n2))
        elif op == 3:
            print("Resultado:", multiplicacion(n1, n2))
        elif op == 4:
            print("Resultado:", division(n1, n2))
        elif op == 5:
            print("Resultado:", division_entera(n1, n2))
        elif op == 6:
            print("Resultado:", potencia(n1, n2))
        elif op == 7:
            print("Resultado:", modulo(n1, n2))
    else:
        print("Numero no valido, selecciona una opcion del menu")