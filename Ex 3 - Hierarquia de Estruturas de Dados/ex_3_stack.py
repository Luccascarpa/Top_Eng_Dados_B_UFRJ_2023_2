from array import array

class Stack:
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