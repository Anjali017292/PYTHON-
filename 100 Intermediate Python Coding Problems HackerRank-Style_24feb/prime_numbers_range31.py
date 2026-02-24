# Generate prime numbers in between 1 to n
n = int(input("Enter the range: "))
print("Prime numbers between 1 and", n, "are:")
# Iterate through the numbers from 1 to n
for num in range(1, n + 1):
    # Check if the number is greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            

'''Output:
Enter the range: 20
Prime numbers between 1 and 20 are:
2
3
5
7
11
13
17
19
'''