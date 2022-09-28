from email import message
from unittest import result


def sum(num1, num2):
  return num1 + num2


def rest(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def divi(num1, num2):
  return num1 / num2

def return_values():
  num1 = int(input("Ingresa tu primer valor: "))
  num2 = int(input("Ingresa tu sugundo valor: "))
  return 

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion \n 1 - suma \n 2 - resta \n 3 - multiplicacion \n 4 - divición  \n"
    while True:
      opcion = int(input(message))
      if opcion ==1:
        result_sum = sum (23, 54)
        print("El resultado de la suma es: ", result_sum)
      elif opcion ==2:
        result_rest = rest(23, 54)
        print("El resultado de la resta es: ", result_rest)
      if opcion ==3:
        result_multi = multiplication(23, 54)
        print("El resultado de la multiplicacion es: ",result_multi)
      if opcion == 4:
        result_div = divi(23, 54)
        print("El resultado de la divicion es: ",result_div)
      if opcion == 5:
        print("Bye!")
        break
      else:
        print("Opcion incorrecta!!!")

#if_name == 'main':
 #   print("Hola mundo!")