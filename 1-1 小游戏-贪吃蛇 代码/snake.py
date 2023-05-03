import pygame
import random

# 初始化 Pygame 库
pygame.init()

# 设置游戏窗口的大小
window_width = 500
window_height = 500

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 设置蛇的初始位置和长度
snake_x = window_width / 2
snake_y = window_height / 2
snake_speed = 10
snake_length = 1
snake = []

# 设置食物的初始位置
food_x = round(random.randrange(0, window_width - snake_speed) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_speed) / 10.0) * 10.0

# 设置游戏循环标志
game_over = False

# 创建游戏循环
while not game_over:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 处理键盘输入事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_speed
    elif keys[pygame.K_RIGHT]:
        snake_x += snake_speed
    elif keys[pygame.K_UP]:
        snake_y -= snake_speed
    elif keys[pygame.K_DOWN]:
        snake_y += snake_speed

    # 绘制游戏背景
    window.fill(white)

    # 绘制食物
    pygame.draw.rect(window, green, [food_x, food_y, snake_speed, snake_speed])

    # 检测是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - snake_speed) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - snake_speed) / 10.0) * 10.0
        snake_length += 1

    # 检测蛇是否撞墙或撞到自己
    if snake_x < 0 or snake_x > window_width - snake_speed or snake_y < 0 or snake_y > window_height - snake_speed:
        game_over = True
    if snake_length > 1:
        for i in range(1, len(snake)):
            if snake_x == snake[i][0] and snake_y == snake[i][1]:
                game_over = True

    # 更新蛇的身体坐标
    snake.append([snake_x, snake_y])

    if len(snake) > snake_length:
        del snake[0]

    for i in range(len(snake)):
        pygame.draw.rect(window, black, [snake[i][0], snake[i][1], snake_speed, snake_speed])

    # 刷新游戏窗口
    pygame.display.update()

    # 控制游


    # 控制游戏速度
    clock = pygame.time.Clock()
    clock.tick(30)

    #if game_over == True:
    #    pygame.quit()
