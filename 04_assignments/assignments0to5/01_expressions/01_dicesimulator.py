import random  # Import the random module

def roll_dice():
    """Rolls two dice and returns the results as a tuple."""
    die1 = random.randint(1, 6)  # Generates a random number between 1 and 6
    die2 = random.randint(1, 6)
    return die1, die2  # Returns both dice rolls as a tuple

def main():
    for i in range(3):  # Loop to roll dice three times
        die1, die2 = roll_dice()  # Call roll_dice function
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}")  # Print results

if __name__ == '__main__':
    main()
