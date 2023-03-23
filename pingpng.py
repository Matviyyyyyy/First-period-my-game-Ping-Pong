from pygame import *
window = display.set_mode((700, 500))
clock = time.Clock()

window = display.set_mode((700, 500))
clock = time.Clock()
def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    text = font.Font(None, 70).render(message, True, (255, 255, 255))
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                quit()
        window.blit(text, (250, 250))
        display.update()
        clock.tick(60)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))


class OneHero(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
            print(self.rect.y)
        if keys[K_s]:
            self.rect.y += self.speed

class TwoHero(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
    def update(self):
        keys = key.get_pressed()
        if keys[K_o]:
            self.rect.y -= self.speed
        if keys[K_l]:
            self.rect.y += self.speed

class Grenade(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
    def update(self):
        self.rect.x +=self.speed
     
    
        



one_hero = OneHero("D:\\Projects\\maze\\Pubg Mascot Logo (11).png", 50, 40, 5, 70, 150)
two_hero = TwoHero("D:\\Projects\\maze\\PUBG-Download-Free-PNG.png", 650, 40, 5, 70, 150)
background = transform.scale(image.load("D:\\Projects\\maze\\ping-pong\\1920x1080-light-green-solid-color-background.jpg"), (700,500))
grenade = Grenade("D:\\Projects\\maze\\Icon_weapon_Grenade (1).png", 200, 300, 5, 40, 40)
font.init()
font1 = font.Font(None, 20)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        #обробка подій
    if grenade.rect.colliderect(one_hero.rect):
        grenade.speed = grenade.speed * (-1)
    if grenade.rect.colliderect(two_hero.rect):
       grenade.speed = grenade.speed * (-1)
            

    # оновлення обєктів
    one_hero.update()
    two_hero.update()
    grenade.update()
    # відмалювqати
    window.blit(background, (0, 0))
    one_hero.draw(window)
    two_hero.draw(window)
    grenade.draw(window)
    display.update()
    clock.tick(60)

