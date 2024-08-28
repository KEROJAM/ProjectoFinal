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
product_type = ("1", "2", "3", "4", "5")
color_options_hoddies = ("1", "2", "3",)
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
# aqui pedimos el nombre del usuario
print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes",
      "listo para otro dia de trabajo?")
# mensaje de bienvenida
print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Zapatos ")
# ponemos una lista de los productos que hay en stock
print("| \n! A continuacion te mostraremos el catalogo para que selecciones tus productos !")


def mensaje_espera():
    print("| Por favor, espera redirigiendo al menu ")
    time.sleep(5)
    # aqui ponemos un tiempo de espera de 5 segundos
    print("| ¡Gracias por esperar!")


mensaje_espera()

def shopping_cart():
    while True:
        try:
            Shopping_Cart = int(
                input("| ¿Cuántos artículos quieres agregar al carrito? "))
            #aqui se le pregunta al usuario cuantos productos va a agregar a su carrito de compras 
            
            if Shopping_Cart <= 0:
                print("| No tienes artículos en tu carrito.")
                # si el usuario no ha agregado ningun producto , se le notificara que no tiene ningun producto en el carrito 
                print(bar)
            elif Shopping_Cart > 10:
                print("| No puedes comprar más de 10 artículos.")
                #como tenemos un stock de 10 para todos los productos no se le permitira comprar mas 10 productos simultaneamente
                print(bar)
                time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
            else:
                print("| En tu carrito hay:", Shopping_Cart, "artículo/s.")
                #aqui se le notifica al usario el total de productos que tiene en su carrito de compra
                print(bar)
                return Shopping_Cart
        except ValueError:
            print("| El numero seleccionado supera la cantidad de articulos que hay en stock , favor de seleccionar otra cantidad.")
            #si el usuario excede la cantidad permitida de articulos , se le notificara que no se puede proceder con su transaccion

def Menu_principal():
    while True:
        print(bar)
        print("|     *Menu*")
        print("| 1 - Ordenar Porductos\n| 2 - Agregar Inventario\n| Q - Salir ")
        # este es el menu de opciones que aparece al principio , sirve para elegir que accion quieres hacer dentro del programa 
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
        print("| 1- Hoodies\n| 2- Camisetas\n| 3- Calcetines\n| 4- Jeans\n| 5- Tenis ")
        # aqui es otro menu para que el usuario pueda escoger que tipo de prenda de vestir desesa adquirir
        TipoPro = input("| ")
        if TipoPro in product_type:
            break
        elif TipoPro not in product_type:
            print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
            # si el usurio escribe mal una opcion aparecera el mesaje que se muestra arriba para que el usuario sea notificado de que escribio mal la opcion que deseaba elegir , por lo tanto tendra la oportunidad de escribirla nuevamente 
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        else:
            print("| No tenemos / tienes Ese producto")
            #si no hay stock de un producto o el usuario escoge una opcion que no esta dentro del menu de opciones aparecea el mensaje que se muestra en la parte de arriba 
    return TipoPro


def Quit_Menu():
    sys.exit()


def Hoodies_Color_select():
    while True:
        print(bar)
        print("| Elige que Color quieres: ")
        print("| 1-", colorV, "\n| 2-", colorB, "\n| 3-", colorN)
        # en las dos lineas anteriores a este comentario , el programa le da la oportunidad al usario de que escoja el color de la prenda que quiere, en este caso hoodies 
        colorP = input("| ")
        if colorP in color_options_hoddies:
            break
        elif colorP not in color_options_hoddies:
            print("| Ese no es un color\n| (Revise si esta escrito como esta en la pantalla)")
            #si el usuario escoge un color que no esta dentro del menu de opciones , el programa le notificara que ha escrito mal algo y le dara la oportunidad de volverlo a escribir
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        else:
            print("| No tenemos ese color")
    return colorP


def Hoodies_Color_Green_Size_Select():
    while True:
        print(bar)
        print("| Elige la Talla: ")
        print("| S, M, L")
        # aqui aparece un menu para poder elegir que talla quieres en la prenda que deseas comprar 
        TallaV = input("| ")
        if TallaV not in size_options:
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            #si el usuario selecciona una opcion incorrecta o que no aparece como tal en el menu de opciones , se le mostrara un mensaje que le indicara al usuario que vuelva a escribir o elegir la opcion deseada
        if TallaV == "S" and productlist.hoodies["cantidadVS"] == 0:
            print(no_stock)
            #si no hay existencias disponibles de hoodies en talla 'S' , se le notificara al usuario que no tenemos existencias de ese producto 
            print(bar)
            #se imprime una barra
        if TallaV == "S" and productlist.hoodies["cantidadVS"] >= 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadVS"], " en Talla S")
            #con el print que esta arriba de este comentario notifica al usuario cuantos productos tenemos disponibles con las caracteristicas del producto que escogio anteriormente
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaV == "M" and productlist.hoodies["cantidadVM"] == 0:
            print(no_stock)
            # si no hay existencia o se agota la cantidad de productos de la talla que el usuario selecciono , se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
        
        if TallaV == "M" and productlist.hoodies["cantidadVM"] > 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadVM"], " en Talla M")
            # si hay existencias en la talla del producto que selecciono el usuario , se le mostrara un mensaje que indique cuantas existencias del producto tenemos excatamente en la talla que eligio 
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaV == "L" and productlist.hoodies["cantidadVL"] == 0:
            print(no_stock)
            #si no hay existencias de hoodies en talla 'L' se le avisara al usuario que no hay existencias disponibles
        if TallaV == "L" and productlist.hoodies["cantidadVL"] >= 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadVL"], " en Talla L")
            #si tenemos existencias de hoodies de talla 'L' se le notificara al usario la cantidad que hoodies que tenemos disponibles en la talla que el escogio 
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        return TallaV


def Hoodies_Color_White_Size_Select():
    while True:
        print(bar)
        print("| Elige la Talla: ")    
        print("| S, M, L")
        #en los dos prints anteriores se le muestra al usuario un menu para elegir la talla del producto que quiere adquirir
        TallaB = input("| ")
        if TallaB == "S" and productlist.hoodies["cantidadBS"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadBS"], " en Talla S")
            #si selecciona la talla 'S' se le mostrara al usario cuantas existencias tenemos en esa talla
            print(bar)
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "S" and productlist.hoodies["cantidadBS"] == 0:
            print(no_stock)
            #si no tenemos existencias en la talla seleccionada por el usuario se le mostrara un mensaje que le notifiqueal usuario que no tenemos stock en la talla del producto que selecciono 
        if TallaB == "M" and productlist.hoodies["cantidadBM"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadBM"], " en Talla M")
            print(bar)
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "M" and productlist.hoodies["cantidadBM"] == 0:
            print(no_stock)
        if TallaB == "L" and productlist.hoodies["cantiadBL"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadBL"], " en Talla L")
            print(bar)
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "L" and productlist.hoodies["cantidadBL"] == 0:
            print(no_stock)
        return TallaB


def Hoodies_Color_Black_Size_select():
    while True:
        print(bar)
        #aqui se imprime una barra por cuestiones esteticas del programa 
        print("| Elige la Talla: ")
        #este es el titulo del menu para empezar a escoger la talla del producto 
        print("| S, M, L")
        #estas son las tallas disponibles que se mostraran en el menu
        TallaN = input("| ")
        if TallaN == "S" and productlist.hoodies["cantidadNS"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadNS"], " en Talla S")
            #se le mostrara al usuario el stock que tenemos de la talla seleccionada
            print(bar)
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaN == "S" and productlist.hoodies["cantidadNS"] == 0:
            print(no_stock)
            #si no hay existencias en la talla que el usuario selecciono se le mostrara un mensaje que le hara saber que no contamos con productos disponibes de la talla que eligio 
        if TallaN == "M" and productlist.hoodies["cantidadNM"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadNM"], " en Talla M")
            #el print de arriba le dira al usuario cuantas tallas tenemos en talla 'M' del producto que selecciono
            print(bar)
            #imprimira una barra por cuestiones esteticas del programa 
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaN == "M" and productlist.hoodies["cantidadNM"] == 0:
            print(no_stock)
            #si no hay existencias de la talla seleccionada para que el usuario sepa que no contamos con productos disponibles en la talla que escogio 
        if TallaN == "L" and productlist.hoodies["cantidadNL"] < 0:
            print("| Tenemos: ",
                  productlist.hoodies["cantidadNL"], " en Talla L")
            #se le mostrara al usuario la cantidad de productos talla 'L' que hay en stock 
            print(bar)
            #se imprimira una barra para que el programa se vea mas ordenado
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaN == "L" and productlist.hoodies["cantidadNL"] == 0:
            print(no_stock)
            #si no hay existencias en la talla sellecionada se le informara al usario que no hay existencias disponibles
        if TallaN in size_options:
            return TallaN
        else:
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            # si el usuario no escribio o selecciono mal una opcion se le mostrara un mensaje para que corrobore si escribio bien si opcion





if Menu_principal() == "1":
    product_select = Product_Type()
    if product_select == "1":
        color_size_select = Hoodies_Color_select()
        if color_size_select == "1":
            Hoodie_Green_Size_Select = Hoodies_Color_Green_Size_Select()
        if color_size_select == "2":
            Hoodie_Black_Size_Select = Hoodies_Color_Black_Size_select()
        if color_size_select == "3":
            Hoodie_White_Size_Select = Hoodies_Color_White_Size_Select()

        Shopping_Cart = shopping_cart()
        

if Menu_principal == "Q" or "q":
    Quit_Menu()
