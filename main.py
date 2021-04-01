import numpy as np
import matplotlib.pyplot as plt

possible_moves = np.array(['papier', 'kamien', 'nozyce'])
moves_played = np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])
last_user_move = 'papier'
score = 0
score_list = []


def string_to_numb(move):
    if move == 'papier':
        return 0
    elif move == 'kamien':
        return 1
    elif move == 'nozyce':
        return 2


def numb_to_string(move):
    if move == 0:
        return 'papier'
    elif move == 1:
        return 'kamien'
    elif move == 2:
        return 'nozyce'


def decide_computer_move(user_input):
    if user_input == 0:
        computer_input = np.random.choice(possible_moves, p=moves_played[0] / np.sum(moves_played[0]))
    elif user_move == 1:
        computer_input = np.random.choice(possible_moves, p=moves_played[1] / np.sum(moves_played[1]))
    else:
        computer_input = np.random.choice(possible_moves, p=moves_played[2] / np.sum(moves_played[2]))

    return possible_moves[np.where(possible_moves == computer_input)[0][0] - 1]


#for i in range(1000):
while True:

    rounds = 0
    user_move = input()
    #user_move = np.random.choice(possible_moves, p=[0.2, 0.7, 0.1])
    user_move = string_to_numb(user_move)
    last_user_move = string_to_numb(last_user_move)
    moves_played[last_user_move, user_move] += 1

    last_user_move = numb_to_string(user_move)
    computer_move = decide_computer_move(user_move)

    print(possible_moves[string_to_numb(computer_move)])

    user_move = numb_to_string(user_move)
    score_change = 0

    if user_move == computer_move:
        score_change = 0
    elif user_move == 'papier':
        if computer_move == 'kamien':
            score_change = 1
        else:
            score_change = -1
    elif user_move == 'kamien':
        if computer_move == 'papier':
            score_change = -1
        else:
            score_change = 1
    elif user_move == 'nozyce':
        if computer_move == 'kamien':
            score_change = -1
        else:
            score_change = 1

    rounds += 1
    score += score_change
    score_list.append(score)

    plt.plot(score_list)
    plt.xlabel('rounds')
    plt.ylabel('player score')
    plt.show()

