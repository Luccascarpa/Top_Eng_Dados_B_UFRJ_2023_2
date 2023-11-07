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

# Exemplo de uso da FilaSimples (Problema do Bandejão)
fila = FilaSimples()

# Adicionando usuários na fila (Usuário, tempo de atendimento em minutos)
fila.entrar_na_fila("Usuário 1", 5)
fila.entrar_na_fila("Usuário 2", 5)
fila.entrar_na_fila("Usuário 3", 5)

# Simulação de retirada dos pratos
fila.atualizar_tempos_de_espera('12:15')  # Simula o tempo real de entrega do prato

# Verificando a fila após atualização dos tempos de espera
print("Fila após atualização dos tempos de espera:")
current = fila.front
while current is not None:
    print(f"Usuário: {current.user}, Tempo para retirada: {current.hora_para_retirada}")
    current = current.next
