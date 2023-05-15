import lgm


next_game = True

while next_game:
    number_of_tries = 10
    colors_4 = ["red", "green", "blue", "yellow"]
    colors_6 = ["red", "green", "blue", "yellow", "white", "purple"]
    user_input = []
    difficulty = lgm.difficulty_input()
    colors_which_can_be_use = lgm.get_colors(difficulty, colors_4, colors_6)
    separator = lgm.get_separator(difficulty)
    lgm.game_rules_short(colors_which_can_be_use)
    guessed_colors = lgm.get_guessed_colors(difficulty, colors_which_can_be_use)
    print(guessed_colors)
    total_outcome = []
    for number_try in range(number_of_tries):
        wrong_input_1 = True
        while wrong_input_1:
            user_input = lgm.user_guessing_input(guessed_colors)
            wrong_input_1 = lgm.is_user_input_right(user_input,
                                                    guessed_colors,
                                                    colors_which_can_be_use)
        print(separator)
        evaluated_round = lgm.evaluate_round(user_input, guessed_colors)
        outcome_one_round = lgm.make_outcome_one_round(black=evaluated_round["black"],
                                                       white=evaluated_round["white"],
                                                       wrong=evaluated_round["wrong"],
                                                       )
        if lgm.is_total_outcome_black(colors_which_can_be_use,
                                      black=evaluated_round["black"]) is False:
            break
        lgm.get_total_outcome(total_outcome,
                              user_input,
                              outcome_one_round,
                              colors_which_can_be_use)
        print(separator)
    else:
        lgm.game_over()

    next_game = lgm.continue_in_game()
