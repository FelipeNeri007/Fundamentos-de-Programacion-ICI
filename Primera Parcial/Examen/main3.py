#Modificar un articulo y cualquiera de sus datos menos el ID.

import inventario as inv

def modificar_articulo(idt:list,nom:list,prc:list,ext:list)->None:
    inv.inventario(idt,nom,prc,ext,30)
    
    while True:
        i=int(input("Ingrese el ID del producto a modificar:"))

        if i not in idt:
            print("El ID no se encuentra en el inventario")
        else:
            break

    pos=idt.index(i)

    print("""
    ¿Que deseas modificar?

    1) Nombre
    2)Precio
    3)Existencias
    4)Salir
    """)

    while True:
        opcion=int(input("Ingrese una opcion a realizar:"))
        match opcion:
            case 1:
                nom[pos]=input("Ingrese el nuevo nombre del producto:")
            case 2:
                p=0
                while p<=0:
                    p=float(input("Ingrese el nuevo precio del producto:  $"))
                    if p<=0:
                        print("Ingrese un precio valido.")
                    prc[pos]=p
            case 3:
                e=0
                while e <=0:
                    e=int(input("Ingrese la nueva cantidad de productos disponibles:"))
                    if e <=0:
                        print("Ingrese una cantidad valida.")
                    ext[pos]=e
            case 4:
                break
            case _:
                print("Operacion Inexistente")
    
    inv.inventario(idt,nom,prc,ext,30)
