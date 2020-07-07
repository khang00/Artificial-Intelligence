import math


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(n):
    sequence = [0, 1]
    first = 0
    second = 1
    for i in range(2, n):
        third = first + second
        sequence.append(third)
        first = second
        second = third

    return sequence


def map_collection(collection, f):
    for i in range(len(collection)):
        collection[i] = f(collection[i])
    return collection


def is_prime(number):
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def mutate(groups):
    groups.append(1)


def main():
    group = []
    for item in group:
        print(item)


if __name__ == "__main__":
    main()
