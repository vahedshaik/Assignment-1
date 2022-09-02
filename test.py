#prime number
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    for n in range(1, 20):
        if is_prime(n):
            print(n, end=' ')
    print()

if __name__ == '__main__':
    main()

    #palindrome 
def is_palindrome(n):
    temp = n
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == n

def main():
    num = int(input('Please enter a number: '))
    if is_palindrome(num):
        print('%d is a palindrome.' % num)
    else:
        print('%d is not a palindrome.' % num)

if __name__ == '__main__':
    main()

#even number    
def is_even(n):
    return n % 2 == 0

def main():
    for n in range(1, 20):
        if is_even(n):
            print(n, end=' ')
    print()

if __name__ == '__main__':
    main()  
    
    #odd number
def is_odd(n):
    return n % 2 == 1

def main():
    for n in range(1, 20):
        if is_odd(n):
            print(n, end=' ')
    print()

if __name__ == '__main__':
    main()

    #random number generator
import random

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    return a + b + c

def main():
    print(roll_dice())
    print(roll_dice(3))
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(c=50, a=100, b=200))

if __name__ == '__main__':
    main()


#largest number
def max2(x, y):
    if x > y:
        return x
    else:
        return y

def max3(x, y, z):
    return max2(x, max2(y, z))

def main():
    print(max2(3, 5))
    print(max2(2, 1))
    print(max2(3, 3))
    print(max3(3, 6, 9))
    print(max3(9, 3, 6))
    print(max3(7, 8, 7))

if __name__ == '__main__':
    main()

    #factorial
