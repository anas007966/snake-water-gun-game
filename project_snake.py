import random
import playsound

def winning_music():
    """
    Plays the winning music.
    """
    win_music = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print("Error playing winning sound:", e)

def losing_music():
    """
    Plays the losing music.
    """
    lose_music = ["Nope.mp3", "Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print("Error playing losing sound:", e)

def tie_music():
    """
    Plays the tie music.
    """
    try:
        playsound.playsound("Awkward Cricket.mp3")
    except Exception as e:
        print("Error playing tie sound:", e)

# Main game starts here
if __name__ == "__main__":
    print("\nWelcome to the Snake Water Gun game!\n")

    attempts = 1
    your_point = 0
    computer_point = 0

    while attempts <= 10:
        options = ["s", "w", "g"]
        computer_choice = random.choice(options)

        inp = input("Enter your choice (Snake(s), Water(w), Gun(g)): ").lower()

        if inp == computer_choice:
            print("Tie")
            print(f"\nYou chose {inp} and Computer also chose {computer_choice}! ")
            print("Nobody gets a point\n")
            tie_music()

        elif inp == "s" and computer_choice == "w":
            your_point += 1
            print(f"\nYou chose snake and Computer chose water!")
            print("The snake drank the water.\nYou won this round.")
            print("You got 1 point\n")
            winning_music()

        elif inp == "w" and computer_choice == "s":
            computer_point += 1
            print(f"\nYou chose water and Computer chose snake!")
            print("The snake drank the water.\nYou lost this round.")
            print("Computer gets 1 point\n")
            losing_music()

        elif inp == "w" and computer_choice == "g":
            your_point += 1
            print(f"\nYou chose water and Computer chose gun!")
            print("The gun sank in water.\nYou won this round.")
            print("You got 1 point\n")
            winning_music()

        elif inp == "g" and computer_choice == "w":
            computer_point += 1
            print(f"\nYou chose gun and Computer chose water!")
            print("The gun sank in water.\nYou lost this round.")
            print("Computer gets 1 point\n")
            losing_music()

        elif inp == "g" and computer_choice == "s":
            your_point += 1
            print(f"\nYou chose gun and Computer chose snake!")
            print("The snake was shot and it died.\nYou won this round.")
            print("You got 1 point\n")
            winning_music()

        elif inp == "s" and computer_choice == "g":
            computer_point += 1
            print(f"\nYou chose snake and Computer chose gun!")
            print("The snake was shot and died.\nYou lost this round.")
            print("Computer gets 1 point\n")
            losing_music()

        else:
            print("Invalid input! Please enter s, w, or g.\n")
            continue

        print("No. of guesses left:", 10 - attempts)
        attempts += 1

    # Game summary
    print("\nGame over!\n")
    print(f"Your score: {your_point} \nComputer's score: {computer_point}")

    if computer_point > your_point:
        print("Computer won and you lost!")
    elif computer_point < your_point:
        print("You won and the computer lost!")
    else:
        print("It was a tie!")

    print(f"\nFinal Score: You = {your_point}, Computer = {computer_point}\n")
