import pygame
from pygame import mixer
from fighter import Fighter
from mago import Mago
from guerreiro import Guerreiro

pygame.init()
mixer.init()

# criando tela do jogo
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 840

# set framerate
clock = pygame.time.Clock()
fps = 60


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('IFKOMBAT')

# define game varialbles
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0,0]
round_over = False
round_over_cooldown = 2000


# define fighter variables
PLAYER1_SIZE = 162
PLAYER1_SCALE = 6.5
PLAYER1_OFFSET = [72, 56]
PLAYER1_DATA = [PLAYER1_SIZE, PLAYER1_SCALE, PLAYER1_OFFSET]
PLAYER2_SIZE = 250
PLAYER2_SCALE = 3.8
PLAYER2_OFFSET = [116, 114]
PLAYER2_DATA = [PLAYER2_SIZE, PLAYER2_SCALE, PLAYER2_OFFSET]
PLAYER1_INICIAL_POSITION = [200, 270]
PLAYER2_INICIAL_POSITION = [700, 360]

# defininado informação dos personagens
caracters_status = [
    {
     'nome': 'Guerreiro',
     'dano1' : 16,
     'dano2' : 22,
     'defesa': 6,
     'speed': 8,
     'largura': 120,
     'altura': 290,
     'posicao_inicial': [200, 270],
     'attack_animation_cooldown' : 90,
     'attack_box_size_1': [2.2,1.1],
     'attack_box_size_2': [2,1.09],
     'ult_min': 3,
     'attack_coldwon1': 15,
     'attack_coldwon2': 55,
     'knock_back': 3

    },
     {
     'nome': 'Mago',
     'dano1' : 10,
     'dano2' : 14,
     'defesa': 2,
     'speed': 12,
     'largura': 100,
     'altura': 200 ,
     'posicao_inicial': [700, 360],
     'attack_animation_cooldown' : 50,
     'attack_box_size_1': [3.8, 2],
     'attack_box_size_2': [4, 2],
     'dash_coldown': 500,
     'ult_min': 5,
     'attack_coldwon1': 10,
     'attack_coldwon2': 45,
     'knock_back': 1
     }
]


# uploads
bg_image = pygame.image.load('./assets/images/background/background.jpg').convert_alpha()
player1_sheet = pygame.image.load('./assets/images/warrior/Sprites/warrior.png').convert_alpha()
player2_sheet = pygame.image.load('./assets/images/wizard/Sprites/wizard.png').convert_alpha()
fonte = pygame.font.Font('./assets/fonts/turok.ttf', 80) 
scorefonte = pygame.font.Font('./assets/fonts/turok.ttf', 30) 
# musica e sons
mixer.music.load('./assets/audio/music.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1, 0.0, 5000)
sword_fx = mixer.Sound('./assets/audio/sword.wav')
sword_fx.set_volume(0.3)
staff_fx = mixer.Sound('./assets/audio/magic.wav')
sword_fx.set_volume(0.3)

# define number of steps in animations
WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS = [8,8,1,8,8,3,7]



# function for draw backgorund
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))
# function for draw health bar
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, 'white', (x - 2,y - 2, 405, 35))
    pygame.draw.rect(screen, 'red', (x,y, 400, 30))
    pygame.draw.rect(screen, 'green', (x,y, 400 * ratio, 30))

# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#mago = Mago(1, True,PLAYER1_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1])
#guerreiro = Fighter(2, False,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0])

# create players instances
esc1 = int(input('player 1: 1- guerriero, 2 - mago '))
esc2 = int(input('player 1: 1- guerriero, 2 - mago '))
if esc1 == 1:
    fighter_1 = Guerreiro(1, False,PLAYER1_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
else:
    fighter_1 = Mago(1, False,PLAYER1_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
if esc2 == 1:
    fighter_2 = Guerreiro(2, True,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
else:
    fighter_2 = Mago(2, True,PLAYER2_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)




# Game Loop
run = True
while run:
    clock.tick(fps)

    #draw background
    draw_bg()

    # show player status
    draw_health_bar(fighter_1.health, fighter_1.inicial_position[0]-160, 20)
    draw_health_bar(fighter_2.health, fighter_2.inicial_position[0]-160, 20)
    draw_text('P1: '+ str(fighter_1.ult_points), scorefonte, 'red', fighter_1.inicial_position[0]-160,60)
    draw_text('P2: '+ str(fighter_2.ult_points), scorefonte, 'red', fighter_2.inicial_position[0]-160,60)
    

    if intro_count <= 0 and round_over == False:
    # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)
    elif intro_count > 0 and round_over == False:
        #update countdown
        draw_text(str(intro_count),fonte, 'red', SCREEN_WIDTH/2, SCREEN_HEIGHT/8)
        if pygame.time.get_ticks() - last_count_update > 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

   


    

    # draw fighters
    fighter_1.draw()
    fighter_2.draw()

    # update figthers
    fighter_1.update()
    fighter_2.update()

    # event hendler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # check for victory
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        draw_text('Victory',fonte, 'red', SCREEN_WIDTH/2.5, SCREEN_HEIGHT/8)
        if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
            round_over = False
            #fighter_1 = Fighter(1, 200, 360,False, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, 10, sword_fx)
            #fighter_2 = Fighter(2, 700, 360,True, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, 30, staff_fx)
            intro_count = 3

    
    # update display
    pygame.display.update()

# saindo do pygame
pygame.quit()