''' # Bloque de un programa comentado que usa una funcion que introduce el ancho y agarra datos de listas para simular una base de datos de calificaciones de una escuela

materias = ["Nombre", "Est Dat", "Prog Func", "Ingles"]    # Creamos una lista con los nombres de las materias
alumnos = ["Hugo Alberto", "Paco", "Luis", "Lupita"]      # Creamos una lista con los nombres de los alumnos
materia1 = [9,7,9,8]    # Creamos una lista con las calificaciones de la materia1
materia2 = [8,9,7,8]      # Creamos una lista con las calificaciones de la materia2
materia3 = [6,7,9,8]    # Creamos una lista con las calificaciones de la materia3

   
def calificaciones(ancho:int) -> int: # Creamos una funcion que pide un dato str y retorna un dato int
    print(f"{materias[0]:^{ancho}} {materias[1]:^{ancho}} {materias[2]:^{ancho}} {materias[3]:^{ancho}}") # Imprimimos "Nombre", "Est Dat", "Prog Func", "Ingles" de manera espaciada
    for i in range(len(alumnos)):   # Un ciclo For en un rango de la longitud de la variable alumnos
        print(f"{alumnos[i]:*<{ancho}} {materia1[i]:+^{ancho}} {materia2[i]:#>{ancho}} {materia3[i]:-^{ancho}}")    # Imprimimos de manera espaciada cada valor correspondiente a las listas
    return 0    # Todas las funciones tienen que retornar valores de caso contrario es una mala practica de programacion

if __name__ == "__main__":
    ancho = 15    # Asignamos un valor de la variable ancho
    calificaciones(ancho)   # Mandamos a llamar la funcion calificaciones con el parametro de la variable ancho
'''    
    
'''
Escriba una funcion que genere una tabla de multiplicar recibiendo como argumento la cantidad de numeros y la tabla a generar
'''

def multiplicar2numeros(x:int,y:int)->int: return x*y   # Funcion que recibe dos datos de tipo int y retorna un valor de tipo int

def tablamultiplicar(num:int,total:int)->int:       # Funcion que recibe dos datos de tipo int y retorna un valor de tipo int
    print(f"Tabla de multiplicar del {num}")        # Imprime la tabla de multiplicar del numero dado
    for i in range(1, total+1):           # Un ciclo For en un rango de 1 hasta el numero total de numeros de la tabla de multiplicar
        print(f"{num:<3}x{i:^4}={multiplicar2numeros(i,num):>4}")   # Imprime el numero multiplicado y el resultado por cada numero de la tabla de multiplicar dados y el resultado de manera espaciada
    return 0    # Todas las funciones tienen que retornar valores como buena practica de programacion

'''
Hacer una funcion que haga n tablas de multiplicar de n hasta n numeros con n numeros de la tabla de multiplicar de la misma
'''
  
def multitablas(numtablas:int,num:int,total:int)->int:    # Funcion que recibe tres datos de tipo int y retorna un dato de tipo int
    print(f"Tablas de multiplicar de 1 hasta {numtablas}")   # Imprime el titulo de las tablas de multiplicar de 1 hasta el numero de total de tablas a dar
    for i in range(1, numtablas+1):         # Ciclo For en un rango de 1 hasta numero total de tablas+1 para llegar al dado
        tablamultiplicar(num,total)     # Manda a llamar a la funcion tablamultiplicar dando los dos parametros para que la misma imprima la tabla de multiplicar 
        print()   # Puse que se imprimiera un espacio para una mejor presentacion entre tabla y tabla de multiplicar
        num+=1    # Se le añadira un 1 al numero dado para que se vaya ciclando el numero de la tabla de multiplicar siguiente
    return 0

if __name__ == "__main__":
    tablamultiplicar(1, 10)     # Manda a llamar la funcion de la tablademultiplicar dando dos parametros para que la misma funcione
    multitablas(3, 1, 10)      # Manda a llamar la funcion de multitablas dando tres parametros para que la misma funcione
    
#Cristian Larios ©
