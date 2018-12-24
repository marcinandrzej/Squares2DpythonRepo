import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class SquaresClass:

    def __init__(self, window_w=500, window_h=500):

        self.grid = []
        for row in range(4):
            self.grid.append([])
            for column in range(4):
                self.grid[row].append(0)

        self.width = window_w // 4
        self.height = window_h // 4
        self.window_w = window_w
        self.window_h = window_h

        self.width_w = min((self.window_w // 100),5)
        self.width_h = min((self.window_h // 100),5)

        self.font = pygame.font.SysFont('Arial', 30, True, False)

        self.shuffle()

    def drawScene(self, screen, win):

        screen.fill(BLACK)

        if not win:
            for row in range(4):
                for col in range(4):
                    if self.grid[row][col] == 0:
                        color = WHITE
                    elif self.grid[row][col] == 1:
                        color = RED
                    elif self.grid[row][col] == 2:
                        color = GREEN
                    else:
                        color = BLUE
                    pygame.draw.rect(screen, color, [col * self.width, row * self.height, self.width, self.height])

            pygame.draw.line(screen, BLACK, [self.width, 0], [self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [2 * self.width, 0], [2 * self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [3 * self.width, 0], [3 * self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [0, self.height], [self.window_w, self.height], self.width_h)
            pygame.draw.line(screen, BLACK, [0, 2 * self.height], [self.window_w, 2 * self.height], self.width_h)
            pygame.draw.line(screen, BLACK, [0, 3 * self.height], [self.window_w, 3 * self.height], self.width_h)
        else:
            text = self.font.render("CONGRATULATIONS", True, YELLOW)
            screen.blit(text, [self.window_w // 3, self.window_h // 3])
            text = self.font.render("Press R to Restart", True, YELLOW)
            screen.blit(text, [self.window_w // 3, self.window_h // 2])

        pygame.display.flip()

    def update(self, player_position):

        if player_position[0] > 0 and player_position[0] < (4 * self.width) and \
            player_position[1] > 0 and player_position[1] < (4 * self.height):
            row = min((player_position[1]) // self.height, 3)
            col = min((player_position[0]) // self.width, 3)
            self.grid[row][col] = (self.grid[row][col] + 1) % 4
            self.updateNeighbours(row, col)


    def updateNeighbours(self, row, col):
        if row > 0 and row < 3 and col > 0 and col < 3:
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row - 1][col - 1] = (self.grid[row - 1][col - 1] + 1) % 4
            self.grid[row + 1][col - 1] = (self.grid[row + 1][col - 1] + 1) % 4
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row - 1][col + 1] = (self.grid[row - 1][col + 1] + 1) % 4
            self.grid[row + 1][col + 1] = (self.grid[row + 1][col + 1] + 1) % 4
        elif row == 0 and col == 0:
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row + 1][col + 1] = (self.grid[row + 1][col + 1] + 1) % 4
        elif row == 0 and col == 3:
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row + 1][col - 1] = (self.grid[row + 1][col - 1] + 1) % 4
        elif row == 3 and col == 0:
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row - 1][col + 1] = (self.grid[row - 1][col + 1] + 1) % 4
        elif row == 3 and col == 3:
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row - 1][col - 1] = (self.grid[row - 1][col - 1] + 1) % 4
        elif row == 0 and col > 0 and col < 3:
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row + 1][col - 1] = (self.grid[row + 1][col - 1] + 1) % 4
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row + 1][col + 1] = (self.grid[row + 1][col + 1] + 1) % 4
        elif row == 3 and col > 0 and col < 3:
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row - 1][col - 1] = (self.grid[row - 1][col - 1] + 1) % 4
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row - 1][col + 1] = (self.grid[row - 1][col + 1] + 1) % 4
        elif col == 0 and row > 0 and row < 3:
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row][col + 1] = (self.grid[row][col + 1] + 1) % 4
            self.grid[row - 1][col + 1] = (self.grid[row - 1][col + 1] + 1) % 4
            self.grid[row + 1][col + 1] = (self.grid[row + 1][col + 1] + 1) % 4
        elif col == 3 and row > 0 and row < 3:
            self.grid[row - 1][col] = (self.grid[row - 1][col] + 1) % 4
            self.grid[row + 1][col] = (self.grid[row + 1][col] + 1) % 4
            self.grid[row][col - 1] = (self.grid[row][col - 1] + 1) % 4
            self.grid[row - 1][col - 1] = (self.grid[row - 1][col - 1] + 1) % 4
            self.grid[row + 1][col - 1] = (self.grid[row + 1][col - 1] + 1) % 4

    def checkWin(self):
        if (self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == self.grid[0][3] ==
                self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == self.grid[1][3] ==
                self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == self.grid[2][3] ==
                self.grid[3][0] == self.grid[3][1] == self.grid[3][2] == self.grid[3][3]):
            return True
        else:
            return False

    def shuffle(self):
        for row in range(4):
            for col in range(4):
                randi = random.randrange(4)
                self.grid[row][col] = randi