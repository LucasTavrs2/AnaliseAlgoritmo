def selecionar_atividades(atividades):
    """
    Seleciona o máximo de atividades compatíveis (que não se sobrepõem) usando 
    o algoritmo guloso de ordenar por horário de término e escolher sequencialmente.
    
    Parâmetro:
      - atividades: lista de tuplas (s, f) representando início e fim de cada atividade.
    Retorna:
      - lista das atividades selecionadas (tuplas), em ordem de seleção.
    """
    # Ordena as atividades pelo horário de término (elemento [1] da tupla)
    atividades_ordenadas = sorted(atividades, key=lambda x: x[1])
    
    selecionadas = []           # lista de atividades escolhidas na solução
    fim_ultima = None           # horário de término da última atividade selecionada
    
    for (s, f) in atividades_ordenadas:
        # Se a atividade atual começa depois (ou exatamente quando) a última selecionada terminou, podemos escolhê-la
        if fim_ultima is None or s >= fim_ultima:
            selecionadas.append((s, f))
            fim_ultima = f     # atualiza o horário de término da última atividade escolhida
    
    return selecionadas

# Exemplo de uso:
atividades = [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]
resultado = selecionar_atividades(atividades)
print("Atividades selecionadas:", resultado)
# Saída esperada (uma das soluções ótimas possíveis para o conjunto dado):
# Atividades selecionadas: [(1, 4), (5, 7), (8, 11), (12, 14)]



def mochila_fracionaria(capacidade, itens):
    """
    Resolve o problema da mochila fracionária de forma gulosa.
    
    Parâmetros:
      - capacidade: peso máximo que a mochila suporta.
      - itens: lista de tuplas (peso, valor) para cada item.
    Retorna:
      - valor_total: o valor máximo obtido colocando itens (possivelmente fracionários) na mochila.
      - fracao_itens: lista de frações escolhidas para cada item na ordem original.
                      (Ex: 1.0 significa item inteiro, 0.5 significa metade do item, etc.)
    """
    # Calcula a razão valor/peso para cada item, mantendo índice original para referência
    itens_com_razao = []
    for idx, (peso, valor) in enumerate(itens):
        razao = valor / peso
        itens_com_razao.append((razao, peso, valor, idx))
    # Ordena os itens por razão decrescente (item mais valioso por peso primeiro)
    itens_com_razao.sort(key=lambda x: x[0], reverse=True)
    
    valor_total = 0.0
    fracao_itens = [0.0] * len(itens)  # inicia todas frações em 0 (nenhuma parte selecionada)
    
    for razao, peso, valor, idx in itens_com_razao:
        if capacidade == 0:
            break  # mochila já cheia
        if peso <= capacidade:
            # pega o item inteiro
            capacidade -= peso
            valor_total += valor
            fracao_itens[idx] = 1.0
        else:
            # pega fração do item que cabe na capacidade restante
            frac = capacidade / peso
            valor_total += valor * frac
            fracao_itens[idx] = frac
            capacidade = 0  # enche a mochila
    
    return valor_total, fracao_itens

# Exemplo de uso (usando os itens do exemplo acima):
itens = [(40, 840), (30, 600), (20, 400), (10, 100), (20, 300)]
capacidade = 50
valor_max, fracao = mochila_fracionaria(capacidade, itens)
print(f"Valor máximo: {valor_max}") 
print("Fração dos itens selecionados:", fracao)
# Saída esperada:
# Valor máximo: 1040.0
# Fração dos itens selecionados: [1.0, 0.3333333333333333, 0.0, 0.0, 0.0]




def troco_guloso(valor, moedas):
    """
    Determina o menor número de moedas para totalizar 'valor' usando o método guloso.
    
    Parâmetros:
      - valor: valor do troco a ser dado.
      - moedas: lista de valores das moedas disponíveis.
    Retorna:
      - lista com os valores das moedas utilizadas para compor o troco.
    """
    # Ordena as moedas em ordem decrescente para tentar as maiores primeiro
    moedas.sort(reverse=True)
    
    resultado = []
    restante = valor
    for moeda in moedas:
        # Enquanto a moeda atual couber no restante, usamos essa moeda
        while restante >= moeda:
            resultado.append(moeda)
            restante -= moeda
            # (não há necessidade de break aqui, o while controla quantas vezes pegar essa moeda)
    return resultado

# Exemplo de uso 1: sistema de moedas típico (25,10,5,1) onde o guloso é ótimo
moedas1 = [25, 10, 5, 1]
troco1 = troco_guloso(42, moedas1)
print("Troco para 42 centavos com moedas", moedas1, ":", troco1)
# Saída esperada: Troco para 42 centavos com moedas [25, 10, 5, 1] : [25, 10, 5, 1, 1]  (5 moedas, solução ótima)

# Exemplo de uso 2: sistema de moedas não canônico (4,3,1) onde o guloso pode falhar
moedas2 = [4, 3, 1]
troco2 = troco_guloso(6, moedas2)
print("Troco para 6 centavos com moedas", moedas2, ":", troco2)
# Saída do guloso: Troco para 6 centavos com moedas [4, 3, 1] : [4, 1, 1]  (3 moedas, solução não-ótima)
# O troco ótimo nesse caso seria [3, 3] (2 moedas), mas o algoritmo guloso não o encontrou.

