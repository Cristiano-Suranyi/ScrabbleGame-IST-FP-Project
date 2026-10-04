#projeto


alfabeto = ['A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O', 'P','Q','R','S','T','U','V','X','Z']



def cria_conjunto(tletras,tnumeros):
    """
    cria_conjunto: tuplo x tuplo → conjunto letras
    Recebe dois tuplos de igual tamanho contendo letras únicas e suas ocorrências,
    devolvendo um conjunto de letras (dicionário).
    Gera erro 'cria_conjunto: argumentos inválidos' se argumentos forem inválidos.
    """

    if not(isinstance(tletras,tuple)and isinstance(tnumeros,tuple)and len(tletras)==len(tnumeros)):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
    conjunto={}
    
    for i in range(len(tletras)):

        if not(tletras[i]in alfabeto and isinstance(tnumeros[i],int) and tnumeros[i]>0):
            raise ValueError("cria_conjunto: argumentos inválidos")
        
        if tletras[i] in conjunto:
            raise ValueError("cria_conjunto: argumentos inválidos")

        conjunto[tletras[i]]=tnumeros[i]
    
    return conjunto





def gera_numero_aleatorio(estado):
    """
    gera_numero_aleatorio: inteiro → inteiro
    Recebe um inteiro positivo e devolve um número pseudoaleatório usando
    o gerador xorshift de 32 bits.
    """

    if not(isinstance(estado,int) and estado>0):
        raise ValueError("Argumento inválido")
    
    estado ^= ( estado << 13 ) & 0xFFFFFFFF
    estado ^= ( estado >> 17 ) & 0xFFFFFFFF
    estado ^= ( estado << 5 ) & 0xFFFFFFFF

    return estado 




def permuta_letras(letras1,estado):
    """
    permuta_letras: lista x inteiro → {}
    
    Recebe uma lista de letras e um inteiro positivo, modificando destrutivamente
    a lista com os seus elementos permutados.
    """
    n=len(letras1)
    i=n-1
    
    while i>=1:
        estado=gera_numero_aleatorio(estado)
        j=estado%(i+1)                              #O operador % sempre retorna um valor entre 0 
        letras1[j],letras1[i]=letras1[i],letras1[j] #(inclusive) e i(exclusive),daí a soma de (i+1)
        i-=1
    
    

def ordena(conj):
    """
    ordena: conjunto letras → lista
    
    Função auxiliar que devolve lista ordenada com todas as letras do conjunto,
    respeitando a ordem do alfabeto português.
    """
    lista=[]
    for letra in alfabeto:
        if letra in conj:
            lista+=[letra]*conj[letra]
    return lista


def baralha_conjunto(conj,estado):
    """
    baralha_conjunto: conjunto letras x inteiro → lista
    
    Recebe um conjunto de letras e um inteiro positivo, devolvendo lista baralhada
    com todas as letras. Não altera o conjunto original.
    """
    conj=ordena(conj)
    permuta_letras(conj,estado) 
    return conj



def testa_palavra_padrao(palavra,padrao,conj):
    """
    testa_palavra_padrao: cad. carateres x cad. carateres x conjunto letras → booleano
    
    Recebe palavra, padrão (letras e '.') e conjunto de letras. Devolve True se for
    possível formar a palavra substituindo '.' por letras do conjunto, False caso contrário.
    Não modifica os argumentos.
    """

    if len(palavra)!=len(padrao):
        return False
    
    letras_usadas={}

    for i in range(len(padrao)):
        letra = palavra[i]
        simbolo = padrao[i]

        if simbolo ==".":
            if letra not in conj:
                return False
            letras_usadas[letra] = letras_usadas.get(letra, 0) + 1
        elif simbolo in alfabeto:
            if letra != simbolo:
                return False
        else:
            return False
        
    for letra, quantidade in letras_usadas.items():
        if quantidade > conj[letra]:
            return False

    return True




def cria_tabuleiro():
    """
    cria_tabuleiro: {} → tabuleiro
    
    Devolve um tabuleiro vazio (lista de 15 listas com 15 elementos '.' cada).
    """
    i=0
    i2=0
    lista=[]

    while i<15:
        lista.append([])
        while i2<15:
            lista[i].append('.')
            i2+=1
        i2=0
        i+=1

    return lista




def cria_casa(l,c):
    """
    cria_casa: inteiro x inteiro → casa
    
    Recebe linha e coluna (1-15) e devolve casa do tabuleiro (tuplo).
    Gera erro 'cria_casa: argumentos inválidos' se argumentos forem inválidos.
    """
    if not(isinstance(l, int) and isinstance(c, int)):
        raise ValueError("cria_casa: argumentos inválidos")
    if not( 1<= l <=15 and 1<= c <=15 ):
        raise ValueError("cria_casa: argumentos inválidos")
    return (l,c)




def obtem_valor(tab,casa):
    """
    obtem_valor: tabuleiro x casa → cad. carateres
    
    Recebe tabuleiro e casa, devolvendo o valor contido nessa casa.
    """

    l=casa[0]
    c=casa[1]

    return tab[l-1][c-1]



def insere_letra(tab,casa,letra):
    """
    insere_letra: tabuleiro x casa x cad. carateres → tabuleiro
    
    Recebe tabuleiro, casa e letra, inserindo a letra na casa indicada
    e modificando destrutivamente o tabuleiro.
    """

    l=casa[0]-1
    c=casa[1]-1
    tab[l][c]=letra

    return tab



def obtem_sequencia(tab,casa,direcao,tamanho):
    """
    obtem_sequencia: tabuleiro x casa x cad. carateres x inteiro → cad. carateres
    
    Recebe tabuleiro, casa, direção ('H' ou 'V') e tamanho, devolvendo cadeia
    de caracteres formada pelos valores nas casas a partir da casa na direção indicada.
    """

    t=0
    frase=""

    if direcao=="H":
        while t<tamanho:
            if casa[1] + t > 15:
                break
            frase+=obtem_valor(tab,(casa[0],casa[1]+t))
            t+=1
    t=0

    if direcao=="V":
        while t<tamanho:
            if casa[0] + t > 15:
                break
            frase+=obtem_valor(tab,(casa[0]+t,casa[1]))
            t+=1

    return frase




def insere_palavra(tab,casa,direcao,palavra):
    """
    insere_palavra: tabuleiro x casa x cad. carateres x cad. carateres → tabuleiro
    
    Recebe tabuleiro, casa, direção ('H' ou 'V') e palavra, inserindo-a letra a letra inicialmente na casa indidicada e nas sucessivas,
    e direção indicadas, modificando destrutivamente o tabuleiro.
    """

    t=0

    if direcao=="H":
        while t<len(palavra):
            insere_letra(tab,(casa[0],casa[1]+t),palavra[t])
            t+=1
        
    t=0

    if direcao=="V":
        while t<len(palavra):
            insere_letra(tab,(casa[0]+t,casa[1]),palavra[t])
            t+=1

    return tab



def tabuleiro_para_str(tab):
    """
    tabuleiro_para_str: tabuleiro → cad. carateres
    
    Recebe tabuleiro e devolve cadeia de caracteres com sua representação externa.
    """
    linha = ""
    linha += "                       1 1 1 1 1 1\n"
    linha += "     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n"
    linha += "   +-------------------------------+\n"

    i2=0
    letra=""

    for i in range(1,16):
        while i2<15:
            letra+=" "+str(tab[i-1][i2])
            i2+=1
        i2=0
        linha+= str(i).rjust(2)+" |"+letra+" |\n"
        letra=""

    linha += "   +-------------------------------+"

    return linha



def cria_jogador(ordem,pontos,conj_letras):
    """
    cria_jogador: inteiro x inteiro x conjunto letras → jogador
    
    Recebe ordem do jogador (1-4), pontos iniciais e conjunto de letras,
    devolvendo jogador (dicionário com 'id', 'pontos' e 'letras').
    Gera erro 'cria_jogador: argumentos inválidos' se argumentos forem inválidos.
    """
    
    if not(isinstance(ordem, int) and isinstance(pontos, int) and isinstance(conj_letras, dict)):
        raise ValueError("cria_jogador: argumentos inválidos")
    if not(0<ordem<=4 and pontos>=0 and 0<=len(conj_letras)<=7):
        raise ValueError("cria_jogador: argumentos inválidos")
    for letra in conj_letras.keys():
        if not isinstance(letra, str) or letra not in alfabeto or len(letra) != 1:
            raise ValueError("cria_jogador: argumentos inválidos")
    for valor in conj_letras.values():
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("cria_jogador: argumentos inválidos")
        
    toltal_de_letras=sum(conj_letras.values())
    if toltal_de_letras>7:
        raise ValueError("cria_jogador: argumentos inválidos")
    
    
    dicio={"id":ordem,"pontos":pontos,"letras":conj_letras}
    return dicio



def jogador_para_str(jog):
    """
    jogador_para_str: jogador → cad. carateres
    
    Recebe jogador e devolve cadeia de caracteres com sua representação externa.
    Letras são mostradas ordenadas alfabeticamente.
    """
    valores = [x for x in jog.values()]
    
    conjdeletras = ""
    for letra in ordena(valores[2]):
        conjdeletras += " " + letra

    frase = "#" + str(valores[0]) + " (" + str(valores[1]).rjust(3) + "):" + conjdeletras
    return frase

def distribui_letra(letras,jogador):
    """
    distribui_letra: lista x jogador → booleano
    
    Recebe lista de letras e jogador. Retira última letra da lista acrescentando-a
    ao conjunto do jogador e devolve True, ou devolve False se lista vazia.
    Modifica destrutivamente lista e jogador.
    """

    if len(letras)==0:
        return False
    
    if letras[-1] in jogador["letras"]:
        jogador["letras"][letras[-1]]+=1
        del letras[-1]
    else:
        jogador["letras"][letras[-1]]=1
        del letras[-1]

    return True


def joga_palavra(tab,palavra,casa,direcao,con_letras,primeira):
    """
    joga_palavra: tabuleiro x palavra x casa x cad. carateres x conjunto letras x booleano → tuplo
    
    Recebe tabuleiro, palavra, casa, direção, conjunto de letras e booleano (primeira jogada).
    Se possível formar palavra com letras do conjunto e jogada válida, insere palavra no
    tabuleiro e devolve tuplo com letras utilizadas ordenadas. Caso contrário devolve tuplo vazio.
    Não altera conjunto de letras.
    """
    
    l=[x for x in palavra]
    casa_central=(8,8)
    
    passa_casa_central=0
    tuplo=()
    letras_usadas=[]
    

    if direcao == "H" and casa[1] -1 + len(palavra) > 15:
        return tuplo
    if direcao == "V" and casa[0] -1 + len(palavra) > 15:
        return tuplo

    if primeira==True:
        if len(palavra)>=2:
            
            letras_necessarias = {}     #verifica se as letras da palavra pertencem ao conjunto e o nº de letras repetidas não excede a quantidade
            for letra in l:             #  de ocorrencias definida pelo o conjunto
                letras_necessarias[letra] = letras_necessarias.get(letra, 0) + 1
            
            for letra, oco in letras_necessarias.items():
                if letra not in con_letras or con_letras[letra] < oco:
                    return tuplo
                
            for i in range(len(palavra)): 
                if direcao=="H":
                    if (casa[0],casa[1]+i)==casa_central:
                        passa_casa_central=1
                if direcao=="V":
                    if (casa[0]+i,casa[1])==casa_central:
                        passa_casa_central=1
                        
            if passa_casa_central==1:
                for letra in l:
                    letras_usadas.append(letra)
                insere_palavra(tab,casa,direcao,palavra)
                tuplo = tuple(sorted(letras_usadas))
                return tuplo
            else:
                return tuplo 
        else:
            return tuplo
    
    padrao=obtem_sequencia(tab,casa,direcao,len(palavra))
    
    if primeira==False:
        if len(palavra)>=1:

            toca_letra_existente = 0 
            tem_letra_nova = 0              #verifica se toca pelo menos uma letra já no tabuleiro e se a letra do tabueiro é igual a
            for i in range(len(palavra)):   #letra da palavra que vai ser inserida
                if direcao == "H":        
                    if tab[casa[0]-1][casa[1]+i-1] != ".":
                        toca_letra_existente = 1
                        if tab[casa[0]-1][casa[1]+i-1]  != palavra[i]:
                            return tuplo
                    else:
                        tem_letra_nova = 1
                if direcao == "V":
                    if tab[casa[0]+i-1][casa[1]-1] != ".":
                        toca_letra_existente = 1
                        if tab[casa[0]+i-1][casa[1]-1] != palavra[i]:
                            return tuplo
                    else:
                        tem_letra_nova = 1
            
            if toca_letra_existente == 0 or tem_letra_nova == 0:
                return tuplo

            if not testa_palavra_padrao(palavra, padrao, con_letras):
                return tuplo
            
            for i in range(len(palavra)):
                if direcao=="H":
                    if tab[casa[0]-1][casa[1]+i-1] == ".":
                        letras_usadas.append(palavra[i])
                        insere_letra(tab,(casa[0],casa[1]+i),palavra[i])

                if direcao=="V":
                    if tab[casa[0]+i-1][casa[1]-1] == ".":
                        letras_usadas.append(palavra[i])
                        insere_letra(tab,(casa[0]+i,casa[1]),palavra[i])
                
            tuplo = tuple(sorted(letras_usadas))
            return tuplo
        else:
            return tuplo
    else:
        return tuplo



def processa_jogada(tab,jog,pilha,pontos,primeira):
        """
    processa_jogada: tabuleiro x jogador x lista x dicionário x booleano → booleano
    
    Recebe tabuleiro, jogador, lista de letras, dicionário de pontos e booleano (primeira jogada).
    Processa turno completo do jogador, repetindo mensagem até jogada válida.
    Aceita: 'P' (passar), 'T <letras>' (trocar), 'J <l> <c> <dir> <palavra>' (jogar).
    Devolve False se passar, True caso contrário.
    """
        
        while True:
            jogada = input(f"Jogada J{jog['id']}: ")
            
            if jogada == '':
                continue
            
            jogada=jogada.split()

            if len(jogada) == 0:
                continue
        
            if jogada[0]=="P":
                return False

            elif jogada[0]=="T":
                if not(len(pilha)>=7):
                    continue
                
                letras_a_trocar = jogada[1:]
                if len(letras_a_trocar) == 0:
                    continue
                    
                contagem_troca = {}
                for letra in letras_a_trocar:
                    contagem_troca[letra] = contagem_troca.get(letra, 0) + 1
            
                pode_trocar=True  #verifica se o jogador tem as letras solicitadas e suas respetivas quantidades para a troca
                for letra, qtd in contagem_troca.items():
                    if letra not in jog["letras"] or jog["letras"][letra] < qtd:
                        pode_trocar=False
                        break
                
                if not pode_trocar:
                    continue
            
                for letra in letras_a_trocar: #retira letras do jog
                    jog["letras"][letra] -= 1
                    if jog["letras"][letra] == 0:
                        del jog["letras"][letra]
        
                for i in range(len(letras_a_trocar)): #adiciona letras do jog
                    if len(pilha) > 0:
                        nova_letra = pilha.pop()  
                        if nova_letra in jog["letras"]:
                            jog["letras"][nova_letra] += 1
                        else:
                            jog["letras"][nova_letra] = 1
                return  True

            elif jogada[0]=="J"and len(jogada)>=5:
                            
                casa=cria_casa(int(jogada[1]),int(jogada[2]))
                if not casa:
                    continue
                
                l = jogada[1]
                c = jogada[2]
                if not (l.isdigit() and c.isdigit()):
                    continue
                l = int(l)
                c = int(c)
                if not (1 <= l <= 15 and 1 <= c <= 15):
                    continue
                if jogada[3] not in ("H", "V"):
                    continue
                
                direcao=jogada[3]
                palavra=""
                
                for l in jogada[4:]:
                    palavra+=l
                palavra=palavra.upper()
                    
                tuplo_letras = joga_palavra(tab,palavra,casa,direcao,jog["letras"],primeira)
                if tuplo_letras==():
                    continue
                            
                for letra in tuplo_letras:
                    jog["letras"][letra] -= 1
                    if jog["letras"][letra] == 0:
                        del jog["letras"][letra]
                            
                pontos_totais = 0 
                for letra in palavra: 
                    if letra in pontos:
                        pontos_totais += pontos[letra] 
                jog["pontos"] += pontos_totais
    
                for i in range(len(tuplo_letras)):
                    if len(pilha) > 0:
                        distribui_letra(pilha, jog)
                            
                return True
            else:
                continue
            
            
    
def scrabble(jogadores,saco,pontos,seed):
    """
    scrabble: inteiro x conjunto letras x dicionário x inteiro → tuplo
    
    Função principal para jogar Scrabble completo de 2-4 jogadores.
    Recebe número de jogadores, conjunto de letras do saco, dicionário de pontos
    e seed para gerador aleatório. Devolve tuplo com pontuação final de cada jogador.
    Gera erro 'scrabble: argumentos inválidos' se argumentos forem inválidos.
    Jogo termina quando todos passam consecutivamente ou jogador esgota letras com saco vazio.
    """
    
    if not(isinstance(jogadores,int)and isinstance(saco,dict)and isinstance(pontos,dict)and isinstance(seed,int)):
        raise ValueError('scrabble: argumentos inválidos')

    if not(2 <= jogadores <= 4 and seed > 0 and len(saco) > 0):
        raise ValueError('scrabble: argumentos inválidos')
    
    if len(pontos) != len(alfabeto):
        raise ValueError('scrabble: argumentos inválidos')
    
    for key in pontos.keys():
        if key not in alfabeto:
            raise ValueError('scrabble: argumentos inválidos')
        
    for key in pontos.keys():
        if not isinstance(pontos[key], int) or pontos[key] <= 0:
            raise ValueError('scrabble: argumentos inválidos')
        
    for key in saco.keys():
        if key not in pontos:
            raise ValueError('scrabble: argumentos inválidos')
        
    for key in saco.keys():
        if not isinstance(saco[key], int) or saco[key] <= 0:
            raise ValueError('scrabble: argumentos inválidos')
    
    
    tab=cria_tabuleiro()
    
    
    pilha=saco.copy()
    pilha=baralha_conjunto(pilha,seed)
            
    print("Bem-vindo ao SCRABBLE.")
    print(tabuleiro_para_str(tab)) 
           
    conta=jogadores
    
    lista_de_jogadores=[]
    for i in range(1,jogadores+1):
        conj_letras=cria_conjunto((),())
        jog=cria_jogador(i,0,conj_letras)
        
        for i2 in range(7):
            distribui_letra(pilha,jog)
        lista_de_jogadores.append(jog)
        
        if conta==jogadores:
            print(jogador_para_str(lista_de_jogadores[i-1]))
        
    primeira=True
    passes_consecutivos=0
    jogador_atual=0
    
    while True:
        jog=lista_de_jogadores[jogador_atual]
        
        if conta>jogadores: # só faz este codigo inicialmente
            print(tabuleiro_para_str(tab)) 
            for i in range(1,jogadores+1):
                print(jogador_para_str(lista_de_jogadores[i-1]))
        conta+=1 
        
        resultado=processa_jogada(tab, jog, pilha, pontos, primeira)
        
        if resultado==True:
            passes_consecutivos=0
            if primeira:
                primeira=False
                
            if len(jog["letras"]) == 0 and len(pilha) == 0:
                break

            
        if resultado== False:
                passes_consecutivos+=1
        
                if passes_consecutivos>=jogadores:
                    break
        
        jogador_atual=(jogador_atual+1)%jogadores#sempre entre 1 e 4

    tuplo=()
    for jog in lista_de_jogadores:
        tuplo+=(jog["pontos"],)
    return tuplo






                        




