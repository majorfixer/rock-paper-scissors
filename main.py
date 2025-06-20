import random

value = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

# Skorlar
user_score = 0
computer_score = 0
draws = 0
turn = 1  # kaçıncı turda olduğumuzu takip eder

while True:
    try:
        RPS = int(input(f"\nRound {turn} - What do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
        if RPS not in [0, 1, 2]:
            print("Enter a number between 0 and 2.")
            continue

        choice = random.randint(0, 2)

        print(f"\nComputer chose: {value[choice]}\nYour choice: {value[RPS]}")

        if RPS == choice:
            print("Draw")
            draws += 1
        elif (RPS == 0 and choice == 2) or (RPS == 1 and choice == 0) or (RPS == 2 and choice == 1):
            print("You Win")
            user_score += 1
        else:
            print("You Lose")
            computer_score += 1

        # Her 11 turda bir kullanıcıya devam etmek istiyor mu diye sor
        if turn % 11 == 0:
            again = input("\nDo you want to continue playing? (yes/no): ").strip().lower()
            if again == "no":
                print("\n🧾 Final Score:")
                print(f"You: {user_score}")
                print(f"Computer: {computer_score}")
                print(f"Draws: {draws}")
                print("Thanks for playing!")
                break
            elif again != "yes":
                print("Invalid input. Continuing by default...")

        turn += 1

    except ValueError:
        print("Invalid input. Please enter a number.")