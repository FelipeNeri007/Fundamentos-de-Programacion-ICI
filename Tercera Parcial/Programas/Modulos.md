## • Un módulo puede estar dentro de un archivo. 
```.ex
defmodule Calculadora do
 def suma(n1,n2) do
 n1 + n2
 end
end
defmodule Areas do
 def area_cuadrado(l) do
 l*l
 end
end
```
### Salida:
````.ex
iex()> c("modulo01.ex")
warning: redefining module Calculadora (current version defined in memory
)
modulo01.ex:1
[Areas, Calculadora]
iex()> Areas.area_cuadrado(4)
16 
iex()> Calculadora.suma(5,5) 
10
```
`````
## Regla de Modulos:
```
– Inicia con una letra mayúscula 
– Se escribe con el estilo CamelCase
– Puede consistir en caracteres alfanuméricos, subrayados y puntos (.). 
Regularmente se usa para la organización jerárquica de los módulos
```
```.ex
defmodule Geometria.Cuadrado do
 def perimetro(l) do
 4*l
 end
end
defmodule Geometria.Rectangulo do
 def perimetro(l1,l2) do
 2*l1 + 2*l2
 end
end
```
### Salida:
```.ex
iex()> c("modulo01.ex") 
[Geometria.Cuadrado, Geometria.Rectangulo]
iex()> Geometria.Cuadrado.perimetro(4)
16
iex()> Geometria.Rectangulo.perimetro(4,2)
12
```
## • También se pueden anidar de la siguiente forma: 
```.ex
defmodule Geometria do
 defmodule Cuadrado do
 def perimetro(l) do
 4*l
 end
 end
 defmodule Rectangulo do
 def perimetro(l1,l2) do
2*l1 + 2*l2
 end
 end
end
```
### Salida:
```.ex
iex(7)> c("modulo01.ex")
warning: redefining module Geometria.Cuadrado (current version defined in 
memory)
 modulo01.ex:2
warning: redefining module Geometria.Rectangulo (current version defined 
in memory)
 modulo01.ex:7
[Geometria, Geometria.Cuadrado, Geometria.Rectangulo]
iex(8)> Geometria.Cuadrado.perimetro(4) 
16
iex(9)> Geometria.Rectangulo.perimetro(4,2)
12
```
## • Invocaciones internas de una función no requieren del prefijo del nombre del módulo:
```.ex
defmodule Geometria do
 def perimetro1(l), do: cuadrado(l)
 def perimetro2(l), do: Geometria.cuadrado(l)
 def cuadrado(l), do: 4*l
end
```
### Salida:
```.ex
iex()> c("modulo01.ex") 
[Geometria]
iex()> Geometria.perimetro1(4) 
16
iex()> Geometria.perimetro2(4) 
16
iex()> Geometria.cuadrado(4) 
16
```
## Modulo de Geometria:
```.ex
defmodule Geometria do
 def perimetro1(l), do: cuadrado(l)
 def perimetro2(l), do: Geometria.cuadrado(l)
 defp cuadrado(l), do: 4*l
end
```
### Salida:
```.ex
iex()> c("modulo01.ex") 
[Geometria]
iex()> Geometria.perimetro1(4)
16
iex()> Geometria.perimetro2(4)
** (UndefinedFunctionError) function Geometria.cuadrado/1 is undefined or 
private
 Geometria.cuadrado(4)
iex()> Geometria.cuadrado(4)
** (UndefinedFunctionError) function Geometria.cuadrado/1 is undefined or 
private
 Geometria.cuadrado(4)
