import datetime

class Node:
    def __init__(self, user, service_time):
        self.user = user
        self.wait_time = 0
        self.service_time = service_time
        self.pickup_time = None
        self.next = None
        

class Queue:
    def __init__(self):
        self.front = None  # início da queue
        self.back = None  # fim da queue
        self.size = 0

    def is_empty(self):
        return self.front is None

    def push(self, user, service_time): # entrar na queue
        new_node = Node(user, service_time)
        
        if self.back is None:
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.size += 1

    def pop(self): # sair da queue
        if self.esta_vazia():
            return None

        user = self.front.user
        self.front = self.front.next
        if self.front is None:
            self.back = None
        self.size -= 1
        return user

    def update_wait_times(self, real_delivery_time):
        current = self.front
        real_time = datetime.datetime.strptime(real_delivery_time, '%H:%M')
        position = 1  # Variável para controlar a posição na queue

        while current is not None:
            # Cálculo do tempo estimado de atendimento baseado na posição na queue e no tempo médio de atendimento
            current.wait_time = position * current.service_time

            # Contador regressivo de tempo para atendimento
            tempo_entrega = real_time + datetime.timedelta(minutes=current.wait_time)
            current.pickup_time = tempo_entrega.strftime('%H:%M')
            
            # Incremento da posição para considerar o próximo usuário na queue
            position += 1

            current = current.next

# Exemplo de uso da Queue (Problema do Bandejão)
queue = Queue()

# Adicionando usuários na queue (Usuário, tempo de atendimento em minutos)
queue.push("Usuário 1", 5)
queue.push("Usuário 2", 5)
queue.push("Usuário 3", 5)

# Simulação de retirada dos pratos
queue.update_wait_times('12:15')  # Simula o tempo real de entrega do prato

# Verificando a queue após atualização dos tempos de espera
print("fila após atualização dos tempos de espera:")
current = queue.front
while current is not None:
    print(f"Usuário: {current.user}, Tempo para retirada: {current.pickup_time}")
    current = current.next
