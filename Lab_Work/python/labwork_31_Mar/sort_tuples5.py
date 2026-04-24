# list of tuples (name, marks)
data = [("A", 50), ("B", 20), ("C", 40)]

# sort based on second value (marks)
data.sort(key=lambda x: x[1])

# display sorted data
print(data)

'''# Output:
[('B', 20), ('C', 40), ('A', 50)]
'''