import re #Para poder verificar la estructura de la fecha de nacimiento y otras propiedades de cadena, expresiones regulares

#Funciones

def menu(): ##Menu de navegacion
    print("\nMenu")
    print("1) Registrar dueños y mascotas")
    print("2) Ver datos registrados")
    print("3) Veterinarios, precio y horarios")
    print("4) Confirmar/Cancelar y salir\n")
    eleccion = int(input("Ingrese su eleccion: "))
    while(eleccion < 1 or eleccion > 4): #Opcion entre 1 a 4
        eleccion = int(input("\nIngrese una opcion Válida"))
    return eleccion

def registrar_d(): ##Registra el dueño en el Diccionario
    nombre = str(input("\nIngrese su nombre: "))
    telefono = int(input("Ingrese su telefono: "))
    fnacimiento = input("Ingrese su fecha de nacimiento DD/MM/AAAA: ")
    
    while(True):   ##Comprueba la estructura fnacimiento, para que sea DD/MM/AAAA, no tiene en cuenta fechas validas
        if re.fullmatch(r"\d{2}/\d{2}/\d{4}", fnacimiento):
            break
        else:
            print("Formato incorrecto")
        fnacimiento = input("Ingrese su fecha de nacimiento DD/MM/AAAA: ")
    
    return {"nombre": nombre, "telefono": telefono, "nacimiento": fnacimiento}

def registrar_m(mascotas=None): ##Registra las Mascotas en un diccionario anidado dentro de Dueño
    if (mascotas == None): ##Si Mascotas no tiene ningun elemento
        mascotas = [] ##Crea la lista mascotas
        
    nombre = str(input("\nIngrese el nombre de su mascota: "))
    especie = str(input("Ingrese que animal es su mascota: "))
    raza = str(input("Ingrese la raza de su mascota: "))
    
    mascotas.append({ ##Agrega manualmente estos datos como primer elemento de la lista
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
    })
    
    print("\n¿Desea registrar otra mascota? 1) Sí / 2) No")    
    mas_mascotas = int(input())
    while(mas_mascotas < 1 or mas_mascotas > 2):
        mas_mascotas = int(input("Ingrese 1 o 2: "))
        
    if (mas_mascotas == 1): 
        registrar_m(mascotas) ##Se llama a si misma, recursiva, ya registro los datos anteriores, ahora agregara otros datos del mismo tipo nuevamente hasta que el usuario decida parar
        
    return mascotas #retorna la lista de mascotas, guardando la lista en el diccionario anidado

def registro():
    datos = { ##estructura del diccionario de dueño y mascotas
        "dueño": {
            **registrar_d(),
            "mascotas": registrar_m() ##anidada, llama a la funcion para que se pueda ingresar los datos a la lista, la lista en si como elemento para el diccionario
        }
    }
    return datos
    
def mostrar_d(datos):
    print("\nSu nombre es: ",datos["dueño"]["nombre"])
    print("Su telefono es el numero: ",datos["dueño"]["telefono"])
    print("Su fecha de nacimiento es: ", datos["dueño"]["nacimiento"])
    print("\nUsted a registrado a sus siguientes mascotas: ")
    
    for i in range(len(datos["dueño"]["mascotas"])): ##este for recorre las mascotas registradas
        print(datos["dueño"]["mascotas"][i]["nombre"],"un/a", datos["dueño"]["mascotas"][i]["especie"] ,"de raza:", datos["dueño"]["mascotas"][i]["raza"])
        
def Vet_Diccionario(): ##Diccionario de veterinarios, para sus datos
    veterinarios = {
        1:{
            "Nombre": "Leo",
            "Precio": 12000,
            "Turnos": {
                "Lunes":["8:00 a 12:00","16:00 a 20:00"],
                "Martes":["8:00 a 12:00","16:00 a 20:00"],
                "Viernes":["8:00 a 12:00","16:00 a 20:00"],
                "Sabado":["10:00 a 12:00","16:30 a 18:30"]
            }
            },
        2: {
            "Nombre": "Christian",
            "Precio": 15000,
            "Turnos": {
                "Lunes":["7:30 a 12:00","15:30 a 21:00"],
                "Martes":["7:30 a 12:00","15:30 a 21:00"],
                "Miercoles":["7:30 a 12:00","15:30 a 21:00"],
                "Jueves":["7:30 a 12:00","15:30 a 21:00"],
                "Viernes":["7:30 a 12:00","15:30 a 21:00"]
            }
            },
        3:{
            "Nombre": "Laura",
            "Precio": 10000,
            "Turnos": {
                "Lunes":["6:30 a 10:00","15:30 a 20:00"],
                "Miercoles":["8:00 a 10:00","17:00 a 19:00"],
                "Viernes":["8:00 a 10:00","17:00 a 19:00"],
                "Domingo":["15:00 a 17:00"]
            }
        }
    }
    return veterinarios

def mostrar_datos_vet(veterinario): ##Funcion aparte para mostrar datos de los veterinarios ordenadamente, recibiendo el veterinario para ver mas a fondo
    print(veterinario["Nombre"],"cobra",veterinario["Precio"],"por consulta.\n")
    print("Horarios: ")
    
    for dia, horarios in veterinario["Turnos"].items(): ##Examina el diccionario, tanto sus keys, como el contenido
        print(dia, "-", ", ".join(horarios)) ##Ordena la lista, separando el dia(key) con un "-" del contenido uniendo los datos de la lista para formar una cadena

def turnos(veterinarios):
    while True:
        for i in veterinarios: ##Solo para evitar usar mas lineas, por veterinario
            print(i, ") Veterinario:", veterinarios[i]["Nombre"])

        eleccion_t = int(input("\nSelecciona un veterinario para ver sus datos: "))

        if eleccion_t not in veterinarios:
            print("Opción inválida.")
            continue
        
        mostrar_datos_vet(veterinarios[eleccion_t]) ##Funcion auxiliar, para otro proposito
        
        print("\n¿Elegir este veterinario? 1) SI / 2) NO")
        confirmacion = int(input())
        while(confirmacion < 1 or confirmacion > 2):
            confirmacion = int(input("Ingrese 1 o 2: "))

        if confirmacion == 1:
            return eleccion_t

#Main

def main():
    opcion = menu()
    registrado = False ##Bandera de la opcion 1
    completado = False ##Bandera de todas las opciones realizadas
    
    while(opcion != 4):
        
        if(opcion == 1):
            datos = registro()
            registrado = True
            
        elif(opcion == 2):
            if(registrado):
                mostrar_d(datos)
            else:
                print("Completa el registro para ver tus datos ingresados")        
        elif(opcion == 3):
            if(registrado):
                veterinarios = Vet_Diccionario()
                vet_elegido = turnos(veterinarios)
                completado = True
            else:
                print("Completa el registro para ver tus datos ingresados")
        else:
            print("opcion ivalida")
        opcion = menu()
        
        if(opcion == 4 and completado): ##Si decide salir, haciendo todas las opciones, sale normalmente
            break
        elif(opcion == 4 and registrado): ##Si decide salir, realizando la opcion 1, se preguntara en caso de error, cancelar o seguir
            salir = int(input("Seguro que quieres cancelar? 1) SI / 2) NO"))
            while(salir < 1 or salir > 2):
                salir = int(input("Ingresa 1 o 2: "))
            if(salir == 2):
                opcion = menu()
            else:
                break
            
    if(completado):        
        print(veterinarios[vet_elegido]["Nombre"],"lo atendera!\n")

main()