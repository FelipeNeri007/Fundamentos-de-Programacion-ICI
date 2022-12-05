# Funciones
```
Una función siempre debe estar dentro de un módulo
Los nombres de funciones son igual que las variables: 
– El nombre de una variable siempre inicia con un caracter alfabético en 
minúscula o caracter de subrayado (_) 
– Después puede llevar cualquier combinación de estos caracteres 
– La convención es usar solo letras, dígitos y subrayados 
– Pueden terminar con los carateres ? o !. 
– Por convención el ? se utiliza cuando la función retorna true o false 
– El ! se utiliza generalmente en funciones que podrían provocar algún error 
en tiempo de ejecución 
– Tanto defmodule como def NO son palabras reservadas del lenguaje, son 
macros.
```
## Funcion sin Argumentos
```.ex
defmodule HolaMundo do
 def mensaje do
IO.puts("Hola Mundo")
 end
end
```
## Funcion con Argumentos
```.ex
defmodule Calculadora do
 def suma(n1,n2) do
 n1 + n2
 end
end
```
## • Las funciones pueden expresarse de manera condensada:
```.ex
defmodule Geometria do
 def perimetro_cuadrado(l), do: 4*l
 def perimetro_rectangulo(l1,l2), do: 2*l1 + 2*l2
end
```
### Salida:
```.ex
iex()> c("modulo01.ex") 
[Geometria]
iex()> Geometria.perimetro_cuadrado(4) 
16 
iex()> Geometria.perimetro_rectangulo(4,3)
14
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
## Visibilidad de Funciones:
```
• Se pueden utilizar funciones privadas con el constructor defp
• Función Publica y privada:
```
```.ex
defmodule TestPublicoPrivado do
 def funcion_publica(msg) do
 IO.puts("#{msg} publico")
 funcion_privada(msg)
 end
 defp funcion_privada(msg) do
 IO.puts("#{msg} privado")
 end
end
TestPublicoPrivado.funcion_publica("este es un mensaje")
```
### Salida:
```.ex
iex> c("modulo01.ex")
este es un mensaje publico
este es un mensaje privado
[TestPublicoPrivado]
```
### • Funciones:
```.ex
defmodule Calculadora do
def div(_,0) do
{:error, "No se puede dividir por 0"}
end
def div(n1, n2) do
{:ok, "El resultado es: #{n1/n2}"}
end
end
IO.inspect(Calculadora.div(5,0))
IO.inspect(Calculadora.div(5,3))
```
### Salida:
```.ex
>elixir main.ex
{:error, "No se puede dividir por 0"}
{:ok, "El resultado es: 1.6666666666666667"}
```
### • Si invertimos el orden de las funciones, es decir:
```.ex
defmodule Calculadora do
def div(n1, n2) do
{:ok, "El resultado es: #{n1/n2}"}
end
def div(_,0) do
{:error, "No se puede dividir por 0"}
end
end
IO.inspect(Calculadora.div(5,0))
IO.inspect(Calculadora.div(5,3))
```
### Salida:
```.ex
>elixir main.ex
warning: this clause for div/2 cannot match because a previous clause at
line 2 always matches
main.ex:5
** (ArithmeticError) bad argument in arithmetic expression
main.ex:3: Calculadora.div/2
main.ex:10: (file)
(elixir 1.10.4) lib/code.ex:926: Code.require_file/2
```
### Guardas:
```.ex
defmodule Numero do
def cero?(0), do: true
def cero?(n) when is_integer(n), do: false
def cero?(_), do: "No es entero"
end
IO.puts(Numero.cero?(0))
IO.puts(Numero.cero?(2))
IO.puts(Numero.cero?("3"))
```
### Salida:
```.ex
>elixir main.ex
true
false
```
No es entero
