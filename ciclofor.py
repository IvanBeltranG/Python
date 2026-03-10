#-------------------------
"""for x in range(1, 11):
    print(x)"""
#-------------------------
"""for x in range(5):
    print(x)"""
#-------------------------
"""for x in range(1, 11, 2):
    print(x)"""
#-------------------------
"""texto = "Python"
for letra in texto:
    print(letra)"""
#-------------------------

num = int(input("Digite el numero de la tabla que desea: "))
for x in range(1, 11):
    print(f"{x} x {num} = ",(x*num))
