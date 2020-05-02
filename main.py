import pygame

import GameBoard

WIDTH = 400
HEIGHT = 600
FPS = 60

pygame.init()  # Запускаем pygame.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Задаём разрешение экрана.
pygame.display.set_caption('Змейка')  # Заголовок окна игры.
clock = pygame.time.Clock()  # Инициализируем время, отсчет идет от init()

# Инициализируем наши объекты.
snake = GameBoard.snake(screen)
board = GameBoard.board(screen, snake.life, 0)
eat = GameBoard.eat(screen)

running = True
while running:
    clock.tick(20)
    # Ввод собития.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Выясняем какая именно кнопка была нажата.

            # Кнопки вектора движения. Змейка не должна себя съедать, меняя вектор на  противоположный.
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

    # Обновление.
    if len(snake.coordinate):
        snake.stepping(eat)
    else:
        running = False

    board.update(snake.life, snake.score)

    # Визуализация.
    screen.fill(GameBoard.color['BLACK'])  # Очистка эрана. Заливка черным цветом.

    board.draw()
    snake.draw()
    eat.draw(snake)

    pygame.display.flip()  # Показываем кадр.

pygame.quit()