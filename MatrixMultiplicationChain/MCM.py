def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]
    s = [[0] * (n+1) for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return "A" + str(i)
    else:
        return "(" + print_optimal_parens(s, i, s[i][j]) + "" + print_optimal_parens(s, s[i][j] + 1, j) + ")"

input_file = open("./input.txt", "r")
if not input_file:
    print("File doesn't exist.")
else:
    arr = []
    i = 0
    while 1:
        key = input_file.readline().strip()
        if not key:
            break
        arr.append(int(key))
        i += 1

    input_file.close()

    output_file = open("./output.txt", "w")
    m, s = matrix_chain_order(arr)
    output_file.write(str(m[1][len(arr)-1]) + "\n")
    output_file.write(print_optimal_parens(s, 1, len(arr)-1))
    output_file.close()
