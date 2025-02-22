import random

# Constants for the range of numbers
LOWER_BOUND = 1
UPPER_BOUND = 45
NUMBERS_PER_PICK = 6


def generate_quick_pick():
    # Generate a list of 6 unique random numbers between 1 and 45
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        num = random.randint(LOWER_BOUND, UPPER_BOUND)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()  # Sort the numbers in ascending order
    return quick_pick


def main():
    # Ask the user how many quick picks to generate
    num_picks = int(input("How many quick picks? "))

    # Generate the requested number of quick picks
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Print each pick, formatted to align neatly
        print(" ".join(f"{num:2}" for num in quick_pick))


# Run the program
if __name__ == "__main__":
    main()
