def main():
    while True:
        print("="*150,"\n VETERINARIA SANDOVAL"," "*50,"\n", "="*150, "\n//Menu") #
        r = ["registrar nueva mascota","mostrar registros","eliminar registros", "horarios de consulta", "apagar"] #---> Las opciones que puse son solo de relleno, mientras se valla avanzando agreguen o quiten las que necesiten
        for i,m in enumerate(r) :
            print(f"({i+1})",m)   
        
        eleccion = int(input("\n:"))    
        if eleccion == 5:
            print("apagando sistema")
            break
    
main()  