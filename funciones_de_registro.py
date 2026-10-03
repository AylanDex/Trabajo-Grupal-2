veterinarios = {
    "Enrique Salazar":"viernes 16hs-20hs, lunes 14hs-17hs",    #----> este diccionario en realidad tendria que ir en main, este es solo para testear
    "Monica Soria":"martes 14hs-17hs, miercoles 19hs-22hs"
}


def turnos():
    for i, (nombre, horario) in enumerate(veterinarios.items(),1):
        print("-"*80)
        print(i, "|", nombre +"|", horario +"|")
        print("-"*80)    
    
    print("(1)Volver \t(2)Añadir entrada")
    m = int(input("\n:"))
    
    if m == 2:
        print("\n para añadir una entrada siga el siguiente orden: <veterinario> : <dia, hs>")
        entrada = input(":")
        pna, hs = entrada.split(":", 1)
        tem = {pna.strip(): hs.strip()}
        
        veterinarios.update(tem)
        print(veterinarios)
    elif m == 1:
        print("volviendo al menu...", "\n", "="*150)
    else:
        m = int(input(":"))




turnos()