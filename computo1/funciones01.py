#crea una funcion
def suma_numero(num1, num2):
    return num1 + num2

#solicitar la variable
num1 =int(input("introduzca el primer numero: "))
num2 =int(input("introduzca el segundo numero: "))

#imprimir resultado
print(f'la suma de {num1} y {num2} es {suma_numero(num1,num2)}')
