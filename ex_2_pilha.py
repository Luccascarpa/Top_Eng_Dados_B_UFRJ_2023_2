from array import array

class Pilha:
    def __init__(self, capacidade):
        self.items = array('i', []) # array de inteiros
        self.capacidade = capacidade
    
    def pilha_esta_vazia(self):
        return len(self.items) == 0
    
    def pilha_esta_cheia(self):
        return len(self.items) == self.capacidade
    
    def empilha(self, dado):
        if self.pilha_esta_cheia():
            raise PilhaCheiaError("Pilha está cheia")
        
        elif not isinstance(dado, int):
            raise TipoError("Tipo incorreto")
    
        else:
            self.items.append(dado)
            return f'O valor {dado} foi adicionado ao topo da pilha. \nPilha atualizada: {self.items}'

    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaError
        
        else:
            dado = self.items.pop()
            return dado, f'O valor {dado} foi removido do topo da pilha. \nPilha atualizada: {self.items}'

    def troca(self):
        dado_topo = self.items[-1]
        dado_seguinte = self.items[-2]

        self.items[-1] = dado_seguinte
        self.items[-2] = dado_topo

        return f'Os valores do topo ({dado_topo}) e o seguinte ({dado_seguinte}) foram trocados de posição. \nPilha atualizada: {self.items}'

    def tamanho(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return f'Pilha: {self.items}'


class PilhaVaziaError(Exception):
    pass


class PilhaCheiaError(Exception):
    pass


class TipoError(Exception):
    pass


### PREENCHE REGIAO ###

# RECURSIVO

def preencher_regiao_recursiva(matriz, posicao_inicial_linha, posicao_inicial_coluna):
    # Verificar se a psição está dentro dos limites da matriz
    if posicao_inicial_linha < 0 or posicao_inicial_linha >= len(matriz) or posicao_inicial_coluna < 0 or posicao_inicial_coluna >= len(matriz[0]):
        return

    # Verificar se a célula já foi visitada ou se é uma das bordas da matriz
    if matriz[posicao_inicial_linha][posicao_inicial_coluna] != 0:
        return

    # Preencher a célula visitada com 1
    matriz[posicao_inicial_linha][posicao_inicial_coluna] = 1

    # Chamar a função recursivamente para as células vizinhas (até que os limites sejam encontrados)
    preencher_regiao_recursiva(matriz, posicao_inicial_linha - 1, posicao_inicial_coluna)  # Célula acima
    preencher_regiao_recursiva(matriz, posicao_inicial_linha + 1, posicao_inicial_coluna)  # Célula abaixo
    preencher_regiao_recursiva(matriz, posicao_inicial_linha, posicao_inicial_coluna - 1)  # Célula à esquerda
    preencher_regiao_recursiva(matriz, posicao_inicial_linha, posicao_inicial_coluna + 1)  # Célula à direita

# Função para preencher a matriz a partir de uma posição inicial
def preencher_tudo_recursivo(matriz, posicao_inicial_linha, posicao_inicial_coluna):
    if matriz[posicao_inicial_linha][posicao_inicial_coluna] == 0:
        preencher_regiao_recursiva(matriz, posicao_inicial_linha, posicao_inicial_coluna)


# PILHA
def preencher_regiao_pilha(matriz, linha_inicial, coluna_inicial):
    pilha = Pilha(len(matriz) * len(matriz[0])) # Criando uma pilha com capacidade suficiente para a matriz
    pilha.empilha(linha_inicial * len(matriz[0]) + coluna_inicial)  # Empilhando a posição inicial

    while not pilha.pilha_esta_vazia():
        posicao = pilha.desempilha()[0]  # Desempilhar a posição atual
        linha = posicao // len(matriz[0])
        coluna = posicao % len(matriz[0])

        # Verificar se a posição é válida e se ela ainda não foi preenchida
        if 0 <= linha < len(matriz) and 0 <= coluna < len(matriz[0]) and matriz[linha][coluna] == '0':
            matriz[linha][coluna] = '1'  # Marqcar a célula preenchida com 1

            # Empilhar as posições vizinhas
            pilha.empilha((linha - 1) * len(matriz[0]) + coluna)  # Célula acima
            pilha.empilha((linha + 1) * len(matriz[0]) + coluna)  # Célula abaixo
            pilha.empilha(linha * len(matriz[0]) + coluna - 1)  # Célula à esquerda
            pilha.empilha(linha * len(matriz[0]) + coluna + 1)  # Célula à direita



# Função para imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(' '.join(linha))

# Exemplo de uso:
matriz = [
    ['1', '0', '0', '0'],
    ['0', '1', '0', '0'],
    ['1', '0', '1', '1'],
    ['1', '0', '0', '1'],
    ['0', '0', '0', '1'],
    ['1', '1', '1', '1']
]

linha_inicial = 4
coluna_inicial = 1

preencher_regiao_pilha(matriz, linha_inicial, coluna_inicial)

# Imprime a matriz resultante
imprimir_matriz(matriz)