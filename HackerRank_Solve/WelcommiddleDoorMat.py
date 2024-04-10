def print_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    mat = pattern + [welcome] + pattern[::-1]
    print('\n'.join(mat))

if __name__ == "__main__":
    N, M = map(int, input().split())
    print_door_mat(N, M)
