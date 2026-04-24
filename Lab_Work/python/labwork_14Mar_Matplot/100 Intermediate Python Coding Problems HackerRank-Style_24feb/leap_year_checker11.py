# Leap Year Checker
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
'''#output
Enter a year: 2020
2020 is a leap year.
Enter a year: 2021
2021 is not a leap year.'''