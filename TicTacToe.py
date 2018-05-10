# Lets the player play tic tac toe vs the AI

import logging


class TicTacToe():

    def __init__(self):
        logging.info("Started a new game")

        self.board = {i: " " for i in range(1, 10)}
        self.wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.corners = [1, 3, 7, 9]
        self.sides = [2, 4, 6, 8]
        while True:
            choice = str(input("Möchten Sie X oder O sein? (X fängt an) "))
            if choice == "X":
                print("Sie sind X und spielen gegen O. Sie dürfen anfangen.")
                self.player = "X"
                self.AI = "O"
                logging.info(f"Player: {self.player}, Computer: {self.AI}, Player begins")
                break
            elif choice == "O":
                print("Sie sind O und spielen gegen X. Der Computer fängt an.")
                self.player = "O"
                self.AI = "X"
                logging.info(f"Player: {self.player}, Computer: {self.AI}, Computer begins")
                break
            else:
                print("Keine gültige Eingabe. Bitte versuchen Sie es erneut.")

    def player_turn(self):
        while True:
            try:
                field = int(input("Auf welches Feld möchten Sie setzen? "))
                if field in range(1, 10):
                    if self.board[field] == " ":
                        self.board[field] = self.player
                        logging.info(f"Player set on field {field}")
                        break
                    else:
                        print("Diese Feld ist bereits besetzt. Bitte geben Sie ein gültiges Feld ein.")
                else:
                    print("Keine gültige Eingabe. Bitte versuchen Sie es erneut.")
            except ValueError:
                print("Keine gültige Eingabe. Bitte versuchen Sie es erneut.")

    def check_row(self, row, person, field):  # checks a row for possible win
        if field[row[0]] == person and field[row[1]] == person and field[row[2]] == " ":
            return (True, row[2])
        if field[row[0]] == person and field[row[2]] == person and field[row[1]] == " ":
            return (True, row[1])
        if field[row[1]] == person and field[row[2]] == person and field[row[0]] == " ":
            return (True, row[0])
        return (False, 0)

    def AI_win(self):
        for row in self.wins:
            if self.check_row(row, self.AI, self.board)[0]:
                win_field = self.check_row(row, self.AI, self.board)[1]
                self.board[win_field] = self.AI
                logging.info(f"AI: found field {win_field} to win")
                return True
        logging.info("AI: could not win, continuing")
        return False

    def AI_block(self):
        for row in self.wins:
            if self.check_row(row, self.player, self.board)[0]:
                block_field = self.check_row(row, self.player, self.board)[1]
                self.board[block_field] = self.AI
                logging.info(f"AI: found field {block_field} to block")
                return True
        logging.info("AI: could not block, continuing")
        return False

    def AI_center(self):
        if self.board[5] == " ":
            self.board[5] = self.AI
            logging.info("AI: placed on center")
            return True
        logging.info("AI: could not place on center")
        return False

    def AI_opposite_corner(self):
        for i in range(4):
            if self.board[self.corners[i]] == self.player:
                if self.board[self.corners[::-1][i]] == " ":
                    self.board[self.corners[::-1][i]] = self.AI
                    logging.info(f"AI: placed on field {self.corners[::-1][i]} opposite corner")
                    return True
        logging.info("AI: could not place on opposite center")
        return False

    def AI_empty_corner(self):
        for i in self.corners:
            if self.board[i] == " ":
                self.board[i] = self.AI
                logging.info(f"AI: placed on empty corner field {i}")
                return True
        logging.info("AI: could not place on empty corner")
        return False

    def AI_empty_side(self):
        for i in self.sides:
            if self.board[i] == " ":
                self.board[i] = self.AI
                logging.info(f"AI: placed on empty side field {i}")
                return True
        logging.info("AI: could not place on empty side")
        return False

    def AI_turn(self):
        if not self.AI_win():
            if not self.AI_block():
                if not self.AI_opposite_corner():
                    if not self.AI_empty_corner():
                        if not self.AI_center():
                            self.AI_empty_side()

    def check_win(self):
        for row in self.wins:
            if self.board[row[0]] == self.player and self.board[row[1]] == self.player and self.board[row[2]] == self.player:
                print("Glückwunsch, Sie haben gewonnen!")
                logging.info("Player won")
                logging.info("Game finished")
                logging.info("-----------------------------------------------")
                return True
            elif self.board[row[0]] == self.AI and self.board[row[1]] == self.AI and self.board[row[2]] == self.AI:
                print("Sie haben verloren!")
                logging.info("AI won")
                logging.info("Game finished")
                logging.info("-----------------------------------------------")
                return True
        if " " not in self.board.values():
            print("Unentschieden!")
            logging.info("Draw")
            logging.info("Game finished")
            logging.info("-----------------------------------------------")
            return True
        return False

    def draw(self):
        print(" ")
        print("Spielfeld:                Bezeichnungen:")
        for i in [1, 4, 7]:
            print("-------------------       -------------------")
            print("|     |     |     |       |     |     |     |")
            print("| ", self.board[i], " | ", self.board[i + 1], " | ", self.board[i + 2], " |     ", " | ", i, " | ", i + 1, " | ", i + 2, " |")
            print("|     |     |     |       |     |     |     |")
        print("-------------------       -------------------")
        print(" ")

    def play(self):
        if self.player == "X":
            while not self.check_win():
                self.draw()
                self.player_turn()
                if self.check_win():
                    break
                self.draw()
                self.AI_turn()
            self.draw()
        if self.AI == "X":
            while not self.check_win():
                self.draw()
                self.AI_turn()
                if self.check_win():
                    break
                self.draw()
                self.player_turn()
            self.draw()


def main():
    logging.basicConfig(filename="TicTacToe.log", level=logging.INFO, format="%(levelname)s:%(message)s")
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
