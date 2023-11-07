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
        if(len(self.matrix1[0]) != len(self.matrix2)):
            raise ValueError("""Para realizar a operação de multiplicação entre matrizes, a segunda
                             matriz deve ter o número de linhas igual ao número de colunas da primeira""")
        
        result_matrix = []
        for i in range(len(self.matrix1[0])):
            # print("i: ",i)
            row = []
            for k in range(len(self.matrix2[0])):
                element = []
                for j in range(len(self.matrix2)):
                    # print("j: ",j)
                    # print(self.matrix1[i][j])
                    # print(self.matrix2[j][i])
                    element.append(self.matrix1[i][j] * self.matrix2[j][k])
                row.append(sum(element))
            print(row)
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


# Testando
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[9, 0, 0], [6, 5, 0], [3, 2, 1]]

    calculator = MatrixCalculator(matrix2, matrix1)

    try:
        result = calculator.matrix_determinant()
        print("Resultado da soma das matrizes: ")
        print(result)
    except ValueError as e:
        print(e)