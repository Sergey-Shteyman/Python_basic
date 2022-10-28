class Board:

    board = list(range(1, 10))

    def display_board(self):
        print('-' * 13)
        for cell in range(3):
            print('|', self.board[0 + cell * 3],
                  '|', self.board[1 + cell * 3],
                  '|', self.board[2 + cell * 3], '|')
            print('-' * 13)


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def take_input(self):
        valid = False
        while not valid:
            player_answer = input('Куда поставим ' + self.symbol + '? ')
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод. Вы уверены, что ввели число?')
                continue
            if 1 <= player_answer <= 9:
                if str(Board.board[player_answer - 1]) not in 'XO':
                    Board.board[player_answer - 1] = self.symbol
                    valid = True
                else:
                    print('Эта клеточка уже занята!')
            else:
                print('Некорректный ввод. Введите число от 1 до 9 чтобы походить.')


class Victories:

    def __init__(self):
        self.win_coord = (
            (0, 1, 2), (3, 4, 5),
            (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )

    def check_win(self):
        for each in self.win_coord:
            if Board.board[each[0]] == Board.board[each[1]] == Board.board[each[2]]:
                return Board.board[each[0]]
        return False


def game():
    board = Board()
    result = Victories()
    counter = 0
    win = False
    while not win:
        board.display_board()
        if counter % 2 == 0:
            Player('X').take_input()
        else:
            Player('O').take_input()
        counter += 1
        if counter > 4:
            tmp = result.check_win()
            if tmp:
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    board.display_board()


game()
input("Нажмите 'ENTER для выхода'")
