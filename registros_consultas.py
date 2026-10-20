def registro_consultas(): # una funcion para guardar cada datos de la consulta
    print("\n-----Registro de nueva consulta-----")
    fecha = input("Ingrese fecha de la consulta:")
    motivo = input("¿Cual es el motivo de su consulta:")   
    diagnostico = input("Ingrese el diagnostico:") 
    medicamentos = input("Ingrese los medicamentos indicados:") 
    return {
        "fecha":fecha,
        "motivo":motivo,
        "diagnostico":diagnostico,
        "medicamentos": medicamentos
    } 
# menu
def main():
    opcion = menu()
    registrado = False ##Bandera de la opcion 1
    completado = False ##Bandera de todas las opciones realizadas
    
    while(opcion != 5): # lo puse que salga en 5 por que agregue la funcion registros_consulta
        
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
        elif(opcion == 4): #agregue un elif mas 
            if (registrado):
                registro_consultas()
            else:
                print("Completa el registro (opcion 1) antes de cargar una consulta")       
        else:
            print("opcion ivalida")
        opcion = menu()
        
        if(opcion == 5 and completado): ##Si decide salir, haciendo todas las opciones, sale normalmente
            break
        elif(opcion == 5 and registrado): ##Si decide salir, realizando la opcion 1, se preguntara en caso de error, cancelar o seguir
            salir = int(input("Seguro que quieres cancelar? 1) SI / 2) NO"))
            while(salir < 1 or salir > 2):
                salir = int(input("Ingresa 1 o 2: "))
            if(salir == 2):
                opcion = menu()
            else:
                break
