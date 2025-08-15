n1 =float(input("ingrese el primer numero: "))
n2 =float(input("ingrese el segundo numero: "))

operacion =(input("ingrese la operacion,suma, resta, multi, divi: "))

if operacion == "suma" :
    print(": ",n1 + n2)
elif operacion == "resta":
    print(": ",n1 - n2)
elif operacion == "divi":
    print(": ",n1 % n2 )
elif operacion == "multi":
    print(": ",n1 * n2)
else:
    print("no existe en mi codigo")
