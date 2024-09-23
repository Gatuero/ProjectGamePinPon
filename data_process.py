def check_collision(entity, ball):
    aux_hspeed = 0
    aux_hspeed = is_collision_left(entity,ball,aux_hspeed)
    aux_hspeed = is_collision_right(entity,ball,aux_hspeed)
    if aux_hspeed!=0 and ball.time==0:
        ball_top = ball.y
        ball_bottom = ball.y+ball.height

        entity_top = entity.y
        entity_top_middle = entity.y+(entity.height/4)
        entity_middle = entity.y+(entity.height/2)
        entity_bottom_middle= entity.y+(entity.height*(3/4))
        entity_bottom = entity.y+entity.height

        if entity_top < ball_bottom and ball_top<entity_bottom:
            if entity_top < ball_bottom < entity_top_middle:
                ball.vspeed = 3
            elif entity_top_middle<ball_bottom<entity_middle:
                ball.vspeed = 2
            elif entity_middle < ball_top < entity_bottom_middle:
                ball.vspeed = -2
            elif entity_bottom_middle < ball_top < entity_bottom:
                ball.vspeed = -3
            ball.hspeed = aux_hspeed
            return True
        else:
            return False
    else:
        return False
def checks_borders(ball, outside_x, outside_y):
    collision=False
    if ball.x < -25:
        ball.x = outside_x-ball.width+25
        ball.y = outside_y - ball.y
    elif ball.x+ball.width  > outside_x+25:
        ball.x = -25
        ball.y = outside_y - ball.y
    if ball.y <0:
        ball.vspeed=-3
        collision=True
    elif ball.y+ball.height > outside_y:
        ball.vspeed=3
        collision=True
    return collision
def is_collision_left(entity,ball,aux_hspeed):
    if ball.x<entity.x + entity.width<(ball.x+ball.width):
        aux_hspeed=-4
    return aux_hspeed
def is_collision_right(entity,ball,aux_hspeed):
    if ball.x<entity.x<(ball.x+ball.width):
        aux_hspeed=4
    return aux_hspeed
def entity_rect(entity, pygame):
    return pygame.Rect(entity.x, entity.y, entity.width, entity.height)
def check_blocks(blocks,players):
    num_blocks=len(blocks)
    for i in range(num_blocks):
        if blocks[i].points>2:
            j=blocks[i].give_player
            if j!=0:
                players[j-1].point+=1
            blocks.pop(i)
            break
def check_player_ball(ball,player,moveRandom):
    if ball.y>player.y+(player.height/2):
        player.move=-moveRandom
    elif ball.y<player.y+(player.height/3):
        player.move=moveRandom
    else:
        player.move=0
