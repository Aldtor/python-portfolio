#6. Write a Program that generate a set of prime numbers and another set of odd numbers.
#Display the result of union, intersection, difference and symmetric difference operations.

odd = set([x * 2 + 1 for x in range(5)])
primes = set()
for i in range(2, 10):
    f = 0
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        primes.add(i)
print("Odd Numbers: ", odd)
print("Prime Numbers: ", primes)
print("Union: ", odd.union(primes))
print("Intersection: ", odd.intersection(primes))
print("Difference: ", odd.difference(primes))
print("Symmetric Difference: ", odd.symmetric_difference(primes))
