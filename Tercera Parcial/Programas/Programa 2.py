#Ejemplo de Programacion Orientada a Objetos
#Calculadora en Python
```class Objeto_Calculadora:
 def __init__(self, n1,n2):
 self.num1 = n1
 self.num2 = n2
 def Suma(self):
 return self.num1+self.num2
 def Resta(self):
 return self.num1-self.num2
 def Multiplicacion(self):
 return self.num1*self.num2
 def Division(self):
 return self.num1/self.num2
 def __del__(self):
 self.num1 = None
 self.num2 = None
def menu():
 print("Menú de Opciones")
 print("[1] Suma")
 print("[2] Resta")
 print("[3] Multiplicación")
 print("[4] División")
 print("[5] Salir") 
def pedir_valor(mensaje):
 num = int(input(mensaje))
 return num
if __name__ == "__main__":
 Mi_Calculadora = Objeto_Calculadora(0,0)
 opc = 1
 while opc != 5:
 while opc >= 1 and opc <= 5:
 menu()
 opc=int(input("Seleccione su opción[1-4]"))
 if (opc == 1):
 Mi_Calculadora.num1 = pedir_valor("Dame el primer valor a 
sumar: ")
 Mi_Calculadora.num2 = pedir_valor("Dame el segundo valor 
a sumar: ")
 print("Resultado: "+str(Mi_Calculadora.Suma())+"\n\n")
 elif (opc == 2):
 Mi_Calculadora.num1 = pedir_valor("Dame el primer valor a 
restar: ")
 Mi_Calculadora.num2 = pedir_valor("Dame el segundo valor 
a restar: ")
 print("Resultado: "+str(Mi_Calculadora.Resta())+"\n\n")
 elif (opc == 3):
 Mi_Calculadora.num1 = pedir_valor("Dame el primer valor a 
multiplicar: ")
 Mi_Calculadora.num2 = pedir_valor("Dame el segundo valor 
a multiplicar: ")
 print("Resultado: "+str(Mi_Calculadora.Multiplicacion())+
"\n\n")
 elif (opc == 4):
 Mi_Calculadora.num1 = pedir_valor("Dame el primer valor a 
dividir: ")
 Mi_Calculadora.num2 = pedir_valor("Dame el segundo valor 
a dividir: ")
 print("Resultado: "+str(Mi_Calculadora.Division())+"\n\n"
)
 elif (opc == 5):
 break 
      else:
 pass
 else:
 print("Por favor introduzca una opción válida [1..5]\n\n")
 opc = 1
 print("\nGracias por utilizar la calculadora\n")
