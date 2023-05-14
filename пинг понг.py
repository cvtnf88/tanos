from pygame import *

win_wight = 700
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption('пинг понг')
background = transform.scale(image.load('фон пинг понг.png'),(win_wight,win_height))
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, w, h, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed
        self.speed_y = speed
        self.rect = Rect(self.rect.x, self.rect.y, 61, 100)
        self.score = 0
    def reset(self):
        window.blit(self.image, (self.rect.x-25, self.rect.y))

x = 500
y = 380


class Player1(GameSprite):
    def update(self): 
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed  

class Player2(GameSprite):
    def update(self): 
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed            

class Ball(GameSprite):
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > 650 or self.rect.x < 0:
            self.speed_x *= -1
            if self.rect.x > 650:
                player1.score +=1
            else:
                player2.score += 1
        if self.rect.y > 450 or self.rect.y < 0:
            self.speed_y *= -1
       
        


player1 = Player1('игрок1.png', 0, 400, 100,100, 2) 
player2 = Player2('игрок2.png', 600, 0, 90,100, 2)
ball = Ball('фаербол.png',300, 300, 50,50,3)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                finish = False
                player1.score = 0
                player2.score = 0
                ball.rect.x = 300
                ball.rect.y = 300

    if not finish:
        window.blit(background,(0, 0))
    
    
        score_text = font.Font(None, 80).render(f'{player1.score} : {player2.score}', True, (255, 255, 255))
        window.blit(score_text, (300, 20))
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball.speed_x *= -1
        ball.update()
        player2.update()
        player2.reset()
        player1.update()
        player1.reset()
            
        if player1.score > 1:
            finish = True


        if player2.score > 1:
            finish = True    
        display.update()


