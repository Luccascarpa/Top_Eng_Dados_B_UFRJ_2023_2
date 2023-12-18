import csv

class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Para casos reais, vale utilizar uma função de hash mais robusta, como SHA-256
        return hash(key) % self.size

    def set_val(self, key, value):
        hashed_key = self.hash_function(key)
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break  # Adiciona esta linha para interromper a iteração ao encontrar o email
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = self.hash_function(key)
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                return record_value
        return "No record found with that email address"

    def remove_val(self, key):
        hashed_key = self.hash_function(key)
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            del bucket[index]
            self.write_to_csv('hash_project_data.csv')  # Atualiza o CSV após a remoção
            print("\nEmail removido com sucesso!")
        else:
            print("\nNo record found with that email address")

    def write_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding="ISO-8859-1") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            for bucket in self.hash_table:
                for record in bucket:
                    csv_writer.writerow(record)

    def __str__(self):
        table_str = "Hash Table:\n"
        for i, bucket in enumerate(self.hash_table):
            table_str += f"Bucket {i}: {bucket}\n"
        return table_str


# Inicializa a tabela hash
hash_table = AlgoHashTable(256)

# Abre o arquivo CSV
with open('hash_project_data.csv', 'r', encoding="ISO-8859-1") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Itera sobre as linhas do CSV
    for row in csv_reader:
        # Assume que a primeira coluna é a chave e a segunda coluna é o valor
        key, value = row
        # Adiciona o par chave-valor à tabela hash
        hash_table.set_val(key, value)

sep = 100
run = True
while run:
    print("\n" + '-'*sep)
    decision = input("Para buscar email, digite 1. Para cadastrar novo email, digite 2. Para remover email, digite 3. Para mostrar a tabela hash, digite 4. Para sair, digite 0: ")

    if decision == "0":
        run = False
    elif decision == "1":
        email = input(f'\nInsira seu email para buscar sua frase correspondente: ')
        print("\n" + '-'*sep)
        print("\nEmail: ", email)
        print("Frase: ", hash_table.get_val(email))
    elif decision == "2":
        new_email = input("\nInsira o novo email: ")
        new_frase = input("Insira a nova frase: ")
        hash_table.set_val(new_email, new_frase)
        print("\n" + '-'*sep)
        print("\nNovo email cadastrado com sucesso!")
    elif decision == "3":
        remove_email = input("\nInsira o email a ser removido: ")
        hash_table.remove_val(remove_email)
    elif decision == "4":
        print("\n" + '-'*sep)
        print(hash_table)  # Mostra a tabela hash
    else:
        print("Opção inválida")

print("\n" + '-'*sep)
print("Programa encerrado.")