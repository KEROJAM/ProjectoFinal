import productlist
import time
import sys

no_stock = "No hay Stock en esa Talla"
bar = "|----------------------------------------------|"
menu_options = ("1", "2", "3",)
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


print(bar)
nombre = input("| Porporcione el nombre del empleado : ")

print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes", "listo para otro dia de trabajo?")

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
    print("| V - Venta\n| C - Compra\n| Q - Salir ")
    print(bar)
    user_input = input("| Elige una opcion: ")
    if user_input in menu_options:
        break
    else:
        print("| Esa no es una Opcion")


def Product_Type():
    while True:
        print(bar)
        print("| Elige que tipo de producto quieres: ")
        print("| Hoodies, Camisetas, Calcetines, Jeans, Tenis ")
        TipoPro = input("| ")
        if TipoPro in product_type:
            break
        elif TipoPro not in product_type:
            print(
                "| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
        else:
            print("| No tenemos tienes Ese producto")
        break
    return TipoPro


def Quit_Menu():
    sys.exit()


def Hoodies_Color_select():
    TipoPro = Product_Type()
    while True:
        if TipoPro == "Hoodies":
            print(bar)
            print("| Elige que Color quieres: ")
            print("| ", colorV, ", ", colorB, ", ",  colorN)
            colorP = input("| ")
            if colorP == colorV:
                break
    return colorP


Hoodies_Color_select()


def Color_Green_Size_Select():
    colorP = Hoodies_Color_select()
    if Hoodies_Color_select() == "Verde":
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaV = input("| ")
            if productlist.hoodies["cantidadVL"] == 0:
                print("No hay Stock en esa Talla") 
            if TallaV == "S":
                print("| Tenemos: ",
                  productlist.hoodies["cantidadVS"], " en Talla S")
            if TallaV == "M":
                print("| Tenemos: ",
                  productlist.hoodies["cantidadVM"], " en Talla M")
            if TallaV == "L":
                print("| Tenemos: ",
                  productlist.hoodies["cantidadVL"], " en Talla L")
            if Hoodies_Color_select(colorP) == "Blanco":
                while True:
                    print(bar)
            if productlist.hoodies["cantidadBL" or "cantidadBM" or "cantidadBS"] == 0:
                print("No hay stock ")
            
            

            if colorP == "Negro  ":
                while True:
                    print(bar)
            if productlist.hoodies["cantidadNL" or "cantidadNM" or "cantidadNS"] == 0:
                print("No hay stock ")
                
        break


Color_Green_Size_Select()
VentaC = int(input("| Cantidad de productos que quieres: "))
print("| En tu carrito hay: ", VentaC, " articulos")

if user_input == "1":
    Product_Type()
if user_input == "2":
    Quit_Menu()


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
