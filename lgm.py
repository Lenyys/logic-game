import random

separator = "=" * 64


def difficulty_input() -> int:
    """
    This method asks user to choose difficulty.
    If user input is in options then returns difficulty.
    If it's not in options then prints info and asks user again.
    """

    def wrong_difficulty_input() -> None:
        print("Your choice is not in options, try again.")
        print(separator)

    while True:
        try:
            difficulty = int(input("""
Choose difficulty:
1 = easy - 4 colors - colors can't repeat
2 = medium - 4 colors - colors can repeat
3 = hard - 6 colors - colors can't repeat
4 = extreme - 6 colors - colors can repeat
"""))
            print(separator)
        except ValueError:
            print(separator)
            wrong_difficulty_input()
            continue
        else:
            if difficulty in [1, 2, 3, 4]:
                return difficulty
            else:
                wrong_difficulty_input()
                continue


def get_colors(difficulty: int, colors_4: list[str], colors_6: list[str]) -> list[str]:
    """
    This method returns list of colors that can be use in game.
    Depends on difficulty.
    """
    colors = []
    if difficulty == 1 or difficulty == 2:
        colors = colors_4
    elif difficulty == 3 or difficulty == 4:
        colors = colors_6
    return colors


def get_separator(difficulty: int) -> str:
    """
    This method return separator-string.
    The length of the separator depends on difficulty.
    """
    if difficulty == 1 or difficulty == 2:
        return "=" * 64
    elif difficulty == 3 or difficulty == 4:
        return "=" * 90


def game_rules_short(colors_which_can_be_use: list[str]) -> None:
    """
    This method prints game rule.
    """
    print(f'Try to guest {len(colors_which_can_be_use)} color in right order. ',
          'You have 10 rounds to finish it',
          f'You can choose from following {len(colors_which_can_be_use)} colors:',
          f'({", ".join(colors_which_can_be_use)})',
          separator,
          sep="\n")


def get_guessed_colors(difficulty: int, guessed_colors: list[str]) -> list[str]:
    """
    This method returns list of colors that user is going to guess.
    Depends on difficulty.
    """
    if difficulty == 1 or difficulty == 3:
        random.shuffle(guessed_colors)
    elif difficulty == 2 or difficulty == 4:
        colors_1 = []
        for _ in range(len(guessed_colors)):
            colors_1.append(random.choice(guessed_colors))
        guessed_colors = colors_1
    return guessed_colors


def user_guessing_input(guessed_colors: list[str]) -> list[str]:
    """
    This method  returns list of colors entered by the user.
    """
    user_input_1 = (input(f"Write {len(guessed_colors)} colors separated by \",\": \n")).split(",")
    user_input = []
    for u in user_input_1:
        u1 = u.strip()
        user_input.append(u1)
    return user_input


def is_user_input_right(user_input: list[str], guessed_colors: list[str], colors_which_can_be_use: list[str]) -> bool:
    """
    This method returns bool.
    True if user writes right colors and right number of colors.
    False if user writes wrong color or wrong number of colors or both.
    If method returns False then informs user what he writes wrong.
    """
    if len(user_input) == len(guessed_colors):
        for i in range(len(user_input)):
            if user_input[i] not in colors_which_can_be_use:
                print("Your colors are not in options",
                      "try again..", sep="\n")
                print(separator)
                wrong_input_1 = True
                break
            elif user_input[i] in colors_which_can_be_use:
                continue
        else:
            wrong_input_1 = False
    else:
        print(f"You didn't write {len(guessed_colors)} colors",
              "try again....", sep="\n")
        print(separator)
        wrong_input_1 = True
    return wrong_input_1


def evaluate_round(user_input: list[str], guessed_colors: list[str]) -> dict:
    """
    This method evaluate user input of colors and returns dict of 3 values: black, white, wrong.
    if color is in guessing colors and is in right place then black +1
    if color is in guessing colors but is in wrong place then white +1
    if color is not in guessing colors then wrong +1
    total number: black + white + wrong == length of guessing colors
    """
    black = 0
    white = 0
    wrong = 0
    for i1 in range(len(guessed_colors)):
        if user_input[i1] in guessed_colors \
                and user_input[i1] == guessed_colors[i1]:
            black += 1
        elif user_input[i1] in guessed_colors \
                and user_input[i1] != guessed_colors[i1]:
            for j in range(len(guessed_colors)):
                if i1 != j and user_input[i1] == guessed_colors[j] \
                        and user_input[i1] != guessed_colors[i1]:
                    if user_input[j] != guessed_colors[j]:
                        if user_input.count(user_input[i1]) <= guessed_colors.count(user_input[i1]):
                            white1 = white
                            white += 1
                            if white > white1:
                                break
                            else:
                                continue
                        elif user_input.count(user_input[i1]) > guessed_colors.count(user_input[i1]):
                            white1 = white
                            white += 1
                            wrong += 1
                            if white > white1:
                                break
                            else:
                                continue
                    elif user_input[j] == guessed_colors[j] \
                            and user_input.count(user_input[i1]) > guessed_colors.count(user_input[i1]):
                        wrong1 = wrong
                        wrong += 1
                        if wrong > wrong1:
                            break
                        else:
                            continue
                else:
                    continue
        else:
            wrong += 1

    white2 = white
    for i3 in range(len(guessed_colors)):
        if (user_input.count(user_input[i3]) and guessed_colors.count(user_input[i3])) > 0 \
                and user_input.count(user_input[i3]) > guessed_colors.count(user_input[i3]):
            if user_input[i3] == guessed_colors[i3]:
                break
            elif user_input[i3] != guessed_colors[i3]:
                for x in range(len(guessed_colors)):
                    if user_input[i3] == guessed_colors[x] \
                            and user_input[x] != guessed_colors[x] \
                            and user_input[i3] != guessed_colors[i3]:
                        if white == white2:
                            white -= 1
                            wrong -= 1
                            break
                        else:
                            continue
                    else:
                        continue
        else:
            continue
    return {"black": black, "white": white, "wrong": wrong}


def make_outcome_one_round(black: int, white: int, wrong: int) -> list[str]:
    """
    This method returns evaluation of user input as list of string.
    """
    outcome = []
    for i_1 in range(black):
        outcome.append("B")
    for i_2 in range(white):
        outcome.append("W")
    for i_4 in range(wrong):
        outcome.append("-")
    return outcome


def is_total_outcome_black(colors_which_can_be_use: list[str], black: int,) -> bool:
    """
    This method returns bool False if users colors are totally right.
    """
    if black == len(colors_which_can_be_use):
        print("You have all colors in right place.",
              f"YOU WIN...... ",
              f"Right answer is {' | '.join(colors_which_can_be_use)}",
              sep="\n")
        return False


def get_total_outcome(total_outcome: list, user_input: list[str],
                      outcome_one_round: list[str], colors_which_can_be_use: list[str]) -> None:
    """
    This method prints evaluated all rounds.
    """
    user_input_and_outcome = (user_input, outcome_one_round)
    total_outcome.append(user_input_and_outcome)

    for i_3 in range(len(total_outcome)):
        print(f'round {i_3 + 1}:|', end="")
        for j_3 in range(len(colors_which_can_be_use)):
            color = total_outcome[i_3][0][j_3]
            print(f'{color.center(8)}|', end="")
        print(f'=| {" | ".join(total_outcome[i_3][1])} |')


def game_over() -> None:
    print("You didn't guest right answer in 10 rounds",
          "GAME OVER.....",
          sep="\n")


def continue_in_game() -> bool:
    """
    This method return True if user writes y or Y.
    and False if user writes anything else.
    """
    user_continue_input = input("Do you want play new game? \n"
                                "for yes press 'y', for no  press anything else: ")
    if user_continue_input.lower() == "y":
        print(separator)
        return True
    else:
        print(separator)
        print("ENDING GAME ...... ")
        return False
