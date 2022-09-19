#Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla "<mensaje> <nombre>"
def funcion1(a: str, b: str) -> str:  # Asignar como valores de entrada a y b cuyo tipo de dato seran de tipo string(str) y el valor de salida será tipo string(str)
    return f"<{a}> <{b}>"

#Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: "Hola <nombre> tienes <edad> años"
def funcion2(a: str, b: int) -> str:  # Asignar como valores de entrada a y b cuyo tipo de dato seran de tipo string(str) y el valor de salida será tipo string
    return f"Hola {a} tienes {b} años"
  
#Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años"
def funcion3(a: int, b: int, c: str) -> str:  # Asignar como valores de entrada a y b cuyo tipo de dato seran de tipo integer(int) y c será de tipo string(str) y el valor de salida será tipo string(str)
    edad = a - b
    return funcion2(c, edad)
  
if __name__ == "__main__":
    print("Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla '<mensaje> <nombre>'")
    print(funcion1("Hola", "Cristian")) # Se imprime el valor del resultado que retorna la funcion a llamar funcion1 metiendo los 2 parametros que pide
    print("Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: 'Hola <nombre> tienes <edad> años'")
    print(funcion2("Cristian", 18)) # Se imprime el valor del resultado que retorna la funcion a llamar funcion2 metiendo los 2 parametros que pide
    print("Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: 'Hola <nombre> tienes <edad> años'")
    print(funcion3(2022, 2003, "Cristian")) # Se imprime el valor del resultado que retorna la funcion a llamar funcion3 metiendo los 3 parametros que pide
# Cristian Larios ©
