def rtoOrgin(moves):
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')

move = input('Enter the move: ')
print(rtoOrgin(move))