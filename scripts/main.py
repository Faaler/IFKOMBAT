import pygame
from pygame import mixer
import utils
from cenas import Menu, Selecao, Batalha
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'
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



# uploads
bg_image2 = pygame.image.load('./assets/images/background/background.jpg').convert_alpha()
bg_image3 = pygame.image.load('./assets/images/background/lago.gif').convert_alpha()
bg_image4 = pygame.image.load('./assets/images/background/tree.gif').convert_alpha()
bg_image5 = pygame.image.load('./assets/images/background/hell.gif').convert_alpha()
bg_image6 = pygame.image.load('./assets/images/background/ship.gif').convert_alpha()
bg_image7 = pygame.image.load('./assets/images/background/house.gif').convert_alpha()
bg_image = pygame.image.load('./assets/images/background/voluntarios_fauna.png').convert_alpha()
cenarios = [bg_image2, bg_image3, bg_image4, bg_image5, bg_image6, bg_image7]
fonte = pygame.font.Font('./assets/fonts/turok.ttf', 80) 
scorefonte = pygame.font.Font('./assets/fonts/turok.ttf', 30) 
# musica e sons
mixer.music.load('./assets/audio/music.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1, 0.0, 5000)





# function for draw backgorund
def draw_bg(bg_image):
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
# esc1 = int(input('player 1: 1- guerriero, 2 - mago '))
# esc2 = int(input('player 1: 1- guerriero, 2 - mago, 0 - playerbot'))
# if esc1 == 1:
#     fighter_1 = Guerreiro(1, False,PLAYER1_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
# elif esc1 == 2:
#     fighter_1 = Mago(1, False,PLAYER1_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
# elif esc1 == 3:
#     fighter_1 = Cavaleiro(1, False, PLAYER1_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
# elif esc1 == 4:
#     fighter_1 = 
# elif esc1 == 5:
#     fighter_1 = 
#     fighter_1 = Deusa(1, False,PLAYER1_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, caracters_status[5], screen)
# if esc2 == 1:
#     fighter_2 = Guerreiro(2, True,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
# elif esc2 == 2:
#     fighter_2 = Mago(2, True,PLAYER2_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
# elif esc2 == 3:
#     fighter_2 = Cavaleiro(2, True, PLAYER2_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
# elif esc2 == 4:
#     fighter_2 = Robo(2, True, PLAYER2_INICIAL_POSITION, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], screen)
# elif esc2 == 5:
#     fighter_2 = Paladino(2, True, PLAYER2_INICIAL_POSITION, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], screen)
# elif esc2 == 6:
#     fighter_2 = Deusa(2, True,PLAYER2_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, caracters_status[5], screen)
# else:
#     #fighter_2 = Bot_mago(2, True,PLAYER2_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
# # fighter_1 = Bot_player(1, False,PLAYER1_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
#     fighter_2 = Bot_guerreiro(2, True,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)


# utils.fighter_1 = fighter_1
# utils.fighter_2 = fighter_2

scenes = {
    'menu': Menu(screen),
    # Passamos o estado correto para a classe Selecao saber qual jogador ela representa:
    'selecaov1': Selecao(screen, 'selecaov1'), 
    'selecaov2': Selecao(screen, 'selecaov2'),
    'selecaod': Selecao(screen, 'selecaod'),
    'batalha': Batalha(screen)
}

cenaAtual = 'menu'
cenaAnterior = None # Variável para rastrear a cena no frame anterior

# Game Loop
run = True
while run:
    clock.tick(fps)
    
    
    # -----------------------------------------------
    if cenaAtual != cenaAnterior:
        
        # Se a transição foi para o menu, reseta os estados internos das Seleções
        if cenaAtual == 'menu' and cenaAnterior in ['selecaov1', 'selecaov2', 'selecaod']:
            utils.desafio_level = 0
            
            # SOLUÇÃO CHAVE: RESETA O ESTADO INTERNO DA CLASSE Selecao
            # para que ela retorne o próprio nome na próxima vez que for chamada.
            scenes['selecaov1'].estado = 'selecaov1'
            scenes['selecaov2'].estado = 'selecaov2'
            scenes['selecaod'].estado = 'selecaod'
    # draw background
    draw_bg(bg_image)

    # -----------------------------------------------
    # 2. ATUALIZAÇÃO DA CENA ATIVA
    # Chama o método atualizar da cena ativa e pega o próximo estado
    cenaAtual = scenes[cenaAtual].atualizar() 
    # -----------------------------------------------

    # Se a cena ativa for a Batalha, desenha e move os lutadores
    if cenaAtual == 'batalha':
        if utils.desafio_level == 0:
            draw_bg(cenarios[utils.vs_background])
        else:
            draw_bg(cenarios[utils.desafio_level-1])
        # Seus comandos de jogo da Batalha (movimento, desenho e HUD)

        if utils.intro_count <= 0:
            utils.fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, utils.fighter_2)
            if utils.fighter_2.alive:
                utils.fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, utils.fighter_1)
        else:
            draw_text(str(utils.intro_count),fonte, 'red', SCREEN_WIDTH/2, SCREEN_HEIGHT/8)
            if pygame.time.get_ticks() - utils.last_count_update > 1000:
                utils.intro_count -= 1
                utils.last_count_update = pygame.time.get_ticks()
        if utils.fighter_1.num_vitorias > 1 or utils.fighter_2.num_vitorias > 1:
            scenes['batalha'].over = False
            scenes['batalha'].batalha_done = False
            utils.fighter_1.alive = True
            utils.fighter_1.health = 100
            utils.fighter_1.ult_points = 0
            utils.fighter_2.alive = True
            utils.fighter_2.helath = 100
            utils.fighter_2.ult_points = 0


        utils.fighter_1.draw()
        utils.fighter_2.draw()
        utils.fighter_1.update()
        utils.fighter_2.update()
        
        # Desenho da HUD na Batalha
        draw_health_bar(utils.fighter_1.health, 40, 20)
        draw_health_bar(utils.fighter_2.health, 980, 20)
        draw_text('P1: '+ str(utils.fighter_1.ult_points), scorefonte, 'blue', 200-160,60)
        draw_text(str(utils.fighter_1.num_vitorias), scorefonte, 'blue', 680,20)
        draw_text(str(utils.fighter_2.num_vitorias), scorefonte, 'red', 715,20)
        draw_text('-', scorefonte, 'white', 700,18)
        draw_text('P2: '+ str(utils.fighter_2.ult_points), scorefonte, 'red', 1200-220,60)
        
        if utils.existis_goddess:
            utils.existis_goddess.update()
            pass
        # Lógica de vitória/derrota da Batalha deve ser movida para cá ou para o Batalha.update()
        # Mas por enquanto, vamos focar no reset:
        if scenes[cenaAtual].over:
            scenes[cenaAtual].desenhar_texto()
            if scenes[cenaAtual].batalha_done:
                scenes[cenaAtual].resetar_batalha()

    if cenaAtual == 'selecaod' and utils.fighter_1 and utils.fighter_2:
        scenes['batalha'].over = False
        scenes['batalha'].batalha_done = False
        scenes['batalha'].estado = 'batalha'
        scenes['selecaod'].estado = 'selecaod'
        utils.fighter_1.alive = True
        utils.fighter_1.health = 100
        utils.fighter_1.ult_points = 0
        utils.fighter_1.num_vitorias = 0
        utils.fighter_2.alive = True
        utils.fighter_2.helath = 100
        utils.fighter_2.ult_points = 0
        utils.fighter_2.num_vitorias = 0
        for inimigo in utils.inimigos:
            if None not in utils.inimigos:
                inimigo.ult_points = 0
                inimigo.health = 100
                inimigo.alive = True
                inimigo.num_vitorias = 0
    if cenaAtual == 'selecaov2' and utils.fighter_1 and utils.fighter_2:
        scenes['batalha'].over = False
        scenes['batalha'].batalha_done = False
        scenes['batalha'].estado = 'batalha'
        scenes['selecaod'].estado = 'selecaod'
        utils.fighter_1.alive = True
        utils.fighter_1.health = 100
        utils.fighter_1.ult_points = 0
        utils.fighter_1.num_vitorias = 0
        utils.fighter_2.alive = True
        utils.fighter_2.helath = 100
        utils.fighter_2.ult_points = 0
        utils.fighter_2.num_vitorias = 0
        utils.desafio_level = 0
        for inimigo in utils.inimigos:
            if None not in utils.inimigos:
                inimigo.ult_points = 0
                inimigo.health = 100
                inimigo.alive = True
                inimigo.num_vitorias = 0
    if cenaAtual != cenaAnterior:
            
            # Ao SAIR da seleção e IR para o menu, você deve garantir que o estado interno
            # das instâncias 'selecaov1', 'selecaov2' e 'selecaod' volte ao seu valor padrão.
            
            if cenaAtual == 'menu' and cenaAnterior in ['selecaov1', 'selecaov2', 'selecaod']:
                # Reseta o nível do desafio ao voltar ao menu
                utils.desafio_level = 0
                
                # Garante que a cena de seleção não tente mais retornar 'menu' na próxima vez que for chamada
                # (Se você estivesse usando a instância Selecao em vez de recriá-la, precisaria disso)
                # scenes['selecaov1'].estado = 'selecaov1'
                # scenes['selecaov2'].estado = 'selecaov2'
                # scenes['selecaod'].estado = 'selecaod'

    cenaAnterior = cenaAtual # Atuali



    # event hendler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if utils.sair:
        run = False

    # update display
    pygame.display.update()

# saindo do pygame
pygame.quit()