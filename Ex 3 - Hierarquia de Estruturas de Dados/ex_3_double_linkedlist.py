class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

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
        
# Testing

my_list = DoubleLinkedList()

my_list.create_from_list([50, 40, 30, 20, 10])

my_list.push(60)
my_list.push_back(5)

popped_item = my_list.pop()
print("Item removido do início:", popped_item)
popped_back_item = my_list.pop_back()
print("Item removido do fim:", popped_back_item)

index = 2
item_at_index = my_list.get_i_item(index)
if item_at_index is not None:
    print(f"Item na posição {index}:", item_at_index)
else:
    print(f"Posição {index} não encontrada na lista.")

node1 = my_list.head.next
node2 = my_list.head.next.next
my_list.swap(node1, node2)

my_list.bubble_sort()

print("\nPercorrendo a lista em ordem direta:")
my_list.run_through_list("BEGINNING_TO_END")
print("\nPercorrendo a lista em ordem inversa:")
my_list.run_through_list("END_TO_BEGINNING")
