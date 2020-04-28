import pygame

import GameBoard

WIDTH = 400
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

snake = GameBoard.snake(screen)
board = GameBoard.board(screen, snake.life, 0)
eat = GameBoard.eat(screen)

x = 1
y = 0

running = True
while running:
    clock.tick(10)
    # Ввод собития
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Выясняем какая именно кнопка была нажата
            if event.key == pygame.K_LEFT:
                if snake.vector != [1, 0]:
                    snake.vector = [-1, 0]
            if event.key == pygame.K_RIGHT:
                if snake.vector != [-1, 0]:
                    snake.vector = [1, 0]
            if event.key == pygame.K_UP:
                if snake.vector != [0, 1]:
                    snake.vector = [0, -1]
            if event.key == pygame.K_DOWN:
                if snake.vector != [0, -1]:
                    snake.vector = [0, 1]

    # Обновление
    if len(snake.coordinate):
        snake.stepping(eat)
    else:
        running = False

    board.update(snake.life, snake.score)
    all_sprites.update()
    # Визуализация
    screen.fill(BLACK)  # Очистка эрана
    all_sprites.draw(screen)
    board.draw()
    snake.draw()
    eat.draw(snake)
    pygame.display.flip()  # Показываем кадр

pygame.quit()