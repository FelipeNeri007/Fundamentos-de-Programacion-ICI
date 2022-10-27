// SIMULACRO EXAMEN PRACTICO

void main(List<String> args) {
  // vehiculo rx-3 = new vehiculo(4, 'mazda', 'negro', '1978');
  // // rx-3.llantas = 4;
  // // rx-3.color = 'negro';
  // // rx-3.modelo = '1978';
  // // rx-3.marca = 'mazda';

  // rx-3.imprimircaracteristicas();
  // rx-3.arrancar();
  // rx-3.correr();
  // rx-3.frenar();

  // print('');

  // vehiculo 240Z = new vehiculo(4, 'Verde', 'Datsun', '1970');
  // crx.llantas = 4;
  // crx.marca = 'Honda';
  // crx.color = 'negro';
  // crx.modelo = '1985';

  // crx.imprimircaracteristicas();
  // crx.arrancar();
  // crx.correr();
  // crx.frenar();

  vehiculo miClassic = new vehiculo(4, 'Naranja', 'Acura', 'NSX');
  // vehiculo miClassic = new vehiculo(4, 'Negro', 'NSX', 'Acura');
  print('');
  miClassic.imprimircaracteristicas();
  print('');
  // showVehiculo(miClassic);
}

class vehiculo {
  int? _num_llantas;
  String? _color;
  String? _modelo;
  String? _marca;

  void imprimircaracteristicas() {
    print(
        "Modelo: $_modelo\nColor: $_color\nMarca: $_marca\nNumero de llantas: $_num_llantas");
  }

  void arrancar() {
    if (_num_llantas == 4) {
      print('El auto se esta encendiendo....tucutucutucu.');
    } else {
      print('Le faltan llantas al vehiculo, no puede arrancar');
    }
  }

  void correr() {
    print("Xxxx, el vehiculo va en movimiento");
  }

  void frenar() {
    print('Ishhh, el vehiculo se ha detenido.');
  }

  void set llantas(int llantas) => _num_llantas = llantas;
  void set color(String color) => _color = color;
  void set modelo(String modelo) => _modelo = modelo;
  void set marca(String marca) => _marca = marca;   //setters

  int get llantas => llantas;
  String get color => color;  // getters
  String get modelo => modelo;
  String get marca => marca;

  vehiculo(int llantas, String color, String marca, String modelo) {
    this._num_llantas = llantas;
    this._color = color; // constructor
    this._marca = marca;
    this._modelo = modelo;
  }

//   vehiculo(this._num_llantas, this._color, this._marca, this._modelo);
//   vehiculo.marca(this._marca);  // Constructor resumido
}

void showVehiculo(vehiculo miCarro) {
  print('Marca        ${miCarro.marca}');
  print('Modelo');
  print('Color');
  print('No de llantas:');
}
