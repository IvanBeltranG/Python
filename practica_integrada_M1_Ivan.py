""" Ejercicio Práctico 1: Sistema de Gestión Básica de Empleados
 
Contexto
Una empresa quiere desarrollar un pequeño programa en Python que permita registrar empleados y calcular su pago final de forma simple 
desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de empleados, calcular su 
salario y mostrar un resumen final.

Requisitos del programa

El programa debe permitir:

Registrar empleados
Calcular el salario bruto
Calcular un bono según el salario
Mostrar el salario final
Permitir registrar varios empleados usando un menú
Mostrar un resumen final
Reglas del sistema
Para cada empleado se debe ingresar:

Nombre
Edad
Horas trabajadas
Pago por hora
El programa debe calcular:

salario_bruto=horas_trabajadas × pago_por_hora

Luego debe calcular un bono según esta regla:

Salario bruto	Bono

>=2000	10% del salario bruto
<2000	5% del salario bruto

Después debe calcular:

salario_final = salario_bruto+bono

1. Función para registrar empleado
Debe pedir:

nombre
edad
horas trabajadas
pago por hora
Debe retornar los datos.

2. Función para calcular salario bruto
3. Función para calcular bono
4. Función para calcular salario final
5. Menú principal con bucle
    Debe usar un while para permitir registrar varios empleados.

    Validaciones mínimas
El programa debe validar:

Que la edad sea mayor que 0
Que las horas trabajadas sean mayores o iguales a 0
Que el pago por hora sea mayor que 0
Si los datos no son válidos, debe pedirlos nuevamente.

Parte final obligatoria
Al terminar el programa debe mostrar:

Total de empleados registrados: X
Promedio de salario final: X

"""

def pedirEdad():
    try:
        while True:
            edad = int(input("Por favor Ingrese la edad del Empleado: "))
            if edad > 0:
                return edad
            else:
                print("Por favor ingrese una edad valida")

    except ValueError:
        print("Error: Ingrese un valor valido")

def horasTrabajadas():
    try:
        while True:
            horasTrabajadas = float(input("Por favor Ingrese en numero la canttidad de horas TRabajadas del empleado: "))
            if horasTrabajadas > 0:
                return horasTrabajadas
            else:
                print("Por favor ingrese cantidad de horas correctas")
    
    except ValueError:
        print("Por favor ingrese los datos adecuados")

def pagoHoras():
    try:
        while True:
            pagoHoras = float(input("Ingrese el pago por hora"))
            if pagoHoras > 0:
                return pagoHoras
            else:
                print("Por Favor Ingrese la cantidad de horas correctas")

    except ValueError:
        print("Por Favor Ingrese unDato Valido")
        

def regEmpleado():
    nombre = input("Por favor Ingrese el nombre del empleado: ")
    edad = pedirEdad()
    salarioBruto = horasTrabajadas() * pagoHoras()
    


