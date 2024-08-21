import productlist
import time
import sys

no_stock = "No hay Stock en esa Talla"
bar = "|----------------------------------------------|"
menu_options = ("C", "V", "Q",)
product_type = ("Hoodies", "Camisetas", "Calcetines", "Jeans", "Tenis")
color_options_hoddies = ("V", "N", "B",)
color_options_camisetas = ("A", "N", "B",)
color_options_calcetines = ("N", "B",)
color_options_tenis = ("B", "N", "B/N",)
color_options_jeans = ("A", "N",)
size_options = ("S", "M", "L",)
colorV = productlist.hoodies.get("colorV")
colorN = productlist.hoodies.get("colorN")
colorB = productlist.hoodies.get("colorB")


user_input=input("| Elige una opcion: ")
TipoPro=input("| ")
colorP = input("| ")
TallaV = input("| ")

print(bar)
nombre = input("| Porporcione un nombre: ")

print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes")

print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Zapatos ")

print("| \n! A continuacion te mostraremos el catalogo para que selecciones tus productos !")


def mensaje_espera():
    print("| Por favor, espera redirigiendo al menu ")
    time.sleep(5)
    print("| ¡Gracias por esperar!")


mensaje_espera()

while True:
    print(bar)
    print("|     *Menu*")
    print("| C - Compra\n| V - Venta\n| Q - Salir ")
    print(bar)
    user_input
    if user_input in menu_options:
        break
    else:
        print("| Esa no es una Opcion")


if user_input == "C":
    while True:
        print(bar)
        print("| Elige que tipo de producto quieres: ")
        print("| Hoodies, Camisetas, Calcetines, Jeans, Tenis ")
        TipoPro
        if TipoPro in product_type:
            break
        elif TipoPro not in product_type:
            print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
        else:
            print("| No tenemos tienes Ese producto")
        break


def Quit_inicio():
    if user_input == "Q":
        sys.exit()


def Hoodies_Color_select():
    if TipoPro == "Hoodies":
        while True:
            print(bar)
            print("| Elige que Color quieres: ")
            print("| " + colorV + ", " + colorB + ", " + colorN)
            colorP
            break


def Color_Green_Size_Select():
    if colorP == "Verde":
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaV
            if productlist.hoodies["cantidadVL"] == 0:
                print("No hay Stock en esa Talla")
            break
        if TallaV == "S":
            print("| Tenemos: ", productlist.hoodies["cantidadVS"], " en Talla S")
        if TallaV == "M":
            print("| Tenemos: ", productlist.hoodies["cantidadVM"], " en Talla M")
        if TallaV == "L":
            print("| Tenemos: ", productlist.hoodies["cantidadVL"], " en Talla L")

def Color_White_Size_Select():
    if colorP == "Blanco":
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaV
    if productlist.hoodies["cantidadBL" or "cantidadBM" or "cantidadBS"] == 0:
                print("No hay stock ")
    if colorP == "Negro  ":
        while True:
          print(bar)
          break
    if productlist.hoodies["cantidadNL" or "cantidadNM" or "cantidadNS"] == 0:
       print("No hay stock ")


VentaC = int(input("| Cantidad de productos que quieres: "))
print("| En tu carrito hay: ", VentaC, " articulos")


print("| Stock del los articulos Seleccionados: ",  productlist.hoodieVSC)
if TipoPro == "Hoodies" and colorP == "Verde ":
    print("| Tenemos este stock en verde talla L",
          productlist.hoodies["cantidadVL"])
if TipoPro == "Hoodies" and colorP == "Verde ":
    print("| Tenemos este stock en verde talla M ",
          productlist.hoodies["cantidadVM"])
if TipoPro == "Hoodies" and colorP == "Verde ":
    print("|Tenemos este stock en Verde talla S",
          productlist.hoodies["cantidadVS"])


# print(productlist.hoodies)
ventaV = productlist.hoodies.get("cantidadVM")
ventaV = ventaV-VentaC
productlist.hoodies.update({"cantidadVM": ventaV})
print("siuuuuuu")
