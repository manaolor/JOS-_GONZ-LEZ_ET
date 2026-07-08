planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}
inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}
def menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================""")
def leer_opcion():
    try:
        opcion = int(input("Elija una opción: "))
        return opcion
    except ValueError:
        print("ERROR: Ingrese una opcion del 1 al 6.\n")

def buscar_codigo(codigo):
    if codigo in planes:
        return True
    else:
        return False
    
def buscar_precio(codigo, nuevo_precio):
    if codigo in inscripciones:
        inscripciones[codigo][0] = nuevo_precio
        print(f"El precio del plan {planes[codigo][0]} ha sido actualizado a {nuevo_precio}.")
    else:
        print("ERROR: El código del plan no existe.")

def cupos_tipo(tipo):
    for p in inscripciones:
        if planes[p][1] == tipo:
            print(f"{planes[p][0]}: {inscripciones[p][1]} cupos disponibles")
        else:
            print("Este plan no existe.")
            break
def busqueda_precio(p_minimo, p_maximo):
    for p in inscripciones:
        if p_minimo <= inscripciones[p][0] <= p_maximo:
            print(f"{planes[p][0]}: {inscripciones[p][0]}")

while True:
    menu()
    opcion = leer_opcion()
    if opcion == 1:
        print("Ingrese un tipo de plan para ver sus cupos: ")
        tipo = input("Ingrese tipo de plan (mensual, trimestral, anual): ").lower()
        cupos_tipo(tipo)
    
    elif opcion == 2:
        print("Ingrese un rango de precio para encontrar un plan:")
        p_minimo = int(input("Ingrese precio mínimo: "))
        p_maximo = int(input("Ingrese precio máximo: "))
        busqueda_precio(p_minimo, p_maximo)

    elif opcion == 3:
        print("Ingrese plan al que se desea cambiar el precio: ")
    elif opcion == 4:
        print("Ingrese los datos del plan para agregarlo:")

    elif opcion == 5:
        print("Ingrese el plan que desea eliminar: ")

    elif opcion == 6:
        print("Programa finalizado.")
        break
    else:
        print("ERROR: Ingrese una de las opciones disponibles.")