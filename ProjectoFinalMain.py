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
        User = os.getlogin()
        # Guarda el nombre del usuario para usarlo en la lista del directorio
        Path = "C:\\Users\\{}\\ProyectoFinalFundamentos\\DataBaseFinalProject.csv".format(User)
        # Guarda el directorio de donde esta el archivo csv
        # Si el sistema operativo es windows
        with open(Path, 'r') as file:
            # Se abre el archivo de la base de datos de manera que podamos leer el contenido y poder escribir en el
            Reader = csv.reader(file, delimiter=',')
            # Se guardan los datos del archivo en una variable llamada Reader
            ProductListCSV = list(Reader)
            # Y se hace una lista con el contenido
else:
        # Si el sistema operativo no es windows
        with open("DataBaseFinalProject.csv", 'r+') as file:
            # Se abre el archivo de la base de datos de manera que podamos leer el contenido y poder escribir en el
            Reader = csv.reader(file, delimiter=',')
            # Se guardan los datos del archivo en una variable llamada Reader
            ProductListCSV = list(Reader)
            # Y se hace una lista con el contenido
file.close()
# Se cierra la base de datos

no_stock = "| No hay Stock en esa Talla"
# Declaramos que  no hay stock para no tener que esribirlo muchas veces
bar = "|--------------------------------------------------------|"
# Una bara para para que se vea bien y separa secciones del menu
ReturnPrint = "| R - Regresar "
# Se define el boton de regresar
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
o = 0
# Se inicia un contador para agregar inventario
t = 0
# Se inicia un contador para mostrar que ya se compro un producto
Shopping_Cart_List=[]
# Esta es la lista del carrito que tiene el usuario por session
print(bar)
# Se imprime la barra para poder separar el contenido y que se vea mejor
NoteShopping_Cart_List=[]
# Se inicia una lista para imprimir nota
nombre = input("| Porporcione el nombre del empleado : ")
# aqui pedimos el nombre del usuario
print("| \n| Hola!", nombre, "que gusto verte por aqui, bienvenido a: \n| Tecmi clothes","listo para otro dia de trabajo?")
# mensaje de bienvenida
print("| \n| Estos son los productos que tenemos disponibles:\n| Hoodies , Camisas , Jeans , Calcetines y Pants")
# ponemos una lista de los productos que hay en stock
print("| \n| A continuacion te mostraremos el catalogo\n| Para que selecciones tus productos !")
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
            print("|{:^4}|{:^12}|{:^17}|{:^5}|{:^6}|{:^7}|".format("Cant","Prod","Color","Talla","Precio","Total"))
            # Se impirme el inico de la tabla
            for i in range(LengthShopping):
                # Se inicia un ciclo del tamaño de la tabla
                Cant = s[i][0]
                # Se guarda la cantidad del producto en la lista de carrito de compras
                Prod = s[i][1]
                # Se guarda el nombre del porducto que esta en el carrrito de compras
                Car1 = s[i][2]
                # Se guarda la caracteristica 1 del producto en el carrito de compras
                Car2 = s[i][3]
                # Se guarda la caracteristica 2 del producto en el carrito de compras
                Precio = s[i][4]
                # Se guarda el precio de la cantidad de producto
                Total = s[0][5]
                # Se guarda el precio total de todo el carrito de compras
                print("|","{:^3}|{:^12}|{:^17}|{:^5}|{:^6}|".format(Cant,Prod,Car1,Car2,Precio), end="")
                # Se impirme lo que hay en  el carrtio de compras mediante una lista que tiene un contador para mostar cada producto
                if i == 1:
                        print("{:^7}|".format(Total))
                else:
                        LenTotal=len(Total)
                        print("{:^7}|".format(" "*LenTotal))
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
        # Si el producto es 1/ hoddies
        h = 1
        # El contador es 1
    elif m == "2":
        # Si el producto es 2 / camisetas
        h = 4
        # El contador es 4
    elif m == "3":
        # Si el producto es 3 / Jeans
        h = 7
        # El contador es 7
    elif m == "4":
        # Si el producto es 4 / calcetnies
        h = 10
        # El contador es 10
    elif m == "5":
        # Si el producto es 5 / Pants
        h = 13
        # El contador es 13
    ClearTer()
    # Se limipa la terminal
    while True:
        # Se inica un ciclo para poder repetir el menu sin tener que escribirlo muchas veces
        try:
            #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            print(bar), 
            #imprime otra barra
            print("| Elige que Color quieres: ")
            #es el titulo del menu para empezar a escoger el color del producto que selecciono el usuario
            for i in range(3):
                    # pro i en el rango de 3
                i+=1
                # a i se le suma 1
                print("|",i,"-",ProductListCSV[h][1])
                # Se imprime el color de la lista de productos de acuerdo con el indice e la i y h
                h+=1
                # Se le suma 1 a h
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
            print("Caracter Invalido")
            #este es el cartel que se imprime cuando el usuario se equivoca


def Size_Select(m,h,o):
    # Se define la opcion de hoodies verde para que el usuario seleccione la talla
    i = int(m)
    # La variable i se agarra del valor de el producto elegido
    k = int(h)
    # Y la variable k es el valor del color elegido
    if i == 1:
        # Si i es igual a 1 / hoddies
        if k == 1:
        # Y k es igual a 1 /color
           v = 1
           # El contador es 1
        elif k == 2:
        # Si k es igual a 2 / color
           v = 2
           # El contador es 2
        elif k == 3:
        # Si K es igual a 3 / color
           v = 3
           # El contador es 3
    elif i == 2:
        # Si i es igual a 2 / camisetas
        if k == 1:
        # Y K es igual a 1
           v = 4
           # El contador es 4
        elif k == 2:
        # Si k es igual a 2 / color
           v = 5
           # El contador es 5
        elif k == 3:
        # Si k es iguala 3 / color
           v = 6
           # El contador es 6
    elif i == 3:
        # Si i es igual a 3 / Jeans
        if k == 1:
        # Y k es igual a 1
           v = 7
           # el contador es 7
        elif k == 2:
        # Si K es igual a 2
           v = 8
           # El contador es 8
        elif k == 3:
        # Si K es igual a 3
           v = 9
           # El contador es 9
    if i == 4:
        # Si i es igual a 4 / calcetines
        if k == 1:
        # Si k es igual a 1
           v = 10
           # El contador es 10
        elif k == 2:
        # Si k es igual a 2
           v = 11
           # el contador es 11 
        elif k == 3:
        # Si k es igual a 3
           v = 12
           # El contador es 12
    if i == 5:
        # Si i es igual a 5
        if k == 1:
        # y k es igual a 1
           v = 13
           # El contador es 13
        elif k == 2:
        # Si k es igual a 2
           v = 14
           # El contador es 15
        elif k == 3:
        # Si k es 3
           v = 15
           # El contador es 15
    ClearTer()
    # Se limipa la pantalla
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
        if o == 1 and TallaV == "S" and ProductListCSV[v][3] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
            print(bar)
            # Se impirme una barra para separar contenido
            return TallaV
            # Declara la talla como no
        elif o == 1 and TallaV == "M" and ProductListCSV[v][3] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
            print(bar)
            # Se impirme una barra para separar contenido
            return TallaV
            # Declara la talla como no
        elif o == 1 and TallaV == "L" and ProductListCSV[v][3] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
            print(bar)
            # Se impirme una barra para separar contenido
            return TallaV
            # Declara la talla como no
        if TallaV == "S" and ProductListCSV[v][2] > 0:
            # Si la talla es S y hay mas inventario que 0
            print("| Tenemos:", ProductListCSV[v][2], "En Talla S")
            #con el print que esta arriba de este comentario notifica al usuario cuantos productos tenemos disponibles con las caracteristicas del producto que escogio anteriormente
            print(bar)
            #se imprime una barra
            time.sleep(2)
            # Le da tiempo al usuario de leer el contenido
        elif o == 0 and TallaV == "S" and ProductListCSV[v][2] == 0:
        # Si la talla es S y no hay inventario en talla S en el color
            print(no_stock)
            #Se impirme que no hay inventario
            print(bar)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa
            TallaV = "no"
            # Declara la talla como no

        if TallaV == "M" and ProductListCSV[v][3] > 0:
            # Si la talla es M y el inventario es mayor de 0
            print("| Tenemos:", ProductListCSV[v][3], "En Talla M")
            # se le mostrara un mensaje que indique cuantas existencias del producto tenemos excatamente en la talla que eligio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa
            #
        elif o == 0 and TallaV == "M" and ProductListCSV[v][3] == 0:
            # S la talla es M y no hay inventario en esa talla
            print(no_stock)
            # se imprimira un texto que indique al usuario que no hay existencias disponibles en esa talla
            print(bar)
            # Se impirme una barra para separar contenido
            TallaV = "no"
            # Declara la talla como no

        if TallaV == "L" and ProductListCSV[v][4] > 0:
            # Si la talla es L y en el inventario hay mas de 0
            print("| Tenemos:", ProductListCSV[v][4], "en Talla L")
            #se le notificara al usario la cantidad que hoodies que tenemos disponibles en la talla que el escogio
            print(bar)
            #se imprime una barra
            time.sleep(2)
            #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa

        elif o == 0 and  TallaV == "L" and ProductListCSV[v][4] == 0:
            # Si la talla es L y no hay inventario
            print(no_stock)
            # Se le informa al usuario que no hay existencias
            print(bar)
            #se le avisara al usuario que no hay existencias disponibles
            TallaV = "no"
            # Declara la talla como no
        if TallaV in size_options[0] or TallaV == "no":
        # Si la talla elegida esta en las opcinoes
                return TallaV
            # Regresa el valor de Talla para poder usarse y pasar al siguiente menu
        else:
        # Si no esta en las opciones
            print("| Ese no es un Producto\n| (Verifica si el nombre esta Bien escrito)")
            # Se le informa al usuario que no existe
            time.sleep(2)
            # Y se le da tiempo de leer

def shopping_cart(n,j,u,w):
    # Aqui se define un a funciion para el carrito de compras
    c = int(w)
    # El valor del numero que color que eligio el usuario es guardado como c para mas facilidad e uso
    TempShopping_Cart_List=[]
    while True:
        # Se empieza el ciclo para que el menu sigua aunque este mal la respuesta
        try :
        #esto se pone en caso de que el usuario se equivoque al teclear algo , el programa le de la oportunidad de seleccionar de nuevo regresandolo a la parte donde se quedo
            if u == "no":
                # Si la talla es no
                break
                # Rompe el ciclo
            elif u == "S":
                    # Si la talla es S
                    v = 2
                    # el contador es 2
            elif u == "M":
                    # Si la talla es M
                    v = 3
                    # El contador es 3
            elif u == "L":
                    # Si la talla es l
                    v = 4
                    # El contador es 4

            if n == "1":
                # Si el usuario eligio Hoodies
                print("| Las hoodies cuestan $600")
                # Se le informa cuanto cuestan las Hoodies
                ProductPrice = 600
                # Se asigna el precio al producto para mostrarlo al final
                ProductName = "Hoodies"
                # Se le asigna El nombre de producto para mostrarlo
                i = 1
                # el contador i se le asigna 1
                if c == 1:
                # Si C / color es igual a 1
                    h = 1
                    # al contador se le asigna 1
                elif c == 2:
                # Si c / color es igual a 2
                    h = 2
                    # Se le asigna 2 al contador
                elif c == 3:
                # Si c / color es igual a 3
                    h = 3
                    # Se le asigna 3 al contador
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
                if c == 1:
                # Si el color es 1
                    h = 4
                    # Se le asinga 4 a la h
                elif c == 2:
                # Si el color es 2
                    h = 5
                    # Se le asigna 5 a h
                elif c == 3:
                # Si el color es 3
                    h = 6
                    # Se le asigna 5 a h
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
                if c == 1:
                # Si el color fue 1
                    h = 7
                    # Se le asigna a h 7
                elif c == 2:
                # Si el color fue 2
                    h = 8
                    # Se le asinga a h 8
                elif c == 3:
                # Si el color fue 3
                    h = 9
                    # Se le asina a h 9
            elif n == "4":
                # Si el usuario eligo calcetines
                print("| Los Calcetines cuestan $40")
                # Se le infroma al usuario el costo de los calcetines
                ProductPrice = 40
                # Se asigna el precio al producto
                ProductName = "Calcetines"
                # y se asigna el producto para mostarlo en el carrito de compras
                i = 4
                # Sirve como indice en la lista de productos
                if c == 1:
                # Si el color fue 1
                    h = 10
                    # Se le asinga a h 10
                elif c == 2:
                # Si el color fue 2
                    h = 11
                    # Se le asinga a h 11
                elif c == 3:
                # Si el color es 3
                    h = 12
                    # Se le asinga a h 12
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
                if c == 1:
                # Si el color es 1
                    h = 13
                    # Se le asigna a h 13
                elif c == 2:
                # Si el color es 2
                    h = 14
                    # Se le asinga a h 14
                elif c == 3:
                # Si el color es 3
                    h = 15
                    # Se le asinga a h 15

        except ValueError :
        #con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo#con esto se detecta el error que tuvo el usuario para asi poder regresarlo y que lo pueda intentar de nuevo
            print("Caracter Invalido")
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
                ProductListCSV[h][v]-=Shopping_Cart_Amount
                # Se le resta la cantidad de articulos elegidos a el inventario
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
                    # Se agrega el carrito temporal al carrito de compras de la nota
                    Shopping_Cart_List.append(TempShopping_Cart_List)
                    # Se le agrega a el shopping cart principal la lista de los productos mas el precio total del shopping cart
                elif j > 0:
                    # Si j es mayor que 0
                    TotalShoppingCart = int(Shopping_Cart_List[0][-1])
                    # Se agara el valor del precio total de todo el carrito de compras
                    TotalShoppingCart = TotalShoppingCart + TotalProductPrice
                    # Se suma el valor total de Carrito de compras a el valor total de los productos elegidos ahorita
                    TotalShoppingCartSTR = str(TotalShoppingCart)
                    # Combierte el valor de el shopping cart a string para poder mostrarlo mas facil
                    NoteShoppingTotal = int(NoteShopping_Cart_List[0][-1])
                    # Combierte en integer el ultimo valor de la lista 1 que es el precio total
                    NoteShoppingTotal = NoteShoppingTotal + TotalProductPrice
                    # Suma el precio total del shopping cart mas el precio del producto comprado
                    NoteShoppingTotalSTR = str(NoteShoppingTotal)
                    # Se convierte el total del carrito de compras a stirng para poder impirmirlo en la nota
                    del NoteShopping_Cart_List[0][-1]
                    # borra el valor antiguo del shopping cart
                    NoteShopping_Cart_List[0].append(NoteShoppingTotalSTR)
                    # y agrega el nuevo valor como una string para mostrarlo mas facil
                    NoteShopping_Cart_List.append(TempShopping_Cart_List)
                    # Y lo agrega el valor a el carrito temporal
                    del Shopping_Cart_List[0][-1]
                    # Borra el valor total de las compras
                    Shopping_Cart_List[0].append(TotalShoppingCartSTR)
                    # Agregar el valor total nuevo que incluye el precio total de todas tus compras
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

def AddInv(p,w,s):
        c = int(w)
        if s == "S":
                    # Si la talla es S
              v = 2
                    # el contador es 2
        elif s == "M":
                    # Si la talla es M
                v = 3
                    # El contador es 3
        elif s == "L":
                    # Si la talla es l
                v = 4
                    # El contador es 4
        if p == "1":
                # Si el usuario eligio Hoodies
                print("| Las hoodies cuestan $600")
                # Se le informa cuanto cuestan las Hoodies
                ProductPrice = 600
                # Se asigna el precio al producto para mostrarlo al final
                ProductName = "Hoodies"
                # Se le asigna El nombre de producto para mostrarlo
                i = 1
                # el contador i se le asigna 1
                if c == 1:
                # Si C / color es igual a 1
                    h = 1
                    # al contador se le asigna 1
                elif c == 2:
                # Si c / color es igual a 2
                    h = 2
                    # Se le asigna 2 al contador
                elif c == 3:
                # Si c / color es igual a 3
                    h = 3
                    # Se le asigna 3 al contador
        elif p == "2":
                # Si el usuario eligio Camisas
                print("| Las camisas cuestan $350")
                # Se le informa cuanto cuestan las camisas
                ProductPrice = 350
                # Se asigna el precio indicado
                ProductName = "Camisetas"
                # Se asigna el Producto para mostarlo al final
                i = 2
                # Sirve como indice en la lista de productos
                if c == 1:
                # Si el color es 1
                    h = 4
                    # Se le asinga 4 a la h
                elif c == 2:
                # Si el color es 2
                    h = 5
                    # Se le asigna 5 a h
                elif c == 3:
                # Si el color es 3
                    h = 6
                    # Se le asigna 5 a h
        elif p == "3":
                # Si el usuario eligio Jeans
                print("| Los Jeans cuestan $360")
                # Se le informa cuanto es el costo de los Jeans
                ProductPrice = 360
                # Se le asigna un valor al costo
                ProductName = "Jeans"
                # Se le asigna el Producto para mostrarlo en el carrito
                i = 3
                # Sirve como indice en la lista de productos
                if c == 1:
                # Si el color fue 1
                    h = 7
                    # Se le asigna a h 7
                elif c == 2:
                # Si el color fue 2
                    h = 8
                    # Se le asinga a h 8
                elif c == 3:
                # Si el color fue 3
                    h = 9
                    # Se le asina a h 9
        elif p == "4":
                # Si el usuario eligo calcetines
                print("| Los Calcetines cuestan $40")
                # Se le infroma al usuario el costo de los calcetines
                ProductPrice = 40
                # Se asigna el precio al producto
                ProductName = "Clacetines"
                # y se asigna el producto para mostarlo en el carrito de compras
                i = 4
                # Sirve como indice en la lista de productos
                if c == 1:
                # Si el color fue 1
                    h = 10
                    # Se le asinga a h 10
                elif c == 2:
                # Si el color fue 2
                    h = 11
                    # Se le asinga a h 11
                elif c == 3:
                # Si el color es 3
                    h = 12
                    # Se le asinga a h 12
        elif p == "5":
                # Si el usuario eligio pants
                print("| Los Pants cuestan $400")
                # Se le informa al usuario el costo de los Pants
                ProductPrice = 400
                # Se les asigna un valor a los pantalones
                ProductName = "Pants"
                # Se asigna un producto para poder mostar el producto en el carrito de compras
                i = 5
                # Sirve como indice en la lista de productos
                if c == 1:
                # Si el color es 1
                    h = 13
                    # Se le asigna a h 13
                elif c == 2:
                # Si el color es 2
                    h = 14
                    # Se le asinga a h 14
                elif c == 3:
                # Si el color es 3
                    h = 15
                    # Se le asinga a h 15

                    #
        while True:
                try:
                    AddInv_Amount = int(input("| ¿Cuántos artículos quieres agregar al inventario? "))
                    #aqui se le pregunta al usuario cuantos productos va a agregar a su carrito de compras

                    if AddInv_Amount <= 0:
                    # Si el carrito de compras es menor o igual a 0
                            print("| No Puedes agregar 0 arcticulos.")
                            # se le notificara que no tiene ningun producto en el carrito
                            print(bar)
                            # Se imprime la barra para separar el menu
                    elif AddInv_Amount > 30:
                    # Si el carrito de compras es mas de 10
                            print("| Si agregas tantos articulos luego no se venderan , favor de seleccionar otra cantidad.")
                            #como tenemos un stock de 10 para todos los productos no se le permitira comprar mas 10 productos simultaneamente
                            print(bar)
                            # Se imprime la barra para separar el menu
                            time.sleep(2)
                #se le da al programa una instruccion de esperar 2 segundos para que aparezca la siguiente opcion del programa
                    else:
                        # Si no
                            ProductListCSV[h][v] += AddInv_Amount
                            # Se le agrega al produco la cantidad que el usuario pidio
                            break
                            # Se rompe el ciclo del programa para seguir comprando
                except ValueError:
                       print("| Caracter Invalido")
def Imprimir_Inv():
# Se define la funcion de imprimir inventario
    while True:
                # Se inicia un ciclo para repetir el menu si el usuario se equivoca
        try:
                # Se caputra cualquier error que se precente
                TotalInv = 0
                # El inventario empiza en 0
                h = 0
                # El contador empieza en 0
                print(bar)
                # Se impirme una barra para separar contenido
                print("| Inventario Total: ")
                # Se imprime el texto de inventario total
                for i in range(5):
                        # Este ciclo se va a repetir 5 veces porque tenemos 5 productos
                        for m in range(3):
                                # Este otro ciclo se repite 3 veces porque tenemos 3 colores cada uno con su propio inventario
                                h+=1
                                # Se agrega 1 al contador
                                s = 2
                                # Se empieza otro contador en 2
                                for u in range(3):
                                        # este otro ciclo se repite 3 veces porque tenemos 3 tallas diferentes y cada una tiene su inventario
                                        TotalInv += ProductListCSV[h][s]
                                        # Se agrega al total de inventario que indexa el producto y sus tallas
                                        s+=1
                                        # Se le agrega 1 al contador de s para moverse a la siguiente talla
                                m += 1
                                # Se le agrega 1 al otro contador para moverse al siguente paso
                        print("|",ProductListCSV[h][0],TotalInv)
                        # Se impirme el nombre del producto y se impirme el inventario total
                        TotalInv = 0
                        # Se reincia el inventario total
                        i+=1
                        # y se agrega 1 al contador
                InvRes = input("| R- Regresar ")
                # Se impirme el boton de regresar y una opcion al usuario para teclear
                if InvRes in imprNot_opt[0]:
                        # Si lo que puso el usuario esta en las opciones
                        return InvRes
                # Se rompe el ciclo y regresa el valor
                else:
                # Si no
                        print("| Esa no es una opcion Porfavor eliga R")
                        # Se impirme que esa no es una opcion
        except ValueError:
                # Si el usuario puso un caracter que no es una letra
                print("| Caracter invalido")
                # Le marca que es un caracter invalido

def MontoTotalVentas(j):
    # Este es el menu de Monto total de ventas
    s = 0
    while True:
        # Se inicia un ciclo para repetir el menu si el usuario se equivoco
            if j == 0:
                print("| Tu monto Total de ventas es:",s,"{:>15}".format("|"))
            elif j >= 1:
                print("| Este es el monto total de todas las ventas de Session:",Shopping_Cart_List[0][-1])
            # Se imprime monto total de ventas en la session
            MontoTotalOpcion=input(ReturnPrint)
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
            if MenuPrincipal == "1":
                # Si la opcion del menu es 1
                Size_select = 0
                product_select = Product_Type()
                # Se declara una enunciado para guardar el resultado de la texto que contiene el menu de los usuarios
                if product_select == "1":
                # Si la opcion del producto es igual a 1 que es hoodies
                    Color_selectRes = Color_select(product_select)
                    # Se ejecuta la texto del menu de color de hoodies y se guarda el resultado en una enunciado
                    if Color_selectRes == "1":
                        # Si la opcion del menu de colores es 1 (Verde)
                        Size_select = Size_Select(product_select,Color_selectRes,o)
                        # Se ejecuta el menu de seleccion de talla para el color verde y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "2":
                        # Si la opcion del menu de colores es 2 (Negro)
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        # Se ejecuta el menu de seleccion de talla para el color negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "3":
                        # la opcion de la seleccion de colores es 3 (Blanco)
                        Size_select = Size_Select(product_select, Color_selectRes,o)
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
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        # Se ejecuta el menu de seleccion de talla para el color Azul y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes ==  "2":
                        # Si la opcion del menu es igual a 2 se abrira el menu para empezar a personalizar tu pedido de camisetas de color negro
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        # Se ejecuta el menu de seleccion de talla para el color Negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "3" :
                        #si se selecciona la opcion 3 empezara a elegir camisetas de color blanco
                        Size_select = Size_Select(product_select, Color_selectRes,o)
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
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        #Se ejecuta el menu de seleccion de talla para el color negro y se guarda su resultado en una enunciado para poder usarse
                    elif Color_selectRes == "2":
                        #si la opcion seleccionada es igal a 2 quiere decir que el usuario esta eligiendo el color negro para sus calcetines
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        #se ejecuta el menu de seleecion de tallas para el color blanco para calcetines y se guarda el resultado
                    elif Color_selectRes == "3":
                        Size_select = Size_Select(product_select, Color_selectRes,o)
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
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                    # Se le pregunta que talla va a nececitar para los Jeans Azules
                    elif Color_selectRes == "2" :
                    # Si Eligio Jeans Negros
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        # Se le pregunta la Talla de los Jeans Negros
                    elif Color_selectRes == "3" :
                    # Si Eligio Jeans azul oscuro
                        Size_select = Size_Select(product_select, Color_selectRes,o)
                        # Se le pregunta la Talla de los Jeans azul oscuro
                    elif Color_selectRes == "R":
                        # Si eligio Regresar
                        ClearTer()
                        # Se limipa la pantalla
                        continue
                    # Y Se regersa al menu principal

                elif product_select == "5":
                        # Si eligio Pants
                        Color_selectRes = Color_select(product_select)
                        #Se le da la opcion de elegi que color va a querer en Pants
                        if Color_selectRes == "1":
                                # Si el color Es blanco y nergo
                                Size_select = Size_Select(product_select, Color_selectRes,o)
                                # Se le pide al usuario que seleccione una talla
                        elif Color_selectRes == "2":
                                # Si selecciono Negro
                                Size_select = Size_Select(product_select, Color_selectRes,o)
                                # Se le pide al usuario que eliga que Talla va a necesitar para Pants Negros
                        elif Color_selectRes == "3":
                                # Si eligo Pants Blancos
                                Size_select = Size_Select(product_select, Color_selectRes,o)
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
                        Imprimir_Nota_Res = Imprimir_Nota(j,NoteShopping_Cart_List)
                        # Se imprime la nota de todo el inventario
                        if Imprimir_Nota_Res == "R":
                                # Si la opcion en Imprimir nota es R
                                continue
                        # Se regresa al menu principal
                elif product_select == "R":
                        # Si el usuario eligio Regresar en la seleccion de productos
                        NoteShopping_Cart_List=[]
                        # Reinicia la nota de compra
                        j = 0
                        # Se reinicia el contador
                        break
                # Se regresa al menu principal
                if Size_Select == 0 or Size_Select == "R":
                        # Si la talla es igual a 0
                        continue
                        # Se regresa al menu de productos
                else:
                        Shopping_CartRes = shopping_cart(product_select , j, Size_select, Color_selectRes)
                        # Se ejecuta la texto de carrito de compras y se guarda su resultado en una enunciado para poder usarse
                        j+=1
                        # Se le agrega 1 al contador para que se vaya a la siguiente producto
                        t+=1
                        # Se agrega 1 al contador para mostrar que ya tenemos un producto en el carrito
                        time.sleep(5)
                        # Le da al usuario tiempo de ver el precio de los productos que eligieron
            elif MenuPrincipal == "2":
                # Si el usuario eligio en el menu 2
                   o+=1
                   product_select = Product_Type()
                   # Se ejecuta la funcion de producto para que eliga el producto que quiere
                   if product_select == "6":
                        Imprimir_Nota_Res = Imprimir_Nota(j,NoteShopping_Cart_List)
                        if Imprimir_Nota_Res == "R":
                            break
                   if product_select == "R":
                        # Si dentro del producto el usuario elige r
                           break
                        # Se regresa al menu principal
                   Color_selectRes = Color_select(product_select)
                   # Se ejecuta la funcion de elegir color con el resultado de el producto elegido
                   if Color_selectRes == "R":
                        # Si el usuario eligio R en color
                           break
                          # Se regresa al menu anterior
                   # Se le agrega 1 al contador de o
                   Size_select = Size_Select(product_select, Color_selectRes,o)
                   # Se ejecuta la funucion de seleccionar tamaño con el resultado de color producto y el contador o
                   if Size_select == "R":
                        # Si el ususuario eligio R en la talla
                           break
                        # Se regresa al menu anterior
                   AddInvRes = AddInv(product_select,Color_selectRes,Size_select)
                   # Se ejecuta la funcion de agregar inventario con las respuestas de producto color y talla
                   o = 0
                   # Se reinicia el contador de o
            elif MenuPrincipal == "3":
                    # Si el usuario eligio en el menu 3
                Imprimir_InvRes = Imprimir_Inv()
                # Se ejecuta la funcion de impirmir inventario
                if Imprimir_InvRes == "R":
                # Si en impirmir inventario selecciona R
                   break
                    # Se sale del menu de imprimir inventario

            elif MenuPrincipal == "4":
                # Si el usuario eligio Monto total de ventas en el menu principal
                Monto_Ventas_Total = MontoTotalVentas(t)
                # Se ejecuta el menu de Monto total de Ventas
                if Monto_Ventas_Total == "R":
                    # Si el usuario eligio regresar al menu principal en Monto de ventas
                        break
                    # Se regresa al menu principal

            elif MenuPrincipal == "Q" or "q":
            # Si la opcion del Menu Principal es Q
                if os.name == "nt":
                        # Si el sistema operativo es windows
                        with open(Path, 'w', newline='') as file:
                                # Se abre el archivo de la base de datos de manera que podamos escribir en el
                                Write = csv.writer(file)
                                # Se guarda la funcion de escribir en una variable para no escribirla completo
                                Write.writerows(ProductListCSV)
                                # Guarda la lista con inventario a el archivo
                else:
                # SI el sistema oprerativo no es windows
                        with open("DataBaseFinalProject.csv", 'w', newline='') as file:
                                # Se abre el archivo de la base de datos de manera que podamos escribir en el
                                Write = csv.writer(file)
                                # Se guarda la funcion de escribir en una variable para no escribirla completo
                                Write.writerows(ProductListCSV)
                                # Guarda la lista con inventario a el archivo
                file.close()
                # Y se cierra el archivo
                Quit_Menu()
                # Se ejectua la texto de salir del programa
