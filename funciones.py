"""
# no recibe nada y no devuelve nada
def suma1():
    a = int(input("Ingrese el primer Numero: "))
    b = int(input("Ingrese el segundo Numero: "))
    res = a + b
    print(f"La suma de {a} y {b} es: {res}")

print("Hola Mundo")
suma1()
"""
#---------------------------------------------
"""
# Recibe dos parametos pero no devuelve nada
def suma2(a, b):
    res = a + b 
    print(f"La suma de {a} y {b} es: {res}")
n1 =int(input("Ingrese el primer Numero: "))
n2 = int(input("Ingrese el segundo Numero: "))
suma2(n1, n2)
"""
#---------------------------------------------
"""
# No recibe nada y devuelve algo

def suma3():
    a = int(input("Ingrese el primer Numero: "))
    b = int(input("Ingrese el segundo Numero: "))
    res = a + b
    return res

print(suma3())      # dentro del print el llamdo se convierte el valor de retorno 
"""
#---------------------------------------------

# Recibe algo y devuelve algo 
def suma4(a, b):
    res = a + b
    return res 
n1 =int(input("Ingrese el primer Numero: "))
n2 = int(input("Ingrese el segundo Numero: "))

print(suma4(n1, n2))