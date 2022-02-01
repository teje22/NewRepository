# -*- coding: utf-8 -*-
"""
@author: DavidCamposSerrano y Pablo Tejedor Rivadulla
"""

import random

listaNums=[[1,10,19,28,37,46],
           [2,11,20,29,38,47],
           [3,12,21,30,39,48],
           [4,13,22,31,40,49],
           [5,14,23,32,41,50],
           [6,15,24,33,42],
           [7,16,25,34,43],
           [8,17,26,35,44],
           [9,18,27,36,45],
           ]

listaEstrellas=[[1,5,9],
                [2,6,10],
                [3,7,11],
                [4,8,12],
    ]



boletoGanador=[]
boletoGanadorAux=[]
boletoGanadorNum=[]
miBoleto=[]
miBoletoAux=[]
miBoletoAuxNum=[]
aciertos=0
estrellas=0


print("Bienvenidos al sorteo de la loteria del EuroMillon del 3 de Diciembre de 2021 ")

print("\n Para participar debe elegir 5 numeros de los primeros y 2 mas de la segunda")

for i in listaNums:
    print(*i)

        
while len(miBoletoAuxNum)<5: #Hacemos con un while diciendole que mientras la longitud de la lista "miBoletoAuxNum" sea menor que 5 nos pida nos pida otro numero
    boleto=int(input("Elija 5 numeros: ")) #Creamos una variable que sea donde se guardan los valores que introducimos para que se vayan introduciendo en la lista
    if boleto not in miBoletoAuxNum and boleto >=1 and boleto <=50: #Le ponemos la condicion al bucle while de que si el numero que introducimos el cual se encuentra guardado en "boleto" no esta ya en la lista "miBoletoAuxNum" y esta comprendido entre los numeros 1 y 50 entonces pase al siguiente paso que es introducirlo en la lista 
        miBoletoAuxNum.append(boleto) #Hacemos que si cumple la condicion anterior se incluya el numero en la lista
    else:
        print("Número no valido o repetido ") #Si no se cumple las condiciones de antes entonces sale un mensaje por pantalla de numero no valido y no se introduce en la lista
        
# Creamos un bucle para que se vaya recorriendo nuestra lista de listas y cuando encuentre los números repetidos de nuestro boleto en la lista de todos los numeros y los cambie por una X
for l1 in listaNums:
    for numBoleto in miBoletoAuxNum:
            cont=0
            for e in l1:
                if(l1[cont]==numBoleto):
                    l1[cont]=" X"
                cont+=1
print("Los números que ha elegido se han borrado de su lista")
# Volvemos a mostrar la lista de los números pero esta vez con las X añadidas
for i in listaNums:
    print(*i)
                
            
print("Vamos a elegir ahora las estrellas")
for i in listaEstrellas:
    print(*i)

while len(miBoletoAux)<2: #Le decimos que mientras la longitud de la lista "miBoletoAux" sea menor que 5 nos pida nos pida otro numero
    boletoAux=int(input("Elija 2 estrellitas: ")) #Creamos variable para que guarde las estrellas
    if boletoAux not in miBoletoAux and boletoAux >=1 and boletoAux <=12: #Le ponemos las condiciones igual que anteriormente pero ahora entre el 1 y el 12 en vez de entre el el 1 y el 50
        miBoletoAux.append(boletoAux)
    else:
        print("Estrella no valida o repetida ")
        
# Cambiamos las estrellas elegidas por X como anteriormente en los números.
for e1 in listaEstrellas:
    for estBoleto in miBoletoAux:
            cont=0
            for e in e1:
                if(e1[cont]==estBoleto):
                    e1[cont]="X"
                cont+=1

# Mostramos las estrellas con las X
for i in listaEstrellas:
    print(*i)
        
miBoletoAuxNum.sort() #Ordenamos la lista de los 5 numeros que hemos elegido
miBoletoAux.sort() #Ordenamos la lista de las 2 estrellas que tenemos
miBoleto=[miBoletoAuxNum]+[miBoletoAux]  #----->Lo que hacemos es juntar las dos listas para que se nos cree una misma lista que sera nuestro boleto para jugar en el sorteo

print(f"El número que has elegido para participar en el sorteo es: {miBoleto}")

while len(boletoGanadorNum)<5:
    boletoRandom=random.randint(1, 50) #Creamos una variable en la que nos guarde un numero que se ha generado de forma aleatoria entre el 1 y el 50
    if boletoRandom not in boletoGanadorNum and boletoRandom >=1 and boletoRandom <=50:
        boletoGanadorNum.append(boletoRandom)
        
while len(boletoGanadorAux)<2:
    boletoRandomAux=random.randint(1, 12)
    if boletoRandomAux not in boletoGanadorAux and boletoRandomAux >=1 and boletoRandomAux <=12:
        boletoGanadorAux.append(boletoRandomAux)
      
boletoGanadorNum.sort() #Ordenamos la lista de los 5 numeros que se han generado
boletoGanadorAux.sort() #Ordenamos la lista de los 2 numeros que se han generado  
boletoGanador=[boletoGanadorNum]+[boletoGanadorAux] #Jumtamos las dos listas para tener un boleto ganador

