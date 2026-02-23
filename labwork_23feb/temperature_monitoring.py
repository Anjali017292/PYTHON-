
# Temperature Monitoring System

# Enter number of days
n = int(input("Enter number of days: "))

if n <= 0:
    print("Invalid number of days")
else:
    temps = []

    # Input temperatures
    for i in range(n):
        t = float(input("Enter temperature: "))
        temps.append(t)

    # Find hottest and coldest
    hottest = max(temps)
    coldest = min(temps)

    # Count extreme days (>40)
    extreme_days = 0
    for t in temps:
        if t > 40:
            extreme_days += 1

    # Replace temp above 45 with Heat Alert
    updated = []
    for t in temps:
        if t > 45:
            updated.append("Heat Alert")
        else:
            updated.append(t)

    # Output
    print("Hottest Temperature:", hottest)
    print("Coldest Temperature:", coldest)
    print("Extreme Days (>40°C):", extreme_days)
    print("Updated Temperature List:", updated)
    
'''#output
Enter number of days: 5
Enter temperature: 38
Enter temperature: 42
Enter temperature: 46
Enter temperature: 39
Enter temperature: 41
Hottest Temperature: 46.0
Coldest Temperature: 38.0
Extreme Days (>40°C): 2
Updated Temperature List: [38.0, 42.0, 'Heat Alert', 39.0, 41.0]
'''