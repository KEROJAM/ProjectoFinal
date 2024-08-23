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

print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes",
      "listo para otro dia de trabajo?")

print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Zapatos ")

print("| \n! A continuacion te mostraremos el catalogo para que selecciones tus productos !")


def mensaje_espera():
    print("| Por favor, espera redirigiendo al menu ")
    time.sleep(2)
    print("| ¡Gracias por esperar!")


mensaje_espera()

def Menu_principal():
    while True:
        print(bar)
        print("|     *Menu*")
        print("| 1 - Venta\n| 2 - Compra\n| Q - Salir ")
        print(bar)
        user_input = input("| Elige una opcion: ")
        if user_input in menu_options:
            break
        else:
            print("| Esa no es una Opcion")
        return user_input

def Product_Type():
    while True:
        print(bar)
        print("| Elige que tipo de producto quieres: ")
        print("| Hoodies, Camisetas, Calcetines, Jeans, Tenis ")
        TipoPro = input("| ")
        if TipoPro in product_type:
            break
        elif TipoPro not in product_type:
            print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
        else:
            print("| No tenemos tienes Ese producto")
        break
    return TipoPro


def Quit_Menu():
    sys.exit()


def Hoodies_Color_select():
    while True:
        print(bar)
        print("| Elige que Color quieres: ")
        print("| ", colorV, ", ", colorB, ", ",  colorN)
        colorP = input("| ")
        if colorP == colorV:
            break
    return colorP



def Hoodies_Color_Green_Size_Select():
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaV = input("| ")
            if TallaV == "S":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadVS"], " en Talla S")
            elif TallaV == "S" and productlist.hoodies["cantidadVS"] == 0:
                print(no_stock)
            if TallaV == "M":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadVM"], " en Talla M")
            elif TallaV == "M" and productlist.hoodies["cantidadVM"] == 0:
                print(no_stock)
            if TallaV == "L":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadVL"], " en Talla L")
            elif TallaV == "L" and productlist.hoodies["cantidadVL"] == 0:
                print(no_stock)
            return TallaV


def Hoodies_Color_White_Size_Select():
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaB = input("| ")
            if TallaB == "S":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadBS"], " en Talla S")
            elif TallaB == "S" and productlist.hoodies["cantidadBS"] == 0:
                print(no_stock)
            if TallaB == "M":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadBM"], " en Talla M")
            elif TallaB == "M" and productlist.hoodies["cantidadBM"] == 0:
                print(no_stock)
            if TallaB == "L":
                print("| Tenemos: ",
                      productlist.hoodies["cantidadBL"], " en Talla L")
            elif TallaB == "L" and productlist.hoodies["cantidadBL"] == 0:
                print(no_stock)
            return TallaB


def Hoodies_Color_Black_Size_select():
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaN = input("| ")
            if TallaN == "S":
                TallaN = "S"; productlist.hoodies["cantidadNS"]
                print("| Tenemos: ",
                      productlist.hoodies["cantidadNS"], " en Talla S")
            elif TallaN == "S" and productlist.hoodies["cantidadNS"] == 0:
                print(no_stock)
            if TallaN == "M":
                TallaN = "M"; productlist.hoodies["cantidadNM"]
                print("| Tenemos: ",
                      productlist.hoodies["cantidadNM"], " en Talla M")
            elif TallaN == "M" and productlist.hoodies["cantidadNM"] == 0:
                print(no_stock)
            if TallaN == "L":
                TallaN = "L"; productlist.hoodies["cantidadNL"]
                print("| Tenemos: ",
                      productlist.hoodies["cantidadNL"], " en Talla L")
            elif TallaN == "L" and productlist.hoodies["cantidadNL"] == 0:
                print(no_stock)
            return TallaN

    


Menu_principal()
if Menu_principal in menu_options:
    Product_Type()
if Menu_principal in ["Q", "q"]:
    Quit_Menu()
if Product_Type in product_type:
    Hoodies_Color_select()
if Hoodies_Color_select == "Verde":
    Hoodies_Color_Green_Size_Select()
if Hoodies_Color_select == "Negro":
    Hoodies_Color_Black_Size_select()
if Hoodies_Color_select == "Blanco":
    Hoodies_Color_White_Size_Select()




#print("| Stock del los articulos Seleccionados: ",  productlist.hoodieVSC)
#if Product_Type == "Hoodies" and Hoodies_Color_select() == "Verde ":
#    print("| Tenemos este stock en verde talla L",
#          productlist.hoodies["cantidadVL"])
#if TipoPro == "Hoodies" and colorP == "Verde ":
#    print("| Tenemos este stock en verde talla M ",
#          productlist.hoodies["cantidadVM"])
#if TipoPro == "Hoodies" and colorP == "Verde ":
#    print("|Tenemos este stock en Verde talla S",
#          productlist.hoodies["cantidadVS"])

VentaC = int(input("| Cantidad de productos que quieres: "))
print("| En tu carrito hay: ", VentaC, " articulos")


# print(productlist.hoodies)
ventaV = productlist.hoodies.get("cantidadVM")
ventaV = ventaV-VentaC
productlist.hoodies.update({"cantidadVM": ventaV})
