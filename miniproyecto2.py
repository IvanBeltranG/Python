"""
Vas a crear una clase llamada CuentaBancaria que simule una billetera digital como Nequi o Daviplata.
🔹 Requisitos

1. Atributos
Debes usar los tres niveles de acceso:

titular → Público
_historial → Protegido
__saldo → Privado

2. Constructor
Debe recibir:

titular
saldo inicial

3. Métodos obligatorios
🔹 Getters y Setters

Obtener saldo (NO acceso directo)
Modificar saldo SOLO con validación

🔹 Funcionalidades
depositar(monto)
retirar(monto)
ver_saldo()
ver_historial()

4. Validaciones
No permitir saldo negativo
No permitir retiros mayores al saldo
No permitir depósitos negativos
5. Prueba del sistema

En el programa principal:

Crear una cuenta
Depositar dinero
Retirar dinero
Mostrar saldo
Mostrar historial
"""

class CuentaBancaria:
    # Constructor
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Público
        self._historial = []            # Protegido
        self.__saldo = 0                # Privado

        if saldo_inicial >= 0:
            self.__saldo = saldo_inicial
            self._historial.append(f"Cuenta creada con saldo inicial de ${saldo_inicial}")
        else:
            print("Error: El saldo inicial no puede ser negativo.")

    # Getter
    def obtener_saldo(self):
        return self.__saldo

    # Setter
    def modificar_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
            self._historial.append(f"Saldo modificado a ${nuevo_saldo}")
        else:
            print("Error: No se puede colocar un saldo negativo.")

    # Depositar
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            self._historial.append(f"Depósito: +${monto}")
            print("Depósito realizado con éxito.")
        else:
            print("Error: El depósito debe ser mayor que 0.")

    # Retirar
    def retirar(self, monto):
        if monto <= 0:
            print("Error: El retiro debe ser mayor que 0.")
        elif monto > self.__saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.__saldo -= monto
            self._historial.append(f"Retiro: -${monto}")
            print("Retiro realizado con éxito.")

    # Ver saldo
    def ver_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.__saldo}")

    # Ver historial
    def ver_historial(self):
        print(f"\nHistorial de {self.titular}:")
        if len(self._historial) == 0:
            print("No hay movimientos.")
        else:
            for movimiento in self._historial:
                print("-", movimiento)


# Programa principal con menú
print("=== CREAR CUENTA BANCARIA ===")
titular = input("Ingrese el nombre del titular: ")
saldo_inicial = float(input("Ingrese el saldo inicial: "))

cuenta = CuentaBancaria(titular, saldo_inicial)

opcion = 0

while opcion != 5:
    print("\n=== MENÚ ===")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Ver historial")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto a depositar: "))
        cuenta.depositar(monto)

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta.retirar(monto)

    elif opcion == 3:
        cuenta.ver_saldo()

    elif opcion == 4:
        cuenta.ver_historial()

    elif opcion == 5:
        print("Gracias por usar el sistema.")

    else:
        print("Opción no válida. Intente de nuevo.")
