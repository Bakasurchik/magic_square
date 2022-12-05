# Добавление элементов в матрицу
def filling_matrix():
    n = int(input())
    matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
    return matrix

# Проверка, составлен ли квадрат из последовательности чисел 1-n^2
def is_square_1_n2(square):
    list_square = []
    for i in range(len(square)):
        list_square.extend(square[i])
    for i in range(1, len(list_square) + 1):
        if list_square.count(i) != 1:
            return False
    return True

# Проверка, является ли квадрат магическим
def is_square_magic(square):
    n = len(square)
    list_of_sums = [0] * (2)
    if not is_square_1_n2(square):
        return 'NO'
    # нахождение сумм
    for i in range(n):
        list_of_sums[0] += square[i][i]
        list_of_sums[1] += square[n - 1 - i][i]
        
        total = 0
        for j in range(n):
            total += square[j][i]
        list_of_sums.append(total)
        list_of_sums.append(sum(square[i]))
    
    # Проверка, равны ли суммы
    compare_number = list_of_sums[0]
    for elem in list_of_sums:
        if compare_number != elem:
            return 'NO'
        compare_number = elem
    return 'YES'

def main():
    matrix = filling_matrix()
    print(is_square_magic(matrix))

if __name__ == '__main__':
    main()