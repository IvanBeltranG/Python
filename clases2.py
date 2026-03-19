class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre   # self.__"----" lo vuelve privado 
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
persona1 = Persona("Juan")
#print(persona1.nombre)
print(persona1.get_nombre())  # saca → juan
persona1.set_nombre("Pedro")  # con este le envio informacion 
print(persona1.get_nombre())  # saca → pedro
p1= Persona("Maria")
print(p1.get_nombre())

"""
mancito = Persona("Carlos")

print(mancito.__nombre) # Manda error por q __nombre lo vuelve privado 
"""
# getters y setters son metodos que se utilizan para acceder y modificar 