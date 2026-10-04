# projeto 2

#Tad casa

#construtor

def cria_casa(lin,col):
    """
    cria_casa: int x int → casa
    
    Recebe dois inteiros correspondentes à linha lin e coluna col e 
    devolve a 
    casa correspondente. Gera ValueError com a mensagem 'cria_casa: 
    argumentos 
    inválidos' caso os argumentos não sejam válidos (inteiros entre 1 e 
    15).
    """
    if not(type(lin)==int and type(col)==int):
        raise ValueError("cria_casa: argumentos inválidos")
    if not(1<=lin<=15 and 1<=col<=15):
        raise ValueError("cria_casa: argumentos inválidos")
    
    return (lin,col)

#seletor

def obtem_col(casa):
    """
    obtem_col: casa → int
    
    Devolve a coluna col da casa c.
    """
    return casa[1]

def obtem_lin(casa):
    """
    obtem_lin: casa → int
    
    Devolve a linha lin da casa c.
    """
    return casa[0]

#recohecedor

def eh_casa(casa):
    """
    eh_casa: universal → bool
    
    Devolve True caso o seu argumento seja um TAD casa e False caso 
    contrário.
    """
    if type(casa)!=tuple or len(casa)!=2:
        return False
    if not(type(obtem_lin(casa))==int and type(obtem_col(casa))==int):
        return False
    if not(1<=obtem_lin(casa)<=15 and 1<=obtem_col(casa)<=15):
        return False
    return True

#teste

def casas_iguais(casa1,casa2):
    """
    casas_iguais: universal x universal → bool
    
    Devolve True apenas se c1 e c2 são casas e são iguais, e False caso 
    contrário.
    """
    if not(eh_casa(casa1)and eh_casa(casa2)):
        return False
    if not(obtem_lin(casa1)==obtem_lin(casa2)and obtem_col(casa1)==obtem_col(casa2)):
        return False
    return True


#transformador

def casa_para_str(casa):
    """
    casa_para_str: casa → str
    
    Devolve a cadeia de caracteres que representa o seu argumento no 
    formato '(lin,col)'.
    """
    return f"({obtem_lin(casa)},{obtem_col(casa)})"

def str_para_casa(string):
    """
    str_para_casa: str → casa
    
    Devolve a casa representada pelo seu argumento.
    """
    numeros=string.strip("()")
    numeros=numeros.split(",")
    return cria_casa(int(numeros[0]),int(numeros[1]))

#

def incrementa_casa(c,d,s):
    """
    incrementa_casa: casa x str x int → casa
    
    Devolve a casa dum tabuleiro de Scrabble a seguir de c na direção d 
    ('H' ou 'V') e a distância s (inteiro positivo). Caso não exista, 
    devolve a casa c.
    """
    linha=obtem_lin(c)
    coluna=obtem_col(c)
    if d=="H":
        if 1<=coluna+s<=15:
            return cria_casa(linha,coluna+s)
        else:
            return c
    if d=="V":
        if 1<=linha+s<=15:
            return cria_casa(linha+s,coluna)
        else:
            return c


#Tad jogador

#construtor

def cria_humano(nome):
    """
    cria_humano: str → jogador
    
    Recebe uma cadeia de caracteres (não vazia) a representar o nome do 
    jogador e devolve o jogador de Scrabble humano com 0 pontos e sem 
    letras.
    Gera ValueError com a mensagem 'cria_humano: argumento inválido' 
    caso o argumento não seja válido.
    """
    if type(nome)!=str or len(nome)==0:
        raise ValueError('cria_humano: argumento inválido')
    jog={"nome":nome,"pontos":0,"letras":[]}
    return jog

def cria_agente(nivel):
    """
    cria_agente: str → jogador
    
    Recebe uma cadeia de caracteres a representar o nível do jogador 
    ('FACIL','MEDIO' ou 'DIFICIL') e devolve o jogador de Scrabble 
    agente com 0 pontos e sem letras. Gera ValueError com a mensagem 
    'cria_agente: argumento inválido' caso o argumento não seja válido.
    """
    if nivel not in ["FACIL","MEDIO","DIFICIL"]:
        raise ValueError('cria_agente: argumento inválido')
    jog={"nivel":nivel,"pontos":0,"letras":[]}
    return jog


#seletores

def jogador_identidade(jog):
    """
    jogador_identidade: jogador → str
    
    Devolve o nome do jogador j se é um jogador humano ou o nível se é 
    um agente.
    """
    if "nome" in jog:
        return jog["nome"]
    else:
        return jog["nivel"]


def jogador_pontos(jog):
    """
    jogador_pontos: jogador → int
    
    Devolve os pontos do jogador j.
    """
    return jog["pontos"]

####
alfabeto = ['A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O', 'P','Q','R','S','T','U','V','X','Z']

def ordena_string(conj):
    """
    ordena: conjunto letras → string
    
    Função auxiliar que devolve string ordenada com todas as letras do 
    conjunto,respeitando a ordem do alfabeto português.
    """
    string=""
    for letra in alfabeto:
        if letra in conj:
            string+=letra*conj.count(letra)
    return string
####


def jogador_letras(jog):
    """
    jogador_letras: jogador → str
    
    Devolve a cadeia de caracteres ordenada com todas as letras do 
    jogador j.
    """
    conj=jog["letras"]
    if len(conj)!=0:
        return ordena_string(conj)
    else:
        return ""

def jogador_letras_string(jog):
    """
    jogador_letras_string: jogador → str
    
    Função auxiliar que retorna string com espaços entre as letras do 
    jogador, para uso na representação externa do jogador.
    """
    conj = jogador_letras(jog)
    return " ".join(conj)


#modificadores

def recebe_letra(jog,l):
    """
    recebe_letra: jogador x str → jogador
    
    Modifica destrutivamente o jogador j acrescentando a letra l às 
    suas letras, e devolve o próprio jogador.
    """
    jog["letras"].append(l)
    return jog

def usa_letra(jog,l):
    """
    usa_letra: jogador x str → jogador
    
    Modifica destrutivamente o jogador j retirando a letra l das suas 
    letras, e devolve o próprio jogador.
    """
    jog["letras"].remove(l)
    return jog

def soma_pontos(jog,p):
    """
    soma_pontos: jogador x int → jogador
    
    Modifica destrutivamente o jogador j somando os pontos p à sua 
    pontuação atual, e devolve o próprio jogador.
    """
    jog["pontos"]+=p
    return jog

#reconhecer

def eh_jogador(arg):
    """
    eh_jogador: universal → bool
    
    Devolve True caso o seu argumento seja um TAD jogador e False caso 
    contrário.
    """
    if isinstance(arg,dict)and "pontos" in arg and "letras" in arg and ("nome" in arg or "nivel" in arg):
        return True
    return False

def eh_humano(arg):
    """
    eh_humano: universal → bool
    
    Devolve True caso o seu argumento seja um TAD jogador humano e 
    False caso contrário.
    """
    if isinstance(arg,dict)and "pontos" in arg and "letras" in arg and "nome" in arg:
        return True
    return False

def eh_agente(arg):
    """
    eh_agente: universal → bool
    
    Devolve True caso o seu argumento seja um TAD jogador agente e 
    False caso contrário.
    """
    if isinstance(arg,dict)and "pontos" in arg and "letras" in arg and "nivel" in arg:
        return True
    return False

#teste

def jogadores_iguais(arg1,arg2):
    """
    jogadores_iguais: universal x universal → bool
    
    Devolve True apenas se j1 e j2 forem jogadores e forem iguais.
    """
    if not(eh_jogador(arg1) and eh_jogador(arg2)):
        return False
    
    if eh_humano(arg1) != eh_humano(arg2):
        return False
    
    if (jogador_identidade(arg1) == jogador_identidade(arg2) and 
        jogador_pontos(arg1) == jogador_pontos(arg2) and 
        jogador_letras(arg1) == jogador_letras(arg2)):
        return True
    return False


#transformador

def jogador_para_str(jog):
    """
    jogador_para_str: jogador → str
    
    Devolve a cadeia de caracteres que representa o jogador.
    Para humanos: 'Nome (pontos): letras'
    Para agentes: 'BOT(NIVEL) (pontos): letras'
    """
    identidade= jogador_identidade(jog)
    pontos=jogador_pontos(jog)
    letras=jogador_letras_string(jog)
    
    if eh_humano(jog):
        if letras!="":
            return f'{identidade} ({str(pontos).rjust(3)}): {letras}'
        else:
            return f'{identidade} ({str(pontos).rjust(3)}):'
    else:
        if letras!="":
            return f'BOT({identidade}) ({str(pontos).rjust(3)}): {letras}'
        else:
            return f'BOT({identidade}) ({str(pontos).rjust(3)}):'


####

def distribui_letras(jog,saco,num):
    """
    distribui_letras: jogador x list x int → jogador
    
    Retira um máximo de num letras do final da lista saco 
    (potencialmente vazia) e as acrescenta ao jogador jog, devolvendo 
    o jogador. A função modifica destrutivamente a lista de letras e o 
    jogador passados como argumento.
    """
    if len(saco)!=0:
        while num>0 and len(saco)>0:
            letra=saco.pop()
            recebe_letra(jog,letra)
            num-=1
    return jog
####

#Tad vocabulario

pontos_letras = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4,'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3,'O': 1, 'P': 2, 'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1,'V': 4, 'X': 8, 'Z': 8}

#construtor

def cria_vocabulario(tuplo):
    """
    cria_vocabulario: tuple → vocabulario
    
    Devolve o vocabulário que contém as palavras contidas no tuplo. O 
    construtor verifica a validade do seu argumento, gerando 
    ValueError com a mensagem 'cria_vocabulario: argumento inválido'. 
    O tuplo contém pelo menos uma palavra e as palavras são cadeias de 
    caracteres únicas de letras maiúsculas do abecedário Português de 
    comprimento entre 2 e 15 letras.
    """
    if len(tuplo)==0 or not isinstance(tuplo,tuple):
        raise ValueError('cria_vocabulario: argumento inválido')
    if len(tuplo) != len(set(tuplo)):
        raise ValueError('cria_vocabulario: argumento inválido')

    for palavras in tuplo:
        if not isinstance(palavras, str):
            raise ValueError('cria_vocabulario: argumento inválido')
        if not(2<=len(palavras)<=15):
            raise ValueError('cria_vocabulario: argumento inválido')
        for letras in palavras:
            if letras not in alfabeto:
                raise ValueError('cria_vocabulario: argumento inválido')
    dicio={}
    for palavra in ordena_palavras(tuplo):
        if len(palavra) not in dicio:
            dicio[len(palavra)] = {}
        if palavra[0] not in dicio[len(palavra)]:
            dicio[len(palavra)][palavra[0]] = {}
        dicio[len(palavra)][palavra[0]][palavra]=0
        dicio[len(palavra)][palavra[0]][palavra]=obtem_pontos(dicio,palavra)
    
    return dicio

#seletores

def obtem_pontos(vocab,palavra):
    """
    obtem_pontos: vocabulario x str → int
    
    Devolve os pontos da palavra do vocabulário, ou 0 caso não se 
    encontre.
    """
    tamanho=len(palavra)
    letra_inicial=palavra[0]
    if tamanho in vocab and letra_inicial in vocab[tamanho] and palavra in vocab[tamanho][letra_inicial]:
        return sum(pontos_letras[letra] for letra in palavra)
    return 0

######

LET_2_INDEX=dict(zip(alfabeto,range(len(alfabeto))))
def ordena_letras(seq):
    """
    ordena_letras: list/tuple → list
    
    Função auxiliar que ordena uma sequência de letras de acordo com a 
    ordem do alfabeto português.
    """
    return sorted(seq,key=lambda x:LET_2_INDEX[x])

def ordena_palavras(seq):
    """
    ordena_palavras: list/tuple → list
    
    Função auxiliar que ordena uma sequência de palavras de acordo com 
    a ordem lexicográfica do alfabeto português.
    """
    return sorted(seq,key=lambda x:tuple(LET_2_INDEX[l]for l in x))

#######

def obtem_palavras(vocab,comp,letra):
    """
    obtem_palavras: vocabulario x int x str → tuple
    
    Devolve um tuplo de pares que correspondem a todas as palavras com 
    comprimento comp e primeira letra letra. Cada par do tuplo contém 
    a palavra e a respetiva pontuação. Os pares devem estar ordenados 
    por ordem decrescente de pontuação das palavras, e em caso de 
    empate, em ordem lexicográfica. Caso não existam no vocabulário 
    palavras com o comprimento e primeira letra indicados, a função 
    deverá devolver um tuplo vazio.
    """
    lista=[]
    if comp not in vocab or letra not in vocab[comp]:
        return tuple()
    for palavra in vocab[comp][letra]:
        lista.append((palavra,vocab[comp][letra][palavra]))
    lista= sorted(lista,key=lambda x: -x[1])
    return tuple(lista)


#teste

def testa_palavra_padrao(vocab,palavra,padrao,letras):
    """
    testa_palavra_padrao: vocabulario x str x str x str → bool
    
    Devolve True caso exista a palavra palavra no vocabulário 
    vocabulario e seja possível formar a palavra fornecida 
    substituindo os caracteres '.' do padrão padrao por letras de 
    letras. Caso contrário, devolve False.
    """
    tamanho = len(palavra)
    letra_inicial = palavra[0]
    
    if tamanho not in vocab or letra_inicial not in vocab[tamanho] or palavra not in vocab[tamanho][letra_inicial]:
        return False
    
    if len(palavra) != len(padrao):
        return False
    
    letras_disponiveis = list(letras)
    
    for i in range(len(padrao)):
        if padrao[i]==".":
            if palavra[i] in letras_disponiveis:
                letras_disponiveis.remove(palavra[i])
            else:
                return False
        else:
            if palavra[i]!=padrao[i]:
                return False
    return True

#transformador

def ficheiro_para_vocabulario(nome_fich):
    """
    ficheiro_para_vocabulario: str → vocabulario
    
    Devolve o vocabulário formado a partir das palavras contidas no 
    ficheiro nome_fich. O ficheiro contém uma palavra por linha, 
    podendo ter linhas vazias (que serão ignoradas). As palavras 
    consideradas são as palavras entre 2 e 15 letras do abecedário 
    português, convertidas para letras maiúsculas.
    """
    with open(nome_fich,"r",encoding="utf-8") as f:
        lista = f.readlines()
    
    palavras_validas = []
    for linha in lista:
        
        palavra = linha.strip().upper()
        if len(palavra) == 0:
            continue
        if not palavra or not (2 <= len(palavra) <= 15):
            continue
        
        valida = True
        for letra in palavra:
            if letra not in alfabeto:
                valida = False
                break
        
        if valida:
            palavras_validas.append(palavra)
        
    return cria_vocabulario(tuple(set(palavras_validas)))

def vocabulario_para_str(vocab):
    """
    vocabulario_para_str: vocabulario → str
    
    Devolve uma cadeia de caracteres que concatena todas as palavras 
    guardadas no vocabulário "vocab", separadas por um caracter de 
    mudança de linha, que já vem por ordem definida na função 
    obtem_palavras.
    """
    resultado = []
    
    for comp in range(2, 16):
        for letra in alfabeto:
            palavras = obtem_palavras(vocab, comp, letra)
            for palavra, pontos in palavras:
                resultado.append(palavra)
    
    return '\n'.join(resultado)

def procura_palavra_padrao(vocab, padrao, letras, min_pontos):
    """
    procura_palavra_padrao: vocabulario x str x str x int → tuple
    
    Devolve o tuplo formado pela palavra e a pontuação, que 
    correspondem à palavra do vocabulario com maior pontuação que é 
    possível formar utilizando as letras da cadeia de caracteres 
    letras para completar todos os espaços livres do padrão padrao, 
    cumprindo a restrição de que a pontuação da palavra não poderá ser 
    inferior a min_pontos. Caso a função não encontre nenhuma palavra, 
    deverá devolver o tuplo ('', 0).
    
    Mecanismo de procura:
        - Se o padrão começa por letra: acede às palavras do 
        vocabulário correspondentes ao comprimento e primeira letra, e 
        devolve a palavra com melhor pontuação.
        - Se o padrão começa por espaço livre: repete o procedimento 
        anterior para cada letra disponível no conjunto de letras, por 
        ordem lexicográfica.
    """
    palavra_nota_max = 0
    palavra_max = ""
    
    # Fazer a procura com o tamanho e a primeira letra
    if padrao[0] != ".":
        palavras = obtem_palavras(vocab, len(padrao), padrao[0])
        
        for palavra, pontos in palavras:
            if pontos >= min_pontos and testa_palavra_padrao(vocab, palavra, padrao, letras):
                palavra_max = palavra
                palavra_nota_max = pontos
                break
    
    else:  # padrao[0] == "."
        for letra in ordena_string(str(set(letras))):
            palavras = obtem_palavras(vocab, len(padrao), letra)
            
            for palavra, pontos in palavras:
                if pontos >= min_pontos and testa_palavra_padrao(vocab, palavra, padrao, letras):
                    if pontos > palavra_nota_max:
                        palavra_max = palavra
                        palavra_nota_max = pontos
                        break
    return (palavra_max, palavra_nota_max)

#Tad tabuleiro

#construtor

def cria_tabuleiro():
    """
    cria_tabuleiro: {} → tabuleiro
    
    Devolve um tabuleiro de Scrabble vazio.
    """
    return {}

#seletores

def  obtem_letra(tab,casa):
    """
    obtem_letra: tabuleiro x casa → str
    
    Devolve a letra contida na casa do tabuleiro "tab". Devolve '.' se 
    a casa estiver vazia.
    """
    if casa in tab:
        return tab[casa]
    else:
        return "."

#modificadores

def insere_letra(tab,casa,letra):
    """
    insere_letra: tabuleiro x casa x str → tabuleiro
    
    Modifica destrutivamente o tabuleiro "tab" colocando a letra  na casa, e devolve o próprio tabuleiro.
    """
    tab[casa]=letra
    return tab

#reconhecedor

def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal → bool
    
    Devolve True caso o seu argumento seja um TAD tabuleiro e False 
    caso contrário.
    """
    if not isinstance(arg, dict):
        return False
    for casa in arg:
        if not eh_casa(casa):
            return False
        if not isinstance(arg[casa], str) or len(arg[casa]) != 1:
            return False
    return True

def eh_tabuleiro_vazio(arg):
    """
    eh_tabuleiro_vazio: universal → bool
    
    Devolve True caso o seu argumento seja um TAD tabuleiro e estiver 
    vazio (sem letras) e False caso contrário.
    """
    if eh_tabuleiro(arg) and len(arg)==0:
        return True
    return False

#teste

def tabuleiros_iguais(arg1,arg2):
    """
    tabuleiros_iguais: universal x universal → bool
    
    Devolve True apenas se arg1 e arg2 forem tabuleiros e forem iguais.
    """
    if not(eh_tabuleiro(arg1) and eh_tabuleiro(arg2)):
        return False
    return arg1==arg2

#transformador

def tabuleiro_para_str(tab):
    """
    tabuleiro_para_str: tabuleiro → cad. carateres
    
    Recebe tabuleiro e devolve cadeia de caracteres com sua representação externa.
    """
    linha = ""
    linha += "                       1 1 1 1 1 1\n"
    linha += "     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5\n"
    linha += "   +-------------------------------+\n"

    i2=1
    letra=""

    for i in range(1,16):
        while i2<=15:
            casa=cria_casa(i,i2)
            letras=obtem_letra(tab,casa)
            letra+=" "+letras
            i2+=1
        i2=1
        linha+= str(i).rjust(2)+" |"+letra+" |\n"
        letra=""

    linha += "   +-------------------------------+"

    return linha

#####

def obtem_padrao(tab,casa_i,casa_f):
    """
    obtem_padrao: tabuleiro x casa x casa → str
    
    Devolve a sequência de letras contida no tabuleiro "tab" entre a 
    casa_i e a casa_f (ambas inclusive) na mesma linha vertical ou 
    horizontal.
    """
    l_i=obtem_lin(casa_i)
    l_f=obtem_lin(casa_f)
    c_i=obtem_col(casa_i)
    c_f=obtem_col(casa_f)
    
    if casas_iguais(casa_i,casa_f):
        return obtem_letra(tab,casa_i)
    
    sequencia_letras=""
    if l_i==l_f:
        distancia=c_f-c_i
        for i in range(distancia+1):
            casa=cria_casa(l_i,c_i+i)
            sequencia_letras+=obtem_letra(tab,casa)
    if c_i==c_f:
        distancia=l_f-l_i
        for i in range(distancia+1):
            casa=cria_casa(l_i+i,c_i)
            sequencia_letras+=obtem_letra(tab,casa)

    return sequencia_letras


def insere_palavra(tab,casa,direcao,palavra):
    """
    insere_palavra: tabuleiro x casa x str x str → tabuleiro
    
    Modifica destrutivamente o tabuleiro "tab" colocando a palavra 
    na casa na direção ('H' para horizontal ou 'V' para vertical), e 
    devolve o próprio tabuleiro.
    """
    tamanho=len(palavra)
    
    for i in range(tamanho):
        casa_agora=incrementa_casa(casa,direcao,i)
        insere_letra(tab,casa_agora,palavra[i])
    return tab

def obtem_subpadroes(tab,casa_i,casa_f,l):
    """
    obtem_subpadroes: tabuleiro x casa x casa x int → tuple x tuple
    
    Devolve dois tuplos de igual tamanho. O primeiro tuplo contém 
    todos os subpadrões viáveis ordenados gerados a partir do padrão 
    original contido no tabuleiro "tab" entre as casa_i e casa_f 
    (ambas inclusive), com no máximo l espaços livres. O segundo tuplo 
    contém a casa onde começa cada um dos subpadrões correspondentes 
    do primeiro tuplo. A casa_i e a casa_f pertencem à mesma linha 
    vertical ou horizontal.
    
    Um subpadrão é inviável se:
    (1) não contém qualquer letra (só espaços livres)
    (2) não contém qualquer espaço livre (só letras)
    (3) existe no padrão original uma letra antes ou depois do 
    subpadrão
    """
    padrao=obtem_padrao(tab,casa_i,casa_f)
    sub_padroes=[]
    sub_casas=[]
    n=len(padrao)
    
    l_i=obtem_lin(casa_i)
    l_f=obtem_lin(casa_f)
    c_i=obtem_col(casa_i)
    c_f=obtem_col(casa_f)
    
    
    for i in range(n):
        for j in range(n, 0, -1):
            
            if i > 0 and padrao[i-1] != '.':
                continue 
            if j < n and padrao[j] != '.':
                continue
            
            sub_padrao=padrao[i:j]
            
            if not any(letra != '.' for letra in sub_padrao):
                continue
            if not any(letra == '.' for letra in sub_padrao):
                continue
            
            if sub_padrao.count('.') > l:
                continue
            sub_padroes.append(sub_padrao)
            
            if l_i==l_f:
                casa=cria_casa(l_i,c_i+i)
            if c_i==c_f:
                casa=cria_casa(l_i+i,c_i)
            sub_casas.append(casa)
    
    return (tuple(sub_padroes), tuple(sub_casas))

def gera_todos_padroes(tab,l):
    """
    gera_todos_padroes: tabuleiro x int → tuple x tuple x tuple
    
    Devolve três tuplos de igual tamanho. O primeiro contém todos os 
    sub-padrões viáveis do tabuleiro que contenham no máximo l espaços 
    livres, formado pelos sub-padrões ordenados obtidos de cada uma 
    das linhas completas do tabuleiro (da primeira à última), seguidos 
    dos sub-padrões ordenados obtidos de cada coluna completa (da 
    primeira até a última). O segundo e terceiro tuplos correspondem à 
    casa de início e à direção ('V' ou 'H') do sub-padrão 
    correspondente do primeiro tuplo.
    """
    padroes=[]
    casas=[]
    direcoes=[]
    
    for linha in range(1,16):
        casa_i=cria_casa(linha,1)
        casa_f=cria_casa(linha,15)
        padroes_por_linha,casas_por_linha=obtem_subpadroes(tab,casa_i,casa_f,l)
        
        for padrao,casa in zip(padroes_por_linha,casas_por_linha):
            padroes.append(padrao)
            casas.append(casa)
            direcoes.append("H")
            
    for coluna in range(1,16):
        casa_i_c=cria_casa(1,coluna)
        casa_f_c=cria_casa(15,coluna)
        padroes_por_coluna,casas_por_coluna=obtem_subpadroes(tab,casa_i_c,casa_f_c,l)
        
        for padrao,casa in zip(padroes_por_coluna,casas_por_coluna):
            padroes.append(padrao)
            casas.append(casa)
            direcoes.append("V")
            
    return (tuple(padroes), tuple(casas), tuple(direcoes))


#funções adicionais

def ordena_conj(conj):
    """
    ordena_conj: dict → list
    
    Função auxiliar que devolve lista ordenada com todas as letras do 
    dicionário conj (onde as chaves são letras e os valores são as 
    ocorrências), respeitando a ordem do alfabeto português.
    """
    lista=[]
    for letra in alfabeto:
        if letra in conj:
            lista+=[letra]*conj[letra]
    return lista



def baralha_saco(estado):
    """
    baralha_saco: int → list
    
    Recebe um inteiro positivo estado representando o estado inicial 
    do gerador pseudo-aleatório e devolve uma lista baralhada com 
    todas as letras contidas no saco de Scrabble. Para baralhar as 
    letras: 1) constrói uma lista com todas as letras contidas no saco 
    em ordem lexicográfica; e 2) permuta as letras usando o gerador 
    xorshift de 32 bits.
    """
    ocorrencias = {
        'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11, 'F': 2,
        'G': 2, 'H': 2, 'I': 10, 'J': 2, 'L': 5, 'M': 6, 'N': 4,
        'O': 10, 'P': 4, 'Q': 1, 'R': 6, 'S': 8, 'T': 5, 'U': 7,
        'V': 2, 'X': 1, 'Z': 1}
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
    
    ocorrencias=ordena_conj(ocorrencias)
    permuta_letras(ocorrencias,estado) 
    return ocorrencias

def jogada_humano(tab,jog,vocab,pilha,ui_acao):
    """
    jogada_humano: tabuleiro x jogador x vocabulario x list → bool
    
    Recebe um tabuleiro, um jogador humano, um vocabulario e uma lista 
    de letras. A função processa o turno completo do jogador humano 
    devendo apresentar a mensagem "Jogada <nome>: ", repetindo a 
    mensagem até o jogador introduzir uma jogada válida num formato 
    dependente da ação pretendida:
        - Passar: 'P'. Devolve False sem alterar nenhum dos argumentos.
    
        - Trocar: 'T <seq_letras>', sendo <seq_letras> a sequência de 
        uma ou mais letras separadas por espaços do conjunto de letras 
        do jogador para trocar. Devolve True e modifica o jogador 
        retirando novas letras do final da lista.
    
        - Jogar: 'J <linha> <coluna> <dir> <palavra>'. Devolve True e 
        modifica o tabuleiro, atualiza o jogador (pontuação e letras).
    
    Para a primeira jogada, a palavra deve cobrir a casa central (8,
    8). Para jogadas seguintes, as casas devem formar um padrão viável 
    e as palavras devem estar no vocabulário.
    """
    
    identidade = jogador_identidade(jog)
    
    while True:
            if ui_acao["tipo"] == "PASSAR":
                return False

            if ui_acao["tipo"] == "TROCAR":
                letras = ui_acao["letras"]
            
            if jogada == '':
                continue
            
            jogada=jogada.split()

            if len(jogada) == 0:
                continue
        
            if jogada[0]=="P":#passar
                return False

            elif jogada[0]=="T":#trocar
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
                    if letra not in jogador_letras(jog) or jogador_letras(jog).count(letra) < qtd:
                        pode_trocar=False
                        break
                
                if not pode_trocar:
                    continue
                
                for letra in letras_a_trocar:
                    usa_letra(jog, letra)
                
                distribui_letras(jog,pilha,len(letras_a_trocar))
                
                return  True

            elif jogada[0]=="J"and len(jogada)>=5:#jogar
                            
                l = jogada[1]
                c = jogada[2]
                if not (l.isdigit() and c.isdigit()):
                    continue
                l = int(l)
                c = int(c)
                
                if jogada[3] not in ("H", "V"):
                    continue
                
                if not eh_casa(cria_casa(l,c)):
                    continue
                casa=cria_casa(l,c)
                
                direcao=jogada[3]
                palavra=""
                
                for le in jogada[4:]:
                    palavra+=le
                palavra=palavra.upper()
                
                if not incrementa_casa(casa, direcao, len(palavra) - 1):#verifica se a palavra cabe no tabuleiro
                    continue
                
                casa_final = incrementa_casa(casa, direcao, len(palavra) - 1)
                    
                if casas_iguais(casa, casa_final) and len(palavra) > 1:
                    continue
                
                if direcao=="H":#verifica se há letras antes ou depois da palavra
                    if 1<=c-1<=15:
                        if not(obtem_letra(tab,cria_casa(l,c-1))=="."):
                            continue
                if direcao=="V":
                    if 1<=l-1<=15:
                        if not(obtem_letra(tab,cria_casa(l-1,c))=="."):
                            continue
                    
                if eh_tabuleiro_vazio(tab):#jogada inicial
                    casa_central=cria_casa(8,8)
                    passa_central=False
                    for i in range(len(palavra)):
                        casa_agora=incrementa_casa(casa,direcao,i)
                        if casas_iguais(casa_agora,casa_central):
                            passa_central=True
                            break
                    if not passa_central:
                        continue
                    
                    if obtem_pontos(vocab, palavra) == 0:#verifica se a palavra está no vocabulário
                        continue
                    
                    letras_jog=list(jogador_letras(jog))
                    tem_letras=True
                    for letra in palavra:
                        if letra in letras_jog:
                            letras_jog.remove(letra)
                        else:
                            tem_letras=False
                    if tem_letras==False:
                        continue
                    
                    insere_palavra(tab, casa, direcao, palavra)
                    
                    for letra in palavra:
                        usa_letra(jog,letra)
                    
                    pontos_palavra = obtem_pontos(vocab, palavra)
                    soma_pontos(jog, pontos_palavra)
                    
                    distribui_letras(jog, pilha, len(palavra))
                    
                else:#jogada normal
                    casa_final = incrementa_casa(casa, direcao, len(palavra) - 1)
                    padrao = obtem_padrao(tab, casa, casa_final)
                    
                    if len(padrao) != len(palavra):
                        continue
                    if "." not in padrao:
                        continue  
                    
                    if padrao == "." * len(padrao):
                        continue
                    
                    tem_letra_fixa = False
                    for c in padrao:
                        if c != ".":
                            tem_letra_fixa = True
                            break
                    
                    if not tem_letra_fixa:
                        continue  
                    
                    if not testa_palavra_padrao(vocab,palavra,padrao,jogador_letras(jog)):
                        continue
                    
                    insere_palavra(tab, casa, direcao, palavra)
                    
                    for i in range(len(palavra)):
                        if padrao[i]==".":
                            usa_letra(jog,palavra[i])
                    
                    pontos_palavra = obtem_pontos(vocab, palavra)
                    soma_pontos(jog, pontos_palavra)
                    
                    num_letras_usadas = padrao.count('.')
                    distribui_letras(jog, pilha, num_letras_usadas)
                    
                return True
            else:
                continue
            


def jogada_agente(tab, jog, vocab, pilha, gui_callback=None, lista_jogadores=None, idx_atual=None):
    """
    jogada_agente: tabuleiro x jogador x vocabulario x list → bool
    
    Recebe um tabuleiro, um jogador agente, um vocabulario e uma lista 
    de letras, e realiza uma das seguintes ações:
    
    - Passar: se for a primeira jogada (tabuleiro vazio) ou se não 
    conseguir Jogar nem Trocar. Devolve False sem alterar os 
    argumentos.
    
    - Trocar: caso não consiga Jogar e existam pelo menos sete letras 
    no saco, troca todas as letras. Devolve True e modifica jogador e 
    pilha.
    
    - Jogar: devolve True e modifica o tabuleiro e jogador. Para 
    escolher a palavra:
        1. Gera todos os padrões possíveis através de 
        gera_todos_padroes
        2. Seleciona um de cada N padrões ([::N]), sendo N=100 se 
        'FACIL', N=50 se 'MEDIO', N=10 se 'DIFICIL'
        3. Invoca procura_palavra_padrao em cada padrão e seleciona a 
        primeira palavra com maior pontuação.
    """
    
    identidade = jogador_identidade(jog)
    letras_jog=jogador_letras(jog)
    
    if eh_tabuleiro_vazio(tab):#não pode jogar com tabuleiro vazio
        if gui_callback and lista_jogadores and idx_atual is not None:
            gui_callback(tab, lista_jogadores, idx_atual, f'BOT({identidade}) passou a vez.', pilha)
        else:
            print(f'Jogada {identidade}: P')
        return False
    else:
        padroes,casas,direcoes=gera_todos_padroes(tab,len(jogador_letras(jog)))
        if identidade=="FACIL":
            N=100
        elif identidade=="MEDIO":
            N=50
        else:
            N=10
        padroes_nivel=padroes[::N]
        casas_nivel=casas[::N]
        direcoes_nivel=direcoes[::N]
        
        melhor_palavra = ""
        melhor_pontos = 0
        melhor_casa = ()
        melhor_direcao = ""
        melhor_padrao = ""
        
        for i in range(len(padroes_nivel)):
            padrao = padroes_nivel[i]
            casa = casas_nivel[i]
            direcao = direcoes_nivel[i]

            palavra, pontos = procura_palavra_padrao(vocab, padrao,letras_jog , melhor_pontos+1)#procura palavra com pontos maiores que melhor_pontos atual
            if pontos > melhor_pontos:
                melhor_pontos = pontos
                melhor_palavra = palavra
                melhor_casa = casa
                melhor_direcao = direcao
                melhor_padrao=padrao
            
        if melhor_palavra == "":#caso que n encontre palavra
            # Tenta trocar se houver letras suficientes
            if len(pilha) >= 7:
                letras_trocar = list(letras_jog)
                for letra in letras_trocar:
                    usa_letra(jog, letra)
                distribui_letras(jog, pilha, len(letras_trocar))
                letras_str = ' '.join(letras_trocar)
                
                if gui_callback and lista_jogadores and idx_atual is not None:
                    gui_callback(tab, lista_jogadores, idx_atual, f'BOT({identidade}) trocou {len(letras_trocar)} letras', pilha)
                else:
                    print(f'Jogada {identidade}: T {letras_str}')
                return True
            else:
                if gui_callback and lista_jogadores and idx_atual is not None:
                    gui_callback(tab, lista_jogadores, idx_atual, f'BOT({identidade}) passou a vez.', pilha)
                else:
                    print(f'Jogada {identidade}: P')
                return False
            
        
        insere_palavra(tab, melhor_casa, melhor_direcao, melhor_palavra)
            
        for i in range(len(melhor_palavra)):
            if melhor_padrao[i] == '.':
                usa_letra(jog, melhor_palavra[i])
            
        soma_pontos(jog, melhor_pontos)
        num_letras_usadas = melhor_padrao.count('.')
        distribui_letras(jog, pilha, num_letras_usadas)
            
        if gui_callback and lista_jogadores and idx_atual is not None:
            msg = f'BOT({identidade}) jogou: {melhor_palavra} em ({obtem_lin(melhor_casa)},{obtem_col(melhor_casa)})'
            gui_callback(tab, lista_jogadores, idx_atual, msg, pilha)
        else:
            print(f'Jogada {identidade}: J {obtem_lin(melhor_casa)} {obtem_col(melhor_casa)} {melhor_direcao} {melhor_palavra}')
        return True



def scrabble2(jogadores,nome_fiche,seed, gui_callback=None, input_callback=None):
    """
    scrabble2: tuple x str x int → tuple
    
    Função principal que permite jogar um jogo completo de Scrabble2 
    de dois a quatro jogadores. Recebe:
    
    - jogadores: tuplo com o nome dos jogadores humanos (string não 
    vazia) e o nível dos jogadores agentes (string começada por '@' 
    seguido do nível) na ordem em que jogam
    - nome_fich: nome de ficheiro com o vocabulário
    - seed: inteiro positivo representando o estado inicial do gerador 
    pseudo-aleatório
    
    Devolve o tuplo com a pontuação final obtida pelos jogadores.
    
    O jogo começa baralhando o saco de letras e distribuindo 7 letras 
    a cada jogador em ordem. O jogo termina quando todos os jogadores 
    passam ou quando um jogador fica sem letras e o saco estiver 
    esgotado.
    
    Gera ValueError com a mensagem 'scrabble2: argumentos inválidos' 
    se os argumentos não forem válidos.
    """
    
    if not(isinstance(jogadores,tuple)and isinstance(nome_fiche,str)and isinstance(seed,int)):
        raise ValueError('scrabble2: argumentos inválidos')

    if not(seed > 0):
        raise ValueError('scrabble2: argumentos inválidos')
    if not(2<=len(jogadores)<=4):
        raise ValueError('scrabble2: argumentos inválidos')
    for jogador in jogadores:
        if not(isinstance(jogador,str)and len(jogador)!=0):
            raise ValueError('scrabble2: argumentos inválidos')
        if jogador[0]=="@" and jogador[1:] not in ["FACIL","MEDIO","DIFICIL"]:
            raise ValueError('scrabble2: argumentos inválidos')
    
    
    tab=cria_tabuleiro()
    vocab=ficheiro_para_vocabulario(nome_fiche)
    pilha=baralha_saco(seed)
    
           
    
    lista_de_jogadores=[]
    n_de_jogadores_humanos=0
    for jogador in jogadores:#cria jogadores e distribui letras
        if jogador[0]=="@":
            jog=cria_agente(jogador[1:])
        else:
            jog=cria_humano(jogador)
            n_de_jogadores_humanos+=1
        
        distribui_letras(jog,pilha,7)
        lista_de_jogadores.append(jog)
        print(jogador_para_str(jog))
        
    if gui_callback:
        gui_callback(tab, lista_de_jogadores, 0, "Bem-vindo ao SCRABBLE2.",pilha)
    else:
        print("Bem-vindo ao SCRABBLE2.")
        print(tabuleiro_para_str(tab))
    
    passes_consecutivos=0
    jogador_atual=0
    n_de_jogadores=len(lista_de_jogadores)
    conta=n_de_jogadores
    
    while True:
        jog=lista_de_jogadores[jogador_atual]#jogador da vez
        
        if conta>n_de_jogadores:
            if gui_callback:
                gui_callback(tab, lista_de_jogadores, jogador_atual, "", pilha)
        else:
            print(tabuleiro_para_str(tab)) 
            for i in range(1,n_de_jogadores+1):
                print(jogador_para_str(lista_de_jogadores[i-1]))
        conta+=1 
        
        if eh_humano(jog):
            print(f"[DEBUG] Vez de humano: {jogador_identidade(jog)}")
            resultado = jogada_humano(tab, jog, vocab, pilha, input_callback)
        else:
            print(f"[DEBUG] Vez de bot: {jogador_identidade(jog)}")
            print(f"[DEBUG] Tabuleiro vazio? {eh_tabuleiro_vazio(tab)}")
            resultado = jogada_agente(tab, jog, vocab, pilha)
            print(f"[DEBUG] Bot jogou, resultado: {resultado}")
    
            # Atualiza GUI após jogada do bot
            if gui_callback:
                identidade = jogador_identidade(jog)
                msg = f'BOT({identidade}) jogou! Pontos: {jogador_pontos(jog)}'
                print(f"[DEBUG] Chamando gui_callback após bot")
                gui_callback(tab, lista_de_jogadores, jogador_atual, msg, pilha)
                        
        
        if resultado==True:#reset aos passes consecutivos
            passes_consecutivos=0
            if len(jogador_letras(jog)) == 0 and len(pilha) == 0:# jogador ficou sem letras e pilha vazia, acaba o jogo
                break
            
        if resultado== False:#incrementa os passes consecutivos
                passes_consecutivos+=1
        
                if passes_consecutivos>=n_de_jogadores:# todos passaram, acaba o jogo
                    break
        
        jogador_atual=(jogador_atual+1)%n_de_jogadores#sempre entre 1 e nªdejogadores

    tuplo=()
    for jog in lista_de_jogadores:
        tuplo+=(jogador_pontos(jog),)
    return tuplo

#jog=("dario","@DIFICIL","@DIFICIL")
#scrabble2(jog,"C:/Users/crist\OneDrive - Universidade de Lisboa\Ambiente de Trabalho/repo_p2\ist1118428/vocab25k.txt",32)














