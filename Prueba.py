#programa para resolver el problema foobar
numero=input("Digite el número ") #Se solicita la digitación del número a comprobar y se obtiene la cantidad de digitos del numero ingresado
ultima=int(numero)%10
suma=0

tam=len(numero) #Se calcula la longitud del numero y se emplea el bucle for para efectuar la sumatoria 
for i in range (tam): 
 suma=suma+int(numero[i])
 
div3=suma%3 #Se realiza validación con las condicionales correspondientes para realizar el proceso
div5=ultima%5
if div3==0 and ultima==0 or ultima==5:
    print("Foobar")
else:
 if div3==0:
    print ("Foo")
 else:
  if ultima==5 or ultima==0:
    print("Bar")

if div3!=0 and ultima!=5 and ultima!=0:
    print(numero)

