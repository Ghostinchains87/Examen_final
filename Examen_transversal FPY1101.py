from os import system
import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = {}

def asignar_sueldos_aleatorios(trabajadores):
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("\nSueldos aleatorios asignados:")
    for trabajador, sueldo in sueldos.items():
        print(f"{trabajador}: {sueldo}")
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {"Menores a $800000": [], "Entre $800000 y $2000000": [], "Superiores a $2000000": []}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["Menores a $800000"].append((trabajador, sueldo))
        elif sueldo < 2000000:
            clasificacion["Entre $800000 y $2000000"].append((trabajador, sueldo))
        else:
            clasificacion["Superiores a $2000000"].append((trabajador, sueldo))

    print("\nClasificación de sueldos:")
    for categoria, empleados in clasificacion.items():
        print(f"{categoria} - Total: {len(empleados)}")
        for trabajador, sueldo in empleados:
            print(f"{trabajador}: {sueldo}")
        print()

    print(f"Total sueldos: {sum(sueldos.values())}")

def ver_estadisticas(sueldos):
    sueldo_mas_alto = max(sueldos.values())
    print(f"\nSueldo más alto: {sueldo_mas_alto}")

    sueldo_mas_bajo = min(sueldos.values())
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")

    promedio_sueldos = round(sum(sueldos.values()) / len(sueldos), 2)
    print(f"Promedio de sueldos: {promedio_sueldos}")

    producto_sueldos = 1
    for sueldo in sueldos.values():
        producto_sueldos *= sueldo
    media_geometrica = round(producto_sueldos ** (1.0 / len(sueldos)), 2)
    print(f"Media geométrica: {media_geometrica}")

def reporte_sueldos(sueldos):
    with open('sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=",")
        escritor_csv.writerow(['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        
        print("\nNombre empleado  \tSueldo base  \tDescuento salud  \tDescuento AFP \tSueldo liquido")        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = round(sueldo - descuento_salud - descuento_afp)
                        
            escritor_csv.writerow([trabajador, round(sueldo, 2), descuento_salud, descuento_afp, sueldo_liquido])
        
            print(f"{[trabajador]}   \t{[sueldo]} \t{[descuento_salud]}  \t\t{[descuento_afp]} \t{[sueldo_liquido]}")

def menu():
    salir = False
    sueldos = {}

    while not salir:
        print("Menú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            sueldos = asignar_sueldos_aleatorios(trabajadores)    
        elif opcion == "2":
            if sueldos:  
                clasificar_sueldos(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")    
        elif opcion == "3":
            if sueldos: 
                ver_estadisticas(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")        
        elif opcion == "4":
            if sueldos:
                reporte_sueldos(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == "5":
            salir = True
            print("\nSaliendo del programa...")
            print("Desarrollado por Bruno Miranda")
            print("Rut 16.476.824-4\n")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")
            
        input()

menu()