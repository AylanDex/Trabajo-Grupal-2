pedidos = []

def tomar_pedido():
    print("--- TOMA DE PEDIDO ---")
    
    mesa = int(input("Ingrese número de mesa: "))
    while mesa <= 0:
        print("Mesa inválida.")
        mesa = int(input("Ingrese número de mesa: "))

    plato = input("Ingrese el nombre del plato: ")
    
    precio = float(input("Ingrese el precio: $"))
    while precio <= 0:
        print("El precio debe ser mayor a 0.")
        precio = float(input("Ingrese el precio: $"))

    item = [mesa, plato, precio]
    pedidos.append(item)
    print("Plato agregado correctamente.")


respuesta = "si"
while respuesta == "si":
    tomar_pedido()
    respuesta = input("\n¿Desea agregar otro pedido? (si/no): ").lower()

print("\n--- TODOS LOS PEDIDOS ---")
print(pedidos)
