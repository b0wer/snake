import pygame
import random

color = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
}

class board(pygame.sprite.Sprite):
    def __init__(self, surface, life, score):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.life = 3 if life > 3 else life
        self.score = score

        self.image = pygame.image.load('sprite/fon.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.img_backLogo = {'image': pygame.image.load('sprite/GameBoard/logo.png').convert_alpha(),
                             'rect': (0, 250)}
        self.img_topBar = {'image': pygame.image.load('sprite/GameBoard/fon_topBar.png').convert_alpha(),
                           'rect': (0, 0)}
        self.img_heart = pygame.image.load('sprite/GameBoard/heart.png').convert_alpha()


    def draw(self):
        self.surface.blit(self.img_backLogo['image'], self.img_backLogo['rect'])  # Фон
        self.surface.blit(self.img_topBar['image'], self.img_topBar['rect'])  # Фон верхнего бара
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
            self.surface.blit(self.img_heart, (32*i+95, 38))

    def _drowText(self, text, x, y, font=None, size=30, color=color['WHITE']):
        font = pygame.font.Font(font, size)
        Text = font.render(text, True, color)
        self.surface.blit(Text, (x, y))

    def _drowField(self):
        FIELD_WIDTH = self.surface.get_width() - 10  # Остступ скраю 10px
        FIELD_HEIGHT = self.surface.get_height() - 92 - 10  # Остступ сверху 92(верхний бар) 10(от бара вниз)

        for y in range(0, int(FIELD_HEIGHT // 20)):
            for x in range(0, int(FIELD_WIDTH // 20)):
                pygame.draw.rect(self.surface, (55, 61, 66), ((20*x+10, 20*y+110, 20, 20)), 1)

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
            pygame.draw.rect(self.surface, color['GREEN'], ((square[0]*20+10, square[1]*20+90, 20, 20)))

    def stepping(self, food):
        x = self.vector[0]
        y = self.vector[1]
        last = self.coordinate[-1]
        width_pt = (self.surface.get_width() - 10) // 20
        height_pt = (self.surface.get_height() - 92 - 10) // 20

        if (0 < last[0]+x < width_pt) and (0 < last[1]+y < height_pt):  # Проверка на границы поля
            self.coordinate.append([last[0]+x, last[1]+y])  # Рисуем голову
            if self.coordinate.count(food.coordinate) == 0:  # Проверка на съеденную еду
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


class food():
    def __init__(self, surface):
        self.surface = surface
        self.coordinate = self._getCoordinate()
        self.image = pygame.image.load('sprite/GameBoard/food/food.png').convert_alpha()

    def draw(self, snake):
        while snake.coordinate.count(self.coordinate):
            self.coordinate = self._getCoordinate()

        x = self.coordinate[0]
        y = self.coordinate[1]
        self.surface.blit(self.image, (x * 20 + 10, y * 20 + 90))

    def _getCoordinate(self):
        width_pt = (self.surface.get_width() - 10) // 20
        height_pt = (self.surface.get_height() - 92 - 10) // 20
        x = random.randrange(1, width_pt, 1)
        y = random.randrange(1, height_pt, 1)
        return [x, y]
