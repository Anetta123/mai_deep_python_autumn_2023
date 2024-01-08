import random


class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            raise ValueError("Player name should be non empty string!")

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role: str):
        if role.lower() in ("crosses", "circles"):
            self._role = role
        else:
            raise ValueError("You need to choose "
                             "your playing side to continue!\n"
                             "'Crosses' and 'Circles' are in option")

    def __str__(self):
        return (f"User object with {self._name}"
                f" name and {self._role} playing side")

    @staticmethod
    def greetings():
        print("Hello! Introduce yourselves!\n"
              "Write down some information in format: <Name> <Playing Side>\n"
              "Where Playing side can be in 'Crosses' and 'Circles' options")

        try:
            name1, role1 = input().split(' ')
            name2, role2 = input().split(' ')
            if role1.lower() == role2.lower():
                raise ValueError
        except ValueError:
            raise ValueError("Check info you are providing, "
                             "may be you forgot to select "
                             "your Playing Side or Name\n"
                             "Also, there is an option that "
                             "you have chosen the same"
                             " Playing Sides, it's prohibitted")

        return User(name1, role1), User(name2, role2)


class Board:

    def __init__(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.graph = [[' '] * 13 for _ in range(13)]

    def set_value(self, i: int, j: int, play_side: str):
        if (isinstance(i, int) and
                isinstance(j, int) and 0 <= i <= 2 and 0 <= j <= 2):
            if self.board[i][j] is not None:
                raise ValueError("Error!"
                                 " Check the place where you drawing figure")
            if play_side.lower() == "crosses":
                self.board[i][j] = 1
            else:
                self.board[i][j] = 0
        else:
            raise ValueError("Error! Check the place where you drawing figure")

    def _fill_board(self):
        for i in range(13):
            for j in range(13):
                if i in (0, 4, 8, 12):
                    self.graph[i][j] = '#'
                if j in (0, 4, 8, 12):
                    self.graph[i][j] = '#'

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is not None:
                    if self.board[i][j] == 1:
                        self.graph[((i * 4 + 2) - 1)][(j * 4 + 2) - 1] = '.'
                        self.graph[(i * 4 + 2)][(j * 4 + 2)] = '.'
                        self.graph[(i * 4 + 2) + 1][(j * 4 + 2) + 1] = '.'
                        self.graph[(i * 4 + 2) + 1][(j * 4 + 2) - 1] = '.'
                        self.graph[(i * 4 + 2) - 1][(j * 4 + 2) + 1] = '.'
                    else:
                        self.graph[(i * 4 + 2) - 1][(j * 4 + 2) - 1] = '.'
                        self.graph[(i * 4 + 2) - 1][(j * 4 + 2)] = '.'
                        self.graph[(i * 4 + 2) - 1][(j * 4 + 2) + 1] = '.'
                        self.graph[(i * 4 + 2)][(j * 4 + 2) - 1] = '.'
                        self.graph[(i * 4 + 2)][(j * 4 + 2) + 1] = '.'
                        self.graph[(i * 4 + 2) + 1][(j * 4 + 2) - 1] = '.'
                        self.graph[(i * 4 + 2) + 1][(j * 4 + 2)] = '.'
                        self.graph[(i * 4 + 2) + 1][(j * 4 + 2) + 1] = '.'

    def show_board(self):
        for i in range(13):
            for j in range(13):
                print(self.graph[i][j], end='')
            print()

    def check_win(self, name: str):
        res = 0
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]
                and isinstance(self.board[0][0], int)):
            res = 1
        elif (self.board[0][0] == self.board[0][1] == self.board[0][2]
              and isinstance(self.board[0][0], int)):
            res = 1
        elif (self.board[1][0] == self.board[1][1] == self.board[1][2]
              and isinstance(self.board[1][0], int)):
            res = 1
        elif (self.board[2][0] == self.board[2][1] == self.board[2][2]
              and isinstance(self.board[2][0], int)):
            res = 1
        elif (self.board[2][0] == self.board[1][1] == self.board[0][2]
              and isinstance(self.board[2][0], int)):
            res = 1
        elif (self.board[0][0] == self.board[1][0] == self.board[2][0]
              and isinstance(self.board[0][0], int)):
            res = 1
        elif (self.board[0][1] == self.board[1][1] == self.board[2][1]
              and isinstance(self.board[0][1], int)):
            res = 1
        elif (self.board[0][2] == self.board[1][2] == self.board[2][2]
              and isinstance(self.board[0][2], int)):
            res = 1

        if res:
            print(f"Congratulations, {name}! It's your win!")
            self._fill_board()
            self.show_board()
        return res

    @staticmethod
    def which_turn(obj: User):
        print(f"{obj.name} choose the place, where you want to set your {obj.role}")

    def turn(self, obj: User):
        self.which_turn(obj)

        try:
            y, x = map(int, input().split(' '))
        except ValueError:
            raise ValueError("Check coordinates you are providing as: <y> <x>")
        self.set_value(y, x, obj.role)
        if self.check_win(obj.name):
            return 1


def main():
    player1, player2 = User.greetings()
    board = Board()

    coin_flip = random.randint(0, 1)
    begin = (player1 if coin_flip == 0 else player2)
    odd = (player1 if begin is player2 else player2)

    print(f"Luckily, {begin.name}, it's your turn!\n"
          f"<HINT> Coordinates format is: <row> <column>")

    game_length = 0
    while game_length < 9:

        if game_length % 2 == 0:
            if board.turn(begin):
                break
        else:
            if board.turn(odd):
                break
        board._fill_board()
        board.show_board()
        game_length += 1

    if game_length == 9:
        print("Oops, seems you are both so strong"
              " in this game! Try again! Draw!")


if __name__ == '__main__':
    main()
