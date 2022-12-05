## Test
### • Se realiza a partir del script del test:
```.ex
defmodule CalculadoraTest do
 use ExUnit.Case
 doctest Calculadora
 
 test "greets the world" do
  assert CALCULADORA.hello() == : world
  end
 end
 ```
 ## case
### • Ejemplo 1:
```.ex
defmodule Matematicas do
def calculadora(opcion,{n1,n2}) do
case opcion do
"+" -> n1+n2
"-" -> n1-n2
"/" when n2 != 0 -> n1/n2
"/" when n2 == 0 -> "No se puede dividir por 0"
"*" -> n1*n2
_ -> :error
end
end
end
IO.inspect Matematicas.calculadora("+",{5,4})
IO.inspect Matematicas.calculadora("-",{5,4})
IO.inspect Matematicas.calculadora("/",{5,4})
IO.inspect Matematicas.calculadora("/",{5,0})
IO.inspect Matematicas.calculadora("*",{5,4})
```
### Salida:
```.ex
>elixir main.exs
9
1
1.25
"No se puede dividir por 0"
20
9
```
## cond
### • Ejemplo 1:
```.ex
defmodule DiaSemana do
def dia(d) do
cond do
d == 1 -> "Lunes"
d == 2 -> "Martes"
d == 3 -> "Miercoles"
d == 4 -> "Jueves"
d == 5 -> "Viernes"
d == 6 -> "Sabado"
d == 7 -> "Domingo"
true -> "Dia no valido"
end
end
end
IO.puts DiaSemana.dia(1)
IO.puts DiaSemana.dia(2)
IO.puts DiaSemana.dia(3)
IO.puts DiaSemana.dia(4)
IO.puts DiaSemana.dia(5)
IO.puts DiaSemana.dia(6)
IO.puts DiaSemana.dia(7)
IO.puts DiaSemana.dia(8)
```
### Salida:
```.ex
C:\semana12>elixir main.ex
Lunes
Martes
Miercoles
Jueves
Viernes
Sabado
Domingo
El dia no es valido
```
### • Ejemplo 2:
```.ex
defmodule DiaSemana do
def dia(d) do
cond do
d == "l" or d == "L" -> "Lunes"
d == "ma" or d == "MA" -> "Martes"
d == "mi" or d == "MI" -> "Miercoles"
d == "j" or d == "J" -> "Jueves"
d == "v" or d == "V" -> "Viernes"
d == "s" or d == "S" -> "Sabado"
d == "d" or d == "D" -> "Domingo"
true -> "Dia no valido"
end
end
end
IO.puts DiaSemana.dia("l")
IO.puts DiaSemana.dia("ma")
IO.puts DiaSemana.dia("mi")
IO.puts DiaSemana.dia("j")
IO.puts DiaSemana.dia("v")
IO.puts DiaSemana.dia("s")
IO.puts DiaSemana.dia("d")
IO.puts DiaSemana.dia("L")
IO.puts DiaSemana.dia("MA")
IO.puts DiaSemana.dia("MI")
IO.puts DiaSemana.dia("J")
IO.puts DiaSemana.dia("V")
IO.puts DiaSemana.dia("S")
IO.puts DiaSemana.dia("D")
IO.puts DiaSemana.dia("Ma")
IO.puts DiaSemana.dia("mA")
```
### Salida:
```.ex
C:\semana12>elixir main.ex
Lunes
Martes
Miercoles
Jueves
Viernes
Sabado
Domingo
Lunes
Martes
Miercoles
Jueves
Viernes
Sabado
Domingo
El dia no es valido
El dia no es valido
```
### • Ejemplo 3:
```.ex
defmodule DiaSemana do
def dia(d) do
d = String.upcase(d)
cond do
d == "L" -> "Lunes"
d == "MA" -> "Martes"
d == "MI" -> "Miercoles"
d == "J" -> "Jueves"
d == "V" -> "Viernes"
d == "S" -> "Sabado"
d == "D" -> "Domingo"
true -> "Dia no valido"
end
end
end
IO.puts DiaSemana.dia("l")
IO.puts DiaSemana.dia("ma")
IO.puts DiaSemana.dia("mi")
IO.puts DiaSemana.dia("j")
IO.puts DiaSemana.dia("v")
IO.puts DiaSemana.dia("s")
IO.puts DiaSemana.dia("d")
IO.puts DiaSemana.dia("L")
IO.puts DiaSemana.dia("MA")
IO.puts DiaSemana.dia("MI")
IO.puts DiaSemana.dia("J")
IO.puts DiaSemana.dia("V")
IO.puts DiaSemana.dia("S")
IO.puts DiaSemana.dia("D")
IO.puts DiaSemana.dia("Ma")
IO.puts DiaSemana.dia("mA")
```
### Salida:
```.ex
iC:\semana12>elixir main.ex
Lunes
Martes
Miercoles
Jueves
Viernes
Sabado
Domingo
Lunes
Martes
Miercoles
Jueves
Viernes
Sabado
Domingo
Martes
Martes
```
## unless
### • Ejemplo 1:
```.ex
Código fuente
defmodule MayorDeEdad do
def mayor1(edad) do
unless edad >= 18 do
"Es menor de edad"
end
end
end
```
### Salida:
```.ex
iex> c("main.ex")
[MayorDeEdad]
iex> MayorDeEdad.mayor(16)
"Es menor de edad"
iex> MayorDeEdad.mayor1(18)
```
### • Ejemplo 2:
```.ex
defmodule MayorDeEdad do
def mayor1(edad) do
unless edad >= 18 do
"Es menor de edad"
end
end
def mayor2(edad) do
if edad < 18 do
"Es menor de edad"
end
end
end
```
### Salida:
iex> c("main.ex")
[MayorDeEdad]
iex> MayorDeEdad.mayor1(16)
"Es menor de edad"
iex> MayorDeEdad.mayor2(16)
"Es menor de edad"
iex(61)> MayorDeEdad.mayor1(18)
nil
iex(62)> MayorDeEdad.mayor2(18)
nil
