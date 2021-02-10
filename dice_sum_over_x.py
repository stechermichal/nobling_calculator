def roll_dice(num_dices, num_sides, lower_bound, current_combination, combination_list):
    if num_dices <= 0:
        if current_combination >= lower_bound:
            combination_list.append(current_combination)
        return combination_list

    for side in range(1, num_sides + 1):
        roll_dice(num_dices - 1, num_sides, lower_bound, current_combination + side, combination_list)
    return combination_list


if __name__ == '__main__':
    nd = int(input("How many dice are you rolling?"))
    ns = int(input("How many sides do your dice have?"))
    lb = int(input("What sum do you want it to equal to or exceed?"))
    comb_list = roll_dice(nd, ns, lb, 0, [])
    print(len(comb_list) / ns ** nd)
