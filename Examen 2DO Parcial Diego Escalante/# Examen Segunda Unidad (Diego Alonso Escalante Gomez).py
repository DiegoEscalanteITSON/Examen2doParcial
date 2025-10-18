# Examen Segunda Unidad
# Diego Alonso Escalante Gomez

def registrar_venta():
        nombre = input("Ingrese el nombre del juego: ")
        precio = float(input("Ingrese el precio del juego: "))

        with open("ventas.txt", "a") as archivo:    
            archivo.write(f"{nombre},{precio}\n")
        
        print(f"Venta registrada exitosamente: {nombre} - ${precio:.2f}")

def mostrar_ventas():
        print("\n--- Ventas Realizadas ---")
        try:
            with open("ventas.txt", "r") as archivo:
                ventas = archivo.readlines()
                
                if not ventas:
                    print("No hay ventas registradas.")
                else:
                    for venta in ventas:
                        nombre, precio = venta.strip().split(",")
                        precio_f = float(precio)
                        print(f"Juego: {nombre}, Precio: ${float(precio):.2f}")
        except FileNotFoundError:
            print("No hay ventas registradas.")

def mostrar_ventas_con_descuento():
        print("\n--- Ticket ---")
        try:
            with open("ventas.txt", "r") as archivo:
                ventas = archivo.readlines()

                if not ventas:
                    print("No hay ventas registradas.")
                    return
                else:
                    total = 0
                    for venta in ventas:
                        nombre, precio = venta.strip().split(",")
                        total += float(precio)

                    # Aplica el descuento si el total supera los 1000
                if total > 1000:
                    descuento = total * 0.10
                    total_con_descuento = total - descuento
                    print(f"Total antes del descuento: ${total:.2f}")
                    print(f"Descuento (10%): -${descuento:.2f}")
                    print(f"Total a pagar: ${total_con_descuento:.2f}")
                else:
                    print(f"Total de ventas: ${total:.2f}")
                    print("No aplica descuento (total menor o igual a $1000).")

        except FileNotFoundError:
             print("No hay ventas registradas.")


# --- Menú Principal ---
while True:
    print("\n--- Menu Principal ---")
    print("1. Registrar una Venta")
    print("2. Ventas Realizadas")
    print("3. Generar Ticket con Descuento")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == '1':
        registrar_venta()

    elif opcion == '2':
        mostrar_ventas()

    elif opcion == '3':
        mostrar_ventas_con_descuento()

    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")  
