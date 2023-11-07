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

# Testing
# Criação da lista
my_list = LinkedList()

# Criar a lista a partir de uma lista de inicialização
my_list.create_from_list([50, 40, 30, 20, 10])

# Inserir um elemento no início da lista
my_list.push(60)

# Consultar, remover e retornar o item de dados do início da lista
popped_item = my_list.pop()
print("Item removido:", popped_item)

# Consultar sem remover, retornar uma cópia do item de dado da posição i-ésima
index = 2
item_at_index = my_list.get_i_item(index)
if item_at_index is not None:
    print(f"Item na posição {index}:", item_at_index)
else:
    print(f"Posição {index} não encontrada na lista.")

# Percorrer e imprimir a lista
my_list.traverse_list()


