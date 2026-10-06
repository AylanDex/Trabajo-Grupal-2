
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
    fecha=input("Ingrese fecha: ")
    motivo=input("Ingrese motivo de consulta: ")
    diagnostico=input("Ingrese diagnóstico: ")
    

    consulta=[fecha, motivo, diagnostico]
    registro=[dueño, mascota, consulta]
    registros.append(registro)

    print("\nMascota registrada correctamente.")


respuesta="si"
while respuesta == "si":
    registrar_mascota()
    respuesta=input("\n¿Desea registrar otra mascota? ").lower()

print("\n--- REGISTROS ---")
print(registros)