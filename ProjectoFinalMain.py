import productlist
# Se importa el archivo de la lista de productos para usarse
import time
# Importamos time para poder tener tiempo de espera
import sys
# Importamos sys para poder salir del programa

# Programa por Majorek Casas, Alan Anduaga
# 2024/08/23
# El programa es un sistema de ventas para la compañia Tecmi Clothes
# que vende ropa como: Hoodies, Camisas, Jeans, Tenis y Calcetines

no_stock = "| No hay Stock en esa Talla"
# Declaramos la variable no_stock para no tener que esribirlo muchas veces
bar = "|----------------------------------------------|"
# Una bara para para que se vea bien y separa secciones del menu
menu_options = ("1", "2", "Q",)
# Esta variable esta para verificar si la respuesta que dio el usuario esta en las opciones
product_type = ("1", "2", "3", "4", "5", "R")
# Esta variable esta para verificar que sea realmente un producto que tenemos
color_options_hoddies = ("1", "2", "3",)
# Esta variable Sirve para verificar si es un color en Hoodies
color_options_camisetas = ("A", "N", "B",)
# Esta variable sirve para verificar si es un color en camisetas
color_options_calcetines = ("N", "B",)
# Esta variable esta para verificar el color de calcetines
color_options_tenis = ("B", "N", "B/N",)
# Se declara esta variable para verificar los colores de los tenis
color_options_jeans = ("A", "N",)
# Se nombra esa variable para verificar los colores de jeans
size_options = ("S", "M", "L",)
# Se nombra la variable para verificar las tallas de los productos
colorV = productlist.hoodies.get("colorV")
# Le ponemos el valor de las hoodies en color verde que esta en el otro archivo
colorN = productlist.hoodies.get("colorN")
# Le ponemos el valor de las hoodies en color negro que esta en el inventario
colorB = productlist.hoodies.get("colorB")
# Le ponemos el valor de las hoodies en color Blanco que esta en la lista de productos


print(bar)
# Se imprime la barra para poder separar el contenido y que se vea mejor
nombre = input("| Porporcione el nombre del empleado : ")
# aqui pedimos el nombre del usuario
print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes",
      "listo para otro dia de trabajo?")
# mensaje de bienvenida
print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Zapatos ")
# ponemos una lista de los productos que hay en stock
print("| \n! A continuacion te mostraremos el catalogo para que selecciones tus productos !")
# Se impirme este mensaje para informar al usuario de lo que va a pasar despues

def mensaje_espera():
# Aqui se define la funcion mensaje de espera prara poder usarla despues
    print("| Por favor, espera redirigiendo al menu ")
    # Dentro de mensaje de espera estamos imprimiendo el mensaje de espera
    time.sleep(5)
    # aqui ponemos un tiempo de espera de 5 segundos
    print("| ¡Gracias por esperar!")
    # Despues de esperar 5 segundos sale un agradecimiento por esperar


mensaje_espera()
# Ejecutamos la funcion mensaje de espera para que el mensaje de espera se vea
def Menu_principal():
    # Declaramos la funcion de mensaje de espera para poner todo el menu principal en una que sea mas accesible
    while True:
        # Se inicia el ciclo para que reaparesca el menu encaso que el usuario puso una opcion incorrecta
        print(bar)
        #con ese print imprime una barra que en total formara una pequeña interfaz para el programa 
        print("|     *Menu*")
        # Se impirme el titulo del menu
        print("| 1 - Ordenar Porductos\n| 2 - Agregar Inventario\n| Q - Salir ")
        # este es el menu de opciones que aparece al principio , sirve para elegir que accion quieres hacer dentro del programa 
        print(bar)
        #se vuelve a imprimir una barra
        user_input = input("| Elige una opcion: ")
        #aqui le da al usuario la indicacion de que ya puede empezar a escoger una indicacion 
        if user_input in menu_options:
            # Si la opcion que eligio el usuario esa en el menu
            return user_input
            # Se regresa el valor que el usuario selecciono para usarlo en el siguiente menu
        else:
            # si no esta en las opciones del menu
            print("| Esa no es una Opcion")
            #le avisara que hay que corregir lo que escribio

def Product_Type():
# definimos la funcion Product_Type para preguntar el usuario cual es el producto que quiere
    while True:
        # Iniciamos el loop para volver a impirmir el menu si el usuario se equivoca
        print(bar)
        #imprime una barra por tema estetico del programa
        print("| Elige que tipo de producto quieres: ")
        #aqui empieza la interaccion del usuario con el menu de productos
        print("| 1- Hoodies\n| 2- Camisetas\n| 3- Calcetines\n| 4- Jeans\n| 5- Tenis\n| R- Regresar", )
        # aqui es otro menu para que el usuario pueda escoger que tipo de prenda de vestir desesa adquirir
        TipoPro = input("| ")
        # Esta variable esta para guardar la opcion que el usuario decidio
        if TipoPro in product_type:
            # Si la opcion que eligio el usuario esta en las opciones
            return TipoPro
            # Regresa la opcion que eligio el usuario y rompe el cicl
        else:
            # Si la opcion que eligio no esta en las opciones
            print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
            # el usuario sea notificado de que escribio mal la opcion que deseaba elegir , por lo tanto tendra la oportunidad de escribirla nuevamente
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 

def Quit_Menu():
    # Se define la funcion de salir para usarla en el menu
    print("| Adios.")
    # imprimimos un mensaje en la pantalla antes de salir
    print(bar)
    # imprimmos una barra para mostrar que es el final
    time.sleep(1)
    # Le agregamos un segundo de espera para que el usuario lo lea
    sys.exit(1)
    # Este es un comando para que el programa termine

def Hoodies_Color_select():
    # Se define la funcion de seleccionar el color de hoodies para usarse en el menu
    while True:
        # Se inica un ciclo para poder repetir el menu sin tener que escribirlo muchas veces
        print(bar)
        #imprime otra barra
        print("| Elige que Color quieres: ")
        #es el titulo del menu para empezar a escoger el color del producto que selecciono el usuario
        print("| 1-", colorV, "\n| 2-", colorB, "\n| 3-", colorN)
        # en las dos lineas anteriores a este comentario , el programa le da la oportunidad al usario de que escoja el color de la prenda que quiere, en este caso hoodies 
        colorP = input("| ")
        # Se le pide al usuario insertar el color que desea y se guarda para usarse despues 
        if colorP in color_options_hoddies:
            # Si el color que inserto el usuario esta en las opciones
            return colorP
            # Se regresa el color que el usuario decidio para usarlo despues
        else:
            #si el color no esta en las opciones
            print("| Ese no es un color\n| (Revise si esta escrito como esta en la pantalla)")
            #el programa le notificara que ha escrito mal algo y le dara la oportunidad de volverlo a escribir
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 

def Hoodies_Color_Green_Size_Select():
    # Se define la opcion de hoodies verde para que el usuario seleccione la talla
    while True:
        # Se inicia el ciclo para que el menu vuelva a aparecer si el usuario se equivoca
        print(bar)
        #imprime una barra
        print("| Elige la Talla: ")
        #es el encabezado del menu para que el usuario escoja la talla del producto que selecciono
        print("| S, M, L")
        # aqui aparece un menu para poder elegir que talla quieres en la prenda que deseas comprar 
        TallaV = input("| ")
        # Se guarda la talla que eligio el usario en TallaV
        if TallaV not in size_options:
            #Si la talla que eligio el usario no esta en las opciones
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            #se le mostrara un mensaje que le indicara al usuario que vuelva a escribir o elegir la opcion deseada
        if TallaV == "S" and productlist.hoodies["cantidadVS"] == 0:
            # Si la talla es S y no hay inventario
            print(no_stock)
            #se le notificara al usuario que no tenemos existencias de ese producto
            print(bar)
            #se imprime una barra
        if TallaV == "S" and productlist.hoodies["cantidadVS"] > 0:
            # Si la talla es S y hay mas inventario que 0
            print("| Tenemos: ", productlist.hoodies["cantidadVS"], " en Talla S")
            #con el print que esta arriba de este comentario notifica al usuario cuantos productos tenemos disponibles con las caracteristicas del producto que escogio anteriormente
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaV == "M" and productlist.hoodies["cantidadVM"] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
        if TallaV == "M" and productlist.hoodies["cantidadVM"] > 0:
            # Si la talla es M y el inventario es mayor de 0
            print("| Tenemos: ", productlist.hoodies["cantidadVM"], " en Talla M")
            # se le mostrara un mensaje que indique cuantas existencias del producto tenemos excatamente en la talla que eligio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaV == "L" and productlist.hoodies["cantidadVL"] == 0:
            # Si la talla es L y no hay inventario
            print(no_stock)
            #se le avisara al usuario que no hay existencias disponibles
        if TallaV == "L" and productlist.hoodies["cantidadVL"] > 0:
            # Si la talla es L y en el inventario hay mas de 0
            print("| Tenemos: ", productlist.hoodies["cantidadVL"], " en Talla L")
            #se le notificara al usario la cantidad que hoodies que tenemos disponibles en la talla que el escogio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        return TallaV
        # Regresa el valor de Talla para poder usarse y pasar al siguiente menu

def Hoodies_Color_White_Size_Select():
    #Se declara la funcion para poder seleccionar la Talla de las Hoodies Blancas
    while True:
        # Se inicia ciclo para que el menu reaparesca si el usuario puso una opcion que no existe
        print(bar)
        # Se impirme una barra para separar contenidos
        print("| Elige la Talla: ")
        # Se impirme la primera parte de las opciones de elegir talla
        print("| S, M, L")
        #en los dos prints anteriores se le muestra al usuario un menu para elegir la talla del producto que quiere adquirir
        TallaB = input("| ")
        #Con la Talla que decidio el usuario se le asigna a TallaB
        if TallaB == "S" and productlist.hoodies["cantidadBS"] > 0:
            # Si el usuario Eligio Talla S verifica si tenemos mayor cantidad que 0 en el stock
            print("| Tenemos: ", productlist.hoodies["cantidadBS"], " en Talla S")
            #si selecciona la talla 'S' se le mostrara al usario cuantas existencias tenemos en esa talla
            print(bar)
            # Se impirme barra para separar los datos
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "S" and productlist.hoodies["cantidadBS"] == 0:
            # Si el usuario eligio talla S pero no hay inventario se imprime
            print(no_stock)
            #notifica al usuario que no tenemos stock en la talla del producto que selecciono
        if TallaB == "M" and productlist.hoodies["cantidadBM"] > 0:
            # Si la talla es M y el inventario es mas que 0
            print("| Tenemos: ", productlist.hoodies["cantidadBM"], " en Talla M")
            # Se imprime la cantidad de Hoodies que hay en esa talla en el inventario
            print(bar)
            # Se imprime la barra para poder separar los menus
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "M" and productlist.hoodies["cantidadBM"] == 0:
            # Si la talla es M y no hay inventario
            print(no_stock)
            # Se imprime que no hay inventario
        if TallaB == "L" and productlist.hoodies["cantiadBL"] > 0:
            # Si la talla L y en el inventario es mas de 0
            print("| Tenemos: ", productlist.hoodies["cantidadBL"], " en Talla L")
            #Se imprime la cantidad de productos que hay en Talla L
            print(bar)
            #Se imprime una barrra para separar los menus
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaB == "L" and productlist.hoodies["cantidadBL"] == 0:
            # Si la talla es L y no hay inventario
            print(no_stock)
            # Se le informa al usuario que no hay inventario
        return TallaB
        # Se Regresa el valor de la variable para poder usarala en el menu y carrito de compras

def Hoodies_Color_Black_Size_select():
    # Se define la funcion de Seleccionar la talla del color negro para Hoodies
    while True:
        # Se inicia el ciclo para poder mostar el menu otravez si el usuario se equivoco
        print(bar)
        #aqui se imprime una barra por cuestiones esteticas del programa 
        print("| Elige la Talla: ")
        #este es el titulo del menu para empezar a escoger la talla del producto 
        print("| S, M, L")
        #estas son las tallas disponibles que se mostraran en el menu
        TallaN = input("| ")
        # Se guarda la talla que eligio el usuario en la variable TallaN
        if TallaN == "S" and productlist.hoodies["cantidadNS"] < 0:
            #Si la Talla es S y el inventario es mayor a 0
            print("| Tenemos: ", productlist.hoodies["cantidadNS"], " en Talla S")
            #se le mostrara al usuario el stock que tenemos de la talla seleccionada
            print(bar)
            # Se imprime una barra para separar los menus
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaN == "S" and productlist.hoodies["cantidadNS"] == 0:
            # Si la talla es S y no hay inventario es 0
            print(no_stock)
            #se le mostrara un mensaje que le hara saber que no contamos con productos disponibes de la talla que eligio
        if TallaN == "M" and productlist.hoodies["cantidadNM"] < 0:
            # Si la talla es M y en el inventario es mayor a 0
            print("| Tenemos: ", productlist.hoodies["cantidadNM"], " en Talla M")
            #el print de arriba le dira al usuario cuantas tallas tenemos en talla 'M' del producto que selecciono
            print(bar)
            #imprimira una barra por cuestiones esteticas del programa 
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaN == "M" and productlist.hoodies["cantidadNM"] == 0:
            # Si la talla es M y no hay inventario
            print(no_stock)
            #Se le menciona al usuario que no hay inventario
        if TallaN == "L" and productlist.hoodies["cantidadNL"] < 0:
            # Si tallaN es L y tenemos mas productos en L que 0
            print("| Tenemos: ", productlist.hoodies["cantidadNL"], " en Talla L")
            #se le mostrara al usuario la cantidad de productos talla 'L' que hay en stock 
            print(bar)
            #se imprimira una barra para que el programa se vea mas ordenado
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaN == "L" and productlist.hoodies["cantidadNL"] == 0:
            #si no hay existencias en la talla sellecionada se le informara al usario que no hay existencias disponibles
            print(no_stock)
            #se muestra la pantalla que que no hay inventario 
        if TallaN in size_options:
            # Se verifica si la opcion de Talla esta en las opciones
            return TallaN
            # Si esta en las opciones se devuelve el valor para usarlo despues
        else:
            # Si no esta en las opciones
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            # se le mostrara un mensaje para que corrobore si escribio bien si opcion

def shopping_cart():
    # Aqui se define un a funciion para el carrito de compras 
    while True:
        # Se empieza el ciclo para que el menu sigua aunque este mal la respuesta
        try:
            Shopping_Cart = int(input("| ¿Cuántos artículos quieres agregar al carrito? "))
            #aqui se le pregunta al usuario cuantos productos va a agregar a su carrito de compras 
            
            if Shopping_Cart <= 0:
                # Si el carrito de compras es menor o igual a 0
                print("| No tienes artículos en tu carrito.")
                # se le notificara que no tiene ningun producto en el carrito
                print(bar)
                # Se imprime la barra para separar el menu
            elif Shopping_Cart > 10:
                # Si el carrito de compras es mas de 10
                print("| No puedes comprar más de 10 artículos.")
                #como tenemos un stock de 10 para todos los productos no se le permitira comprar mas 10 productos simultaneamente
                print(bar)
                # Se imprime la barra para separar el menu
                time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
            else:
                # Si no es menor o igual a cero y no es mayor a 10
                print("| En tu carrito hay:", Shopping_Cart, "artículo/s.")
                #aqui se le notifica al usario el total de productos que tiene en su carrito de compra
                print(bar)
                # Imprime la barra para separar los menus
                return Shopping_Cart
                # Regresa el valor de tu carrito
        except ValueError:
            print("| El numero seleccionado supera la cantidad de articulos que hay en stock , favor de seleccionar otra cantidad.")
            #si el usuario excede la cantidad permitida de articulos , se le notificara que no se puede proceder con su transaccion




while True:
    # Se inicia un ciclo para poder usar el mismo menu si la opcion es incorecta
    if Menu_principal() == "1":
        # Se ejecuta el menu Principal y Si la opcion del menu es 1
        product_select = Product_Type()
        # Se declara una variable para guardar el resultado de la funcion que contiene el menu de los usuarios
        if product_select == "1":
            # Si la opcion del producto es igual a 1 que es hoodies
            color_size_select = Hoodies_Color_select()
            # Se ejecuta la funcion del menu de color de hoodies y se guarda el resultado en una variable
            if color_size_select == "1":
                # Si la opcion del menu de colores es 1 (Verde)
                Hoodie_Green_Size_Select = Hoodies_Color_Green_Size_Select()
                # Se ejecuta el menu de seleccion de talla para el color verde y se guarda su resultado en una variable para poder usarse
            if color_size_select == "2":
                # Si la opcion del menu de colores es 2 (Negro)
                Hoodie_Black_Size_Select = Hoodies_Color_Black_Size_select()
                # Se ejecuta el menu de seleccion de talla para el color negro y se guarda su resultado en una variable para poder usarse
            if color_size_select == "3":
                # la opcion de la seleccion de colores es 3 (Blanco)
                Hoodie_White_Size_Select = Hoodies_Color_White_Size_Select()
                # Se ejecuta la funcion de Selecion de talla para el color blanco y se guarda su resultado en una variable para poder usarse
    if Menu_principal == "Q" or "q":
        # Si la opcion del Menu Principal es Q
        Quit_Menu()
        # Se ejectua la funcion de salir del programa

Shopping_Cart = shopping_cart()
# Se ejecuta la funcion de carrito de compras y se guarda su resultado en una variable para poder usarse
