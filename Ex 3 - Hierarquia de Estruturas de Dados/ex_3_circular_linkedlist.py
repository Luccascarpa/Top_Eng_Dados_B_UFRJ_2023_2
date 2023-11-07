class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

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

# Testing - exercício de geometria

def calculate_perimeter(list_):
    if list_.head is None:
        return 0

    current = list_.head
    perimeter = 0.0

    while current.next != list_.head:
        # Assumindo que os dados são coordenadas x, y dos vértices do triângulo
        perimeter += ((current.data[0] - current.next.data[0]) ** 2 + (current.data[1] - current.next.data[1]) ** 2) ** 0.5
        current = current.next

    perimeter += ((current.data[0] - list_.head.data[0]) ** 2 + (current.data[1] - list_.head.data[1]) ** 2) ** 0.5
    return perimeter

# Criando um triângulo com os vértices
triangulo = CircularLinkedList(size=3)
triangulo.push((0, 0))  # Vértice 1
triangulo.push((3, 0))  # Vértice 2
triangulo.push((0, 4))  # Vértice 3

# Calculando o perímetro do triângulo
perimetro = calculate_perimeter(triangulo)
print("O perímetro do triângulo é:", perimetro)
