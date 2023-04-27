def PARTITION_AROUND(A, p, r, x):
    # Implementation of the PARTITION-AROUND function
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def SELECT(A, p, r, i):
    # Implementation of the SELECT algorithm
    if p == r:
        return A[p]
    x = A[p + (r - p) // 2]  # Choose median of medians as pivot
    q = PARTITION_AROUND(A, p, r, x)
    k = q - p + 1  # Fix: Changed i - p + 1 to q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return SELECT(A, p, q - 1, i)
    else:
        return SELECT(A, q + 1, r, i - k)


# Read input from input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()
    k = int(lines[0].strip())  # Number of integers
    p = int(lines[1].strip())  # The p smallest number
    A = list(map(int, lines[2:]))

# Call SELECT function to find the p-th smallest number
result = SELECT(A, 0, len(A) - 1, p-1)  # Fix: Changed p to p-1
if result is None:
    result = "Element not found"

# Write output to output.txt
with open('output.txt', 'w') as f:
    f.write(f"{len(A)}\n")
    f.write(f"{p}\n")
    f.write(f"{result}\n")
