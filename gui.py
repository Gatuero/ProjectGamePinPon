import random

import pygame, sys, data_process, entities, action_process

def start():
    # Inicializar Pygame
    pygame.init()
    pygame.mixer.init()
    # Sonidos
    sounds_block = [pygame.mixer.Sound('resource/sounds/ball_block1.wav'),
                    pygame.mixer.Sound('resource/sounds/ball_block2.wav')]
    sound_player = pygame.mixer.Sound('resource/sounds/ball_player.wav')
    sound_error =   pygame.mixer.Sound('resource/sounds/ball_error.wav')
    # Configuraciones de pantalla
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juego Simple')
    # Fuente
    font = pygame.font.SysFont('Arial', 40)
    # Colores
    gray = (55,55, 55)
    blue = (0, 0, 255)
    cyan = (150, 150 ,255)
    red = (255, 0, 0)
    lime = (0, 255, 128)
    green = (0, 200, 0)
    dark_green = (0, 150, 0)

    # Configuración del reloj
    clock = pygame.time.Clock()
    players=[]
    p = entities.Player(0,((screen_height // 2)-25),blue,1)
    players.append(p)
    p = entities.Player(screen_width-25,((screen_height // 2)-25),blue,0)
    players.append(p)
    ball = entities.Ball(screen_height // 2,screen_height // 4,red)

    blocks=[]
    for i in range(6):
        for j in range(12):
            b = entities.Block(screen_width//2+(i*25)-75, (j*25)+150, [lime,green,dark_green,gray],25,0)
            blocks.append(b)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        action_process.check_keys(keys, pygame, players, screen_height)

        # Mover el Bola
        ball.update()
        if data_process.checks_borders(ball, screen_width, screen_height):
            sound_error.play()

        # Comprobar colisiones
        screen.fill(gray)
        screen.blit(
            font.render(
                '['+str(players[1].point)+"]====["+str(len(blocks))+"]====[" +str(players[0].point)+']',
                True, cyan
            ),(265, 50)
        )
        ball_rect=data_process.entity_rect(ball,pygame)
        pygame.draw.rect(screen, red, ball_rect,0,10)
        for player in players:
            player_rect=data_process.entity_rect(player,pygame)
            pygame.draw.rect(screen, player.color, player_rect)
            if data_process.check_collision(player, ball):
                sound_player.play()
                ball.touch_player=player.select+1
                pygame.draw.rect(screen, cyan, player_rect)
            player.update()

        for block in blocks:
            block.update()
            block_rect = data_process.entity_rect(block, pygame)
            pygame.draw.rect(screen, block.color, block_rect)
            if data_process.check_collision(block, ball):
                block.points+=1
                block.give_player=ball.touch_player
                sounds_block[
                    action_process.check_sounds(ball)
                ].play()
                ball.time=3
        data_process.check_player_ball(ball, player,random.randint(1,4))
        data_process.check_blocks(blocks,players)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del bucle
        clock.tick(60)
    pygame.quit()
