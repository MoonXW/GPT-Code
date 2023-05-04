import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口尺寸
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

# 设置游戏窗口大小并创建窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("飞机大战")

# 加载游戏素材
player_img = pygame.image.load("D:\PythonWorkspace\\gpt\\fly\\player.png")
bullet_img = pygame.image.load("D:\PythonWorkspace\\gpt\\fly\\bullet.png")
enemy_img = pygame.image.load("D:\PythonWorkspace\\gpt\\fly\\enemy.png")
explosion_imgs = [pygame.image.load(f"D:\PythonWorkspace\\gpt\\fly\\explosion{i}.png") for i in range(1, 6)]

# 飞机和子弹的尺寸
player_size = player_img.get_size()
bullet_size = bullet_img.get_size()
enemy_size = enemy_img.get_size()

# 飞机和子弹的初始位置
player_pos = [WINDOW_WIDTH / 2 - player_size[0] / 2, WINDOW_HEIGHT - player_size[1]]
bullet_pos = [0, 0]

# 飞机和子弹的速度
player_speed = 0.1 #5
bullet_speed = 0.1 #10

# 敌机的属性
enemy_spawn_delay = 60
enemy_spawn_timer = 0
enemy_speed = 0.1 #3
enemies = []

# 爆炸特效的属性
explosion_delay = 505 #5
explosion_timer = 0
explosions = []

# 游戏循环标志
game_running = True

# 游戏主循环
while game_running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 发射子弹
                bullet_pos[0] = player_pos[0] + player_size[0] / 2 - bullet_size[0] / 2
                bullet_pos[1] = player_pos[1]
    
    # 移动玩家飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    elif keys[pygame.K_RIGHT] and player_pos[0] < WINDOW_WIDTH - player_size[0]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    elif keys[pygame.K_DOWN] and player_pos[1] < WINDOW_HEIGHT - player_size[1]:
        player_pos[1] += player_speed
    
    # 移动子弹和敌机，检测碰撞
    if bullet_pos[1] > 0:
        # 子弹在屏幕内时移动
        bullet_pos[1] -= bullet_speed
        for enemy in enemies:
            # 检测子弹与敌机的碰撞
            if bullet_pos[0] + bullet_size[0] > enemy[0] and bullet_pos[0] < enemy[0] + enemy_size[0] and \
               bullet_pos[1] + bullet_size[1] > enemy[1] and bullet_pos[1] < enemy[1] + enemy_size[1]:
                # 敌机被击中，添加爆炸特效
                explosions.append([enemy[0], enemy[1]])
                # 移除敌机和子弹
                enemies.remove(enemy)
                bullet_pos = [0, 0]
                break
    else:
        # 子弹不在屏幕内时重置位置
        bullet_pos = [0, 0]
        
    # 生成敌机
    if enemy_spawn_timer <= 0:
        enemies.append([random.randint(0, WINDOW_WIDTH - enemy_size[0]), -enemy_size[1]])
        enemy_spawn_timer = enemy_spawn_delay
    else:
        enemy_spawn_timer -= 1

    # 移动敌机
    for enemy in enemies:
        enemy[1] += enemy_speed

    # 绘制游戏场景
    window.fill((0, 0, 0))
    window.blit(player_img, player_pos)
    if bullet_pos[1] > 0:
        window.blit(bullet_img, bullet_pos)
    for enemy in enemies:
        window.blit(enemy_img, enemy)
    for explosion in explosions:
        if explosion_timer < explosion_delay:
            window.blit(explosion_imgs[explosion_timer // (explosion_delay // len(explosion_imgs))], explosion)
            explosion_timer += 1
        else:
            explosions.remove(explosion)
            explosion_timer = 0
    pygame.display.update()
        