import pygame as pg
import random as rand
from pygame import mixer

font = pg.font.SysFont('comicsansms', 25)

w = 1000
h = 750

window = pg.display.set_mode((w, h))
pg.display.set_caption('Tripple Shooter')
bg = pg.transform.scale(pg.image.load('bg.png'), (w, h))

player_width = 50
player_height = 100

head_width = 26
head_height = 25

gun_width = 100
gun_height = 10

bomb_width = 25
bomb_height = 25

player_speed = 5

fast_speed = 10

bomb_speed = 3

points = 0

def draw(player, head, gun, bomb_1, bomb_2, bomb_3, score):

    window.blit(bg, (0, 0))

    pg.draw.rect(window, 'darkgreen', player)
    pg.draw.rect(window, 'yellow', head)
    pg.draw.rect(window, 'black', gun)
    pg.draw.rect(window, 'red', bomb_1)
    pg.draw.rect(window, 'red', bomb_2)
    pg.draw.rect(window, 'red', bomb_3)
    score(points)
    
    pg.display.update()

def score(score):

    text = font.render('Score: ' + str(score), True, black)
    gameDisplay.blit(text, [0,0])

def main():

    run = True

    player = pg.Rect(200, rand.randint(0, 650), player_width, player_height)
    head = pg.Rect(212, player.y - 25, head_width, head_height)
    gun = pg.Rect(212, player.y + 40, gun_width, gun_height)
    bomb_1 = pg.Rect(975, rand.randint(0, 725), bomb_width, bomb_height)
    bomb_2 = pg.Rect(975, rand.randint(0, 725), bomb_width, bomb_height)
    bomb_3 = pg.Rect(975, rand.randint(0, 725), bomb_width, bomb_height)

    while run:

        bomb_1.x -= bomb_speed
        bomb_2.x -= bomb_speed
        bomb_3.x -= bomb_speed

        if bomb_1.x <= player.x:

            run = False

        if bomb_2.x <= player.x:

            run = False

        if bomb_3.x <= player.x:

            run = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:

            player.y -= player_speed
            head.y -= player_speed
            gun.y -= player_speed

        if keys[pg.K_UP]:

            player.y -= fast_speed
            head.y -= fast_speed
            gun.y -= fast_speed

        if keys[pg.K_s]:

            player.y += player_speed
            head.y += player_speed
            gun.y += player_speed

        if keys[pg.K_DOWN]:

            player.y += fast_speed
            head.y += fast_speed
            gun.y += fast_speed

        if bomb_1.y >= player.y and bomb_1.y <= player.y + player_height:

            if keys[pg.K_SPACE]:

                bomb_1.x = 975
                bomb_1.y = rand.randint(0, 725)
                points += 1
                

        if bomb_2.y >= player.y and bomb_2.y <= player.y + player_height:

            if keys[pg.K_SPACE]:

                bomb_2.x = 975
                bomb_2.y = rand.randint(0, 725)
                points += 1

        if bomb_3.y >= player.y and bomb_3.y <= player.y + player_height:

            if keys[pg.K_SPACE]:

                bomb_3.x = 975
                bomb_3.y = rand.randint(0, 725)
                points += 1
                
        for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
                break

        draw(player, head, gun, bomb_1, bomb_2, bomb_3, score)

    pg.quit()

if __name__ == '__main__':

    main()
