#input a number and check if it is prime using a function
def is_prime(n):
    #check if n is less than 2, which are not prime numbers
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#call the is_prime function and print the result
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

'''
Output:
Enter a number: 17
17 is a prime number.
Enter a number: 15
15 is not a prime number.
'''