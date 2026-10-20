veterinarios = {
    "Enrique Salazar":"viernes 16hs-20hs, lunes 14hs-17hs",   
    "Monica Soria":"martes 14hs-17hs, miercoles 19hs-22hs"
}

registros=[]

def registrar_mascota():
    print("\n--- DATOS DEL DUEÑO ---")
    dni=int(input("Ingrese DNI del dueño: "))
    while dni <= 0:
        print("DNI inválido.")
        dni=int(input("Ingrese DNI del dueño: "))

    nombre_dueño=input("Ingrese nombre del dueño: ")
    telefono=input("Ingrese teléfono del dueño: ")

    dueño=[dni, nombre_dueño, telefono]

    print("\n--- DATOS DE LA MASCOTA ---")
    nombre_mascota=input("Ingrese nombre de la mascota: ")
    especie=input("Ingrese especie: ")
    raza=input("Ingrese raza: ")

    peso=float(input("Ingrese peso: "))
    while peso <= 0:
        print("El peso debe ser mayor que 0.")
        peso=float(input("Ingrese peso: "))

    mascota=[nombre_mascota, especie, raza, peso]

    print("\n--- DATOS DE LA CONSULTA ---")
    tabla_veterinarios()
    
    fecha=input("Ingrese fecha: ")
    motivo=input("Ingrese motivo de consulta: ")
    diagnostico=input("Ingrese diagnóstico: ")
    

    consulta=[fecha, motivo, diagnostico]
    registro=[dueño, mascota, consulta]
    registros.append(registro)

    print("\n*Mascota registrada correctamente.*")

def turnos():
    tabla_veterinarios()
    
    print("="*90,"\n"*2, "(1)Volver \t(2)Añadir entrada \t(3)Eliminar")
    m = int(input("\n:"))
    
    if m == 1:
        print("\nVolviendo al menu...")

    elif m == 2:
        print("\nPara añadir una entrada siga el siguiente orden: <apellidos nombres> <:> <dia, hs>")
        entrada = input(":")
        
        if ":" not in entrada:
            print("Registro invalido, escriba \":\" para que el registro sea valido ")
            entrada = input("\n")
        
        pna, hs = entrada.split(":", 1)    
        tem = {pna.strip(): hs.strip()}
        veterinarios.update(tem)
        
        tabla_veterinarios()
    
    elif m == 3:
        print("Escriba el numero del indice para eliminar la entrada que quiera")
        s = int(input(":"))
        
        if 1 <= s <= len(veterinarios):
            nombre = list(veterinarios)[s -1]
            veterinarios.pop(nombre)
            
        tabla_veterinarios()
        
    else:
        m = int(input(":"))

def tabla_registros():
    for i, registro in enumerate(registros):
        print("="*150,"\n","-"*150,f"\n{i+1}", registro,"\n","-"*150,"\n","="*150)
    
def tabla_veterinarios():
    for i, (nombre, horario) in enumerate(veterinarios.items(),1):
        print("="*90,"\n","-"*90, f"\n{i}", "||", nombre +" ||", horario +" ||","\n","-"*90)            

def main():
    while True:
        print("="*150,"\n VETERINARIA SANDOVAL"," "*50,"\n", "="*150, "\n// Menu") #
        r = ["mostrar registros", "horarios de consulta", "apagar"] 
        for i,m in enumerate(r) :
            print(f"({i+1})",m)   
        
        eleccion = int(input("\n:"))
        if eleccion == 1:
            tabla_registros()          
            
            if len(registros) == 0:
                print("\n*Actualmente no hay registros ingresados.*")
            print("\n"*2,"(1)volver\t(2)añadir registro")    
            
            n = int(input("\n:"))
            if n == 2:
                print("\n","="*150)
                registrar_mascota()

            elif n == 1:
                print("\nVolviendo al menu...")
            else:
                tabla_registros()
                print("(1)volver\t(2)añadir registro")
                n = int(input("\n:"))
                
        elif eleccion == 2:
            turnos()
        elif eleccion == 3:
            print("apagando sistema")
            break
                    
main()
