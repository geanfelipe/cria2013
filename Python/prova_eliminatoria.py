from numpy import *

"""
version- python 2.7.3
São três salas idênticas com 360 lugares
"""


#poltrona[sala,fila_letra,numero_poltrona]
poltrona = arange(1260)  #matriz dos lugares //principal
poltrona.shape = (3,21,20)
matriz_fileira = "ABCDEFGHIJKLMNOPQRSTU"


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
        for i in range(20):
            if poltrona[sala,fila_numero,i]==0:
                poltrona[sala,fila_numero,i]=1
                print "preenchido na posicao %d da fileira %s " %(i+1,matriz_fileira[fila_numero])
                return 1
        print "fileira totalmente preenchida"
        return 0
        
            

print 
iniciar()

while 1:
    print 'A) comprar ingressso'
    print 'Q) sair'  
    opcao = str(raw_input(": "))

    opcao = opcao.upper()

    if opcao=='A':
        print 'escolha o lugar'
        while 1:
            try:
                sala  = int(input("numero da sala: "))
                if 0<sala<4: break
                else: print 'não existe'
            except:
                print "inválido"
            
        while 1:
            fila_letra = str(raw_input("letra da fileira: "))
            fila_letra = fila_letra.upper()
            if not fila_letra:
                print 'inválido'
            else:
                if matriz_fileira.count(fila_letra): break
                else : print 'não existe'
        while 1:
            try:
                numero_poltrona = int(input("numero da poltrona: "))
                if 0<numero_poltrona<21 : break
                else: print 'não existe'
            except:
                print 'inválido'

        print

        fila_numero = matriz_fileira.find(fila_letra)#saber a posicao do caracter digitado pelo usuário dentro da matriz

        sala = sala -1 #posicao da matriz [0 a 2]
        numero_poltrona = numero_poltrona -1 #posicao da matriz [0 a 19]
        print ("matriz(%d,%s,%d) %d" %(sala,fila_numero,numero_poltrona, poltrona[sala,fila_numero,numero_poltrona]))
        print "antes: ",poltrona[sala,fila_numero,numero_poltrona]

        retorno = preencher(sala,fila_numero,numero_poltrona)
        print "depois: ",poltrona[sala,fila_numero,numero_poltrona]

        print "retorno da funcao deu " ,retorno
        
    if opcao =='Q':
        print 'sair'
        break
