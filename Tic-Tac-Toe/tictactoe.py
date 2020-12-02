class Board:

    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0,]

    def state_to_board(self):
        for i in self.state:
            if int(self.state[place]) == 0:
                continue
            elif int(self.state[place]) == 1:
                self.board[place] = "X"
            elif int(self.state[place]) == 2:
                self.board[place] = "O"

    def win(self, player):
        if player == 1:
            print("\n")
            self.print_board()
            print("\n\n  Player 1 won!\n\n\n")
            return True
        elif player == 2:
            print("\n")
            self.print_board()
            print("\n\n  Player 2 won!\n\n\n")
            return True
        else:
            return False

    def check_win(self):
        if self.state[0] == self.state[1] == self.state[2] != 0:   # - - -
            return self.win(self.state[0])
        if self.state[3] == self.state[4] == self.state[5] != 0:   # - - -
            return self.win(self.state[3])
        if self.state[6] == self.state[7] == self.state[8] != 0:   # - - -
            return self.win(self.state[6])
        if self.state[0] == self.state[3] == self.state[6] != 0:  # |  |  |
            return self.win(self.state[0])
        if self.state[1] == self.state[4] == self.state[7] != 0:  # |  |  |
            return self.win(self.state[1])
        if self.state[2] == self.state[5] == self.state[8] != 0:  # |  |  |
            return self.win(self.state[2])
        if self.state[0] == self.state[4] == self.state[8] != 0:  # \ \ \
            return self.win(self.state[0])
        if self.state[2] == self.state[4] == self.state[6] != 0:  # / / /
            return self.win(self.state[2])

    def is_full(self):
        if 0 in self.state:
            return False
        else:
            return True

    def make_turn(self, place, player):
        if self.valid_turn(place):
            self.state[place] = player
            self.state_to_board()
            return True


    def valid_turn(self, place):
        if self.state[place] == 0:
            return True

    def print_board(self):

        print(f"\n  {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}\n\n"
              f"  {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}\n\n"
              f"  {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}\n")



if __name__ == "__main__":
    player_a = 1
    player_b = 2
    board = Board()
    active_player = player_a
    while not board.is_full():
        print(board.print_board())
        try:
            place = int(input("Where do you want to place your sign? [1-9]\n-->"))
        except ValueError:
            print("\nOnly numbers are allowed!")
            continue

        place -= 1

        if place < 0 or place > 8:
            print("\n\nOnly insert numbers between 1 and 9!")
            continue


        if not board.make_turn(place, active_player):
            print("\n\nInvalid turn - You can't overwrite existing cells!")
        if board.check_win():
            break
        else:
            if active_player == player_a:
                print("\n\n\n\n\nPlayer 2, it's your turn!")
                active_player = player_b
                continue
            else:
                print("\n\n\n\n\nPlayer 1, it's your turn!")
                active_player = player_a
                continue

        print("Both Player won!")
