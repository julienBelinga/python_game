import pygame
from Game import Game


pygame.init()

# générer la fênetre du jeu
pygame.display.set_caption("Comet fall game")

screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg.jpg')
running = True
game = Game()

while running:

    #affichage
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    #récupération
    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    game.player.all_projectiles.draw(screen)
    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #MAJ écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
