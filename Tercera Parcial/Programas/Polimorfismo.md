## Polimorfismo (Sobre Carga)
```
```
### • Dos funciones con el mismo nombre pero con diferente aridad son dos diferentes funciones.
```.ex
defmodule Rectangulo do
def area(l) do
l * l
end
def area(l1,l2) do
l1 * l2
end
end
```
## Salida
```.ex
iex()> c("modulo01.ex")
[Rectangulo]
iex()> Rectangulo.area(4)
16
iex()> Rectangulo.area(4,5)
20
```
### • Haciendo que una función dependa de otra de diferente aridad, se podría realizar lo siguiente:
```.ex
defmodule Calculadora do
def suma(n) do
suma(n,0)
end
def suma(n1,n2) do
n1 + n2
end
end
```
### Salida:
```.ex
iex()> c("modulo01.ex")
[Calculadora]
iex()> Calculadora.suma(4)
4
iex()> Calculadora.suma(4,5)
9
Argumentos por defecto
```
### • Se pueden especificar argumentos por defecto mediante el operador
```.ex
defmodule Calculadora do
def suma(n1,n2 \\ 0) do
n1 + n2
 end
end
```
### • Este módulo genera dos funciones como en el caso anterior
````
````
### Salida
```.ex
iex()> c("modulo01.ex")
[Calculadora]
iex()> Calculadora.suma(7)
7
iex()> Calculadora.suma(7,10)
17
```
### • Se puede utilizar cualquier combinación de argumentos por defecto:
```.ex
defmodule Calculadora do
def funcion(n1,n2 \\ 0, n3 \\ 1, n4, n5 \\ 2) do
n1 + n2 + n3 + n4 + n5
end
end
````
### Salida:
```.ex
iex()> c("modulo01.ex")
[Calculadora]
iex()> Calculadora.funcion(4)
** (UndefinedFunctionError) function Calculadora.funcion/1 is undefined o
r private. Did you mean one of:
* funcion/2
* funcion/3
* funcion/4
* funcion/5
Calculadora.funcion(4)
iex()> Calculadora.funcion(4,5)
12
iex()> Calculadora.funcion(4,5,6)
18
iex()> Calculadora.funcion(4,5,6,7)
24
iex()> Calculadora.funcion(4,5,6,7,8)
30
iex()> Calculadora.funcion(4,5,6,7,8,9)
** (UndefinedFunctionError) function Calculadora.funcion/6 is undefined o
r private. Did you mean one of:
* funcion/2
* funcion/3
* funcion/4
* funcion/5
Calculadora.funcion(4, 5, 6, 7, 8, 9)
iex()>
```
## Imports:
```
```
### • Creamos un archivo fuente main.ex
### • Escribimos el siguiente código:
```.ex
import ModuloImportado
defmodule ModuloMain do
def main do
IO.puts("Funcion main")
funcion_importada("Esta funcion es importada")
end
end
```
### • Creamos el Módulo a importar modsec.ex
### • Escribimos el siguiente código:
```.ex
defmodule ModuloImportado do
def funcion_importada(msg) do
IO.puts(msg)
end
end
```
### • Compilamos en iex la función a importar
```.ex
iex> c("modsec.ex")
[ModuloImportado]
```
### • Compilamos en iex la función que va a importar
```.ex
iex> c("main.ex")
[ModuloMain]
```
### • Ejecutamos la función main
```.ex
iex> ModuloMain.main()
Funcion main
Esta funcion es importada
:ok
```
### • Si no se quiere importar el módulo, se puede utilizar de manera directa indicando el módulo y la función esto es:
```.ex
defmodule ModuloMain do
def main do
IO.puts("Funcion main")
ModuloImportado.funcion_importada("Esta funcion es importada")
end
end
```
### • Es necesario volver a compilar la función main:
```.ex
iex(7)> c("main.ex")
warning: redefining module ModuloMain (current version defined in memory)
main.ex:3
[ModuloMain]
iex(8)> ModuloMain.main()
Funcion main
Esta funcion es importada
:ok
Alias
```
### • Se puede utilizar alias como alternativa a import, permite hacer una referencia a un módulo con otro nombre:
```.ex
defmodule ModuloMain do
alias ModuloImportado, as: MI
def main do
IO.puts("Funcion main")
MI.funcion_importada("Esta funcion es importada con alias")
end
end
```
### • bash:
```.ex
iex(10)> c("main.ex")
warning: redefining module ModuloMain (current version defined in memory)
main.ex:1
[ModuloMain]
iex(11)> ModuloMain.main()
Funcion main
Esta funcion es importada con alias
:ok
```
