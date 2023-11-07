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

# Testing    
arr = Array(capacity=3)
print(arr)
arr.append(5)
arr.append(10)
arr.append(15)
print(arr)
print(arr[1])
arr[1] = 20
print(arr)
arr.append(25)
print(arr)
arr.remove_item(2)
print(arr)
