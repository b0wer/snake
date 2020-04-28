import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class board():
    def __init__(self, surface, life, score):
        self.surface = surface
        self.life = 3 if life > 3 else life
        self.score = score

    def draw(self):
        # Рамка
        pygame.draw.rect(self.surface, (WHITE), ((10, 10, 380, 80)), 5)
        # Жизни
        self._drowText("Life:", 35, 40)
        self._drowLife()
        # Счет
        self._drowText("Score:", 210, 40)
        self._drowText(str(self.score), 290, 40)
        # Поле из клеточек
        self._drowField()

    def _drowLife(self):
        for i in range(self.life):
            pygame.draw.circle(self.surface, RED, ((30 * i + 100, 50)), 10, 0)

    def _drowText(self, text, x, y, font=None, size=30, color=WHITE):
        font = pygame.font.Font(font, size)
        Text = font.render(text, True, color)
        self.surface.blit(Text, (x, y))

    def _drowField(self):
        WIDTH = 400 - 20
        HEIGHT = 500 - 20

        for y in range(0, int(HEIGHT / 10)):
            for x in range(0, int(WIDTH / 10)):
                pygame.draw.rect(self.surface, (30, 30, 30), ((10 * x + 10, 10 * y + 110, 10, 10)), 1)

    def update(self, life, score):
        self.life = life
        self.score = score


class snake():
    def __init__(self, surface):
        self.surface = surface
        self.coordinate = [[1, 1]]
        self.life = 3
        self.score = 0
        self.vector = [1, 0]  # x, y

    def draw(self):
        for square in self.coordinate:
            pygame.draw.rect(self.surface, GREEN, ((square[0] * 10, square[1] * 10 + 100, 10, 10)))

    def stepping(self, eat):
        x = self.vector[0]
        y = self.vector[1]
        last = self.coordinate[-1]
        if (0 < last[0] + x <= 38) and (0 < last[1] + y <= 48):  # Проверка на границы поля
            self.coordinate.append([last[0] + x, last[1] + y])  # Рисуем голову
            if self.coordinate.count(eat.coordinate) == 0:  # Проверка на съеденную еду
                self.coordinate.pop(0)  # Если не съели хавку, удаляем хвост
                if self.coordinate[:-1].count(self.coordinate[-1]) and len(self.coordinate) > 1:  # Съел ли сам себя
                    self._kill()
            else:
                self.score += 1
        else:
            self._kill()

    def _kill(self):
        self.life = self.life - 1
        if self.life > 0:
            self.coordinate = [[1, 1]]
            self.vector = [1, 0]  # x, y
        else:
            self.coordinate.clear()


class eat():
    def __init__(self, surface):
        self.surface = surface
        self.coordinate = self._getCoordinate()

    def draw(self, snake):
        while snake.coordinate.count(self.coordinate):
            self.coordinate = self._getCoordinate()
        x = self.coordinate[0]
        y = self.coordinate[1]
        pygame.draw.circle(self.surface, BLUE, ((x * 10 + 5, y * 10 + 105)), 5)

    def _getCoordinate(self):
        x = random.randrange(1, 38, 1)
        y = random.randrange(1, 48, 1)
        return [x, y]
