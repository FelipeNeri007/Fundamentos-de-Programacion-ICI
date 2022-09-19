#Eliminar articulo de manera logica o fisica de acuerdo a su ID.

import inventario as inv

def eliminar_articulo(idt:list,nom:list,prc:list,ext:list)->None

    inv.inventario(idt,nom,prc,ext,30)

    while True:
        if len (idt)==0:
            print("Inventario Vacio")
            break

        i=int(input("Ingrese el ID del producto a eliminar(intro

        if i==0:
            break
        elif i not in idt:
            print("El ID no se encuentra en el inventario:")
        else:
            pos=idt.index(i)
            del idt[pos]
            del nom[pos]
            del prc[pos]
            del ext[pos]
    
    if len (idt) l==0:
        print("Inventario actualizado")
        inv.inventario(idt,nom,prc,ext,30)
