# -------------------------------------------------------
# Function to validate rating (1 to 5 only)
# -------------------------------------------------------
def is_valid_rating(value):
    try:
        rating = int(value)
        if 1 <= rating <= 5:
            return True
        else:
            return False
    except ValueError:
        return False


# -------------------------------------------------------
# Movie Rating System
# -------------------------------------------------------
def movie_rating_system():

    data = input("Enter movie ratings (1-5) separated by space: ").split()

    ratings = []

    # Validate ratings
    for item in data:
        if is_valid_rating(item):
            ratings.append(int(item))
        else:
            print(f"Invalid rating removed: {item}")

    if not ratings:
        print("No valid ratings entered.")
        return

    print("\nValid Ratings:", ratings)

    # Calculate average rating
    total = 0
    for r in ratings:
        total += r

    average = total / len(ratings)

    # Count 5-star ratings
    five_star_count = 0
    for r in ratings:
        if r == 5:
            five_star_count += 1

    # Sort ratings in ascending order
    ratings.sort()

    # Display results
    print(f"Average Rating: {average:.2f}")
    print(f"Number of 5-Star Ratings: {five_star_count}")
    print("Sorted Ratings (Ascending):", ratings)


# Run Program
movie_rating_system()







'''output
Enter movie ratings (1-5) separated by space: 5 4 3 2 1 6 0
Invalid rating removed: 6
Invalid rating removed: 0
Valid Ratings: [5, 4, 3, 2, 1]
Average Rating: 3.00
Number of 5-Star Ratings: 1
Sorted Ratings (Ascending): [1, 2, 3, 4, 5]
'''