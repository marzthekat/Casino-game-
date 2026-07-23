import random
import time as tm

money = 100
running = True

def sleep(n):
    return tm.sleep(n)

def typewrite(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        tm.sleep(delay)
    print()

def typewrite_input(prompt, delay=0.03, dot_delay=0.5):
    for char in prompt:
        print(char, end='', flush=True)
        if char == '.':
            tm.sleep(dot_delay)
        else:
            tm.sleep(delay)
    return input()

def normalize_text(text):
    return text.strip().lower()


def headortails():
    global money
    typewrite("Welcome to the Coin Flip Game!")
    typewrite(f"You have ${money} to start with. Bet wisely.")

    while money > 0:
        typewrite(f"\nYou currently have ${money}.")
        try:
            bet = int(input("Enter your bet amount (or 0 to quit): "))
        except ValueError:
            typewrite("please enter a valid number!!!")
            continue

        if bet == 0:
            typewrite("Thanks for playing Coin Flip.")
            break
        elif bet < 0:
            typewrite("You cannot bet negative amounts.")
            continue
        elif bet > money:
            typewrite("You can't bet more money than you have.")
            continue

        outcome = random.choice(["heads", "tails"])

        if outcome == "heads":
            money += bet
            typewrite(f"The outcome is HEADS! You now have ${money}.")
            typewrite("Congratulations, you won!")
        else:
            money -= bet
            typewrite(f"The outcome is TAILS! You now have ${money}.")
            typewrite("Sorry, you lost.")

    if money <= 0:
        typewrite("You ran out of money! Game over.")

def rollthedice():
    global money # python searches locally first, then globally. this is telling python to search for the global money variable first, and only.
    typewrite("welcome to roll the dice.")
    typewrite("guess a number between 1 and 6. you double your bet if your right.")

    roll_choice = normalize_text(typewrite_input("do you want to roll? (yes/no): "))

    if roll_choice == 'yes':
        while money > 0:
            typewrite(f"\nyoou currently have ${money}.")
            try:
                bet = int(input("Enter bet amount (0 to quit): "))
                if bet == 0:
                    break
                if bet > money or bet < 0:
                    typewrite("Invalid bet amount.")
                    continue

                guess = int(input("Guess the dice roll (1-6): "))
                if guess < 1 or guess > 6:
                    typewrite("Please pick a number between 1 and 6.")
                    continue
            except ValueError:
                typewrite("please enter valid numbers.")
                continue

            typewrite("Rolling...")
            sleep(1)

            dice_result = random.randint(1, 6)
            typewrite(f"The die landed on: {dice_result}")

            if guess == dice_result:
                money += bet * 2
                typewrite(f"nice hit you doubled your bet. Current money: ${money}")
            else:
                money -= bet
                typewrite(f"you lost ${bet}. Current money: ${money}")


def slotmachine():
    global money
    typewrite ("welcome to the slot machine game!")
    typewrite ("you have $100 to start with, bet wisely.")
    typewrite ("if you run out of money, the game will end.")
    while money > 0:
        typewrite (f"you currently have ${money}.")
        bet = int(input("enter your bet amount (or type 0 to quit): "))
        if bet == 0:
            typewrite ("thanks for playing.")
            break
        elif bet < 0:
            typewrite ("you can't bet a negative amount.")
            continue
        elif bet > money:
            typewrite ("you cant bet more than you have.")
            continue
        outcome = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar"])
        typewrite (f"the outcome is {outcome}.")
        if outcome == "cherry":
            money += bet * 4
            typewrite (f"congratulations, you won ${bet * 4}!")
        else:
            money -= bet
            typewrite (f"sorry, you lost ${bet}.")
    if money <= 0:
        typewrite ("you ran out of money, game over.")

def story():
    typewrite("welcome to story mode, this is a work in progress so it is unfinished.")
    typewrite("You have $100 as a starting amount. Choose the game you want to play to earn or lose money.")


while running:
    typewrite("1. Heads or Tails")
    typewrite("2. Story Mode")
    typewrite("3. Roll the Dice")
    typewrite("4. Slot Machine")
    typewrite("0. Quit Game")

    try:
        choice = int(typewrite_input("Make a choice (0 - 4): "))
    except ValueError:
        typewrite("invalid input. number please.")
        continue

    if choice == 1:
        headortails()
    elif choice == 2:
        story()
    elif choice == 3:
        rollthedice()
    elif choice == 4:
        slotmachine()
        typewrite("game isn't finished but enjoy!")
    elif choice == 0:
        typewrite("thank you for playing")
        running = False
    else:
        typewrite("invalid. please select between 0 and 4")
story()
