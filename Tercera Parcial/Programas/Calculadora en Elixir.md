## Version 1:
```.ex
defmodule Calculadora do
 def suma(n1, n2) do
 n1 + n2
 end
 def resta(n1,n2) do
 n1 - n2
 end
 def multiplicacion(n1, n2) do
 n1 * n2
 end
 def division(n1,n2) do
 n1 / n2
 end
end
```
## Version 2:
```.ex
defmodule Calculadora do
 def suma(n1,n2), do: n1+n2
 def resta(n1,n2), do: n1-n2
 def multiplicación(n1,n2), do: n1*n2
 def división(n1,n2), do: n1/n2
end
```
## Calculadora Distribuida
```.ex
defmodule DistCalculator do
 def suma(n1,n2) do
 IO.puts(n1+n2)
 end
end
```
