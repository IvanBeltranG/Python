a = 10
b = 3

# operadores aritmeticos 
suma = a + b 
print("la suma es:", suma)
resta = a - b
print("la resta es:", resta)
multiplicacion = a * b 
print("la multiplicacion es:", multiplicacion)
division = a / b
print("la division es:", division)
modulo = a % b
print("el modulo es: ", modulo)
potencia = a ** b
print("La potencia es: ", potencia)
division_entera = a // b
print("la division entera es:" , division_entera)

# operadores de asignacion 
a = 5
a = a + 3
print(a)

a = 5
a += 3
print(a)

a = 5
a -= 3
print(a)

a = 5
a *= 3
print(a)

a = 5
a /= 3
print(a)

a = 5
a //= 3
print(a)

a = 5
a **= 3
print(a)

a = 5
a %= 3
print(a)

# operadores de comparacion o relacionales 
a = 5
b = 3
print(a > b)

a = 5
b = 3
print(a < b)

a = 3
b = 3
print(a <= b)

a = 3
b = 3
print(a >= b)

a = 4
b = 4
print(a != b) # "!=" diferente

a = 4
b = 4
print(a == b) # "==" Igual

# operadores logicos 
a = 5
b = 5
c = 3
print(a >= b or b > c)

a = 5
b = 5
c = 3
print(a >= b and b == c)

"""
Ejercicio 1
Mini Script de calculadora basica que pida datos,
procese operaciones y entregue resultados formateados profesionalmente 

Reforzar la comprension profunda de tipos y operaciones.
Promover el uso profesional de nombres, comentarios y estructuras.
Impresion con formato
"""

print("hola mundo", 5+2, "esto es una suma")
print(f"hola mundo {5+2} esto es una suma")
print("hola mundo {} esto es una suma".format(5+2))

a = 5
b = 2
suma = a + b
print("hola mundo", suma, "esto es una suma")
print(f"hola mundo {suma} esto es una suma de {a} y {b}")
print("hola mundo {} esto es una suma de {} y {}".format(suma, a, b))

a, b, c = 1, 2, 3
print(f"Los valores son a={a}, b={b}, c={c}")

edad1 = 25
edad2 = 30
nombre1 = "Juan"
nombre2 = "Maria"
print("La edad de", nombre1, "es", edad1, "y la edad de", nombre2, "es", edad2)
print(f"la edad de {nombre1} es {edad1} y la edad de {nombre2} es {edad2}")

n1 = n2 = n3 = 5
print(f"Los valores son n1={n1}, n2={n2}, n3={n3}")

print(nombre1+nombre2+str(edad1+edad2))
