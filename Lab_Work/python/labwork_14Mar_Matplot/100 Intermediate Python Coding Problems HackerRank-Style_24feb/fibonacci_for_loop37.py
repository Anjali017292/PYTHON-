# Generate Fibonacci series up to n terms using a for loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a)
    a, b = b, a + b
'''#Output:
Enter the number of terms: 10
Fibonacci series:
0
1
1
2
3
5
8
13
21
34'''