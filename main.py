def filling_matrix():
    n = int(input())
    matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
    return matrix



def main():
    print(filling_matrix())

if __name__ == '__main__':
    main()