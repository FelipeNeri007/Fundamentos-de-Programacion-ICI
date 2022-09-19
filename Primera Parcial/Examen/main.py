#Consulta las existencias por ID y nombre

def consultar_existencias(idt:list,nom:list,ext:list)->None:

    print("Productos")
    titulo=["ID","Nombre del Producto"]
    print(f"{titulo[0]:^{30}}{titulo[1]:^{30}}")
    for i in range(len(idt)):
        print(f"{idt[i]:^{30}}{nom[i]:^{30}}")

        opcion=(int(input("Introduce el ID del Producto para conocer sus existencias:")))
        if opcion in idt:
            pos=idt.index(opcion)
            print(f"Hay{ext[pos]}unidades de existencia de {nom[pos]}")
        else:
            print("No hay concidencias")
