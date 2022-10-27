void main(List<String> args) {
  // Animal Tigre = Animal(nombre: 'Tigre', patas: 10);
  // Tigre.info();
  // Tigre.correr();
  Perro perrito = Perro('Chiuahua');
  perrito.caminar();
  perrito.patas = 4;
  perrito.nombre = 'Chencho';
  perrito.ladrar();
  perrito.info();
}

class Animal {
  int? patas;
  String? nombre;

  void info() {
    print('El animal ${nombre} tiene ${patas} patas');
  }

  void caminar() {
    print('Animal caminando');
  }

  Animal({this.nombre, this.patas});
}

class Perro extends Animal {
  String? _raza;

  void ladrar() {
    print('guau guau');
  }

  void caminar() {
    print("Perro caminando");
  }

  void info() {
    print('El animal ${_raza} tiene ${patas} patas y se llama ${nombre}');
  }


  Perro(this._raza);
}

class Ave extends Animal {
  String? _raza;

  void volar() {
    print("Ave volando");
  }

  Ave(this._raza);

  void info() {
    print('El Ave de raza ${_raza} tiene ${patas} patas y se llama ${nombre}');
  }
}
