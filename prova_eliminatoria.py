from numpy import *

"""
version- python 2.7.3
gean felipe, agosto 2014
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
    caso haja lugar já ocupado para a poltrona do usuário
    a funcao preenche num lugar mais próximo na fileira
    caso não haja poltronas vazias na fileira o retorno é 0zero
    """
    global poltrona
    #posicao 0 para poltrona mais próxima ascendente/depois da escolhida
    #posicao 1 para poltrona mais próxima descendente/antes da escolhida
    poltrona_mais_proxima= [0,0]
    
    if poltrona[sala,fila_numero,numero_poltrona] == 0:
        poltrona[sala,fila_numero,numero_poltrona]=1
        return 1
    else:
        print "%%lugar já preenchido"
        if fila_numero<5: #se fileira é de A a E
            for i in range(numero_poltrona,8): # da posicao ocupada escolhida pelo usuário até a 8, que na verdade é 7 -> 0 a 7
                if poltrona[sala,fila_numero,i]==0:
                   poltrona_mais_proxima[0]=i
                   break
            for i in range(numero_poltrona,-1,-1): # da posicao ocupada escolhida pelo usuário até a 0
                if poltrona[sala,fila_numero,i]==0:
                   poltrona_mais_proxima[1]=i
                   break
        else:  # se a fileira é de F em diante
            for i in range(numero_poltrona,20): # da posicao ocupada escolhida pelo usuário até a 8, que na verdade é 7 -> 0 a 7
                if poltrona[sala,fila_numero,i]==0:
                   poltrona_mais_proxima[0]=i
                   break
            for i in range(numero_poltrona,-1,-1): # da posicao ocupada escolhida pelo usuário até a 0
                if poltrona[sala,fila_numero,i]==0:
                   poltrona_mais_proxima[1]=i
                   break

        if poltrona_mais_proxima[0]==0 and poltrona_mais_proxima[1]==0:
            print 'nao há poltronas disponiveis mais nesta fileira'
            return 0

        if poltrona_mais_proxima[0]==0 and poltrona_mais_proxima[1]:
            poltrona[sala,fila_numero,poltrona_mais_proxima[1]]=1
            print 'preenchido na poltrona mais próxima posição %d\nmatriz(%d,%d,%d) ' %(poltrona_mais_proxima[1]+1,sala,fila_numero,poltrona_mais_proxima[1])
            return 1

        if poltrona_mais_proxima[1]==0 and poltrona_mais_proxima[0]:
            poltrona[sala,fila_numero,poltrona_mais_proxima[0]]=1
            print 'preenchido na poltrona mais próxima posição %d\nmatriz(%d,%d,%d) ' %(poltrona_mais_proxima[0]+1,sala,fila_numero,poltrona_mais_proxima[0])
            return 1
        
        if poltrona_mais_proxima[0] and poltrona_mais_proxima[1]:
            lugar_mais_proximo_antes, lugar_mais_proximo_depois = numero_poltrona - poltrona_mais_proxima[1], poltrona_mais_proxima[0]-numero_poltrona

            if lugar_mais_proximo_antes > lugar_mais_proximo_depois:
                poltrona[sala,fila_numero,poltrona_mais_proxima[1]]=1
                print 'preenchido na poltrona mais próxima posição %d\nmatriz(%d,%d,%d) ' %(poltrona_mais_proxima[1]+1,sala,fila_numero,poltrona_mais_proxima[1])
                return 1

            elif lugar_mais_proximo_depois > lugar_mais_proximo_antes:
                poltrona[sala,fila_numero,poltrona_mais_proxima[0]]=1
                print 'preenchido na poltrona mais próxima posição %d\nmatriz(%d,%d,%d) ' %(poltrona_mais_proxima[0]+1,sala,fila_numero,poltrona_mais_proxima[0])
                return 1
            
            #caso os dois valores sejam iguais (poltrona_mais_proxima[0]==poltrona_mais_proxima[1]) entao preencha na poltrona mais
            #proxima seguinte
            else:
                poltrona[sala,fila_numero,poltrona_mais_proxima[0]]=1
                print 'preenchido na poltrona mais próxima posição %d\nmatriz(%d,%d,%d)' %(poltrona_mais_proxima[0]+1,sala,fila_numero,poltrona_mais_proxima[0])
                return 1
                
        
            
def relatorioDasSalas():
    """
    relatório indicando qual a sala mais cheia do momento, qual a
    sala completamente lotada e qual a sala que mais possui
    poltronas sobrando nas três ultimas fileiras
    """
    global poltrona
    sala1,sala2,sala3 = 0,0,0
    for fileira in range(21):
        for cadeiras in range(20):
            if poltrona[0,fileira,cadeiras]==0:
                sala1+=1
            if poltrona[1,fileira,cadeiras]==0:
                sala2+=1
            if poltrona[2,fileira,cadeiras]==0:
                sala3+=1
    print '|%d|%d|%d|' %(sala1,sala2,sala3)

    
    #relatório indicando qual a sala mais cheia do momento, qual a sala completamente lotada
    
    if sala1==0:
        print 'sala 1 completamente lotada'
        if sala2<sala3:
            print 'sala 2 mais cheia que sala 3 (%d)' %sala2
        elif sala3<sala2:
            print 'sala 3 mais cheia que sala 2 (%d)' %sala3
        else: print 'sala 2 e 3 com o mesmo número de lotação (%d)' %sala2
    
    elif sala2==0:
        print 'sala 2 completamente lotada'
        if sala1<sala3:
            print 'sala 1 mais cheia que sala 3 (%d)' %sala1
        elif sala3<sala1:
            print 'sala 3 mais cheia que sala 1 (%d)' %sala3
        else: print 'sala 1 e 3 com o mesmo número de lotação (%d)' %sala3
            
        
    elif sala3==0:
        print 'sala 3 completamente lotada'
        if sala2<sala1:
            print 'sala 2 mais cheia que sala 1 (%d)' %sala2
        elif sala1<sala2:
            print 'sala 1 mais cheia que sala 2 (%d)' %sala1
        else: print 'sala 1 e 2 com o mesmo número de lotação (%d)' %sala2
    else:
        if sala1<sala2<sala3 or sala1<sala3<sala2 or sala1<sala3==sala2:
            print 'sala 1 mais cheia (%d)' %sala1
        elif sala3<sala2<sala1 or sala3<sala1<sala2 or sala3<sala1==sala2:
            print 'sala 3 mais cheia (%d)' %sala3
        elif sala2<sala1<sala3 or sala2<sala3<sala1 or sala2<sala1==sala3:
            print 'sala 2 mais cheia (%d)' %sala2
        elif sala1==sala2<sala3:
            print 'sala 1 e sala 2 mais cheia que sala 3 (%d)' %sala1
        elif sala1==sala3<sala2:
            print 'sala 1 e sala 3 mais cheia que sala 2 (%d)' %sala1
        elif sala2==sala3<sala1:
            print 'sala 2 e sala 3 mais cheia que sala 1 (%d)' %sala2
        else :
            print 'mesmo número de lotação nas salas (%d)' %sala1

    #qual a sala que mais possui poltronas sobrando nas três ultimas fileiras
    sala1,sala2,sala3 = 0,0,0
    for fileira in range(3):
        for lugar in range(20):
            if poltrona[0,18+fileira,lugar]==0:
                sala1 +=1
            if poltrona[1,18+fileira,lugar]==0:
                sala2 +=1
            if poltrona[2,18+fileira,lugar]==0:
                sala3 +=1
    print '|%d|%d|%d|' %(sala1,sala2,sala3)
    if sala1>sala2>sala3 or sala1>sala3>sala2 or sala1>sala3==sala2:
        print 'sala 1 possui mais poltronas sobrando nas 3 ultimas fileiras (%d)' %sala1
    elif sala3>sala2>sala1 or sala3>sala1>sala2 or sala3>sala1==sala2:
        print 'sala 3 possui mais poltronas sobrando nas 3 ultimas fileiras (%d)' %sala3
    elif sala2>sala1>sala3 or sala2>sala3>sala1 or sala2>sala1==sala3:
        print 'sala 2 possui mais poltronas sobrando nas 3 ultimas fileiras (%d)' %sala2
    elif sala1==sala2>sala3:
        print 'sala 1 e 2 possui mais poltronas igualmente sobrando nas 3 ultimas fileiras (%d)' %sala2
    elif sala1==sala3>sala2:
        print 'sala 1 e 3 possui mais poltronas igualmente sobrando nas 3 ultimas fileiras (%d)' %sala1
    elif sala2==sala3>sala1:
        print 'sala 2 e 3 possui mais poltronas igualmente sobrando nas 3 ultimas fileiras (%d)' %sala2
    else : print 'todas com mesma lotação nas 3 ultimas fileiras (%d)' %sala1



iniciar()
while 1:
    print
    print 'A) comprar ingressso'
    print 'B) relatório das salas'
    print 'C) imprimir salas'
    print 'D) especifique [sala,fileira,poltrona] para imprimir'
    print 'E) preencher sala 1'
    print 'Q) sair'  
    opcao = str(raw_input(": "))

    opcao = opcao.upper()

    if opcao=='A':
        print 'escolha o lugar'
        while 1:
            try:
                sala  = int(input("numero da sala: "))
                if 0<sala<4 or sala==10: break
                else: print '#não existe'
            except:
                print "#inválido"
        
        while 1:
            fila_letra = str(raw_input("letra da fileira: "))
            fila_letra = fila_letra.upper()
            if not fila_letra:
                print '#inválido'
            else:
                if matriz_fileira.count(fila_letra): break
                else : print '#não existe'
        while 1:
            posicoes_restringida='ABCDE'  #fileiras que possuem apenas poltronas de 1 a 8
            try:
                
                numero_poltrona = int(input("numero da poltrona: "))
                if posicoes_restringida.count(fila_letra):  # se a letra inserida no loop acima existir na matriz posicoes_restringidas entao só poltronas só podem ser de 1 a 9
                    if 0<numero_poltrona<9: break
                    else: print '#fileira %s poltronas apenas de 1 a 8' %fila_letra
                else:
                    if 0<numero_poltrona<21 : break
                    else: print '#não existe'
            except:
                print '#inválido'

        print

        fila_numero = matriz_fileira.find(fila_letra)#saber a posicao do caracter digitado pelo usuário dentro da matriz

        sala = sala -1 #posicao da matriz [0 a 2]
        numero_poltrona = numero_poltrona -1 #posicao da matriz [0 a 19]
        print ("matriz(%d,%s,%d) %d" %(sala,fila_numero,numero_poltrona, poltrona[sala,fila_numero,numero_poltrona]))
        print "antes: ",poltrona[sala,fila_numero,numero_poltrona]

        retorno = preencher(sala,fila_numero,numero_poltrona)
        print "depois: ",poltrona[sala,fila_numero,numero_poltrona]

        print "retorno da funcao deu " ,retorno

    if opcao == 'B':
        relatorioDasSalas()
        
    if opcao=='C':
        print poltrona
        print

    if opcao=='D':
        while 1:
            try:
                sala  = int(input("numero da sala: "))
                if 0<sala<4 or sala==10: break
                else: print '#não existe'
            except:
                print "#inválido"
        while 1:
            fila_letra = str(raw_input("letra da fileira: "))
            fila_letra = fila_letra.upper()
            if not fila_letra:
                print '#inválido'
            else:
                if matriz_fileira.count(fila_letra): break
                else : print '#não existe'
        while 1:
            posicoes_restringida='ABCDE'  #fileiras que possuem apenas poltronas de 1 a 8
            try:
                
                numero_poltrona = int(input("numero da poltrona: "))
                if posicoes_restringida.count(fila_letra):  # se a letra inserida no loop acima existir na matriz posicoes_restringidas entao só poltronas só podem ser de 1 a 9
                    if 0<numero_poltrona<9: break
                    else: print '#fileira %s poltronas apenas de 1 a 8' %fila_letra
                else:
                    if 0<numero_poltrona<21 : break
                    else: print '#não existe'
            except:
                print '#inválido'
        
        fila_numero = matriz_fileira.find(fila_letra)#saber a posicao do caracter digitado pelo usuário dentro da matriz
        print 'poltrona[%d,%d,%d] = %d' %(sala,fila_numero,numero_poltrona,poltrona[sala-1,fila_numero,numero_poltrona-1])
    
    if opcao=='E':
        global poltrona
        for i in range(21):
            for j in range(20):
                poltrona[0,i,j]=1
    
    if opcao =='Q':
        print 'sair'
        break
