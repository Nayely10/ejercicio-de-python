"""vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de
diferente articulos. El programa pedira :
la cantidad de frutas compradas, en un ciclo for
pedira el nombre de la fruta y el precio de la fruta que se ha vendido
El programa debe mostrar el preciofinal  del articulo apartir de los datos guardados en el dicionrario
Si la fruta no exixte nos dara error.tras  cada consulta el programa nos preguntara si queremos hacer otra consulta."""

productos ={}
cant =  int(input("ingrese la cantidad de frutas")) 

for x in range(1,cant+1):
    nombre = input("ingrese nombre de la fruta")
    precio = int(input("ingrese el precio de la fruta que  se ha vendido"))
    productos [nombre] = precio
    
print(productos)


for i in productos.keys():
    nombre = input("ingrese el nombre de la fruta")
    if nombre in productos:
        cantv = int(input("ingrese la cantidad de frutas compradas"))
        precioTotal = cantv*productos[nombre] 
        print(precioTotal)    
    else:
        print("Error")
    opcion = input("Desea continuar S/N")
    if opcion.lower == "S":
        cant =  int(input("ingrese la cantidad de frutas"))
    else:
        break


