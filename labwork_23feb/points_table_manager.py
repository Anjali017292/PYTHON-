# -------------------------------------------------------
# Function to validate team points (integer allowed)
# -------------------------------------------------------
def is_valid_points(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# -------------------------------------------------------
# Sports Tournament Points Table 
# -------------------------------------------------------
def sports_points_table():

    data = input("Enter team points separated by space: ")

    points = []
    number = ""

    # Manually extract numbers 
    for ch in data:
        if ch != " ":
            number += ch
        else:
            if number != "":
                if is_valid_points(number):
                    points.append(int(number))
                else:
                    print(f"Invalid points ignored: {number}")
                number = ""

    # Add last number
    if number != "":
        if is_valid_points(number):
            points.append(int(number))
        else:
            print(f"Invalid points ignored: {number}")

    if not points:
        print("No valid team points entered.")
        return

    print("\nOriginal Points:", points)

    # Sort leaderboard (descending order)
    points.sort(reverse=True)

    print("Sorted Leaderboard:", points)

    # Find winner and runner-up
    if len(points) >= 2:
        print(f"Winner Points: {points[0]}")
        print(f"Runner-Up Points: {points[1]}")
    elif len(points) == 1:
        print(f"Only one team. Winner Points: {points[0]}")
    else:
        print("Not enough teams to determine winner and runner-up.")


# Run Program
sports_points_table()




'''output example:
Enter team points separated by space: 10 20 15 5 25
Original Points: [10, 20, 15, 5, 25]
Sorted Leaderboard: [25, 20, 15, 10, 5]
Winner Points: 25
Runner-Up Points: 20
'''