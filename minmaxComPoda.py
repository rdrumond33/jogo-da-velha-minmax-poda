import random

def initialize_game():
    print("\nOla O jogo funciona como e linha coluna\nA maquina e o jogador Y e a pessoa e jogador X\nBoa sorte" )
    plays = ["X", "O"]
    player_turn = random.choice(plays)

    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]
    
    while not(isEnd(board) == "X" or isEnd(board) == "O") : 
      print("****************************************************************************")
      print("                                 Jogador {}                                 ".format(player_turn))
      print("****************************************************************************")
 
      if player_turn == "O":
          (m, qx, qy) = vezDaMaquina(board)
          if is_move_valid(board,[qx,qy]):
            moves = [str(qx),str(qy)]
            board, player_turn = update_Board(board, moves, "O")
          continue

      move = input("'Digite seu movimento Exemplo: (`linha coluna`):")
      moves = move.split()
      if not(is_move_valid(board,moves)):
        print("movimento invalido tente de novo")
        print("")
        update_Board(board,None,None)
        continue
      board, player_turn = update_Board(board, moves, player_turn)

    print("Vencedor e `{}`".format(isEnd(board)))
  
def update_Board(board, moves, player):
    if moves:
        x = int(moves[0])
        y = int(moves[1])

        board[x][y] = player
    draw(board)
    return (board, quemJoga(player))

def quemJoga(player_turn):
    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"
    return player_turn

def draw(board):
    for i in range(0, 3):
        for j in range(0, 3):
            print('|{}|'.format(board[i][j]), end=" ")
        print()
    print()

def vezDaMaquina(board):
    return max_poda(board,float('-inf'),float('inf'))

def is_move_valid(board, moves):
    px = int(moves[0])
    py = int(moves[1])
    
    if px < 0 or px > 2 or py < 0 or py > 2:
        return False
    elif board[px][py] != '.':
        return False
    else:
        return True

def isEnd(board):
    for i in range(0, 3):
        if (board[0][i] != '.' and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]
    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'
    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
        board[0][0] == board[2][2]):
        return board[0][0]
    if (board[0][2] != '.' and
        board[0][2] == board[1][1] and
        board[0][2] == board[2][0]):
        return board[0][2]

 
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == '.'):
                return None

    return '.'
    
  
# Mim max com poda 
def max_poda(board, alpha, beta):
    maxv = -2
    x = None
    y = None

    resultado = isEnd(board)

    if resultado == 'X':
        return (-1, 0, 0)
    elif resultado == 'O':
        return (1, 0, 0)
    elif resultado == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                (m, min_i, in_j) = min_poda(board, alpha, beta)
                if m > maxv:
                    maxv = m
                    x = i
                    y = j
                board[i][j] = '.'

                if maxv >= beta:
                    return (maxv, x, y)

                if maxv > alpha:
                    alpha = maxv

    return (maxv, x, y)

def min_poda(board,alpha, beta):
  minv = 2
  x = None
  y = None
  resultado = isEnd(board)

  if resultado == 'X':
      return (-1, 0, 0)
  elif resultado == 'O':
      return (1, 0, 0)
  elif resultado == '.':
      return (0, 0, 0)

  for i in range(0, 3):
      for j in range(0, 3):
          if board[i][j] == '.':
              board[i][j] = 'X'
              (m, max_i, max_j) = max_poda(board,alpha, beta)
              if m < minv:
                  minv = m
                  x = i
                  y = j
              board[i][j] = '.'

              if minv <= alpha:
                  return (minv, x, y)

              if minv < beta:
                  beta = minv

  return (minv, x, y)

initialize_game()
