def check_keys(keys, pygame, players, outside_y):
    if keys[pygame.K_UP] and players[0].y > -25:
        players[0].y -= players[0].move
    if keys[pygame.K_DOWN] and players[0].y < outside_y - players[0].height+25:
        players[0].y += players[0].move

def check_sounds(entity):
    entity.sound += 1
    if entity.sound > 1:
        entity.sound = 0
    return entity.sound