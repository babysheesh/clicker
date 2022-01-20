import os
import sys
import random
import pygame
import time

 
pygame.init()

 
clock = pygame.time.Clock()
autog = 0
coins = 0
display_width = 1920
display_height = 1080
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
light_blue = (173, 216, 230)
grey = (128, 128, 128)
blue = (0, 100, 250)
red = (255, 0, 0)
green1 = (0, 50, 0)
green2 = (0, 100, 0)
green3 = (0, 150, 0)
green4 = (0, 200, 0)
green5 = (0, 250, 0)
foto = "111.jpg"
screen_rect = (0, 0, display_width, display_height)
 
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Кликальный клик")
 
 
def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)
 
def autominer():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog
 
 
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
 
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = 0.3
        
    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()

all_sprites = pygame.sprite.Group()


def create_particles(position):
    q = random.randint(1, 10)
    particle_count = q
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))
 
 
def main_loop():
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3
    mong = 1
    cost1 = 5
    cost2 = 50
    cost3 = 250
    cost4 = 1000
    ccost1 = 10
    cсost2 = 100
    cсost3 = 500
    cсost4 = 5000
    ulta = 10000000
    voz = 1
    nomer = 0 
    kart = 0
    global coins
    game_running = True
    gameDisplay.fill(blue)
    rectangle(gameDisplay, red, 750, 0, 750, 1080)
    rectangle(gameDisplay, green4, 1500, 0, 420, 1080)    
    while game_running:
        if game_running: 
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                create_particles(pygame.mouse.get_pos())
                mopos = pygame.mouse.get_pos()
#                print(mopos)
#                print(mopos[0])
#                print(mopos[1])
                if mopos[0] >= 625 and mopos[1] >= 130:
                    if mopos[0] <= 885 and mopos[1] <= 360:
                        coins += mong
                
                if mopos[0] <= 1350 and mopos[1] <= 50:
                    if mopos[0] >= 1150 and mopos[1] >= 0:
                        if coins >= cost1:
                            coins = coins - cost1
                            cost1 = cost1 * 1.3
                            mong = mong + (1 * voz)
                            cost1 = round(cost1, 0)
                
                if mopos[0] <= 1350 and mopos[1] <= 110:
                    if mopos[0] >= 1150 and mopos[1] >= 60:
                        if coins >= cost2:
                            coins = coins - cost2
                            cost2 = cost2 * 1.3
                            mong = mong + (5 * voz)
                            cost2 = round(cost2, 0)
                
                if mopos[0] <= 1350 and mopos[1] <= 170:
                    if mopos[0] >= 1150 and mopos[1] >= 120:
                        if coins >= cost3:
                            coins = coins - cost3
                            cost3 = cost3 * 1.3
                            mong = mong + (15 * voz)
                            cost3 = round(cost3, 0)
                
                if mopos[0] <= 1350 and mopos[1] <= 230:
                    if mopos[0] >= 1150 and mopos[1] >= 180:
                        if coins >= cost4:
                            coins = coins - cost4
                            cost4 = cost4 * 1.3
                            mong = mong + (50 * voz)
                            cost4 = round(cost4, 0)
                
                if mopos[0] >= 130 and mopos[1] >= 0:
                    if mopos[0] <= 330 and mopos[1] <= 50:
                        if coins >= ccost1:
                            coins = coins - ccost1
                            ccost1 = ccost1 * 1.4
                            autog = autog + (0.1 * voz)
                            ccost1 = round(ccost1, 0)
                
                if mopos[0] >= 130 and mopos[1] >= 60:
                    if mopos[0] <= 330 and mopos[1] <= 110:
                        if coins >= cсost2:
                            coins = coins - cсost2
                            cсost2 = cсost2 * 1.4
                            autog = autog + (0.3 * voz)
                            cсost2 = round(cсost2, 0)
                
                if mopos[0] >= 130 and mopos[1] >= 120:
                    if mopos[0] <= 330 and mopos[1] <= 170:
                        if coins >= cсost3:
                            coins = coins - cсost3
                            cсost3 = cсost3 * 1.4
                            autog = autog + (1 * voz)
                            cсost3 = round(cсost3, 0)
                
                if mopos[0] >= 130 and mopos[1] >= 180:
                    if mopos[0] <= 330 and mopos[1] <= 220:
                        if coins >= cсost4:
                            coins = coins - cсost4
                            cсost4 = cсost4 * 1.44
                            autog = autog + (3.5 * voz)
                            cсost4 = round(cсost4, 0)
                
                if mopos[0] <= 850 and mopos[1] <= 1000:
                    if mopos[0] >= 650 and mopos[1] >= 700:
                        if coins >= ulta:
                            voz += 0.1
                            mong = 1 * voz
                            cost1 = 10
                            cost2 = 50
                            cost3 = 250
                            ccost1 = 10
                            coost2 = 100
                            coost3 = 500
                            ulta = ulta * 10
                            autog = 0
                            coins = 0
                            nomer += 1
                
                if mopos[0] >= 1820 and mopos[1] >= 980:
                    sys.exit()
                
                if mopos[0] >= 1500 and mopos[1] >= 200:
                    if mopos[0] <= 1600 and mopos[1] <= 300:
                        kart = 0
                
                if mopos[0] >= 1660 and mopos[1] >= 200:
                    if mopos[0] <= 1760 and mopos[1] <= 300:
                        kart = 1
                
                if mopos[0] >= 1820 and mopos[1] >= 200:
                    if mopos[0] <= 1920 and mopos[1] <= 300:
                        kart = 2
        
        
        gameDisplay.fill(blue)
        rectangle(gameDisplay, red, 750, 0, 750, 1080)
        rectangle(gameDisplay, green4, 1500, 0, 420, 1080)
        rectangle(gameDisplay, red, 1820, 980, 100, 1000)
        rectangle(gameDisplay, blue, 1500, 200, 100, 100)
        rectangle(gameDisplay, blue, 1660, 200, 100, 100)
        rectangle(gameDisplay, blue, 1820, 200, 100, 100)
        if kart == 0:
            rectangle(gameDisplay, black, 1500, 200, 100, 100)
            rectangle(gameDisplay, blue, 1660, 200, 100, 100)
            rectangle(gameDisplay, blue, 1820, 200, 100, 100)
            foto = "111.jpg"
            image = load_image(foto)
            image1 = pygame.transform.scale(image, (260, 225))
            screen.blit(image1, (625, 130))            
        if kart == 1:
            rectangle(gameDisplay, blue, 1500, 200, 100, 100)
            rectangle(gameDisplay, black, 1660, 200, 100, 100)
            rectangle(gameDisplay, blue, 1820, 200, 100, 100)
            foto = "222.jpg"
            image = load_image(foto)
            image1 = pygame.transform.scale(image, (260, 225))
            screen.blit(image1, (625, 130))                
        if kart == 2:
            rectangle(gameDisplay, blue, 1500, 200, 100, 100)
            rectangle(gameDisplay, blue, 1660, 200, 100, 100)
            rectangle(gameDisplay, black, 1820, 200, 100, 100)
            foto = "333.jpg"
            image = load_image(foto)
            image1 = pygame.transform.scale(image, (260, 225))
            screen.blit(image1, (625, 130))            
        DrawText("Настройки:", black, green4, 1720, 100, 35)        
        DrawText("Выход", black, red, 1875, 1030, 20)
        DrawText("Кликальный клик", black, light_blue, 750, 100, 50)
        DrawText("у вас есть " + str(f'{coins:.2f}') + " монет", black, light_blue, 750, 55, 20)
        DrawText("Обнуление: " + str(nomer), black, light_blue, 750, 27, 20)
#        circle(gameDisplay, blue, 750, 260, 130)
        rectangle(gameDisplay, blue, 1150, 0, 200, 50)
        DrawText("Мышь(+1)", black, light_blue, 1100, 27, 20)
        DrawText("Цена:" + str(int(cost1)), black, light_blue, 1420, 27, 20)
        rectangle(gameDisplay, blue, 1150, 60, 200, 50)
        DrawText("Клава(+5)", black, light_blue, 1100, 87, 20)
        DrawText("Цена:" + str(int(cost2)), black, light_blue, 1420, 87, 20)
        rectangle(gameDisplay, blue, 1150, 120, 200, 50)
        DrawText("Моник(+15)", black, light_blue, 1090, 147, 20)
        DrawText("Цена:" + str(int(cost3)), black, light_blue, 1420, 147, 20)
        rectangle(gameDisplay, blue, 1150, 180, 200, 50)
        DrawText("Игровая мышь(+50)", black, light_blue, 1045, 207, 20)
        DrawText("Цена:" + str(cost4), black, light_blue, 1420, 207, 20)           
        rectangle(gameDisplay, red, 130, 0, 200, 50)        
        DrawText("боковые кнопки мыши(+0.1)", black, light_blue, 485, 27, 20)
        DrawText("Цена:" + str(int(ccost1)), black, light_blue, 70, 27, 20)
        rectangle(gameDisplay, red, 130, 60, 200, 50)        
        DrawText("еда(+0.3)", black, light_blue, 390, 87, 20)
        DrawText("Цена:" + str(int(cсost2)), black, light_blue, 70, 87, 20)
        rectangle(gameDisplay, red, 130, 120, 200, 50)        
        DrawText("Колонки(+1)", black, light_blue, 400, 147, 20)
        DrawText("Цена:" + str(int(cсost3)), black, light_blue, 70, 147, 20)
        rectangle(gameDisplay, red, 130, 180, 200, 50)        
        DrawText("Наушники(+3.5)", black, light_blue, 410, 207, 20)
        DrawText("Цена:" + str(int(cсost4)), black, light_blue, 70, 207, 20)
        if coins >= ulta // 10000:
            rectangle(gameDisplay, green1, 650, 950, 200, 50)
        if coins >= ulta // 1000:
            rectangle(gameDisplay, green2, 650, 900, 200, 100)
        if coins >= ulta // 100:
            rectangle(gameDisplay, green3, 650, 850, 200, 150)
        if coins >= ulta // 10:
            rectangle(gameDisplay, green4, 650, 800, 200, 200)
        if coins >= ulta:
            rectangle(gameDisplay, green5, 650, 750, 200, 250)
        all_sprites.update()
        all_sprites.draw(screen)         
        pygame.display.update()
        clock.tick(60)
 
 
main_loop()
pygame.quit()
quit()