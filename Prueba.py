#programa para resolver el problema foobar
numero=input("Digite el número ")
ultima=int(numero)%10
suma=0

tam=len(numero)
for i in range (tam):
 suma=suma+int(numero[i])
 
div3=suma%3
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

