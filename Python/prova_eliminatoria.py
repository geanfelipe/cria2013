from numpy import *

"""
version- python 2.7.3
São três salas idênticas com 360 lugares
"""


#poltrona[sala,fila_letra,numero_poltrona]
poltrona = arange(1260)  #matriz dos lugares //principal
poltrona.shape = (3,21,20)

print (poltrona)

def iniciar():
    """
    Inicia todas as poltronas como vazia
    """
    global poltrona
    for sala in range(3):
        for fila_letra in range(21):
            for numero_poltrona in range(20):
                poltrona[sala,fila_letra,numero_poltrona]='0'

print 
iniciar()
print (poltrona)

sala  = int(input("numero da sala: "))
fila_letra = str(input("letra da fileira: "))
numero_poltrona = int(input("numero da poltrona: "))

print (sala, fila_letra, numero_poltrona)
