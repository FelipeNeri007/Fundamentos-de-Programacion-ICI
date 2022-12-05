## • Piso de un número flotante:
```.ex
iex> trunc(5/2)
2
iex> floor(5/2)
2
```
### • Techo (cielo) de un número flotante:
```.ex
iex> round(5/2)
3
iex> ceil(5/2)
3
```
### • Números binarios:
```.ex
iex> 0b10101001111
1359
```
### • Números octales:
```.ex
iex> 0o74754
31212
```
### • Números hexadecimales:
```.ex
iex> 0xFFFF
65535
```
### • Azucar Sintáctica para los números:
```.ex
iex> 1_000_000
1000000
iex> 1_000_000.123
1000000.123
```
### Atoms:
• Constantes literales nombradas

• es una constante cuyo nombre es su propio valor

• inician con : (dos puntos)

• seguidos de caracteres alfanuméricos y/o subrayados

• se pueden usar espacios en blanco si se ponen entre comillas
```.ex
iex> :atom
:atom
iex> is_atom(:atom)
true
iex> is_atom(:es_un_atom)
true
iex> is_atom(:"es un atom")
true
iex> i :ok
Term
:ok
```
### Data Type:
```.ex
Atom
Reference modules
Atom
Implemented protocols
IEx.Info, Inspect, List.Chars, String.Chars
```
### • Un atom consta de dos partes:
– texto: el que se pone después de los dos puntos
– valor: es la referencia a la tabla de atoms.
```.ex
iex> var_atom = :atom
:atom
iex> var_atom
:atom
iex> :atom = var_atom
:atom
```
### • Un atom se puede nombrar con mayúscula inicial:
```.ex
iex> is_atom(Un_atom)
true
iex> Un_atom = Elixir.Un_atom
Un_atom
```
• Atomos como booleanos

• Los valores booleanos son atoms
```.ex
iex> is_atom(true)
true
iex> is_boolean(true)
true
iex> is_boolean(:true)
true
iex> is_boolean(:atom)
false
iex> :true == true
true
iex> :false == false
true
Atoms and, or y not
iex> true and true
true
iex> true and false
false
iex> true or true
true
iex> true or false
true
iex> not false
true
iex> not true
false
iex> not not true
```
### • Los átomos nil y false son tratados como valores falsos, mientras que todo lo
demás es tratado como un valor de verdad.
### • Esta propiedad es útil con los operadores de cortocircuito:
– || -> retorna la primera expresión verdadera
– && -> retorna la segunda siempre y cuando la primera lo sea también
– ! -> retorna la negación de la expresión sin importar el tipo de dato
### • || -> retorna la primera expresión verdadera:
```.ex
iex> false || nil || 5 || true
5
iex> false || nil || 5 || false || true
5
iex> false || nil || false || false || true || 5
true
```
### • && -> retorna la segunda siempre y cuando la primera lo sea también:
```.ex
iex> false && 5
false
iex> nil && 5
nil
iex> true && 5
5
iex> true && true
true
iex> 5 && true
true
iex> true && 5 && 4
4
iex> false && 5 && 4
false
iex> true && false && 4
false
iex> true && 4 && false
false
```
• ! ! -> retorna la negación de la expresión sin importar el tipo de dato:
```.ex
iex> !true
false
iex> !false
true
iex> !5
false
iex> !nil
true
iex> not !4
true
iex> !(5+4)
false
iex> not(5+4)
** (ArgumentError) argument error
:erlang.not(9)
