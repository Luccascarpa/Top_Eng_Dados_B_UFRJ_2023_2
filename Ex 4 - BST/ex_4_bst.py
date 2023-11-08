class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, current, key, data):
        if key < current.key:
            if not current.left_child:
                current.left_child = Node(key, data)
            else:
                self._insert(current.left_child, key, data)
        elif key > current.key:
            if not current.right_child:
                current.right_child = Node(key, data)
            else:
                self._insert(current.right_child, key, data)

    def in_order(self):
        '''left, root, right'''
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end=" ")

    def find_value(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, current, key):
        if current:
            if key == current.key:
                return current.data
            elif key < current.key:
                return self._find_value(current.left_child, key)
            else:
                return self._find_value(current.right_child, key)
        else:
            return f"Chave {key} não encontrada na árvore"
        
    def delete_value(self, key):
        self.root = self._delete_value(self.root, key)

    def _delete_value(self, current, key):
        if not current:
            return current

        if key < current.key:
            current.left_child = self._delete_value(current.left_child, key)
        elif key > current.key:
            current.right_child = self._delete_value(current.right_child, key)
        else:
            if not current.left_child:
                temp = current.right_child
                current = None
                return temp
            elif not current.right_child:
                temp = current.left_child
                current = None
                return temp

            temp = self.min_right_subtree(current.right_child)
            current.key = temp.key
            current.data = temp.data
            current.right_child = self._delete_value(current.right_child, temp.key)

        return current

    def min_right_subtree(self, current):
        if not current.left_child:
            return current
        return self.min_right_subtree(current.left_child)
    

# Testing - CPFs

bst = BST()
# Criando registros onde o cpf é a chave e o nome é o valor (usanod 3 cpfs gerados aletoriamente, que funcionam como inteiros neste caso)
registros = {
    45367892184: "João",
    78932145665: "Maria",
    21587634902: "Pedro",

}

# Inserindo registros
print('Testando a inserção de registros:\n')
for cpf, nome in registros.items():
    print(f'\tRegistro inserido: CPF: {cpf}, Nome {nome}')
    bst.insert(cpf, nome)
    print(f'\tÁrvore atualizada:\n')
    bst.in_order()
print('\n')

# Procurando um registro
print("Testando a busca de registros:\n")
cpfs_para_busca = [45367892184, 12345678900]
for idx, cpf_procurado in enumerate(cpfs_para_busca):
    print(f'\tBuscando o CPF: {cpf_procurado}\n...\n...\n...')
    encontrado = bst.find_value(cpf_procurado)
    if encontrado:
        print(f'\tRegistro encontrado para CPF {cpf_procurado}: {encontrado}\n')
    else:
        print(f'\tRegistro não encontrado para CPF {cpf_procurado}\n')

# Removendo registros
print("Testando a remoção de registros:\n")
print("\tPrimeiro, adicionando mais um registro (CPF: 12345678901, Nome: Manoella)")
bst.insert(12345678901, 'Manoella')
print("\tÁrvore atualizada com o novo registro:\n")
bst.in_order()
print('\tRemovendo o registro recém adicionado:\n')
bst.delete_value(12345678901)
print("\tRegistro com chave 12345678901 removido")
print("\tÁrvore atualizada com o registro removido:\n")
bst.in_order()

# Percorrendo em diferetntes ordens:
print("Percorrendo os registros em diferentes ordens:\n")

print("\tPercorrendo em pré-ordem:")
bst.pre_order()
print('\n')

print("\tPercorrendo em pós-ordem:")
bst.post_order()
print('\n')

print("\tPercorrendo em ordem:")
bst.in_order()