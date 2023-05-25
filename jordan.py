import copy


def solve_jordan(matrizA, matrizB):
    n = len(matrizA)
    matrizA_copy = copy.deepcopy(matrizA)
    matrizB_copy = copy.deepcopy(matrizB)

    # Eliminação de Gauss
    for i in range(n):
        # Encontra o pivô
        max_row = i
        for j in range(i + 1, n):
            if abs(matrizA_copy[j][i]) > abs(matrizA_copy[max_row][i]):
                max_row = j

        # Verifica se é possível pivotar
        if abs(matrizA_copy[max_row][i]) < 1e-12:
            return None  # não é possível pivotar, retorna None

        # Troca as linhas
        matrizA_copy[i], matrizA_copy[max_row] = matrizA_copy[max_row], matrizA_copy[i]
        matrizB_copy[i], matrizB_copy[max_row] = matrizB_copy[max_row], matrizB_copy[i]

        # Escalonamento
        for j in range(i + 1, n):
            factor = matrizA_copy[j][i] / matrizA_copy[i][i]
            matrizB_copy[j] -= factor * matrizB_copy[i]
            for k in range(i, n):
                matrizA_copy[j][k] -= factor * matrizA_copy[i][k]

    # Verifica se é possível resolver o sistema
    for i in range(n):
        if abs(matrizA_copy[i][i]) < 1e-12 and abs(matrizB_copy[i]) > 1e-12:
            return None  # não é possível resolver, retorna None

    # Eliminação de Jordan
    for i in range(n):
        pivot = matrizA_copy[i][i]
        if abs(pivot) < 1e-12:
            return None  # não é possível resolver, retorna None

        # Normaliza a linha pivô
        matrizA_copy[i] = [x / pivot for x in matrizA_copy[i]]
        matrizB_copy[i] /= pivot

        # Eliminação da coluna
        for j in range(n):
            if i != j:
                factor = matrizA_copy[j][i]
                matrizB_copy[j] -= factor * matrizB_copy[i]
                matrizA_copy[j] = [x - factor * y for x, y in zip(matrizA_copy[j], matrizA_copy[i])]

    # Arredonda o resultado para o inteiro mais próximo
    solucao_arredondada = [round(valor) for valor in matrizB_copy]
    
    return solucao_arredondada


# Exemplo de uso
def main():
    matriz_coeficientes = [[2, 2, 1, 1], 
                           [1, -1, 2, -1], 
                           [3, 2, -3, -2],
                           [4, 3, 2, 1]]
               
    vetor_termos_independetes = [7, 1, 4, 12]
    solucao = solve_jordan(matriz_coeficientes, vetor_termos_independetes)

    if solucao is None:
        print("Não é possível resolver o sistema utilizando o método de Jordan.")
    else:
        print(f"A solução do sistema é: {solucao}")  


if __name__ == '__main__':
    main()
