def find_primes_in_range(start, end):
    """
    Finds all prime numbers in a given range [start, end].

    Args:
        start (int): The beginning of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        list: A list containing all prime numbers found within the range.
    """
    prime_numbers = []
    # Ensure start is at least 2, as numbers less than 2 are not prime
    if start < 2:
        start = 2

    for num in range(start, end + 1):
        # A flag to check if the number is divisible by any other number
        is_prime = True
        # Optimization: check divisors up to the square root of num
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break  # Not prime, no need to check further

        if is_prime:
            prime_numbers.append(num)

    return prime_numbers


# Example usage:
start_range = 100
end_range = 200
primes = find_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range} are:")
print(primes)