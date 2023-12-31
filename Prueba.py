numero=input("Digite el número ")
ultima=int(numero)%10
suma=0

tam=len(numero)
for i in range (tam):
 suma=suma+int(numero[i])
 
div3=suma%3
if div3==0:
    print ("Foo")

div5=ultima%5
if ultima==5 or ultima==0:
    print("Bar")

if div3==0 or ultima==5 or ultima==0:
    print("Foobar")
  
if div3!=0 and ultima!=5 and ultima!=0:
    print(numero)

