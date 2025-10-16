from os import system
#no es mucho pero es trabajo humilde
print('"hola mundo"',"jose","MANOLO",sep="\n")
'''
JOSE
MARIA
PEREZ
'''
print('"hola mundo"',"jose","MANOLO",sep="\n")

#lista imnutable
tuple=(1,2,3,4,5)
print(tuple)
lista=[1,2,3,4,5]
print(lista)
for elemento in lista:
    print(elemento,end=", ")
print()
#lista que no acepte repetidos
conjunto={1,2,3,4,5,5,5,5}
print(conjunto)
#bucle con una simple condicion

contador= 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
    print("fin del bucle")
    
#iterar una lista
fruta=["manzana","pera","platano"]
for fruta in fruta:
    print(fruta)
    print(fruta[0]>fruta[1])
    
#bucle anidado
letras=["a","b","c"]
numeros=[1,2,3]
for letra in letras:
    for numero in numeros:
        print(f" {letra}{numero} ")