from random import randint
import pgzero
import pgzrun

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill((135, 206, 235))
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="red", topright=(WIDTH-10, 10))
    if game_over:
        screen.fill((211, 211, 211))
        screen.draw.text("Final Score: " + str(score), topleft=(10,10), fontsize=60)
def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT-  20)

def time_up():
    global game_over
    game_over = True
    clock.schedule(quit,5)

def update():
    global score
    if game_over:
        return
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)
        
    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 20.0)
place_coin()










pgzrun.go()

