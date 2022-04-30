import random
from tabnanny import check

def main():
    board_nums = board_values()
    next_player = player_turn('')

    while not has_won(board_nums):
        draw_board(board_nums)
        print(f"Player {next_player}'s turn...")
        square = int(input('Choose a square: '))
        make_move(board_nums, next_player, square)
        next_player = player_turn(next_player)
        
        # To check draw
        num_of_o = 0
        num_of_x = 0
        for nums in board_nums:
            if 'o' == nums:
                num_of_o += 1
            elif 'x' == nums:
                num_of_x += 1
        is_a_draw = num_of_o + num_of_x
        if is_a_draw == 16:
            print("It's a draw.")
            break
   
    draw_board(board_nums)
    print("Good Bye!!!")
   


def board_values():
    values = []
    for number in range(16):
            values.append(number+1)
    return(values)

def draw_board(values):
    print()
    print(f'\t  {values[0]} | {values[1]} | {values[2]} | {values[3]}')
    print('\t ---+---+---+---')
    print(f'\t  {values[4]} | {values[5]} | {values[6]} | {values[7]}')
    print('\t ---+---+---+---')
    print(f'\t  {values[8]} | {values[9]} | {values[10]} | {values[11]}')
    print('\t ---+---+---+---')
    print(f'\t {values[12]} | {values[13]} | {values[14]} | {values[15]}')
    print()

def player_turn(player):
    player1 = 'x'
    player2 = 'o'
    if player == '' or player == player1:
        return player2
    elif player == player2:
        return player1
    

def make_move(values, player, square):
    square -= 1
    values[square] = player
    
    return values

def has_won(values):
    win_combo = (values[0] == values[4] == values[8] == values[12] or
                values[2] == values[6] == values[10] == values[14] or
                values[1] == values[5] == values[9] == values[13] or
                values[3] == values[7] == values[11] == values[15] or
                values[0] == values[1] == values[2] == values[3] or
                values[4] == values[5] == values[6] == values[7] or
                values[8] == values[9] == values[10] == values[11] or
                values[12] == values[13] == values[14] == values[15] or
                values[0] == values[5] == values[10] == values[15] or
                values[3] == values[6] == values[9] == values[12] )
    return win_combo
            


if __name__ == "__main__":
    main()