""" Ejercicio práctico (2 horas)
Sistema de Gestión Básica de Estudiantes
Contexto

Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma 
simple desde la terminal.
Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su 
promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre
Edad
Nota 1
Nota 2
Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre
edad
3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"
"En recuperación"
"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5
Que la edad sea mayor que 0
Si los datos no son válidos, debe pedirlos nuevamente.
Parte final (obligatoria)
Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X"""

def pedirEdad():
    while True:
        try:
            edad = int(input("Ingrese la Edad: "))
            if edad > 0:
                return edad
            else:
                print("Error. Edad Invalida. Ingrese una edad Correcta")

        except ValueError:
            print("Error: Ingrese un número entero válido.")
            

def nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota No. {numero}: "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Ha Ingresado una nota no valida")

        except ValueError:
            print("Error: ingrese un número válido.")


def registroEstudiante():
    nombre = input("Ingrese nombre del Estudiante: ")
    edad = pedirEdad()
    nota1 = nota(1)
    nota2 = nota(2)
    nota3 = nota(3)

    return nombre, edad, nota1, nota2, nota3

def calcularPromedio(n1, n2, n3):
    return (n1 + n2 + n3)/3

def evaluarEstado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En Recuperacion"
    else:
        return "No Aprobado"

def inicio():

    estudiantesRegistrados = 0
    sumaPromedio = 0
    listaEstudiantes = []

    while True:
        print("\n===== SISTEMA DE ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Salir")

        op = input("Seleccione una opcion: ")

        if op == "1":
            nombre, edad, n1, n2, n3 = registroEstudiante()
            promedio = calcularPromedio(n1, n2, n3)
            estado = evaluarEstado(promedio)

            estudiantesRegistrados += 1
            sumaPromedio += promedio
            listaEstudiantes.append((nombre, edad, n1, n2, n3, promedio, estado))

            print("\n===== RESULTADO DEL ESTUDIANTE =====")
            for estudiante in listaEstudiantes:
                print(f"\nNombre: {estudiante[0]}")
                print(f"Edad: {estudiante[1]}")
                print(f"Nota 1: {estudiante[2]}")
                print(f"Nota 2: {estudiante[3]}")
                print(f"Nota 3: {estudiante[4]}")
                print(f"Promedio: {estudiante[5]:.2f}")
                print(f"Estado académico: {estudiante[6]}")

        elif op == "2":
            print("\n===== RESUMEN FINAL =====")
            print(f"Total de estudiantes registrados: {estudiantesRegistrados}")

            if estudiantesRegistrados > 0:
                promedio_general = sumaPromedio / estudiantesRegistrados
                print(f"Promedio general del grupo: {promedio_general:.2f}")

                print("\n===== LISTADO DE ESTUDIANTES =====")
                i = 1
                for estudiante in listaEstudiantes:
                    print(f"- Registro No. {i} - Nombre: {estudiante[0]} - Promedio: {estudiante[5]:.2f} - Estado: {estudiante[6]}")
                    i += 1
            else:
                print("Promedio general del grupo: 0.00")
                print("No hay estudiantes registrados.")

            print("Programa finalizado.")
            break

inicio()
