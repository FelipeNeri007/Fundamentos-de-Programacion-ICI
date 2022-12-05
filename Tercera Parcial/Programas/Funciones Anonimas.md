## Funciones anónimas:
• No tienen nombre
• Se pueden fijar a variables
## Ejemplos de funciones anónimas:
### • Ejemplo 1:
```.ex
defmodule Calculadora do
def suma(n1,n2), do: n1+n2
end
suma_anonima = fn(n1,n2) -> n1 + n2 end
IO.puts(Calculadora.suma(5,4))
IO.puts(suma_anonima.(5,5))
>elixir main.ex
9
10
```
### • Ejemplo 2:
```.ex
mayor? = fn(n1,n2) -> if n1 > n2 do true else false end end
IO.inspect(mayor?.(4,5))
IO.inspect(mayor?.(5,4))
IO.inspect(mayor?.(5,5))
```
### • Salida:
```.ex
>elixir main.exs
false
true
false
```
• Ejemplo de función anónima
• Si se desea personalizar la salida
```.ex
mayor? = fn(n1,n2) -> if n1 > n2 do :si else :no end end
IO.inspect(mayor?.(4,5))
IO.inspect(mayor?.(5,4))
>elixir main.exs
:no
:si
```
### • Ejemplo 3:
```.ex
mayor? = fn(n1,n2) -> if n1 > n2 do :si else :no end end
res = mayor?.(4,5)
IO.puts res
res = mayor?.(5,4)
IO.puts res
```
### Salida:
```.ex
>elixir main.exs
no
si
```
### • Ejemplo 4:
```.ex
mayor = fn(n1,n2) ->
if n1 > n2 do
{:ok, "#{n1} > #{n2}"}
else
{:error, "#{n1} <= #{n2}"}
end
end
IO.inspect mayor.(4,5)
IO.inspect mayor.(5,4)
IO.inspect mayor.(5,5)
```
### Salida:
```.ex
>elixir main.exs
{:error, "4 <= 5"}
{:ok, "5 > 4"}
{:error, "5 <= 5"}
```
### • Ejemplo 5:
```.ex
mayor = fn(n1,n2) ->
if n1 > n2 do
{:ok, "#{n1} > #{n2}"}
else
{:error, "#{n1} <= #{n2}"}
end
end
{status, res} = mayor.(4,5)
IO.puts status
IO.puts res
{status, res} = mayor.(5,4)
IO.puts status
IO.puts res
```
### Salida:
>elixir main.exs
error
4 <= 5
ok
```

5 > 4
