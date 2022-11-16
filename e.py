
import math
for i in range(1, 4):
    print(i)


def checkPrime(num):
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0 and i < num:
            print(f'{num} ko la prime')
            break
    print(f'{num} la prime')


checkPrime(5270959501)
