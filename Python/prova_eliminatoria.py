from numpy import *

"""
version- python 2.7.3
São três salas idênticas com 360 lugares
"""


#poltrona[sala,fila_letra,numero_poltrona]
poltrona = arange(1260)  #matriz dos lugares //principal
poltrona.shape = (3,21,20)
matriz_fileira = "ABCDEFGHIJKLMNOPQRSTU"


print (poltrona)

def iniciar():
    """
    Inicia todas as poltronas como vazia
    """
    global poltrona
    for sala in range(3):
        for fila_letra in range(21):
            for numero_poltrona in range(20):
                poltrona[sala,fila_letra,numero_poltrona]=0

def preencher(sala,fila_numero,numero_poltrona):
    """
    preencher os lugares do cinema
    """
    global poltrona
    if poltrona[sala,fila_numero,numero_poltrona] == 0:
        poltrona[sala,fila_numero,numero_poltrona]=1
        return 1
    else:
        print "lugar já preenchido"
        print "buscando um mais próximo"
        for i in range(20):
            if poltrona[sala,fila_numero,i]==0:
                poltrona[sala,fila_numero,i]=1
                print "preenchido na posicao %d da fileira %s " %(i+1,matriz_fileira[fila_numero])
                return 1
        print "fileira totalmente preenchida"
        return 0
        
            

print 
iniciar()

sala=1
while 1:
    print matriz_fileira
    while 1:
        sala  = int(input("numero da sala: "))
        if not sala:
            while 1:
                try:
                    print ": "
                except:
                    print "inválido"
        if 0<sala<4: break
    while 1:
        fila_letra = str(raw_input("letra da fileira: "))
        fila_letra = fila_letra.upper()
        if matriz_fileira.count(fila_letra): break
    while 1:
        numero_poltrona = int(input("numero da poltrona: "))-1
        if 0<=numero_poltrona<21 : break

    print

    fila_numero = matriz_fileira.find(fila_letra)

    print "antes: ",poltrona[sala,fila_numero,numero_poltrona]

    retorno = preencher(sala,fila_numero,numero_poltrona)
    print "depois: ",poltrona[sala,fila_numero,numero_poltrona]

    print "retorno da funcao deu " ,retorno
