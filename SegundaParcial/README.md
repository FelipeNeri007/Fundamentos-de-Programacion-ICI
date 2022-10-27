# Unidad II: Programación Orientada a Objetos
# Felipe Neri Gonzalez Martinez
## Problemas resueltos en clase
### Ejercicio 1.1. Crear una lista e iterarla imprimiendo cada dato con su indice.
### 1: Descripcion del ejercicio
  Necesitamos crear una lista para posteriormente iterarla con un ciclo for imprimiendo cada dato con su indice en el arreglo.
#### 2: Código
```dart
void main(List<String> args) {
  final miLista = const [1, 2, 3, 4]; // avoid side effects
  print(miLista);
  }
```
 #### 3: Implementación
 ```dart
  for (var i = 0; i < miLista.length; i++) {
    stdout.write("$i: ${miLista[i]} | ");
 ```
#### 4: Salida
```
[1, 2, 3, 4]
0: 1 | 1: 2 | 2: 3 | 3: 4 | 
```

### Ejercicio 1.2. calculadora que lea dos numeros del teclado y obtenga suma, resta, multiplicación y division, usando funciones y asingnado valores a dos variables
### 1: Descripcion del ejercicio
  Necesitamos crear una funcion que indique la operacion que se va a realizar (suma, resta, multiplicacion o división) y crear varias funciones para hacer la operacion echa por el usuario. 
#### 2: Código
```dart
String leerDatos(String mensaje) {
  print(mensaje);
  String data = (stdin.readLineSync()!);
  return data;
}
