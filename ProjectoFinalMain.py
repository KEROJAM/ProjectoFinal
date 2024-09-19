import time
# Importamos time para poder tener tiempo de espera
import sys
# Importamos sys para poder salir del programa
import os
# Importamos os para poder limpiar la pantalla cuando corramos un comando
import csv
# Importamos csv para poder leer archivos csv con mas facilidad

# Programa por Majorek Casas, Alan Anduaga
# 2024/08/23
# El programa es un sistema de ventas para la compañia Tecmi Clothes
# que vende ropa como: Hoodies, Camisas, Jeans, Tenis y Calcetines
if os.name == "nt":
        # Si el sistema operativo es windows
        with open("C:\\Users\\alana\\Downloads\\python\\ProyectoFinalFundamentos\\DataBaseFinalProject.csv", 'r+') as file:
            # Se abre el archivo de la base de datos de manera que podamos leer el contenido y poder escribir en el
            Reader = csv.reader(file, delimiter=',')
            # Se guardan los datos del archivo en una variable llamada Reader
            ProductListCSV = list(Reader)
            # Y se hace una lista con el contenido
else:
        with open("DataBaseFinalProject.csv", 'r+') as file:
            # Se abre el archivo de la base de datos de manera que podamos leer el contenido y poder escribir en el
            Reader = csv.reader(file, delimiter=',')
            # Se guardan los datos del archivo en una variable llamada Reader
            ProductListCSV = list(Reader)
            # Y se hace una lista con el contenido


no_stock = "| No hay Stock en esa Talla"
# Declaramos que  no hay stock para no tener que esribirlo muchas veces
bar = "|----------------------------------------------|"
# Una bara para para que se vea bien y separa secciones del menu
ReturnPrint = "| R - Regresar"
menu_options = ["1", "2", "3","4", "Q"], ["1- Ordenar Productos","2- Agregar Inventario","3- Mostrar Inventario","4- Imprimir Monto total de Ventas","Q- Salir"]
# Esta  es una enunciado ,sirve para verificar si la respuesta que dio el usuario esta en las opciones
product_type = ["1", "2", "3", "4", "5","6","R"], ["1- Hoodies", "2- Camisetas", "3- Jeans", "4- Calcetines", "5- Pants", "6- Imprimir Nota", "R- Regresar"],["600", "350", "360", "40", "400"]
# Esta es otra enunciado, sirve para verificar que sea realmente un producto que tenemos
color_options = ("1", "2", "3","R")
# Este texto Sirve para verificar si es un color en Hoodies
size_options = ["S", "M", "L","R"],["S","M","L","R- Regresar"]
# Se nombra la enunciado para verificar las tallas de los productos
imprNot_opt = [["R"],["Hoodies","Verde", "Negro", "Blanco", "$600"], [ "Camisetas","Azul", "Negro", "Blanco", "$350"],["Jeans","Azul","Negro","Azul Oscuro", "$360"],["Calcetines","Rosas","Negro","Blanco", "$40"],["Pants","Negro y Blanco", "Negro", "Blanco", "$400"],["R- Regresar"]]
# Se cera una lista de todos los productos y sus colores
Shopping_Cart = 0
# Se define la variable Shopping cart para usar el carrito de compras
j = 0
# Se inicia un Contador para moverse entre la lista
Shopping_Cart_List=[]
# Esta es la lista del carrito que tiene el usuario por session
print(bar)
# Se imprime la barra para poder separar el contenido y que se vea mejor
NoteShopping_Cart_List=[]
# Se inicia una lista para imprimir nota
nombre = input("| Porporcione el nombre del empleado : ")
# aqui pedimos el nombre del usuario
print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a Tecmi clothes",
      "listo para otro dia de trabajo?")
# mensaje de bienvenida
print("| \n| Estos son los productos que tenemos disponibles : Hoodies , Camisas , Jeans , Calcetines y Tenis")
# ponemos una lista de los productos que hay en stock
print("| \n| A continuacion te mostraremos el catalogo para que selecciones tus productos !")
# Se impirme este mensaje para informar al usuario de lo que va a pasar despues
LenProductListCSV = len(ProductListCSV) - 1
# De la lista de la base de datos se lee la longitud(16) y se le quita uno para solo usar los datos
h = 1
# Se hace un contador para establecer que queremos el primer producto
for i in range(LenProductListCSV):
    # Se inicia un ciclo que se repite la longitud de la base de datos
    for m in range(4):
        # Se inicia un ciclo dentro del ciclo que se repite 4 veces parra conventir los precios e inventario en numeros que podemos usar
        NumProd = int(ProductListCSV[h][2])
        # Se guarda el numero de la linea especificada como la cantidad de inventario o precio y se convierte en un numero usable
        del ProductListCSV[h][2]
        # Se borra el numero agarrado
        ProductListCSV[h].append(NumProd)
        # Y se agrega otavez pero como numero que podemos usar para operaciones
    h+=1
    # Se le agrega 1 al contador para movernos a la siguiente linea
    i+=1
    # Y se agrega 1 al otro contador para seguir a la siguiente linea

def mensaje_espera():
# Aqui se define la texto mensaje de espera prara poder usarla despues
    print("| Por favor, espera redirigiendo al menu ")
    # Dentro de mensaje de espera estamos imprimiendo el mensaje de espera
    time.sleep(5)
    # aqui ponemos un tiempo de espera de 5 segundos
    print("| ¡Gracias por esperar!")
    # Despues de esperar 5 segundos sale un agradecimiento por esperar

def ClearTer():
    # Se define la funcion de limpiar pantalla
    if os.name == "nt":
        # Si el sistema operativo es windows
        _ = os.system('cls')
        # Se ejecuta el comando cls para limpiar la pantalla en la terminal
    else:
        # Si no es windows osea mac y linux
        _ = os.system('clear')
        # Se ejectua el comando clear para limipar la pantalla en la terminal

mensaje_espera()
# Ejecutamos el texto mensaje de espera para que el mensaje de espera se vea

def Menu_principal():
    # Declaramos el texto de mensaje de espera para poner todo el menu principal en una que sea mas accesible
    while True:
        # Se inicia el ciclo para que reaparesca el menu encaso que el usuario puso una opcion incorrecta
        try:
        #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo        
            print(bar)
            #con ese print imprime una barra que en total formara una pequeña interfaz para el programa
            print("|    Tecmi Clothes")
            #aqui se imprime el titulo o el nombre de la empresa en el menu            
            print("|    Hola ", nombre)
            # Se le saluda al usuario
            print("|     *Menu*")
            # Se impirme el titulo del menu principal
            print("|","\n| ".join(menu_options[1]), end="\n")
            # este es el menu de opciones que aparece al principio , sirve para elegir que accion quieres hacer dentro del programa
            print(bar)
            #se vuelve a imprimir una barra
            user_input = input("| Elige una opcion: ")
            #aqui le da al usuario la indicacion de que ya puede empezar a escoger una indicacion 
            if user_input in menu_options[0]:
                # Si la opcion que eligio el usuario esa en el menu
                return user_input
                # Se regresa el valor que el usuario selecciono para usarlo en el siguiente menu
            else:
                # si no esta en las opciones del menu
                print("| Esa no es una Opcion")
                #le avisara que hay que corregir lo que escribio
        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("Caracter invalido , favor de revisar si selecciono bien la opcion o tuvo algun error al escribir ")
            #este es el cartel que se imprime cuando el usuario se equivoca

def Product_Type():
# definimos el texto Product_Type para preguntar el usuario cual es el producto que quiere
    ClearTer()
    # Se limipa la patnalla
    while True:
        # Iniciamos el loop para volver a impirmir el menu si el usuario se equivoca
        try:
        #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            print(bar)
            #imprime una barra por tema estetico del programa
            print("| Elige que tipo de producto quieres: ")
            #aqui empieza la interaccion del usuario con el menu de productos
            print("|","\n| ".join(product_type[1]), end="\n" )
            # aqui es otro menu para que el usuario pueda escoger que tipo de prenda de vestir desesa adquirir
            TipoPro = input("| ")
            # Esta variable esta para guardar la opcion que el usuario decidio
            if TipoPro in product_type[0]:
                # Si la opcion que eligio el usuario esta en las opciones
                return TipoPro
                # Regresa la opcion que eligio el usuario y rompe el cicl
            else:
                # Si la opcion que eligio no esta en las opciones
                print("| Ese no es un producto\n| (Revise si esta escrito como esta en la pantalla)")
                # el usuario sea notificado de que escribio mal la opcion que deseaba elegir , por lo tanto tendra la oportunidad de escribirla nuevamente
                time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa
        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("Opcion invalida favor de revisar su seleccion ")
            #este es el cartel que se imprime cuando el usuario se equivoca


def Imprimir_Nota(j,s=0):
    # Se Define el menu de Imprimir nota de inventario
    LengthShopping = len(NoteShopping_Cart_List)
    # Se le asigna un valor a la longitud de el carrito de compras para usarlo en el ciclo
    print(bar)
    # Se impirme una barra para separar contenido
    print("| Cantidad de Inventario por cada producto")
    # Se le informa al usuario que es la informacion
    # Se muestra el boton de regresar
    if j == 0:
        # Si j es igual a 0
            print("| No hay nada en su carrito de compras\n| Ponga productos en su carrito para verlos aqui")
            # Se le informa al usuario que no hay nada en su carrito de compras
    if j >= 1:
        # Si j es igual o mayor a 1
            print("| En su carrito hay: ")
            # Se impirme el titulo de la nota
            print("|Cant|  Prod  | Car1 | Car2 | Precio | Total |")
            # Se impirme el inico de la tabla
            for i in range(LengthShopping):
                # Se inicia un ciclo del tamaño de la tabla
                print("|", " | ".join(s[i]), end=" |\n")
                # Se impirme lo que hay en  el carrtio de compras mediante una lista que tiene un contador para mostar cada producto
                i +=1
                # Se le agrega 1 al contador cada vez que pase el ciclo
        # Se impirme el carrito de compras
    ImprNot=input("| Escriba R para Regresar: ")
    # Se le pide al usuario que ingrese regresar
    if ImprNot in imprNot_opt[0]:
        # Si lo que puso el usuario esta en las opciones
        return ImprNot
        # Regresa el valor para usarlo en el menu
        print(bar)
        # Se imprime una barra para separar contenido
    else:
        # Si lo que puso el usuario no esta en las opciones
        print("| Esa no es una opcion, La unica opcion es R")
        # Se le informa al usuario que no es una opcion

def Quit_Menu():
    # Se define el texto de salir para usarla en el menu
    print("| Adios.")
    # imprimimos un mensaje en la pantalla antes de salir
    print(bar)
    # imprimmos una barra para mostrar que es el final
    time.sleep(1)
    # Le agregamos un segundo de espera para que el usuario lo lea
    sys.exit()
    # Este es un comando para que el programa termine

def Color_select(m):
    # Se define el texto de seleccionar el color de hoodies para usarse en el menu
    if m == "1":
        h = 1
    elif m == "2":
        h = 4
    elif m == "3":
        h = 7
    elif m == "4":
        h = 10
    elif m == "5":
        h = 13
    ClearTer()
    while True:
        # Se inica un ciclo para poder repetir el menu sin tener que escribirlo muchas veces
        try:
            #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            print(bar), 
            #imprime otra barra
            print("| Elige que Color quieres: ")
            #es el titulo del menu para empezar a escoger el color del producto que selecciono el usuario
            for i in range(3):
                i+=1
                print("|",i,"-",ProductListCSV[h][1])
                h+=1
            print(ReturnPrint)
            # en las dos lineas anteriores a este comentario , el programa le da la oportunidad al usario de que escoja el color de la prenda que quiere, en este caso hoodies
            colorI = input("| ")
            # Se le pide al usuario insertar el color que desea y se guarda para usarse despues 
            if colorI in color_options:
                # Si el color que inserto el usuario esta en las opciones
                return colorI
                # Se regresa el color que el usuario decidio para usarlo despues
            else:
                #si el color no esta en las opciones
                print("| Ese no es un color\n| (Revise si esta escrito como esta en la pantalla)")
                #el programa le notificara que ha escrito mal algo y le dara la oportunidad de volverlo a escribir
                time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa
        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("Opcion invalida , favor de revisar si selecciono una opcion que este disponible en el menu")
            #este es el cartel que se imprime cuando el usuario se equivoca


def Size_Select(m,h):
    # Se define la opcion de hoodies verde para que el usuario seleccione la talla
    i = int(m)
    k = int(h)
    if i == 1:
        if k == 1:
           v = 1
        elif k == 2:
           v = 2
        elif k == 3:
           v = 3
    elif i == 2:
        if k == 1:
           v = 4
        elif k == 2:
           v = 5
        elif k == 3:
           v = 6
    elif i == 3:
        if k == 1:
           v = 7
        elif k == 2:
           v = 8
        elif k == 3:
           v = 9
    if i == 4:
        if k == 1:
           v = 10
        elif k == 2:
           v = 11
        elif k == 3:
           v = 12
    if i == 5:
        if k == 1:
           v = 13
        elif k == 2:
           v = 14
        elif k == 3:
           v = 15
    ClearTer()
    while True:
        # Se inicia el ciclo para que el menu vuelva a aparecer si el usuario se equivoca
        print(bar)
        #imprime una barra
        print("| Elige la Talla: ")
        #es el encabezado del menu para que el usuario escoja la talla del producto que selecciono
        print("|","\n| ".join(size_options[1]), end="\n")
        # aqui aparece un menu para poder elegir que talla quieres en la prenda que deseas comprar 
        TallaV = input("| ")
        # Se guarda la talla que eligio el usario en TallaV
        if TallaV == "S" and ProductListCSV[v][2] > 0:
            # Si la talla es S y hay mas inventario que 0
            print("| Tenemos:", ProductListCSV[v][2], "En Talla S")
            #con el print que esta arriba de este comentario notifica al usuario cuantos productos tenemos disponibles con las caracteristicas del producto que escogio anteriormente
            print(bar)
            #se imprime una barra
            time.sleep(2)
        elif TallaV == "S" and ProductListCSV[v][2] == 0:
            print(no_stock)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        if TallaV == "M" and ProductListCSV[v][3] > 0:
            # Si la talla es M y el inventario es mayor de 0
            print("| Tenemos:", ProductListCSV[v][3], "En Talla M")
            # se le mostrara un mensaje que indique cuantas existencias del producto tenemos excatamente en la talla que eligio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaV == "M" and ProductListCSV[v][3] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
        if TallaV == "L" and ProductListCSV[v][4] > 0:
            # Si la talla es L y en el inventario hay mas de 0
            print("| Tenemos:", ProductListCSV[v][4], "en Talla L")
            #se le notificara al usario la cantidad que hoodies que tenemos disponibles en la talla que el escogio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
        elif TallaV == "L" and ProductListCSV[v][4] == 0:
            # Si la talla es L y no hay inventario
            print(no_stock)
            #se le avisara al usuario que no hay existencias disponibles
        if TallaV in size_options[0]:
                return TallaV
            # Regresa el valor de Talla para poder usarse y pasar al siguiente menu
        else:
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            time.sleep(2)

def shopping_cart(n,j,u,w):
    # Aqui se define un a funciion para el carrito de compras
    c = int(w)
    # El valor del numero que color que eligio el usuario es guardado como c para mas facilidad e uso
    TempShopping_Cart_List=[]
    while True:
        # Se empieza el ciclo para que el menu sigua aunque este mal la respuesta
        try :
        #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            if n == "1":
                # Si el usuario eligio Hoodies
                print("| Las hoodies cuestan $600")
                # Se le informa cuanto cuestan las Hoodies
                ProductPrice = 600
                # Se asigna el precio al producto para mostrarlo al final
                ProductName = "Hoodies"
                # Se le asigna El nombre de producto para mostrarlo
                i = 1
                # Sirve como un incide en la lista de productos
            elif n == "2":
                # Si el usuario eligio Camisas
                print("| Las camisas cuestan $350")
                # Se le informa cuanto cuestan las camisas
                ProductPrice = 350
                # Se asigna el precio indicado
                ProductName = "Camisetas"
                # Se asigna el Producto para mostarlo al final
                i = 2
                # Sirve como indice en la lista de productos
            elif n == "3":
                # Si el usuario eligio Jeans
                print("| Los Jeans cuestan $360")
                # Se le informa cuanto es el costo de los Jeans
                ProductPrice = 360
                # Se le asigna un valor al costo
                ProductName = "Jeans"
                # Se le asigna el Producto para mostrarlo en el carrito
                i = 3
                # Sirve como indice en la lista de productos
            elif n == "4":
                # Si el usuario eligo calcetines
                print("| Los Calcetines cuestan $40")
                # Se le infroma al usuario el costo de los calcetines
                ProductPrice = 40
                # Se asigna el precio al producto
                ProductName = "Clacetines"
                # y se asigna el producto para mostarlo en el carrito de compras
                i = 4
                # Sirve como indice en la lista de productos
            elif n == "5":
                # Si el usuario eligio pants
                print("| Los Pants cuestan $400")
                # Se le informa al usuario el costo de los Pants
                ProductPrice = 400
                # Se les asigna un valor a los pantalones
                ProductName = "Pants"
                # Se asigna un producto para poder mostar el producto en el carrito de compras
                i = 5
                # Sirve como indice en la lista de productos
        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo#con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("La opcion seleccionada es incorrecta favor de reintentar con otra opcion")
            #este es el cartel que se imprime cuando el usuario se equivoca

        try:
            # nos deja probar si el codigo de abajo textoa para dectectar errores
            Shopping_Cart_Amount = int(input("| ¿Cuántos artículos quieres agregar al carrito? "))
            #aqui se le pregunta al usuario cuantos productos va a agregar a su carrito de compras 
            
            if Shopping_Cart_Amount <= 0:
                # Si el carrito de compras es menor o igual a 0
                print("| No tienes artículos en tu carrito.")
                # se le notificara que no tiene ningun producto en el carrito
                print(bar)
                # Se imprime la barra para separar el menu
            elif Shopping_Cart_Amount > 10:
                # Si el carrito de compras es mas de 10
                print("| No puedes comprar más de 10 artículos.")
                #como tenemos un stock de 10 para todos los productos no se le permitira comprar mas 10 productos simultaneamente
                print(bar)
                # Se imprime la barra para separar el menu
                time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa 
            else:
                # Si no es menor o igual a cero y no es mayor a 10
                TotalProductPrice = Shopping_Cart_Amount*ProductPrice
                # Se multiplica la cantidad de articulos que quiere el usuario por el precio del producto
                print("| Se agrego:", Shopping_Cart_Amount, ProductName, imprNot_opt[i][c] , u , "$",TotalProductPrice, " a tu carrito de compras.")
                #aqui se le notifica al usario el total de productos que tiene en su carrito de compra
                Shopping_Cart_AmountSTR = str(Shopping_Cart_Amount)
                # Se convierte el valor del shoppint cart a una string para poder imprimirlo en la nota
                TempShopping_Cart_List.append(Shopping_Cart_AmountSTR)
                # A la lista se le agega el Monto total de articulos
                TempShopping_Cart_List.append(ProductName)
                # A la lista se le agega el Producto que eligio el usuario
                TempShopping_Cart_List.append(imprNot_opt[i][c])
                # Se agrega el color a la lista temporal
                TempShopping_Cart_List.append(u)
                # Se agrega la talla a la lista temporal
                TotalProductPriceSTR = str(TotalProductPrice)
                # Convierte el precio total de tu compra en string para que se pueda impirmir mas facil
                TempShopping_Cart_List.append(TotalProductPriceSTR)
                # Y se agrega el Precio total de la cantidad por el precio

                if j == 0:
                    # Si J es igual a 0
                    TotalShoppingCart = TotalProductPrice
                    # Se asigna el valor de El total de el producto multiplicado por el precio mas el total de todos los productos
                    TotalShoppingCartSTR = str(TotalShoppingCart)
                    # SE convierte el total del carito en un string
                    TempShopping_Cart_List.append(TotalShoppingCartSTR)
                    # Se le agrega a una lista el Total de todos los productos
                    NoteShopping_Cart_List.append(TempShopping_Cart_List)
                    print(NoteShopping_Cart_List)
                    Shopping_Cart_List.append(TempShopping_Cart_List)
                    # Se le agrega a el shopping cart principal la lista de los productos mas el precio total del shopping cart
                elif j > 0:
                    # Si j es mayor que 0
                    TotalShoppingCart = int(Shopping_Cart_List[0][-1])
                    # Se agara el valor del precio total de todo el carrito de compras
                    TotalShoppingCart = TotalShoppingCart + TotalProductPrice
                    # Se suma el valor total de Carrito de compras a el valor total de los productos elegidos ahorita
                    TotalShoppingCartSTR = str(TotalShoppingCart)
                    print(NoteShopping_Cart_List)
                    NoteShoppingTotal = int(NoteShopping_Cart_List[0][-1])
                    NoteShoppingTotal = NoteShoppingTotal + TotalProductPrice
                    NoteShoppingTotalSTR = str(NoteShoppingTotal)
                    # Se convierte el total del carrito de compras a stirng para poder impirmirlo en la nota
                    del NoteShopping_Cart_List[0][-1]
                    NoteShopping_Cart_List[0].append(NoteShoppingTotalSTR)
                    NoteShopping_Cart_List.append(TempShopping_Cart_List)
                    del Shopping_Cart_List[0][-1]
                    Shopping_Cart_List[0].append(TotalShoppingCartSTR)
                    Shopping_Cart_List.append(NoteShopping_Cart_List)
                    # Se agrega el valor de los productos nuevos al Carrito de compras
                print(bar)
                # Imprime la barra para separar los menus
                return NoteShopping_Cart_List
                # Regresa el valor de tu carrito
        except ValueError:
            # Nos deja solucionar cualquier error que tengamos en este caso que el usuario selecciono una cantidad superior a la que tenemos
            print("| El numero seleccionado supera la cantidad de articulos que hay en stock , favor de seleccionar otra cantidad.")
            #si el usuario excede la cantidad permitida de articulos , se le notificara que no se puede proceder con su transaccion

def Imprimir_Inv():
    while True:
        TotalInv = 0
        h = 0
        print(bar)
        print("| Inventario Total: ")
        for i in range(5):
              for m in range(3):
                    h+=1
                    s = 2
                    for u in range(3):
                          TotalInv += ProductListCSV[h][s]
                          s+=1
                    m += 1
              print("|",ProductListCSV[h][0],TotalInv)
              TotalInv = 0
              i+=1
        InvRes = input("| R- Regresar ")
        if InvRes in imprNot_opt[0]:
            return InvRes
        else:
            print("| Esa no es una opcion Porfavor eliga R")

def MontoTotalVentas():
    # Este es el menu de Monto total de ventas
    while True:
        # Se inicia un ciclo para repetir el menu si el usuario se equivoco
            print("| Este es el monto total de todas las ventas de Session: ",Shopping_Cart[0][-1])
            # Se imprime monto total de ventas en la session
            print("|",imprNot_opt[1][5])
            # Se imprime la opcion de regresar
            MontoTotalOpcion=input("| Eliga Regresar para volver al menu principal: ")
            # Se le informa al usuario que hacer para regresar al menu principal
            if MontoTotalOpcion in imprNot_opt[0]:
                # si el usuario eligo una opcion que si esta en el menu
                return MontoTotalOpcion
                # Se regresa el valor para usarlo en el menu
            else:
                # Si esa opcion no esta en el menu
                print("| Esa no es una opcion porfavor eliga R")
                # Se le informa que es una opcion incorrecta
        

while True:
    # Se inicia un ciclo para poder usar el mismo menu si la opcion es incorecta
    MenuPrincipal = Menu_principal()
    #Se ejecuta el menu Principal
    while True:
        try:
        #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            if MenuPrincipal == "1":
                # Si la opcion del menu es 1
                product_select = Product_Type()
                # Se declara una enunciado para guardar el resultado de la texto que contiene el menu de los usuarios
                if product_select == "1":
                # Si la opcion del producto es igual a 1 que es hoodies
                    Color_selectRes = Color_select(product_select)
                    # Se ejecuta la texto del menu de color de hoodies y se guarda el resultado en una enunciado
                    if Color_selectRes == "1":
                        # Si la opcion del menu de colores es 1 (Verde)
                        Size_select = Size_Select(product_select,Color_selectRes)
                        # Se ejecuta el menu de seleccion de talla para el color verde y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "2":
                        # Si la opcion del menu de colores es 2 (Negro)
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se ejecuta el menu de seleccion de talla para el color negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "3":
                        # la opcion de la seleccion de colores es 3 (Blanco)
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se ejecuta la texto de Selecion de talla para el color blanco y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "R":
                        # Si la opcion es R se
                        ClearTer()
                        # Limpia la pantalla
                        continue
                        # Regresa al menu principal

                elif product_select == "2" :
                    # Si la opcion del producto es igual a 2 quiere decir que el usuario selecciono camisetas
                    Color_selectRes = Color_select(product_select)
                    # Se ejecuta la texto del menu de color de camisetas y se guarda el resultado en una enunciado
                    if Color_selectRes == "1":
                        # Si la opcion del menu de colores es 1 (Azul)
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se ejecuta el menu de seleccion de talla para el color Azul y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes ==  "2":
                        # Si la opcion del menu es igual a 2 se abrira el menu para empezar a personalizar tu pedido de camisetas de color negro
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se ejecuta el menu de seleccion de talla para el color Negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "3" :
                        #si se selecciona la opcion 3 empezara a elegir camisetas de color blanco
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se ejecuta el menu de seleccion de talla para el color Blanco y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "R":
                        # Si el usuario selecciono la opcion R
                        ClearTer()
                        # Se limpia la pantalla
                        continue
                        # Y regresa al menu principal

                elif product_select == "3":
                #si el usuario selecciona la opcion tres lo redirigira al menu para elegir calcetines
                    Color_selectRes=Color_select(product_select)
                    #se ejecuta el texto del menu de color de calcetines y se guarda el resultado
                    if Color_selectRes == "1":
                        #si la opcion seleccionada es 1 el usuario esta eligiendo el color negro para sus calcetines
                        Size_select = Size_Select(product_select, Color_selectRes)
                        #Se ejecuta el menu de seleccion de talla para el color negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "2":
                        #si la opcion seleccionada es igal a 2 quiere decir que el usuario esta eligiendo el color negro para sus calcetines
                        Size_select = Size_Select(product_select, Color_selectRes)
                        #se ejecuta el menu de seleecion de tallas para el color blanco para calcetines y se guarda el resultado
                    elif Color_selectRes == "3":
                        Size_select = Size_Select(product_select, Color_selectRes)
                    elif Color_selectRes == "R":
                        # Si el usuario elige la opcion R
                        ClearTer()
                        # Se limipia la pantala
                        continue
                        # Y vuelve al menu principal

                elif product_select == "4":
                    # Si el usuario eligio Jeans en producto
                    Color_selectRes = Color_select(product_select)
                    # Se le pide el color que eligira
                    if Color_selectRes == "1":
                    # Si el Usuario selecciono azul
                        Size_select = Size_Select(product_select, Color_selectRes)
                    # Se le pregunta que talla va a nececitar para los Jeans Azules
                    elif Color_selectRes == "2" :
                    # Si Eligio Jeans Negros
                        Size_select = Size_Select(product_select, Color_selectRes)
                        # Se le pregunta la Talla de los Jeans Negros
                    elif Color_selectRes == "R":
                        # Si eligio Regresar
                        ClearTer()
                        # Se limipa la pantalla
                        continue
                    # Y Se regersa al menu principal

            elif product_select == "5":
            # Si eligio Pants
                Color_selectRes = Color_select(product_select)
                # Se le da la opcion de elegi que color va a querer en Pants
                if Color_selectRes == "1":
                    # Si el color Es blanco y nergo
                    Size_select = Size_Select(product_select, Color_selectRes)
                    # Se le pide al usuario que seleccione una talla
                elif Color_selectRes == "2":
                    # Si selecciono Negro
                    Size_select = Size_Select(product_select, Color_selectRes)
                    # Se le pide al usuario que eliga que Talla va a necesitar para Pants Negros
                elif Color_selectRes == "3":
                    # Si eligo Pants Blancos
                    Size_select = Size_Select(product_select, Color_selectRes)
                    # Se le pide al usuario que seleccione la Talla de Pants Blancos
                elif Color_selectRes == "R":
                    # Si Selecciona regresar
                    ClearTer()
                    # Se limpia la pantalla
                    continue
                # Y se regersa al menu principal
            elif product_select == "6":
                # Si el usuario eligio 3 en el menu principal
                ClearTer()
                # Se limpia la pantalla para que se vea mas limpio
                Imprimir_Nota_Res = Imprimir_Nota(j,Shopping_Cart)
                # Se imprime la nota de todo el inventario
                if Imprimir_Nota_Res == "R":
                # Si la opcion en Imprimir nota es R
                    continue
                # Se regresa al menu principal
            elif product_select == "R":
            # Si el usuario eligio Regresar en la seleccion de productos
                 NoteShopping_Cart_List=[]
                 j=0
                 break
            # Se regresa al menu principal
            Shopping_Cart = shopping_cart(product_select , j, Size_select, Color_selectRes)
            # Se ejecuta la texto de carrito de compras y se guarda su resultado en una enunciado para poder usarse
            j+=1
            # Se le agrega 1 al contador para que se vaya a la siguiente producto
            time.sleep(2)
            # Le da al usuario tiempo de ver el precio de los productos que eligieron
        elif MenuPrincipal == "3":
                Imprimir_InvRes = Imprimir_Inv()
                if Imprimir_InvRes == "R":
                   continue

            elif MenuPrincipal == "4":
                # Si el usuario eligio Monto total de ventas en el menu principal
                Monto_Ventas_Total = MontoTotalVentas()
                # Se ejecuta el menu de Monto total de Ventas
                if Monto_Ventas_Total == "R":
                    # Si el usuario eligio regresar al menu principal en Monto de ventas

                    continue
                    # Se regresa al menu principal

            elif MenuPrincipal == "Q" or "q":
            # Si la opcion del Menu Principal es Q
                Quit_Menu()
                # Se ejectua la texto de salir del programa
        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("Selecciono una opcion que no es correcta o esta mal escrita , favor de reintentar")
            #este es el cartel que se imprime cuando el usuario se equivoca

file.close()
