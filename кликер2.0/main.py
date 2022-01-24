import os
import sys
import random
import pygame
import time
import sqlite3

pygame.init()

clicks = 0

db = sqlite3.connect('clicker.db')
cur = db.cursor()
clock = pygame.time.Clock()
autog = 0
coins = 10000000
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
nado = 0
green5 = (0, 250, 0)
yel = (255, 255, 0)
foto = "111.jpg"
# Start auto clicker
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)
screen_rect = (0, 0, display_width, display_height)

pygame.mixer.music.load('fon.mp3')
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play()
pygame.mixer.music.play(loops=-1)

sound1 = pygame.mixer.Sound('monnetka.mp3')
sound2 = pygame.mixer.Sound('upgr.mp3')
sound3 = pygame.mixer.Sound('oshibka.mp3')
sound4 = pygame.mixer.Sound('game-won.mp3')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Кликальный клик")


def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)


def autominer():
    global coins
    global autog
    coins = coins + autog


def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)


def create_particles(position, nado):
    q = random.randint(5, 20)
    particle_count = q
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), nado)


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


all_sprites = pygame.sprite.Group()


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера\
    fire = []
    fiire = []
    star1 = 'starr.png'
    star2 = 'starrr.png'
    star3 = 'starrrr.png'
    star4 = 'starrrrr.png'
    for scale in (15, 20, 30):
        fire.append(pygame.transform.scale(load_image(star1), (scale, scale)))
        fiire.append(pygame.transform.scale(load_image(star2), (scale, scale)))
        fiire.append(pygame.transform.scale(load_image(star3), (scale, scale)))
        fiire.append(pygame.transform.scale(load_image(star4), (scale, scale)))

    def __init__(self, pos, dx, dy, nado):
        super().__init__(all_sprites)
        if nado != 0:
            self.image = random.choice(self.fire)
        else:
            self.image = random.choice(self.fiire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.2

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ВЫ начинаете играть в лучшую игру 22 века", "",
                  "Правила игры:",
                  "Кликай",
                  "И",
                  "Очень много кликай"]

    fon = pygame.transform.scale(load_image('menu1.jpg'), (1920, 1080))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 250
    for line in intro_text:
        DrawText(line, black, white, 950, text_coord, 50)
        text_coord += 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(60)


def final_screen(clicks):
    intro_text = ["вы вышли из игры", "",
                  "за всё время вы сделали",
                  str(clicks),
                  "клик(ов)(а)",
                  "моргенштерн доволен",
                  "нажмите ЛКМ для выхода",
                  "или иную баттен для возврата"]

    fon = pygame.transform.scale(load_image('lilmorgen.jfif'), (1920, 1080))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 500
    for line in intro_text:
        DrawText(line, black, white, 950, text_coord, 50)
        text_coord += 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def main_loop():
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3
    global clicks
    sprava_first_lvl = ['деДский сад', 'дошик', 'шаверма', 'вода', 'пицца', 'пюрешка', 'чёрный хлеб', 'суси',
                        'заплесневелый сыр', 'воздух', 'да', 'да', 'да', 'да', 'да']
    sprava_second_lvl = ['шкИла', 'ролтон', 'шаурма', 'чай', 'пицца с ананасами', 'макарошки', 'нормальный хлеб',
                         'роллы',
                         'сыр', 'вакуум', 'нет', 'нет', 'нет', 'нет', 'нет']
    sprava_third_lvl = ['уник', 'лапша', 'гирос', 'кофеёк', 'пепперони', 'котлетки', 'нарезной хлеб', 'рыбка с икрой',
                        'президент', 'пространство', 'возможно', 'возможно', 'возможно', 'возможно', 'возможно']
    sleva_first_lvl = ['хухл', 'мышь', 'клава', 'моник', 'крутая мышь', 'тубаретка', 'подсветка', 'питхон', 'пайчарм',
                       'яндекс', 'lf', 'lf', 'lf', 'lf', 'lf']
    sleva_second_lvl = ['ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn', 'ytn',
                        'ytn', 'ytn']
    sleva_third_lvl = ['djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj',
                       'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', 'djpvj;yj', ]
    grom = 0.07
    groom = 0.5
    kk = random.randint(0, 1720)
    jj = random.randint(0, 980)
    kkk = random.randint(10, 150)
    jjj = random.randint(10, 150)
    sound1.set_volume(groom)
    sound2.set_volume(groom)
    sound3.set_volume(groom)
    sound4.set_volume(groom - 0.3)
    up1 = 1
    up2 = 5
    up3 = 15
    up4 = 50
    up5 = 250
    up6 = 500
    up7 = 1000
    up8 = 2500
    up9 = 5000
    up10 = 8500
    up11 = 0
    up12 = 0
    up13 = 0
    up14 = 0
    up15 = 0
    uup1 = 1
    uup2 = 5
    uup3 = 15
    uup4 = 50
    uup5 = 250
    uup6 = 500
    uup7 = 1000
    uup8 = 2500
    uup9 = 5000
    uup10 = 8500
    uup11 = 0
    uup12 = 0
    uup13 = 0
    uup14 = 0
    uup15 = 0
    mong = 1
    cost1 = 5
    cost2 = 50
    cost3 = 250
    cost4 = 1000
    cost5 = 25000
    cost6 = 100000
    cost7 = 500000
    cost8 = 1500000
    cost9 = 3000000
    cost10 = 5000000
    cost11 = 0
    cost12 = 0
    cost13 = 0
    cost14 = 0
    cost15 = 0
    ccost1 = 10
    ccost2 = 100
    ccost3 = 500
    ccost4 = 2000
    ccost5 = 50000
    ccost6 = 200000
    ccost7 = 1000000
    ccost8 = 3000000
    ccost9 = 6000000
    ccost10 = 10000000
    ccost11 = 0
    ccost12 = 0
    ccost13 = 0
    ccost14 = 0
    ccost15 = 0
    ulta = 10000000
    voz = 1
    kart = 0
    bonus = 0
    nado = 0
    udv = 1
    vrem = 400
    nomer = 0
    global coins
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == MYEVENTTYPE:
                coins = coins + autog

            if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 3):
                clicks += 1

                color = gameDisplay.get_at(pygame.mouse.get_pos())
                mopos = pygame.mouse.get_pos()
                if color[0] == 255 and color[1] == 255 and color[2] == 0 and udv == 1:
                    udv = 2

                if mopos[0] >= 625 and mopos[1] >= 130:
                    if mopos[0] <= 885 and mopos[1] <= 360:
                        sound1.play()
                        coins += mong * udv * voz
                        # if udv != 2:
                        #    create_particles(pygame.mouse.get_pos(), 1)
                        # else:
                        #    create_particles(pygame.mouse.get_pos(), 0)

                if mopos[0] <= 1350 and mopos[1] <= 50:
                    if mopos[0] >= 1150 and mopos[1] >= 0:
                        if coins >= cost1:
                            sound2.play()
                            coins = coins - cost1
                            cost1 = cost1 * 1.3
                            mong = mong + 1
                            cost1 = round(cost1, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 110:
                    if mopos[0] >= 1150 and mopos[1] >= 60:
                        if coins >= cost2:
                            sound2.play()
                            coins = coins - cost2
                            cost2 = cost2 * 1.3
                            mong = mong + 5
                            cost2 = round(cost2, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 170:
                    if mopos[0] >= 1150 and mopos[1] >= 120:
                        if coins >= cost3:
                            sound2.play()
                            coins = coins - cost3
                            cost3 = cost3 * 1.3
                            mong = mong + 15
                            cost3 = round(cost3, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 230:
                    if mopos[0] >= 1150 and mopos[1] >= 180:
                        if coins >= cost4:
                            sound2.play()
                            coins = coins - cost4
                            cost4 = cost4 * 1.3
                            mong = mong + 50
                            cost4 = round(cost4, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 290:
                    if mopos[0] >= 1150 and mopos[1] >= 240:
                        if coins >= cost5:
                            sound2.play()
                            coins = coins - cost5
                            cost5 = cost5 * 1.3
                            mong = mong + 250
                            cost5 = round(cost5, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 350:
                    if mopos[0] >= 1150 and mopos[1] >= 300:
                        if coins >= cost6:
                            sound2.play()
                            coins = coins - cost6
                            cost6 = cost6 * 1.3
                            mong = mong + 500
                            cost6 = round(cost6, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 410:
                    if mopos[0] >= 1150 and mopos[1] >= 360:
                        if coins >= cost7:
                            sound2.play()
                            coins = coins - cost7
                            cost7 = cost7 * 1.3
                            mong = mong + 1000
                            cost7 = round(cost7, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 470:
                    if mopos[0] >= 1150 and mopos[1] >= 420:
                        if coins >= cost8:
                            sound2.play()
                            coins = coins - cost8
                            cost8 = cost8 * 1.3
                            mong = mong + 2500
                            cost8 = round(cost8, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 530:
                    if mopos[0] >= 1150 and mopos[1] >= 480:
                        if coins >= cost9:
                            sound2.play()
                            coins = coins - cost9
                            cost9 = cost9 * 1.3
                            mong = mong + up9
                            cost9 = round(cost9, 0)
                        else:
                            sound3.play()
                if mopos[0] <= 1350 and mopos[1] <= 590:
                    if mopos[0] >= 1150 and mopos[1] >= 540:
                        if coins >= cost10:
                            sound2.play()
                            coins = coins - cost10
                            cost10 = cost10 * 1.3
                            mong = mong + up10
                            cost10 = round(cost10, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 1350 and mopos[1] <= 650:
                    if mopos[0] >= 1150 and mopos[1] >= 600:
                        if coins >= cost11:
                            sound2.play()
                            coins = coins - cost11
                            cost11 = cost11 * 1.3
                            mong = mong + up11
                            cost11 = round(cost11, 0)
                        else:
                            sound3.play()
                if mopos[0] <= 1350 and mopos[1] <= 710:
                    if mopos[0] >= 1150 and mopos[1] >= 660:
                        if coins >= cost12:
                            sound2.play()
                            coins = coins - cost12
                            cost12 = cost12 * 1.3
                            mong = mong + up12
                            cost12 = round(cost12, 0)
                        else:
                            sound3.play()
                if mopos[0] <= 1350 and mopos[1] <= 770:
                    if mopos[0] >= 1150 and mopos[1] >= 720:
                        if coins >= cost13:
                            sound2.play()
                            coins = coins - cost13
                            cost13 = cost13 * 1.3
                            mong = mong + up13
                            cost13 = round(cost13, 0)
                        else:
                            sound3.play()
                if mopos[0] <= 1350 and mopos[1] <= 830:
                    if mopos[0] >= 1150 and mopos[1] >= 780:
                        if coins >= cost14:
                            sound2.play()
                            coins = coins - cost14
                            cost14 = cost14 * 1.3
                            mong = mong + up14
                            cost14 = round(cost14, 0)
                        else:
                            sound3.play()
                if mopos[0] <= 1350 and mopos[1] <= 890:
                    if mopos[0] >= 1150 and mopos[1] >= 840:
                        if coins >= cost15:
                            sound2.play()
                            coins = coins - cost15
                            cost15 = cost15 * 1.3
                            mong = mong + up15
                            cost15 = round(cost15, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 0:
                    if mopos[0] <= 330 and mopos[1] <= 50:
                        if coins >= ccost1:
                            sound2.play()
                            coins = coins - ccost1
                            ccost1 = ccost1 * 1.4
                            autog = autog + (uup1 * voz)
                            ccost1 = round(ccost1, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 60:
                    if mopos[0] <= 330 and mopos[1] <= 110:
                        if coins >= ccost2:
                            sound2.play()
                            coins = coins - ccost2
                            ccost2 = ccost2 * 1.4
                            autog = autog + (uup2 * voz)
                            ccost2 = round(ccost2, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 120:
                    if mopos[0] <= 330 and mopos[1] <= 170:
                        if coins >= ccost3:
                            sound2.play()
                            coins = coins - ccost3
                            ccost3 = ccost3 * 1.4
                            autog = autog + (uup3 * voz)
                            ccost3 = round(ccost3, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 180:
                    if mopos[0] <= 330 and mopos[1] <= 230:
                        if coins >= ccost4:
                            sound2.play()
                            coins = coins - ccost4
                            ccost4 = ccost4 * 1.4
                            autog = autog + (uup4 * voz)
                            ccost4 = round(ccost4, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 240:
                    if mopos[0] <= 330 and mopos[1] <= 290:
                        if coins >= ccost5:
                            sound2.play()
                            coins = coins - ccost5
                            ccost5 = ccost5 * 1.4
                            autog = autog + (uup5 * voz)
                            ccost5 = round(ccost5, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 300:
                    if mopos[0] <= 330 and mopos[1] <= 350:
                        if coins >= ccost6:
                            sound2.play()
                            coins = coins - ccost6
                            ccost6 = ccost6 * 1.4
                            autog = autog + (uup6 * voz)
                            ccost6 = round(ccost6, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 360:
                    if mopos[0] <= 330 and mopos[1] <= 410:
                        if coins >= ccost7:
                            sound2.play()
                            coins = coins - ccost7
                            ccost7 = ccost7 * 1.4
                            autog = autog + (uup7 * voz)
                            ccost7 = round(ccost7, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 420:
                    if mopos[0] <= 330 and mopos[1] <= 470:
                        if coins >= ccost8:
                            sound2.play()
                            coins = coins - ccost8
                            ccost8 = ccost8 * 1.4
                            autog = autog + (uup8 * voz)
                            ccost8 = round(ccost8, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 480:
                    if mopos[0] <= 330 and mopos[1] <= 530:
                        if coins >= ccost9:
                            sound2.play()
                            coins = coins - ccost9
                            ccost9 = ccost9 * 1.4
                            autog = autog + (uup9 * voz)
                            ccost9 = round(ccost9, 0)
                        else:
                            sound3.play()

                if mopos[0] >= 130 and mopos[1] >= 540:
                    if mopos[0] <= 330 and mopos[1] <= 590:
                        if coins >= ccost10:
                            sound2.play()
                            coins = coins - ccost10
                            ccost10 = ccost10 * 1.4
                            autog = autog + (uup10 * voz)
                            ccost10 = round(ccost10, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 600:
                    if mopos[0] <= 330 and mopos[1] <= 650:
                        if coins >= ccost11:
                            sound2.play()
                            coins = coins - ccost11
                            ccost11 = ccost11 * 1.4
                            autog = autog + (uup11 * voz)
                            ccost11 = round(ccost11, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 660:
                    if mopos[0] <= 330 and mopos[1] <= 710:
                        if coins >= ccost12:
                            sound2.play()
                            coins = coins - ccost12
                            ccost12 = ccost12 * 1.4
                            autog = autog + (uup12 * voz)
                            ccost12 = round(ccost12, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 720:
                    if mopos[0] <= 330 and mopos[1] <= 770:
                        if coins >= ccost13:
                            sound2.play()
                            coins = coins - ccost13
                            ccost13 = ccost13 * 1.4
                            autog = autog + (uup13 * voz)
                            ccost13 = round(ccost13, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 780:
                    if mopos[0] <= 330 and mopos[1] <= 830:
                        if coins >= ccost14:
                            sound2.play()
                            coins = coins - ccost14
                            ccost14 = ccost14 * 1.4
                            autog = autog + (uup14 * voz)
                            ccost14 = round(ccost14, 0)
                        else:
                            sound3.play()
                if mopos[0] >= 130 and mopos[1] >= 840:
                    if mopos[0] <= 330 and mopos[1] <= 890:
                        if coins >= ccost15:
                            sound2.play()
                            coins = coins - ccost15
                            ccost15 = ccost15 * 1.4
                            autog = autog + (uup15 * voz)
                            ccost15 = round(ccost15, 0)
                        else:
                            sound3.play()

                if mopos[0] <= 850 and mopos[1] <= 1080:
                    if mopos[0] >= 650 and mopos[1] >= 830:
                        if coins >= ulta:
                            voz += 0.2
                            mong = 1
                            cost1 = 5
                            cost2 = 50
                            cost3 = 250
                            cost4 = 1000
                            cost5 = 25000
                            cost6 = 100000
                            cost7 = 500000
                            cost8 = 1500000
                            cost9 = 3000000
                            cost10 = 5000000
                            ccost1 = 10
                            ccost2 = 100
                            ccost3 = 500
                            ccost4 = 2000
                            ccost5 = 50000
                            ccost6 = 200000
                            ccost7 = 1000000
                            ccost8 = 3000000
                            ccost9 = 6000000
                            ccost10 = 10000000
                            ulta = ulta * 10
                            autog = 0
                            nomer += 1
                            coins = 100000000
                            sound4.play()

                if mopos[0] >= 1820 and mopos[1] >= 980:
                    return

                if mopos[0] >= 1500 and mopos[1] >= 200:
                    if mopos[0] <= 1600 and mopos[1] <= 300:
                        kart = 0
                        pygame.mixer.music.load('fon.mp3')
                        pygame.mixer.music.set_volume(grom)
                        pygame.mixer.music.play()
                        pygame.mixer.music.play(loops=-1)

                if mopos[0] >= 1660 and mopos[1] >= 200:
                    if mopos[0] <= 1760 and mopos[1] <= 300:
                        kart = 1
                        pygame.mixer.music.load('fonn2.mp3')
                        pygame.mixer.music.set_volume(grom)
                        pygame.mixer.music.play()
                        pygame.mixer.music.play(loops=-1)

                if mopos[0] >= 1820 and mopos[1] >= 200:
                    if mopos[0] <= 1920 and mopos[1] <= 300:
                        kart = 2
                        pygame.mixer.music.load('morgenn.mp3')
                        pygame.mixer.music.set_volume(grom)
                        pygame.mixer.music.play()
                        pygame.mixer.music.play(loops=-1)

                if mopos[0] >= 1560 and mopos[1] >= 470:
                    if mopos[0] <= 1660 and mopos[1] <= 500:
                        grom -= 0.01
                        if grom <= 0:
                            grom = 0
                        grom = min(grom, 10.0)
                        pygame.mixer.music.set_volume(grom)

                if mopos[0] >= 1790 and mopos[1] >= 437:
                    if mopos[0] <= 1890 and mopos[1] <= 537:
                        grom += 0.01
                        if grom < 0.01:
                            grom = 0
                        grom = min(grom, 10.0)
                        pygame.mixer.music.set_volume(grom)

                if mopos[0] >= 1560 and mopos[1] >= 670:
                    if mopos[0] <= 1660 and mopos[1] <= 700:
                        groom -= 0.01
                        if groom <= 0:
                            groom = 0
                        groom = min(groom, 10.0)
                        sound1.set_volume(groom)
                        sound2.set_volume(groom)
                        sound3.set_volume(groom)

                if mopos[0] >= 1790 and mopos[1] >= 637:
                    if mopos[0] <= 1890 and mopos[1] <= 737:
                        groom += 0.01
                        if groom <= 0:
                            groom = 0
                        groom = min(groom, 10.0)
                        sound1.set_volume(groom)
                        sound2.set_volume(groom)
                        sound3.set_volume(groom)
        gameDisplay.fill(blue)

        rectangle(gameDisplay, red, 750, 0, 750, 1080)
        rectangle(gameDisplay, green4, 1500, 0, 420, 1080)
        if kart != 2:
            rectangle(gameDisplay, red, 1820, 980, 100, 1000)
        else:
            image2 = load_image('абанк.png')
            blocksred = pygame.transform.scale(image2, (100, 100))
            screen.blit(blocksred, (1820, 980))
        if udv == 2:
            gameDisplay.fill(yel)
            vrem -= 1
            nado = 0
            bonus = 0
            if vrem == 0:
                udv = 1
                vrem = 200
        DrawText(f"Количество кликов: {clicks}", black, light_blue, 150, 1050, 25)
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
        DrawText("Настройки:", black, green4, 1720, 100, 35)
        DrawText("Громкость Музыки:", black, green4, 1720, 400, 35)
        if grom < 0.02 and grom > 0.01:
            grom = 0.02
        if grom < 0.11 and grom > 0.10:
            grom = 0.11
        DrawText(str(round(autog, 2)) + " монет в секунду", black, light_blue, 750, 415, 35)
        DrawText('и ' + str(round(mong * udv * voz, 2)) + " за клик", black, light_blue, 750, 455, 35)
        DrawText("Вы зарабатываете ", black, light_blue, 750, 375, 35)
        rectangle(gameDisplay, red, 1560, 470, 100, 30)
        rectangle(gameDisplay, red, 1790, 470, 100, 30)
        rectangle(gameDisplay, red, 1825, 437, 30, 100)
        DrawText("Громкость эффектов:", black, green4, 1720, 600, 35)
        DrawText(str(int(groom * 100)), black, green4, 1730, 685, 35)
        rectangle(gameDisplay, red, 1560, 670, 100, 30)
        rectangle(gameDisplay, red, 1790, 670, 100, 30)
        rectangle(gameDisplay, red, 1825, 637, 30, 100)
        DrawText("Выход", black, red, 1875, 1030, 20)
        DrawText("Кликальный клик", black, light_blue, 750, 100, 50)
        DrawText("у вас есть " + str(f'{coins:.2f}') + " монет", black, light_blue, 750, 55, 20)
        DrawText("Обнуление: " + str(nomer), black, light_blue, 750, 27, 20)
        DrawText(str(int(grom * 100)), black, green4, 1730, 485, 35)

        for i in range(0, 900, 60):
            rectangle(gameDisplay, blue, 1150, i, 200, 50)
            rectangle(gameDisplay, red, 145, i, 200, 50)
        t = 0
        ccosty = [ccost1, ccost2, ccost3, ccost4, ccost5, ccost6, ccost7, ccost8, ccost9, ccost10, ccost11, ccost12,
                  ccost13, ccost14, ccost15]
        uups = [uup1, uup2, uup3, uup4, uup5, uup6, uup7, uup8, uup9, uup10, uup11, uup12, uup13, uup14, uup15]
        costy = [cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8, cost9, cost10, cost11, cost12, cost13, cost14,
                 cost15]
        ups = [up1, up2, up3, up4, up5, up6, up7, up8, up9, up10, up11, up12, up13, up14, up15]
        for i in range(27, 927, 60):
            if nomer == 0:
                DrawText(f'{sleva_first_lvl[t]}(+{round(ups[t] * voz, 2)})', black, light_blue, 1045, i, 20)
                DrawText(f'{sprava_first_lvl[t]}(+{round(uups[t] * voz, 2)})', black, light_blue, 410, i, 20)
            elif nomer == 1:
                DrawText(f'{sleva_second_lvl[t]}(+{round(ups[t] * voz, 2)})', black, light_blue, 1045, i, 20)
                DrawText(f'{sprava_second_lvl[t]}(+{round(uups[t] * voz, 2)})', black, light_blue, 410, i, 20)
            else:
                DrawText(f'{sleva_third_lvl[t]}(+{round(ups[t] * voz, 2)})', black, light_blue, 1045, i, 20)
                DrawText(f'{sprava_third_lvl[t]}(+{round(uups[t] * voz, 2)})', black, light_blue, 410, i, 20)
            DrawText("цена:" + str(int(costy[t])), black, light_blue, 1425, i, 18)
            DrawText("цена:" + str(int(ccosty[t])), black, light_blue, 73, i, 18)
            t += 1

        if kart == 2:
            foto = "333.jpg"
            image = load_image(foto)
            image1 = pygame.transform.scale(image, (260, 225))
            screen.blit(image1, (625, 130))
            imagee = load_image('альфабанк.png')
            image2 = load_image('абанк.png')
            bankblue = load_image('abankblue.jpg')
            gest = load_image('жесткийбанк.png')
            imagee1 = pygame.transform.scale(image2, (100, 30))
            imagee11 = pygame.transform.scale(imagee, (30, 100))
            blocksred = pygame.transform.scale(image2, (200, 50))
            blocksblue = pygame.transform.scale(bankblue, (200, 50))
            gestyanka = pygame.transform.scale(gest, (100, 100))
            bluemusic = pygame.transform.scale(bankblue, (100, 100))
            screen.blit(imagee11, (1825, 437))
            screen.blit(imagee11, (1825, 637))
            screen.blit(imagee1, (1560, 670))
            screen.blit(imagee1, (1790, 670))
            screen.blit(imagee1, (1560, 470))
            screen.blit(imagee1, (1790, 470))
            screen.blit(gestyanka, (1820, 200))
            screen.blit(bluemusic, (1500, 200))
            screen.blit(bluemusic, (1660, 200))
            for i in range(0, 900, 60):
                screen.blit(blocksred, (145, i))
                screen.blit(blocksblue, (1150, i))

        if coins >= ulta // 10000:
            rectangle(gameDisplay, green1, 650, 1030, 200, 50)
        if coins >= ulta // 1000:
            rectangle(gameDisplay, green2, 650, 980, 200, 100)
        if coins >= ulta // 100:
            rectangle(gameDisplay, green3, 650, 930, 200, 150)
        if coins >= ulta // 10:
            rectangle(gameDisplay, green4, 650, 880, 200, 200)
        if coins >= ulta:
            rectangle(gameDisplay, green5, 650, 830, 200, 250)
            DrawText("УЛЬТУЙ", red, green5, 750, 970, 45)
        nado -= 1
        nado = max(nado, 0)
        bonus += 1
        if nado >= 1:
            rectangle(gameDisplay, yel, kk, jj, kkk, jjj)
        if bonus == 56:
            bonus = 0
            nado = 37
            kk = random.randint(0, 1720)
            jj = random.randint(0, 980)
            kkk = random.randint(10, 150)
            jjj = random.randint(10, 150)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


start_screen()
main_loop()
final_screen(clicks)
pygame.quit()
quit()
