# Continuous Alphabet Pattern
ch = 65
for i in range(1,6):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
    
'''output:
A
B C
D E F
G H I J
K L M N O
'''