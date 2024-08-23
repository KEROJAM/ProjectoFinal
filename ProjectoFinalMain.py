import productlist
import time
import sys

# Programa por Majorek Casas, Alan Anduaga
# 2024/08/23
# El programa es un sistema de ventas para la compañia Tecmi Clothes 
# que vende ropa como: Hoodies, Camisas, Jeans, Tenis y Calcetines

no_stock = "| No hay Stock en esa Talla"
bar = "|----------------------------------------------|"
menu_options = ("1", "2", "Q",)
product_type = ("Hoodies", "Camisetas", "Calcetines", "Jeans", "Tenis")
color_options_hoddies = ("Verde", "Negro", "Blanco",)
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
#aqui pedimos el nombre del usuario
print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes",
      "listo para otro dia de trabajo?")
#mensaje de bienvenida
print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Zapatos ")
#ponemos una lista de los productos que hay en stock 
print("| \n! A continuacion te mostraremos el catalogo para que selecciones tus productos !")


def mensaje_espera():
    print("| Por favor, espera redirigiendo al menu ")
    time.sleep(5)
    #aqui ponemos un tiempo de espera de 5 segundos
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
            time.sleep(2)
        else:
            print("| No tenemos tienes Ese producto")
    return TipoPro


def Quit_Menu():
    sys.exit()


def Hoodies_Color_select():
    while True:
        print(bar)
        print("| Elige que Color quieres: ")
        print("|",colorV,",",colorB,",",colorN)
        colorP = input("| ")
        if colorP in color_options_hoddies:
            break
        elif colorP not in color_options_hoddies:
            print("| Ese no es un color\n| (Revise si esta escrito como esta en la pantalla)")
            time.sleep(2)
        else:
            print("| No tenemos ese color")
    return colorP



def Hoodies_Color_Green_Size_Select():
    while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaV = input("| ")
            if TallaV not in size_options:
                print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            if TallaV == "S" and productlist.hoodies["cantidadVS"] == 0:
                print(no_stock)
                print(bar)
            if TallaV == "S" and productlist.hoodies["cantidadVS"] != 0:
                print("| Tenemos: ", productlist.hoodies["cantidadVS"], " en Talla S")
                print(bar)
            if TallaV == "M" and productlist.hoodies["cantidadVM"] == 0:
                print(no_stock)
            if TallaV =="M" and productlist.hoodies["cantidadVM"] != 0:
                print("| Tenemos: ", productlist.hoodies["cantidadVM"], " en Talla M")
                print(bar)
            if TallaV == "L" and productlist.hoodies["cantidadVL"] == 0:
                print(no_stock)
            if TallaV == "L" and productlist.hoodies["cantidadVL"] != 0:
                print("| Tenemos: ", productlist.hoodies["cantidadVL"], " en Talla L")
                print(bar)
            return TallaV


def Hoodies_Color_White_Size_Select():
        while True:
            print(bar)
            print("| Elige la Talla: ")
            print("| S, M, L")
            TallaB = input("| ")
            if TallaB == "S":
                print("| Tenemos: ", productlist.hoodies["cantidadBS"], " en Talla S")
                print(bar)
            elif TallaB == "S" and productlist.hoodies["cantidadBS"] == 0:
                print(no_stock)
            if TallaB == "M":
                print("| Tenemos: ", productlist.hoodies["cantidadBM"], " en Talla M")
            elif TallaB == "M" and productlist.hoodies["cantidadBM"] == 0:
                print(no_stock)
            if TallaB == "L":
                print("| Tenemos: ", productlist.hoodies["cantidadBL"], " en Talla L")
            elif TallaB == "L" and productlist.hoodies["cantidadBL"] == 0:
                print(no_stock)
            return TallaB


def Hoodies_Color_Black_Size_select():
    while True:
        print(bar)
        print("| Elige la Talla: ")
        print("| S, M, L")
        TallaN = input("| ")
        if TallaN not in size_options:
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
        if TallaN == "S":
            TallaN == "S"; productlist.hoodies["cantidadNS"]
            print("| Tenemos: ", productlist.hoodies["cantidadNS"], " en Talla S")
            print(bar)
        if TallaN == "S" and productlist.hoodies["cantidadNS"] == 0:
            print(no_stock)
        if TallaN == "M":
            TallaN == "M"; productlist.hoodies["cantidadNM"]
            print("| Tenemos: ", productlist.hoodies["cantidadNM"], " en Talla M")
            print(bar)
        elif TallaN == "M" and productlist.hoodies["cantidadNM"] == 0:
            print(no_stock)
        if TallaN == "L":
            TallaN == "L"; productlist.hoodies["cantidadNL"]
            print("| Tenemos: ", productlist.hoodies["cantidadNL"], " en Talla L")
            print(bar)
        elif TallaN == "L" and productlist.hoodies["cantidadNL"] == 0:
            print(no_stock)
        return TallaN

    
def shopping_car():
   
    VentaC = int(input("Cuantos productos desea comprar ?"))
    return VentaC
    

if Menu_principal() == "1":
    product_select=Product_Type()
    if product_select == "Hoodies":
        color_size_select=Hoodies_Color_select()
        if color_size_select == "Verde":
            Hoodie_Green_Size_Select=Hoodies_Color_Green_Size_Select()
        if color_size_select == "Negro":
            Hoodie_Black_Size_Select=Hoodies_Color_Black_Size_select()
        if color_size_select == "Blanco":
            Hoodie_White_Size_Select=Hoodies_Color_White_Size_Select()
        Shopping_Cart=shopping_car()

        if Shopping_Cart <= 0  :
            print("No tienes articulos en tu carrito ")
             
        elif Shopping_Cart > 10:
            print("No puedes comprar mas de 10 articulos  ")
   


if Menu_principal == "Q" or "q":
    Quit_Menu()




   


