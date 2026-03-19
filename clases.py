
# Crear Clases
# Atributos Caracteristicas 
# Metosos son acciones 

class Perro:
    def __init__(self, nombre, edad):     # __init__(self)  siempre va el -self- → metodo constructor 
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):   # → siempre debe llevar el self como minimo 
        return "¡Guau!"
    
    def rascarse(self):
        print("¡Me estoy rascando!")

perro1 = Perro("Fido", 3)
perrito = Perro("Firulais", 3)

print(perro1.nombre, perro1.edad)  # → Salida Fido 3
print(perrito.nombre, perrito.edad)
print(perro1.ladrar()) # → llama al objeto de la clase y le da la accion ladrar()
perro1.rascarse()
