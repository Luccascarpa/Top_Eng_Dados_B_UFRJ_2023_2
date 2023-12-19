import csv
import random

def generate_fake_cpf():
    return f'{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(10, 99)}'

def generate_fake_name():
    first_names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'David', 'Emma', 'Ethan', 'Olivia', 'Liam']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return f'{random.choice(first_names)} {random.choice(last_names)}'

def generate_fake_data(num_rows=100):
    data = []
    for _ in range(num_rows):
        data.append((generate_fake_cpf(), generate_fake_name()))
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# Gerar dados fictícios e escrever no arquivo CSV
csv_filename = 'input.csv'
fake_data = generate_fake_data(num_rows=100)
write_csv(csv_filename, fake_data)
