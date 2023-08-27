def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

arr = [10, 324, 45, 11, 13, 17, 19, 23, 9808]

prime_numbers = [num for num in arr if is_prime(num)]

print("Prime numbers in the array:", prime_numbers)
