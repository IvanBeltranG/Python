menu = """
Restaurante El Buen Sabor
1. Hamburguesa - $20.000
2. Pizza - $15.000
3. Ensalada - $4.500
4. Salchipapa - $8.000
5. Perro Caliente - $12.000
6. Salir
""" 
print(menu)
opcion = 0
total = 0
totalHamburguesa = 0
cantidadHamburguesa = 0
totalPizza = 0
cantidadPizza = 0
totalEnsalada = 0
cantidadEnsalada = 0
totalSalchipapa = 0
cantidadSalchipapa = 0
totalPerroCaliente = 0
cantidadPerroCaliente = 0

while opcion != 6:
    opcion = int(input("Ingrese una opcion del Menu: "))
    if opcion == 1:
        totalHamburguesa += 20000
        cantidadHamburguesa += 1
        print("Has Elegido Hamburguesa")
    elif opcion == 2:
        totalPizza += 15000
        cantidadPizza += 1
        print("Has Elegido Pizza")
    elif opcion == 3:
        totalEnsalada += 4500
        cantidadEnsalada += 1
        print("Has Elegido Ensalada")
    elif opcion == 4:
        totalSalchipapa += 8000
        cantidadSalchipapa += 1
        print("Has Elegido Salchipapa")
    elif opcion == 5:
        totalPerroCaliente += 12000
        cantidadPerroCaliente += 1
        print("Has Elegido Perro Caliente")
    elif opcion == 6:
        total = totalHamburguesa + totalPizza + totalEnsalada + totalSalchipapa + totalPerroCaliente 
        print(f"""Este cliente se va a volar con: ${total:.2f}, asi:
            Total Hamburguesa:------${totalHamburguesa:.2f} y su cantidad es = {cantidadHamburguesa}
            Total Pizza:------------${totalPizza:.2f} y su cantidad es = {cantidadPizza}
            Total Ensalada:---------${totalEnsalada:.2f} y su cantidad es = {cantidadEnsalada}
            Total Salchipapa:-------${totalSalchipapa:.2f} y su cantidad es = {cantidadSalchipapa}
            Total Perro Caliente:---${totalPerroCaliente:.2f} y su cantidad es = {cantidadPerroCaliente}
            Atrapelo!!!!!!!
              """)
        break
    else:
        print("Elegiste una Opcion no Valida. Por favor Elegir una opcion Valida")
    print(menu)
