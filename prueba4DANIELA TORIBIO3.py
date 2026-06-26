#=================================
#==SISTEMA=DE=GESTION=DE=PELICULAS
#=================================

peliculas=[]

def mostrar_menu():
    print("\n========MENU=========")
    print("1.Agregar pelicula")
    print("2.Buscar pelicula")
    print("3.Eliminar pelicula")
    print("4.Actualizar disponibilidad")
    print("5.Mostrar peliculas") 
    print("6.Salir") 

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese una opcion del (1-6):")) 
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opcion invalida ingrese un numero del 1 al 6")
        except ValueError:
            print("Error: Debes ingresar un numero") 

def validar_titulo(titulo):
    if titulo.strip()=="":
        return False
    return True

def validar_duracion(duracion):
    try:
        duracion=int(duracion)
        if duracion >0:
            return True
        return False
    except ValueError:
        return False
    
def validar_calificacion(calificacion):
    try:
        calificacion=float(calificacion)
        if 0.0 <= calificacion <= 10.0:
            return True
        return False
    except ValueError:
        return False
    
def agregar_pelicula(lista):
    titulo=input("Ingrese el titulo de la pelicula:")
    duracion=input("Ingrese la duracion de la pelicula:")
    calificacion=input("Ingrese la calificacion de la pelicula:")
    
    if not validar_titulo(titulo):
        print("Error: el titulo no puede estar vacio")
        return
    
    if not validar_duracion(duracion):
        print("Error: la duracion debe ser mayor que 0")
        return
    
    if not validar_calificacion(calificacion):
        print("Error: la calificacion debe ser decimal entre 0.0 t 10.0 incluidos")
        return
    
    pelicula={
        "titulo":titulo.strip(),
        "duracion":int(duracion),
        "calificacion":float(calificacion),
        "disponible": False
    }

    lista.append(pelicula)
    print(f"Pelicula '{titulo}' registrado correctamente")

def buscar_pelicula(lista,titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"]==titulo:
            return i
    return -1

def eliminar_pelicula(lista):
    titulo = input("Ingresa el titulo de la pelicula que desea eliminar:")
    posicion= buscar_pelicula(lista,titulo)
    if posicion != -1:
        lista.pop(posicion)
        print(f"Pelicula '{titulo}' eliminada correctamente")
    else:
        print(f"Pelicula '{titulo}'no se encuentra registrada")

def actualizar_disponibilidad(lista):
    for i in range(len(lista)):
        if lista[i]["calificacion"]>=7.0:
            lista[i]["disponible"]= True
        else:
            lista[i]["disponible"]= False

def mostrar_peliculas(lista):
    actualizar_disponibilidad(lista)
    for i in range(len(lista)):
        if lista[i]["disponible"]== True:
            estado = "DISPONIBLE"
        else:
            estado =" NO RECOMENDADA"
        print(f"Titulo:{lista[i]['titulo']}")
        print(f"Duracion:{lista[i]['duracion']}")
        print(f"Calificacion:{lista[i]['calificacion']}")
        print(f"Estado:{estado}")
        print("*" * 45)

while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_pelicula(peliculas)
    elif opcion == 2:
        titulo = input("Ingrese el titulo a buscar:")
        posicion=buscar_pelicula(peliculas,titulo)
        if posicion != -1:
            if peliculas[posicion]["disponible"]== True:
                estado = "DISPONIBLE"
            else:
                estado = "NO DISPONIBLE"  
            print(f"Pelicula encontrada en la posicion {posicion}:")
            print(f"Titulo:{peliculas[posicion]['titulo']}")
            print(f"Duracion:{peliculas[posicion]['duracion']}")
            print(f"Calificacion:{peliculas[posicion]['calificacion']}") 
            print(f"Estado:{estado}")
    
    elif opcion == 3:
        eliminar_pelicula(peliculas)
    
    elif opcion == 4:
        actualizar_disponibilidad(peliculas)
        print("Estados actualizados correctamente")

    elif opcion == 5:
        mostrar_peliculas(peliculas)

    elif opcion == 6:
        print("Gracias por usar el sistema .Vuelva pronto")
        break
