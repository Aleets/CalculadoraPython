from email import message


def sum(num1, num2):
  return num1 + num2


def rest(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def divi(num1, num2):
  return num1 / num2

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion \n 1 - suma \n 2 - resta \n 3 - multiplicacion \n 4 - divición  \n"
    while True:
        opcion = int(input(message))
        if opcion == 5:
            print("Bye!")
        break

#if_name == 'main':
 #   print("Hola mundo!")