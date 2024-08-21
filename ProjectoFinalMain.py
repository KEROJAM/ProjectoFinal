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
        elif TipoPro not in product_type:
            print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
        else:
            print("| No tenemos tienes Ese producto")
            break

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
        if productlist.hoodies["cantidadVL" or "cantidadVM" or "cantidadVS"] == 0:
            print("No hay Stock") 
        break       
if colorP == "Blanco"   :
    while True:
        print (bar)  
        if productlist.hoodies["cantidadBL" or "cantidadBM" or "cantidadBS"] == 0 :  
                print("No hay stock ")   
        break 
if colorP =="Negro  " :
    while True :
        print (bar)     
        if productlist.hoodies["cantidadNL" or "cantidadNM" or "cantidadNS"] ==0 : 
                print("No hay stock ")           
        break
           

VentaC=int(input("| Cantidad de productos que quieres: "))
print("| En tu carrito hay: ", VentaC, " articulos")


print("| Stock del articulo Seleccionado: ",  productlist.hoodieVSC)
if TipoPro == "Hoodies" and colorP == "Verde ":
    print("| Tenemos este stock en verde talla L", productlist.hoodies["cantidadVL"])
if TipoPro == "Hoodies" and colorP == "Verde " :
    print("| Tenemos este stock en verde talla M ", productlist.hoodies["cantidadVM"])
if TipoPro == "Hoodies" and colorP == "Verde ":
    print ("|Tenemos este stock en Verde talla S", productlist.hoodies["cantidadVS"])

if VentaC>10 :
    while True:
        print("No hay suficiente stock ")
        break
if VentaC<10:
    while True:
        print("Si lo tenemos en stock")
        break
#print(productlist.hoodies)
ventaV = productlist.hoodies.get("cantidadVM")
ventaV = ventaV-VentaC
productlist.hoodies.update({"cantidadVM":ventaV})



