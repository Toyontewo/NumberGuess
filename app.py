from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Function to check users guess against actual answer


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You Win. The answer is {answer}")

# Make function to set difficulty
def set_diff():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Choosing a random number between 1 and 100
def game():
    print("Welcome to the number Guessing Game!!")
    print("I'm thinking of a number from 1 to 100")
    answer = randint(1, 100)
    print(f"psssttt, the Answer is {answer}")

    turns = set_diff()


    guess = 0
    while guess != answer:
        print(f"You've got {turns} attempts remaining to guess the number")
        # Let the user guess a number
        guess = int(input("Make a Guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, You loose")
            return
        elif guess != answer:
            guess = int(input("Guess again: "))
            turns = check_answer(guess, answer, turns)
# TRack the number of turns and reduce by 1 if they get it wrong

game()
