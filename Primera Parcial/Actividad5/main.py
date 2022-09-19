'''
Hacer una funcion que reciba el nombre de una persona y el año de nacimiento de una persona
el año de nacimiento y el año actual retornando el mensaje "Hola <nombre>, tienes <edad> años"
'''

def funcion1(nombre:str, anoactual:int, anonac:int)->str:       # Funcion que pide un dato de tipo str y dos datos de tipo int
    edad = anoactual - anonac   # Calculamos la edad restando el año actual al año de nacimiento
    return f"Hola {nombre}, tienes {edad} años"     # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"
    #return f"Hola <{nombre}>, tienes <{anoactual - anonac}> años"  # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"

def funcion2(nombre:str, anoactual:int, anonac:int)->str:       # Funcion que pide un dato de tipo str y dos datos de tipo int
    return f"Hola {nombre}, tienes {anoactual - anonac} años"  # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"

def calcular_edad( anoactual:int, anonac:int)->int:      # Funcion que pide un dato de tipo str y dos datos de tipo int
    return anoactual-anonac

def funcion3(nombre:str, anoactual:int, anonac:int)->str:    # Funcion que pide un dato de tipo str y dos datos de tipo int y retorna un valor str
    return f"Hola {nombre}, tienes {calcular_edad(anoactual, anonac)} años"  # Imprime una cadena junto con los valores que ingresamos


if __name__ == "__main__":
    print(funcion1("Cristian", 2022, 2003))                 # Imprimimos el resultado del valor retornado de la funcion1
    print(funcion2("Cristian", 2022, 2003))  # Imprimimos el resultado del valor retornado de la funcion2
    res = funcion1("Cristian", 2022, 2003)   # Asignar el valor del valor retornado de la funcion1 a la variable res
    print(res)      # Imprimir el valor de la variable res
    print(funcion3("Cristian", 2022, 2003)) # Imprimimos el resultado del valor retornado de la funcion3
    
    e = ["Nombre", "Est Dat", "Prog Func", "Ingles"]    # Creamos una lista con los nombres de las materias
    alumnos = ["Hugo Alberto", "Paco", "Luis", "Lupita"]  # Creamos una lista con los nombres de los alumnos
    materia_e_d = [9,7,9,8]   # Creamos una lista con las calificaciones de la materia1
    materia_p_g = [8,9,7,8]   # Creamos una lista con las calificaciones de la materia2
    materia_i = [6,7,9,8]     # Creamos una lista con las calificaciones de la materia3
    ancho = 15                # El ancho que tendrá al imprimirse entre cada variable 

    print(f"{e[0]:^{ancho}} {e[1]:^{ancho}} {e[2]:^{ancho}} {e[3]:^{ancho}}")   # Imprimimos "Nombre", "Est Dat", "Prog Func", "Ingles" de manera espaciada
    for i in range(len(alumnos)):   # Un ciclo For en un rango de la longitud de la variable alumnos
      print(f"{alumnos[i]:<{ancho}} {materia_e_d[i]:^{ancho}} {materia_p_g[i]:^{ancho}} {materia_i[i]:^{ancho}}")   # Imprimimos de manera espaciada cada valor correspondiente a las listas    
    
#Cristian Larios ©
