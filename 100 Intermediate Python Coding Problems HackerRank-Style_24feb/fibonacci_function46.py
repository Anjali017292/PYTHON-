#input a number and generate the fibonacci series up to that number using a function
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

#call the fibonacci function and print the result
num = int(input("Enter a number: "))
result = fibonacci(num)
print(f"Fibonacci series up to {num}: {result}")

'''
Output:
Enter a number: 10
Fibonacci series up to 10: [0, 1, 1, 2, 3, 5, 8]
'''