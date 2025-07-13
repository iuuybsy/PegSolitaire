from enums import Occupy

from consts import HEIGHT, WIDTH
from consts import FORBID_AREA
from consts import FREE_CORD


class GameLogic:
    def __init__(self):
        self.board: list[list[Occupy]] = [[Occupy.STONE for _ in range(HEIGHT)] for __ in range(WIDTH)]
        self.init_board()

    def init_board(self):
        for cord in FORBID_AREA:
            self.board[cord[0]][cord[1]] = Occupy.FORBIDDEN
        self.board[FREE_CORD[0]][FREE_CORD[1]] = Occupy.FREE

    def print_board_info(self):
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.board[i][j] == Occupy.FORBIDDEN:
                    print(". ", end="")
                elif self.board[i][j] == Occupy.FREE:
                    print("O ", end="")
                else:
                    print("X ", end="")
            print("")

    @staticmethod
    def is_valid_cord(x: int, y: int) -> bool:
        return 0 <= x < WIDTH and 0 <= y < HEIGHT

    def is_valid_target(self, x: int, y: int) -> bool:
        return self.is_valid_cord(x, y) and self.board[x][y] == Occupy.STONE

    def is_valid_destination(self, x: int, y: int) -> bool:
        return self.is_valid_cord(x, y) and self.board[x][y] == Occupy.FREE





if __name__ == "__main__":
    game = GameLogic()
    game.print_board_info()
