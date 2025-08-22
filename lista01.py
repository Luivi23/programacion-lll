print("----------------------------------")
print("lista - sumar todos ")
print("----------------------------------")
#solicita un numrro final de la lists
num1 =int (input("ingrse el numero hasta 100: "))

#crea la lista desde uno hara el $num1
lista = list(range(1, num1+1))

#calcular suma
resultado=sum(lista)

#mostrsr el resultado
print(f"la suma de la lista hasta {num1} es {resultado}.")