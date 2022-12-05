### • if, ejemplo 1
```.ex
defmodule Persona1 do
def sexo(sex) do
if sex == :m do
"Masculino"
else
"Femenino"
end
end
end
```
### Salida:
```.ex
iex> c("main.ex")
[Persona1]
iex> Persona1.sexo(:m)
"Masculino"
iex> Persona1.sexo(:f)
"Femenino"
iex> Persona1.sexo(:x)
"Femenino"
```
### • if ejemplo 2
```
defmodule Persona2 do
def sexo(sex) do
if sex == :m do
"Masculino"
else if sex == :f do
"Femenino"
     else
      "Sexo desconocido"
    end
  end
 end
end
```
### Salida:
```.ex
iex> c("main.ex")
[Persona2]
iex> Persona2.sexo(:m)
"Masculino"
iex> Persona2.sexo(:f)
"Femenino"
iex> Persona2.sexo(:x)
"Sexo desconocido"
```
## case
### • case, ejemplo 1:
```.ex
defmodule Persona3 do
  def sexo(sex) do
   case sex do
     :m -> "Masculino"
     :f -> "Femenino"
     _ -> "Sexo desconocido"
   end
 end
end
```
### Salida:
```.ex
iex> c("main.ex")
[Persona3]
iex> Persona3.sexo(:m)
"Masculino"
iex> Persona3.sexo(:f)
"Femenino"
iex> Persona3.sexo(:x)
"Sexo desconocido"
```
### • Match con funciones, ejemplo 1:
```.ex
defmodule Persona4 do
def sexo(sex) when sex == :m do
"Masculino"
end
def sexo(sex) when sex == :f do
"Femenino"
end
def sexo(_sex) do
"sexo desconocido"
end
end
```
### Salida:
```.ex
iex> c("main.ex")
[Persona4]
iex> Persona4.sexo(:m)
"Masculino"
iex> Persona4.sexo(:f)
"Femenino"
iex> Persona4.sexo(:x)
"sexo desconocido"
```
## Match con funciones
### • Ejemplo 2:
```.ex
defmodule Persona5 do
def sexo(sex) when sex == :m, do: "Masculino"
def sexo(sex) when sex == :f, do: "Femenino"
def sexo(_sex), do: "sexo desconocido"
end
```
### Salida:
```.ex
iex> c("main.ex")
[Persona5]
iex> Persona5.sexo(:m)
"Masculino"
iex> Persona5.sexo(:f)
"Femenino"
iex> Persona5.sexo(:x)
"sexo desconocido"
```
## cond
### • cond, ejemplo 1:
```.ex
defmodule Persona6 do
def sexo(sex) do
cond do
sex == :m -> "Masculino"
sex == :f -> "Femenino"
true -> "Sexo desconocido"
end
end
end
```
### Salida:
iex> c("main.ex")
[Persona6]
iex> Persona6.sexo(:m)
"Masculino"
iex> Persona6.sexo(:f)
"Femenino"
iex> Persona6.sexo(:x)
"Sexo desconocido"
