### • Existen los atributos en tiempo de compilación (Mientras están cargados):
```.ex
defmodule Geometria do
@pi 3.141592
def area(r) do
r*r*@pi
end
def circunferencia(r) do
2 * r * @pi
end
end
```
### Salida:
```.ex
iex> c("main.ex")
[Geometria]
iex> alias Geometria, as: G
Geometria
iex> G.area(4)
50.265472
iex> G.circunferencia(4)
25.132736
```
## • Elixir permite el registro de atributos, que se almacenarán en el archivo binario.
### – @moduledoc 
###  @doc
## • Sirven para documentar módulos y funciones
```.ex
defmodule Geometria do
@moduledoc "Calcula el area y el perimetro de un circulo"
@pi 3.141592
@doc "calcula el area del circulo"
def area(r), do: r*r*@pi
@doc "calcula el perimetro de un circulo"
def circunferencia(r), do: 2 * r * @pi
end
```
### • Para comprobar su uso, compilamos en la terminal el código fuente:
– C:>elixirc main.ex}
### • Esto va a generar el archivo:
– Elixir.Geometria.beam
### • abrimos iex y verificamos la documentación:
```.ex
iex> Code.fetch_docs(Geometria)
{:docs_v1, 2, :elixir, "text/markdown",
%{"en" => "Calcula el area y el perimetro de un circulo"}, %{},
[
{{:function, :area, 1}, 6, ["area(r)"],
%{"en" => "calcula el area del circulo"}, %{}},
{{:function, :circunferencia, 1}, 9, ["circunferencia(r)"],
%{"en" => "calcula el perimetro de un circulo"}, %{}}
]}
iex> h Geometria
* Geometria
Calcula el area y el perimetro de un circulo
iex> h Geometria.area
* def area(r)
calcula el area del circulo
iex> h Geometria.circunferencia
* def circunferencia(r)
calcula el perimetro de un circulo
iex(6)>
```
## Tipos de datos
• Elixir utiliza el mismo sistema de tipos de Erlang
### Numeros
• Los números pueden ser enteros o flotantes
```.ex
iex> 3
3
iex> is_number(3)
true
iex> 3.5
3.5
iex> is_number(3.5)
true
```
Integer
```.ex
iex> is_integer(3)
true
iex> is_float(3)
false
iex> i 34 #inspect
Term
34
Data type
Integer
Reference modules
Integer
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```
Float:
```.ex
iex> is_integer(3.5)
false
iex> is_float(3.5)
true
iex> i(3.5)
Term
3.5
Data type
Float
Reference modules
Float
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```
Notación científica:
```.ex
iex> 3.25555e-3
0.00325555
iex> 3.25555e3
3255.55
iex>i 3.25555e3
Term
3255.55
Data type
Float
Reference modules
Float
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```
Operaciones aritméticas
```.ex
iex> 5 * 4 / 3 + 2 - 5
3.666666666666668
iex> 5/4
1.25
iex> 5/5
1.0
iex> div(5,5)
1
iex> rem(5,5)
0
