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
