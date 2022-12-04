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
