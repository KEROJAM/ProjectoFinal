import productlist
import time
import sys

bar="|----------------------------------------------|"
menu_options = ("C", "V", "Q",)
product_type = ("Hoodies", "Camisetas", "Calcetines", "Jeans", "Tenis" )
color_options_hoddies = ("V", "N", "B",)
color_options_camisetas = ("A", "N", "B",)
color_options_calcetines = ( "N", "B",)
color_options_tenis = ("B", "N", "B/N",)
color_options_jeans = ("A", "N",)
size_options = ("S", "M", "L",)

colorV = productlist.hoodies.get("colorV")
colorN = productlist.hoodies.get("colorN")
colorB = productlist.hoodies.get("colorB")

while True:
    print(bar)
    print("|     *Menu*")
    print("| C - Compra\n| V - Venta\n| Q - Salir ")
    print(bar)
    user_input = input("| Elige una opcion: ")
    if user_input in menu_options:
        break 
    else:
        print("| Esa no es una Opcion")

if user_input == "C":
    while True:
        print(bar)
        print("| Elige que tipo de producto quieres: ")
        print("| Hoodies, Camisetas, Calcetines, Jeans, Tenis ")
        TipoPro=input("| ")
        if TipoPro in product_type:
            break
        else:
            print("| No tenemos tienes Ese producto")

if user_input == "Q":
    sys.exit()

if TipoPro == "Hoodies":
    while True:
        print(bar)
        print("| Elige que Color quieres: ")
        print("| " + colorV + ", " + colorB + ", " + colorN)
        colorP = input("| ")
        break

if colorP == "Verde":
    while True:
        print(bar)
        VentaC=int(input("| Cantidad de productos que quieres: ")
        )
        break

VentaC=int(input("| Cantidad de productos que quieres: ")
        )

print("| Tu Carrito: ",  productlist.hoodiesVSC)
if TipoPro == "Hoodies" and colorP == "Verde":
    print("| Tenemos este stock en verde", productlist.hoodies("cantidadVM"))

if VentaC>10 :
    while True:
        print("No hay suficiente stock ")
        break
print(9)

#print(productlist.hoodies)
ventaV = productlist.hoodies.get("cantidadVM")
ventaV = ventaV-VentaC
productlist.hoodies.update({"cantidadVM":ventaV})



