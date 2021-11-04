def Largest_Prime_Factor(n):
    prime_factor = 0
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor


n = input("Enter a number to find the largest prime factor: ")
print(Largest_Prime_Factor(int(n)))
