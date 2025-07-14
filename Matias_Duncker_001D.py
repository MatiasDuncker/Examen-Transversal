productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def validacion_string(Mensaje):
    while True:
        string = input(Mensaje).lower
        if len(string)==0:
            print("Error debe ingresar un texto")
            continue
        else:
            return 
        
def Validacion_Entero(Mensaje):
    while True:
        try:
            entero=int(input(Mensaje))
            return(entero)
        except ValueError:
            print("Error por favor ingrese un numero entero mayor a 0")

def Stock_Marca(Marca):
    modelos = []
    numero = 0
    marca=validacion_string("Ingrese la marca que desea consultar")
    print(marca)
    for i in productos:
        if marca==productos[i][0] or marca.upper()== productos or marca.capitalize()==productos or marca.lower== productos:
            modelos.append(i)
    print(modelos)
    for i in modelos:
        if modelos[i] in stock:
            numero+=stock[modelos[i]][i]
        else:
            continue
    print(f"El stock es {numero}")
      




while True:
    print("***Menu Principal***")
    print("1 - Stock Marca")
    print("2 - Busqueda por precio")
    print("3 - Actualizar precio")
    print("4 - Salir")

    opcion = Validacion_Entero("Por favor ingrece una opcion")

    if opcion == 1:
        Stock_Marca("Ingrese la marca de desea consultar")

   
    
