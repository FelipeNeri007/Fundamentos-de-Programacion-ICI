## Operador pipeline:
```.ex
iex()> 4 |> Geometria.perimetro1
16
```
## • Dado el siguiente programa:
```.ex
defmodule Operaciones do
 def suma(n1,n2), do: n1 + n2
 def cuadrado(n), do: n * n
end
```
## • Obtener el cuadrado de la suma de 2 números (4 y 5):
```.ex
defmodule Operaciones do
 def suma(n1,n2), do: n1 + n2
 def cuadrado(n), do: n * n
end
```
## • Invocando las funciones:
```.ex
iex()> Operaciones.cuadrado(Operaciones.suma(4,5)) 
81
```
## Utilizando pipelines:
```.ex
iex()> 4 |> Operaciones.suma(5) |> Operaciones.cuadrado
81
iex()> Operaciones.suma(4,5) |> Operaciones.cuadrado
81
```
## • Mediante un módulo test que realice las pruebas se podría realizar de la siguiente forma: 
```.ex
defmodule Operaciones do
 def suma(n1,n2), do: n1 + n2
 def cuadrado(n), do: n * n
end
defmodule Test do
 def start do
 4 |> Operaciones.suma(5) |>Operaciones.cuadrado
 end
end
```
