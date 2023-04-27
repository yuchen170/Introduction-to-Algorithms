def double_hashing(m, m_prime, n, nums):

    hash_table = [[] for _ in range(m)]  # Initialize hash table as list of empty slots
    total_collisions = 0
    average_collisions = 0.0
    collision=[]
    indexes=[]

    for num in nums:
        h1 = num % m  # Calculate initial hash value using first hash function
        h2 = m_prime - (num % m_prime)  # Calculate second hash function
        collisions = 0  # Initialize collisions for current element to 0
        i = 0  # Initialize probe number to 0
        while True:
            index = (h1 + i * h2) % m  # Calculate index using double hashing formula
            indexes.append(index)
            if len(hash_table[index]) == 0:  # If slot is empty, insert element
                hash_table[index].append(num)
                break
            else:
                collisions += 1  # Increment collisions count
                i += 1  # Increment probe number
                break
        collision.append(collisions)
        total_collisions += collisions  # Update total collisions count

    # Calculate average collisions
    if n > 0:
        average_collisions = float(total_collisions) / n

    return hash_table, total_collisions, average_collisions,collision,indexes

# Read input from input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()
    m, m_prime, n = map(int, lines[0].strip().split(','))  # Get m, m', n from first line
    nums = [int(line.strip()) for line in lines[1:]]  # Get nums from subsequent lines

# Call double_hashing function
hash_table, total_collisions, average_collisions,collision,indexes = double_hashing(m, m_prime, n, nums)

# Write output to output.txt
with open('output.txt', 'w') as f:
    f.write(f"{m}, {m_prime}, {n}\n")
    for i, num in enumerate(nums):
        f.write(f"{indexes[i]}, {collision[i]}\n")
    f.write(f"{total_collisions}, {average_collisions}\n")
