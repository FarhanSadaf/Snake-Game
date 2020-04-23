import pygame
from data import config
from data.snake import Snake
from data.food import Food
pygame.init()

font = pygame.font.SysFont('agencyfb', 30)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption('Snakes')

snake = Snake(0, 0)
food = Food(config.rand_location())
score = 0


def redraw_window():
    screen.fill((51, 51, 51))
    score_text = font.render(f'Score: {score}', 1, (200, 200, 200))
    screen.blit(score_text, (config.width - score_text.get_width() - 10, 0))

    snake.update()
    snake.show(screen)
    food.show(screen)

    pygame.display.update()


def game_over():
    # The game will wait for 7 sec. for player to tap space
    # else game will quit
    global score
    gameover_text = pygame.font.SysFont('agencyfb', 100).render(
        'Game Over', 1, (200, 200, 200))
    screen.blit(gameover_text, ((config.width-gameover_text.get_width()) //
                                2, (config.height-gameover_text.get_height())//2))
    continue_text = pygame.font.SysFont('agencyfb', 20).render(
        'Tap space to restart', 1, (200, 200, 200))
    screen.blit(continue_text, ((config.width-continue_text.get_width()) // 2,
                                (config.height-gameover_text.get_height())//2 + gameover_text.get_height()))
    pygame.display.update()

    restart_game = False
    for i in range(700):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart_game = True
            break

    if restart_game:
        snake.reborn(0, 0)
        score = 0
    else:
        pygame.quit()


# mainloop
run = True
while run:
    # clock.tick(10)
    fps = 50 + (score-35)//10 if score > 35 else 10 + score
    fps = 90 if fps >= 90 else fps
    clock.tick(fps)

    if snake.hit():
        game_over()

    if snake.eat(food):
        score += 1
        nextfood_pos = config.rand_location()
        while snake.body_in(nextfood_pos[0], nextfood_pos[1]):
            nextfood_pos = config.rand_location()
        food.change_location(nextfood_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.dir(0, -1)
        if keys[pygame.K_DOWN]:
            snake.dir(0, 1)
        if keys[pygame.K_RIGHT]:
            snake.dir(1, 0)
        if keys[pygame.K_LEFT]:
            snake.dir(-1, 0)

    redraw_window()

pygame.quit()
