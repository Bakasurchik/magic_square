def filling_matrix():
    n = int(input())
    matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
    return matrix

def is_square_magic(square):
    n = len(square)
    list_of_sums = [0] * (2)
    for i in range(n):
        list_of_sums[0] += square[i][i]
        list_of_sums[1] += square[n - 1 - i][i]
        
        total = 0
        for j in range(n):
            total += square[j][i]
        list_of_sums.append(total)
        list_of_sums.append(sum(square[i]))
    
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