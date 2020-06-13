while True:  # es una iteracion necesita una condicion si true, itera infinitamente
    print("-" * 100)
    print("1-manzana| 2-pina| 3-fresa| 0-salir")
    fruta = int(input("ingrese numero de la fruta (0-salir): "))

    if str(fruta) in "0123":  # if nuevo
        if fruta == 0:
            break  # break para las iteracion solo funciona con iteraciones

        cantidad = int(input("ingrese cantidad de fruta: "))
        total = 0
        nombreFruta = ""

        if fruta == 1:
            total = cantidad * 1.0
            nombreFruta = "manzana"
        elif fruta == 2:  # elif solo funciona con los if
            total = cantidad * 3.0
            nombreFruta = "pina"
        elif fruta == 3:
            total = cantidad * (2 / 5)
            nombreFruta = "fresa"
    else:
        total = 0
        nombreFruta = "error - intente de nuevo"

    print(f"total {nombreFruta}: ${total:.2f}")
    print("-" * 100)
