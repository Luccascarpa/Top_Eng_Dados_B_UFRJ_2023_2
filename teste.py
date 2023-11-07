class Pilha:
    def __init__(self, capacidade):
        self.items = []
        self.capacidade = capacidade

    def empilha(self, dado):
        if len(self.items) < self.capacidade:
            self.items.append(dado)
        else:
            raise PilhaCheiaError("Pilha está cheia")

    def desempilha(self):
        if not self.pilha_esta_vazia():
            return self.items.pop()

    def pilha_esta_vazia(self):
        return len(self.items) == 0

    def troca(self):
        if len(self.items) >= 2:
            self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

    def tamanho(self):
        return len(self.items)

class PilhaCheiaError(Exception):
    pass

def preenche_regiao(matriz, linha, coluna, capacidade_pilha):
    altura, largura = len(matriz), len(matriz[0])
    pilha = Pilha(capacidade_pilha)
    pilha.empilha((linha * largura + coluna))  # Inicialmente, empilhamos a posição inicial

    while not pilha.pilha_esta_vazia():
        posicao = pilha.desempilha()
        l, c = divmod(posicao, largura)

        # Verificamos se a posição é válida e se é 1
        if 0 <= l < altura and 0 <= c < largura and matriz[l][c] == 1:
            matriz[l][c] = 0  # Preenchendo com 0
            
            # Empilhamos as posições vizinhas
            pilha.empilha((l - 1) * largura + c)  # Vizinho superior
            pilha.empilha((l + 1) * largura + c)  # Vizinho inferior
            pilha.empilha(l * largura + c - 1)  # Vizinho esquerdo
            pilha.empilha(l * largura + c + 1)  # Vizinho direito

# Exemplo de uso
matriz = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Preencha a região a partir da posição (6, 9) com capacidade de pilha igual a 100
preenche_regiao(matriz, 6, 9, 100)

# Imprima a matriz após o preenchimento
for linha in matriz:
    print(" ".join(map(str, linha)))
