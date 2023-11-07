class Abstract:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None]

    def length(self):
        len([item for item in self.data if item])

    def is_empty(self):
        self.length() == 0

    def is_full(self):
        self.length() >= self.capacity

    def create_from_list(self, list_):
        if len(list_) <= self.capacity:
            for item in list_:  
                self.insert(item)
        else:
            return "Lista é grande demais"

    def push(self, value):
        if not self.is_full():
            for idx, item in enumerate(self.data):
                if not item:
                    self.data['index'] = value
                else:
                    continue
        else:
            "Lista está cheia"

    def swap(self, index, value):
        self.data[index] = value

    def pop(self, index):
        poped_value = self.data[index]
        self.data[index] = None
        return poped_value

    def get_item(self, index):
        return self.data[index]


### Classe Array ###

class Array:
    def __init__(self,capacity=10, retractable=True):
        self.capacity = capacity
        self.size = 0
        self.data=[None] * self.capacity
        self.retractable = retractable

    def current_size(self):
        return len([item for item in self.data if item])

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora do alcance da estrutura")
        return self.data[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora do alcance da estrutura")
        self.data[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self._expand_capacity()
        self.data[self.size] = value
        self.size += 1

    def _expand_capacity(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def remove_item(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora do alcance da estrutura")
        
        value = self.data[index]
        self.data[index] = None
        self.size -= 1

        if self.retractable and self.size == self.capacity/2:
            self._retract_capacity()

        return value
    
    def _retract_capacity(self):
        self.capacity /= 2
        new_data = [item for item in self.data if item]
        self.data = new_data

    def __repr__(self):
        return f"Array: {self.data[:self.size]}"


### Classe Pilha ###

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


### Classe Lista encadeada simples ###
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_from_list(self, list_):
        for item in list_:
            self.push(item)

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        current = self.head
        self.head = current.next
        return current.data
    
    def get_i_item(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    
    def traverse_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


### Classe lista encadeada dupla ###
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_from_list(self, list_):
        for item in list_:
            self.push(item)
    
    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if not self.head:
            return None
        current = self.head
        if not current.next:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            self.head.prev = None
        return current.data
    
    def pop_back(self):
        if not self.tail:
            return None
        current = self.tail
        if not current.prev:
            self.head = None
            self.tail = None
        else:
            self.tail = current.prev
            self.tail.next = None
        return current.data
    
    def get_i_item(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    
    def swap(self, node_1, node_2):
        temporary = node_1.data
        node_1.data = node_2.data
        node_2.data = temporary

    def bubble_sort(self):
        if not self.head:
            return
        
        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                if current.data > current.next.data:
                    self.swap(current, current.next)
                current = current.next
            end = current

    def run_through_list(self, direction="BEGINNING_TO_END"):
        aux = None

        if direction == "BEGINNING_TO_END":
            aux = self.head
        else:
            aux = self.tail

        while aux:
            print(aux.data)
            if direction == "BEGINNING_TO_END":
                aux = aux.next
            else:
                aux = aux.prev


### Clase lista circular encadeada simples ###
class CircularLinkedList:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.current_size = 0

    def create_from_list(self, list_):
        for item in list_:
            self.push(item)
        
    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.current_size += 1
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.current_size += 1

    def pop(self, pointer):
        if not self.head  or self.current_size == 0:
            return None
        
        if pointer >= self.current_size:
            pointer = pointer % self.current_size # pensando na circularidade

        current = self.head
        previous = None
        count = 0

        while count < pointer:
            previous = current
            current = current.next
            count += 1

        if previous:
            previous.next = current.next
        
        else:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        self.current_size -= 1
        return current.data
    
    def get_i_item(self, index):
        if not self.head or self.current_size == 0:
            return None

        if index >= self.current_size:
            index = index % self.current_size

        current = self.head
        count = 0

        while count < index:
            current = current.next
            count += 1

        return current.data
    
    def swap(self, node_1, node_2):
        temp = node_1.data
        node_1.data = node_2.data
        node_2.data = temp

    def bubble_sort(self):
        if not self.head or self.current_size < 2:
            return
        
        current = self.head
        for i in range(self.current_size):
            current = self.head
            next_node = self.head.next

            for j in range(self.current_size -i -1):
                if current.data > next_node.data:
                    self.swap(current, next_node)
                current = next_node
                next_node = next_node.next

    def run_through_list(self):
        if not self.head or self.current_size == 0:
            return
        
        current = self.head
        print(current.data)

        while current.next != self.head:
            current = current.next
            print(current.data)


### Classe Fila Simples ###
import datetime

class Node:
    def __init__(self, user, tempo_atendimento):
        self.user = user
        self.tempo_espera = 0
        self.tempo_atendimento = tempo_atendimento
        self.hora_para_retirada = None
        self.next = None
        

class FilaSimples:
    def __init__(self):
        self.front = None  # início da fila
        self.rear = None  # fim da fila
        self.size = 0

    def esta_vazia(self):
        return self.front is None

    def entrar_na_fila(self, user, tempo_atendimento):
        new_node = Node(user, tempo_atendimento)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def sair_da_fila(self):
        if self.esta_vazia():
            return None

        user = self.front.user
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return user

    def atualizar_tempos_de_espera(self, tempo_real_horario_entrega):
        current = self.front
        tempo_real = datetime.datetime.strptime(tempo_real_horario_entrega, '%H:%M')
        posicao = 1  # Variável para controlar a posição na fila

        while current is not None:
            # Cálculo do tempo estimado de atendimento baseado na posição na fila e no tempo médio de atendimento
            current.tempo_espera = posicao * current.tempo_atendimento

            # Contador regressivo de tempo para atendimento
            tempo_entrega = tempo_real + datetime.timedelta(minutes=current.tempo_espera)
            current.hora_para_retirada = tempo_entrega.strftime('%H:%M')
            
            # Incremento da posição para considerar o próximo usuário na fila
            posicao += 1

            current = current.next
