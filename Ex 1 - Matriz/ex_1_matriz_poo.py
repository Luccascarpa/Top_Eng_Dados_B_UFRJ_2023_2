def is_squared(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    return rows == cols

def is_upper_triangular(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != 0:
                return False

    return True

def is_lower_triangular(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False

    return True


class MatrixCalculator:
    '''Classe utilizada para criar as operações de uma calculadora matricial'''
    def __init__(self, matrix1, matrix2=[[0]]):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def add_matrices(self):
        '''Operação de adição matricial'''
        if len(self.matrix1) != len(self.matrix2) or len(self.matrix1[0]) != len(self.matrix2[0]):
            raise ValueError("Para realizar a operação de soma matricial as duas matrizes devem ter as mesmas dimensões.")
        
        result_matrix = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] + self.matrix2[i][j])
            result_matrix.append(row)

        return result_matrix
    
    def subtract_matrices(self):
        '''Operação de subtração matricial'''
        if len(self.matrix1) != len(self.matrix2) or len(self.matrix1[0]) != len(self.matrix2[0]):
            raise ValueError("Para realizar a operação de soma matricial as duas matrizes devem ter as mesmas dimensões.")
        
        result_matrix = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] - self.matrix2[i][j])
            result_matrix.append(row)

        return result_matrix
    
    def multiply_by_scalar(self, scalar):
        '''Operação de multiplicação por um número escalar'''
        result_matrix = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] * scalar)
            result_matrix.append(row)

        return result_matrix
    
    def multiply_matrices(self):
        '''Operação de multiplicação matricial'''
        if len(self.matrix1[0]) != len(self.matrix2):
            raise ValueError("""Para realizar a operação de multiplicação entre matrizes, a segunda
                            matriz deve ter o número de linhas igual ao número de colunas da primeira""")

        result_matrix = []
        for i in range(len(self.matrix1)):
            row = []
            for k in range(len(self.matrix2[0])):
                element = 0
                for j in range(len(self.matrix2)):
                    element += self.matrix1[i][j] * self.matrix2[j][k]
                row.append(element)
            result_matrix.append(row)

        return result_matrix

    
    def transpose(self):
        rows = len(self.matrix1)
        cols = len(self.matrix1[0])

        # matriz vazia com as dimensões 'contrárias'
        transposed_matrix = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = self.matrix1[i][j]

        return transposed_matrix
    
    def matrix_trace(self):
        if not is_squared(self.matrix1):
            raise ValueError("Para calcular o traço a matriz inserida deve ser quadrada")

        main_diagonal_sum = 0
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix1[0])):
                if i == j:
                    main_diagonal_sum += self.matrix1[i][j]
        
        return main_diagonal_sum
    
    def matrix_determinant(self):
        if not is_lower_triangular(self.matrix1) and not is_upper_triangular(self.matrix1):
            raise ValueError("Para calcular o determinante a matriz inserida deve ser triangular")

        main_diagonal_product = 1
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix1[0])):
                if i == j:
                    main_diagonal_product *= self.matrix1[i][j]

        return main_diagonal_product

# Função para imprimir matrizes
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Função para criar matrizes
def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        print(f"\nCriando a linha {i}")
        for j in range(m):
            value_ij = int(input(f"\nInforme o valor para a posição ({i},{j}): "))
            matrix[i][j]=value_ij
    return matrix
    
# Criar "Páginas" da calculadora
def addition_page():
    print("\n")
    print("----- ADIÇÃO DE MATRIZES -----")
    print("\nVamos criar suas matrizes com mesma ordem")
    n = int(input("Quantas linhas terão as matrizes? "))
    m = int(input("E quantas colunas terão as matrizes? "))

    print("\nCriando a primeira matriz:")
    matrix1 = create_matrix(n,m)
    
    print("Matriz 1 criada:")
    print_matrix(matrix1)

    print("\nCriando a segunda matriz:")

    matrix2 = create_matrix(n,m)
    
    print("Matriz 2 criada:")
    print_matrix(matrix2)

    print("\nDeseja somar as matrizes abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print("Matriz 1:")
    print_matrix(matrix1)
    print("Matriz 2: ")
    print_matrix(matrix2)
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nSomando as matrizes...")
        matrix_calculator = MatrixCalculator(matrix1, matrix2)
        print("Resultado:\n")
        print_matrix(matrix_calculator.add_matrices())

    return False


def subtraction_page():
    print("\n")
    print("----- SUBTRAÇÃO DE MATRIZES -----")
    print("\nVamos criar suas matrizes com mesma ordem")
    n = int(input("Quantas linhas terão as matrizes? "))
    m = int(input("E quantas colunas terão as matrizes? "))

    print("\nCriando a primeira matriz:")
    matrix1 = create_matrix(n,m)
    
    print("Matriz 1 criada:")
    print_matrix(matrix1)

    print("\nCriando a segunda matriz:")

    matrix2 = create_matrix(n,m)
    
    print("Matriz 2 criada:")
    print_matrix(matrix2)

    print("\nDeseja subtrair as matrizes abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print("Matriz 1:")
    print_matrix(matrix1)
    print("Matriz 2: ")
    print_matrix(matrix2)
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nSubtraindo as matrizes...")
        matrix_calculator = MatrixCalculator(matrix1, matrix2)
        print("Resultado:\n")
        print_matrix(matrix_calculator.subtract_matrices())

    return False


def multiply_by_scalar_page():
    print("\n")
    print("----- MULTIPLICAÇÃO POR ESCALAR -----")
    print("\nVamos criar sua matriz")
    n = int(input("Quantas linhas terá a matriz? "))
    m = int(input("E quantas colunas terá a matriz? "))

    print("\nCriando a matriz")
    matrix = create_matrix(n,m)
    
    print("Matriz criada:")
    print_matrix(matrix)

    scalar = int(input("\nPor qual escalar deseja multiplicar a matriz? "))

    print("Deseja multiplicar a matriz: ")
    print_matrix(matrix)
    print(f"pelo escalar {scalar} ?\nSe sim, digite 1, se tiver algo de errado, 2")
    
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nMultiplicando...")
        matrix_calculator = MatrixCalculator(matrix)
        print("Resultado:\n")
        print_matrix(matrix_calculator.multiply_by_scalar(scalar))

    return False

# Criar "Páginas" da calculadora
def multiplication_page():
    print("\n")
    print("----- MULTIPLICAÇÃO DE MATRIZES -----")
    print("\nVamos criar suas matrizes. \nLembre-se que a segunda matriz deve ter o número de linhas igual ao número de colunas da primeira.")
    print("\nCriando a primeira matriz:")
    n = int(input("Quantas linhas terá a primeira matriz? "))
    m = int(input("E quantas colunas terá a primeira matriz? "))

    matrix1 = create_matrix(n,m)
    
    print("Matriz 1 criada:")
    print_matrix(matrix1)

    print("\nCriando a segunda matriz:")
    print("Número de linhas: ", n)
    m2 = int(input("Quantas colunas terá a segunda matriz? "))

    matrix2 = create_matrix(n,m2)
    
    print("Matriz 2 criada:")
    print_matrix(matrix2)

    print("\nDeseja multiplicar as matrizes abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print("Matriz 1:")
    print_matrix(matrix1)
    print("Matriz 2: ")
    print_matrix(matrix2)
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nMultiplicando as matrizes...")
        matrix_calculator = MatrixCalculator(matrix1, matrix2)
        print("Resultado:\n")
        print_matrix(matrix_calculator.multiply_matrices())

    return False

def transpose_page():
    print("\n")
    print("----- TRANSPOSIÇÃO -----")
    print("\nVamos criar sua matriz")
    n = int(input("Quantas linhas terá a matriz? "))
    m = int(input("E quantas colunas terá a matriz? "))

    print("\nCriando a matriz")
    matrix = create_matrix(n,m)
    
    print("Matriz criada:")
    print_matrix(matrix)

    print("\nDeseja transpor a matriz abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print_matrix(matrix)
    
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nTranspondo...")
        matrix_calculator = MatrixCalculator(matrix)
        print("Resultado:\n")
        print_matrix(matrix_calculator.transpose())

    return False

def trace_page():
    print("\n")
    print("----- TRAÇO -----")
    print("\nVamos criar sua matriz quadrada")
    n = int(input("Quantas linhas/colunas terá a matriz? "))
    m = n

    print("\nCriando a matriz")
    matrix = create_matrix(n,m)
    
    print("Matriz criada:")
    print_matrix(matrix)

    print("\nDeseja calcular o traço da matriz abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print_matrix(matrix)
    
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nCalculando o traço...")
        matrix_calculator = MatrixCalculator(matrix)
        print("Resultado:\n")
        print(f'Traço: {matrix_calculator.matrix_trace()}')

    return False

def determinant_page():
    print("\n")
    print("----- DETERMINANTE -----")
    print("\nVamos criar sua matriz, lembre-se que ela deve ser triangular")
    n = int(input("Quantas linhas terá a matriz? "))
    m = int(input("Quantas colunas terá a matriz? "))

    print("\nCriando a matriz")
    matrix = create_matrix(n,m)
    
    print("Matriz criada:")
    print_matrix(matrix)

    print("\nDeseja calcular o determinante da matriz abaixo?\nSe sim, digite 1, se tiver algo de errado, 2")
    print_matrix(matrix)
    
    decision = input("Continuar: ")

    if int(decision) == 1:
        print("\nCalculando o traço...")
        matrix_calculator = MatrixCalculator(matrix)
        print("Resultado:\n")
        print(f'Determinante: {matrix_calculator.matrix_determinant()}')

    return False

# Testando
if __name__ == "__main__":
    print("Bem vindo à calculadora de matrizes")
    print("Operações disponíveis:")
    print("\t1 - Adição de matrizes")
    print("\t2 - Subtração de matrizes")
    print("\t3 - Multiplicação de matriz por um escalar")
    print("\t4 - Multiplicação de matrizes")
    print("\t5 - Transposição de matriz")
    print("\t6 - Cálculo deo traço da matriz")
    print("\t7 - Cálculo do determinante da matriz")
    op = int(input("\nQual operação deseja realizar? "))

    paths = {
        1: addition_page,
        2: subtraction_page,
        3: multiply_by_scalar_page,
        4: multiplication_page,
        5: transpose_page,
        6: trace_page,
        7: determinant_page
    }

    paths[op]()

    # matrix1 = [[1, 2, 3], [4, 5, 6]]
    # matrix2 = [[9, 0, 0], [6, 5, 0], [3, 2, 1]]

    # calculator = MatrixCalculator(matrix2, matrix1)

    # try:
    #     result = calculator.matrix_determinant()
    #     print("Resultado da soma das matrizes: ")
    #     print(result)
    # except ValueError as e:
    #     print(e)