def solve(N):
    total_count = 0
    for num in range(1, N + 1):
        total_count += bin(num).count('1')
        print(bin(num))
    return total_count


N = int(input("Enter a number: "))
print(solve(N))
