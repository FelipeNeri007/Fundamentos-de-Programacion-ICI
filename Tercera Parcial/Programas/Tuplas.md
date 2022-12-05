## Tuplas:
• son como estructuras o registros

• permiten agrupar elementos fijos
```.ex
iex>persona = {"Alex", 49}
{"Alex", 49}
iex> i {"Alex", 49}
Term
{"Alex", 49}
Data type
Tuple
Reference modules
Tuple
Implemented protocols
IEx.Info, Inspect
```
### • Para extraer elementos se usa la función elem:
```.ex
iex> nombre = elem(persona, 0)
"Alex"
iex> nombre
"Alex"
iex> edad = elem(persona,1)
49
iex> edad
49
```
### • Para modificar un elemento se usa la función put_elem:
```.ex
iex> put_elem(persona,0,"Alexander")
{"Alexander", 49}
```
### • Las tuplas son inmutables, por lo que no se modifica:
```.ex
iex> persona
{"Alex", 49}
```
### • Si se necesita cambiar, hay que almacenar el cambio en otra variable, o en la
### misma si ya no se desea conservar los valores:
```.ex
iex> persona = put_elem(persona,0,"Alexander")
{"Alexander", 49}
iex> persona
{"Alexander", 49}
```
### Listas
• Manejo dinámico de datos
• Funcionan como listas enlazadas simples
```.ex
iex> numeros_pares = [2,4,6,8,10]
[2, 4, 6, 8, 10]
iex> i [2, 4, 6, 8, 10]
Term
[2, 4, 6, 8, 10]
Data type
List
Reference modules
List
Implemented protocols
Collectable, Enumerable, IEx.Info, Inspect, List.Chars, String.Chars
iex> length(numeros_pares)
5
```
### • Obtener un elemento de la lista mediante la función Enum.at/2:
```.ex
iex> Enum.at(numeros_pares,4)
10
iex> Enum.at(numeros_pares,5)
nil
```
### • Se puede saber si x elemento pertenece a una lista con operador in:
```.ex
iex> 2 in numeros_pares
true
iex> 12 in numeros_pares
false
```
### • Módulo List:
– Modificar o reemplazar un elemento de la lista
```.ex
iex> List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
iex> numeros_pares
[2, 4, 6, 8, 10]
iex> nuevos_pares = List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
iex> numeros_pares = List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
```
### • Insertar un elemento:
```.ex
iex> numeros_pares
[2, 4, 6, 8, 12]
iex> numeros_pares = List.insert_at(numeros_pares,4,10)
[2, 4, 6, 8, 10, 12]
iex> numeros_pares = List.insert_at(numeros_pares,-1,14)
[2, 4, 6, 8, 10, 12, 14]
```
### • Concatenar dos listas:
```.ex
iex> numeros_naturales = [1,2,3,4] ++ [5,6,7,8]
[1, 2, 3, 4, 5, 6, 7, 8]
iex> numeros_naturales
[1, 2, 3, 4, 5, 6, 7, 8]
```
### • Recursion sobre listas:
– El formato de una lista es [head | tail]

– head puede ser de cualquier tipo

– tail siempre es una lista

– si tail es una lista vacía [], indica que es el final de la lista.
```.ex
iex> []
[]
iex> [1|[]]
[1]
iex> [1|[2|[]]]
[1, 2]
iex> [1|[2|[3|[]]]]
[1, 2, 3]
iex> [1|[2|[3|[4|[]]]]]
[1, 2, 3, 4]
iex> [1|[2,3,4]]
[1, 2, 3, 4]
```
### • Funciones hd y tl:
```.ex
iex> numeros = [1,2,3,4,5]
[1, 2, 3, 4, 5]
iex> hd(numeros)
1
iex> tl(numeros)
[2, 3, 4, 5]
iex> [head | tail] = numeros
[1, 2, 3, 4, 5]
iex> head
1
iex> tail
[2, 3, 4, 5]
```
### • Agregar elementos a una lista
```.ex
iex> numeros = [0 | numeros]
[0, 1, 2, 3, 4, 5]
iex> numeros
[0, 1, 2, 3, 4, 5]
```
