import random
print("Let's play Rock, Scissor and Paper!")

options = ["rock", "scissor", "paper"]


while True:

    player_selection = int(input(
        "Choose\n(1) for Rock\n(2) for Scissor\n(3) for Paper\n\tPlease, type your selection: ")) - 1
    computer_selection = random.randint(0, 2)

    print(f"You choose {options[player_selection]}")
    print(f"The computer choose {options[computer_selection]}")

    if player_selection == computer_selection:
        print(
            f"{options[player_selection]} with {options[computer_selection]} is draw!")

    if player_selection == 0 and computer_selection == 1:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, player won!")

    if player_selection == 0 and computer_selection == 2:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, computer won!")

    if player_selection == 1 and computer_selection == 2:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, player won!")

    if player_selection == 1 and computer_selection == 0:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, computer won!")

    if player_selection == 2 and computer_selection == 0:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, player won!")

    if player_selection == 2 and computer_selection == 1:
        print(
            f"{options[player_selection]} with {options[computer_selection]}, computer won!")

# while True:
#     computer_selection = random.randint(1, 3)
#     if player_selection == computer_selection:
#         print(computer_selection)
#         continue
#     else:
#         print(f"Computer has choosen {computer_selection}")
#         print(options[computer_selection])
#         break
