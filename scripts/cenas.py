import pygame
import random
from pygame import mixer
from fighter import Fighter
from mago import Mago
from guerreiro import Guerreiro
from cavaleiro import Cavaleiro
from robo import Robo
from paladino import Paladino
from deusa import Deusa
from bots import Bot_player, Bot_mago, Bot_guerreiro, Bot_cavaleiro, Bot_robo, Bot_paladino, Bot_deusa
import utils
from interfaces import Texto, Botao


# define fighter variables
PLAYER1_SIZE = 162
PLAYER1_SCALE = 6.5
PLAYER1_OFFSET = [72, 56]
PLAYER1_DATA = [PLAYER1_SIZE, PLAYER1_SCALE, PLAYER1_OFFSET]
PLAYER2_SIZE = 250
PLAYER2_SCALE = 3.8
PLAYER2_OFFSET = [116, 113]
PLAYER2_DATA = [PLAYER2_SIZE, PLAYER2_SCALE, PLAYER2_OFFSET]
PLAYER3_SIZE = 135
PLAYER3_SCALE = 6
PLAYER3_OFFSET = [58, 48]
PLAYER3_DATA = [PLAYER3_SIZE, PLAYER3_SCALE, PLAYER3_OFFSET]
PLAYER4_SIZE = 96
PLAYER4_SCALE = 5.3
PLAYER4_OFFSET = [36, 24]
PLAYER4_DATA = [PLAYER4_SIZE, PLAYER4_SCALE, PLAYER4_OFFSET]
PLAYER5_SIZE = 128
PLAYER5_SCALE = 3.5
PLAYER5_OFFSET = [50, 36]
PLAYER5_DATA = [PLAYER5_SIZE, PLAYER5_SCALE, PLAYER5_OFFSET]
PLAYER6_SIZE = 128
PLAYER6_SCALE = 3.5
PLAYER6_OFFSET = [49, 61]
PLAYER6_DATA = [PLAYER6_SIZE, PLAYER6_SCALE, PLAYER6_OFFSET]
PLAYER1_INICIAL_POSITION = [100, 6000]
PLAYER2_INICIAL_POSITION = [1200, 6000]


# defininado informação dos personagens
caracters_status = [
    {
     'nome': 'Guerreiro',
     'dano1' : 10,
     'dano2' : 17,
     'defesa': 3,
     'speed': 8,
     'jump_high': 30,
     'largura': 120,
     'altura': 290,
     'attack_animation_cooldown_1' : 55,
     'attack_animation_cooldown_2' : 90,
     'attack_box_size_1': [2.2,1.1],
     'attack_box_size_2': [2,1.09],
     'frame_att1': 4,
     'frame_att2': 4,
     'ult_min': 6,
     'attack_coldwon1': 10,
     'attack_coldwon2': 50,
     'knock_back': 3.2

    }, 
     {
     'nome': 'Mago',
     'dano1' : 7,
     'dano2' : 12,
     'defesa': 1,
     'speed': 12,
     'jump_high': 30,
     'largura': 100,
     'altura': 200,
     'attack_animation_cooldown_1' : 50,
     'attack_animation_cooldown_2' : 90,
     'attack_box_size_1': [3.4, 2],
     'attack_box_size_2': [3.5, 2],
     'frame_att1': 4,
     'frame_att2': 4,
     'dash_coldown': 600,
     'ult_min': 6,
     'attack_coldwon1': 15,
     'attack_coldwon2': 45,
     'knock_back': 1
     },
    {
    'nome': 'Cavaleiro',
    'dano1' : 6,
    'dano2' : 9,
    'defesa': 2,
    'speed': 9,
    'jump_high': 35,
    'largura': 130,
    'altura': 220,
    'attack_animation_cooldown_1' : 50,
    'attack_animation_cooldown_2' : 55,
    'attack_box_size_1': [2.8, 2],
    'attack_box_size_2': [2.5, 0.9],
    'frame_att1': 3,
    'frame_att2': 2,
    'ult_min': 8,
    'attack_coldwon1': 35,
    'attack_coldwon2': 0,
    'knock_back': 4.2,
    'yknock_back': 12
     },
     {
    'nome': 'Robo',
    'dano1' : 9,
    'dano2' : 18,
    'defesa': 4,
    'speed': 6,
    'jump_high': 26,
    'largura': 130,
    'altura': 240,
    'attack_animation_cooldown_1' : 50,
    'attack_animation_cooldown_2' : 45,
    'attack_box_size_1': [1, 1],
    'attack_box_size_2': [1.4, 0.7],
    'frame_att1': 3,
    'frame_att2': 4,
    'ult_min': 8,
    'attack_coldwon1': 15,
    'attack_coldwon2': 85,
    'knock_back': 2
     },
     {
     'nome': 'Paladino',
     'dano1' : 8.5,
     'dano2' : 13,
     'defesa': 1,
     'speed': 8,
     'jump_high': 30,
     'largura': 100,
     'altura': 200 ,
     'attack_animation_cooldown_1' : 35,
     'attack_animation_cooldown_2' : 90,
     'attack_box_size_1': [1.8, 1],
     'attack_box_size_2': [1.7, 0.7],
     'frame_att1': 8,
     'frame_att2': 2,
     'ult_min': 6,
     'attack_coldwon1': 7,
     'attack_coldwon2': 45,
     'knock_back': 2.5
     },
     {
     'nome': 'Deusa',
     'dano1' : 8,
     'dano2' : 12,
     'defesa': 2,
     'speed': 6.5,
     'jump_high': 30,
     'largura': 100,
     'altura': 230,
     'attack_animation_cooldown_1' : 45,
     'attack_animation_cooldown_2' : 35,
     'attack_box_size_1': [1.3, 0.8],
     'attack_box_size_2': [1.7, 1],
     'frame_att1': 7,
     'frame_att2': 10,
     'ult_min': 10,
     'attack_coldwon1': 8,
     'attack_coldwon2': 35,
     'knock_back': 1
     },
]

goddess_boss =  {
     'nome' : 'Deusa',
     'dano1' : 10,
     'dano2' : 15,
     'defesa': 2.5,
     'speed': 6.5,
     'jump_high': 30,
     'largura': 100,
     'altura': 230,
     'attack_animation_cooldown_1' : 45,
     'attack_animation_cooldown_2' : 35,
     'attack_box_size_1': [1.3, 0.8],
     'attack_box_size_2': [1.7, 1],
     'frame_att1': 7,
     'frame_att2': 10,
     'ult_min': 80,
     'attack_coldwon1': 8,
     'attack_coldwon2': 35,
     'knock_back': 1
     }


player1_sheet = pygame.image.load('./assets/images/warrior/Sprites/warrior.png').convert_alpha()
player2_sheet = pygame.image.load('./assets/images/wizard/Sprites/wizard.png').convert_alpha()
player3_sheet = pygame.image.load('./assets/images/knight/Sprites/knight.png').convert_alpha()
player4_sheet = pygame.image.load('./assets/images/robot/Sprites/Roobot.png').convert_alpha()
player5_sheet = pygame.image.load('./assets/images/paladine/Sprites/paladino.png').convert_alpha()
player6_sheet = pygame.image.load('./assets/images/goddess/Sprites/goddess.png').convert_alpha()

sword_fx = mixer.Sound('./assets/audio/sword.wav')
sword_fx.set_volume(0.3)
staff_fx = mixer.Sound('./assets/audio/magic.wav')
staff_fx.set_volume(0.3)

fonte = pygame.font.Font('./assets/fonts/turok.ttf', 80) 
scorefonte = pygame.font.Font('./assets/fonts/turok.ttf', 30) 

# define number of steps in animations
WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS = [8,8,1,8,8,3,7]
KNIGHT_ANIMATION_STEPS = [10,6,2,5,4,3,9]
ROBOT_ANIMATION_STEPS = [4, 6, 1, 6, 6, 2, 6, 6]
PALADINE_ANIMATION_STEPS = [7, 7, 1, 10, 4, 3, 5]
GODDESS_ANIMATION_STEPS = [8, 8, 1, 7, 10, 2, 10]




class Menu():
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, 'IFKOMBAT', 550, 100, 'red', 50, fonte)
        self.estado = 'menu'
        self.botao_versus = Botao(tela, "Versus", 450,600,20,(200,0,0),(255,255,255))
        self.botao_desafio = Botao(tela, "Desafio", 650,600,20,(200,0,0),(255,255,255))
        self.botao_sair = Botao(tela, "Sair", 850,600,20,(200,0,0),(255,255,255))


    def atualizar(self):
        self.titulo.desenhar()
        self.botao_versus.desenhar()
        self.botao_desafio.desenhar()
        self.botao_sair.desenhar()
        proximo_estado = self.estado
        if self.botao_desafio.get_click():
            utils.desafio_rota = 1
            utils.desafio_level = 1
            proximo_estado = 'selecaod' # <--- Atualiza a variável local
        
        if self.botao_versus.get_click():
            proximo_estado = 'selecaov1' # <--- Atualiza a variável local

        if self.botao_sair.get_click():
            utils.sair = True        

        return proximo_estado

class Selecao:
    def __init__(self, tela, sel_atual):
        self.tela = tela
        self.nome_inicial = sel_atual # Guarde o nome inicial da cena
        self.titulo = Texto(tela, 'Escolha seu lutador', 300, 50, 'red', 20, fonte)
        self.jogador1 = Texto(tela, 'Jogador 1', 650, 150, 'blue', 50, scorefonte)
        self.jogador2 = Texto(tela, 'Jogador 2', 650, 150, 'red', 50, scorefonte)
        self.botao_f1 = Botao(tela, "Guerreiro", 100,200,30,(0,0,255),(255,255,255))
        self.botao_f2 = Botao(tela, "Mago", 100,250,30,(0,0,255),(255,255,255))
        self.botao_f3 = Botao(tela, "Cavaleiro", 100,300,30,(0,0,255),(255,255,255))
        self.botao_f4 = Botao(tela, "Robo", 100,350,30,(0,0,255),(255,255,255))
        self.botao_f5 = Botao(tela, "Paladino", 100,400,30,(0,0,255),(255,255,255))
        self.botao_f6 = Botao(tela, "Deusa", 100,450,30,(0,0,255),(255,255,255))
        self.botao2_f1 = Botao(tela, "Guerreiro", 950,200,30,(200,0,0),(255,255,255))
        self.botao2_f2 = Botao(tela, "Mago", 950,250,30,(200,0,0),(255,255,255))
        self.botao2_f3 = Botao(tela, "Cavaleiro", 950,300,30,(200,0,0),(255,255,255))
        self.botao2_f4 = Botao(tela, "Robo", 950,350,30,(200,0,0),(255,255,255))
        self.botao2_f5 = Botao(tela, "Paladino", 950,400,30,(200,0,0),(255,255,255))
        self.botao2_f6 = Botao(tela, "Deusa", 950,450,30,(200,0,0),(255,255,255))
        self.botao_menu = Botao(tela, 'Menu', 1200, 50, 50, (200,0,0), (0,255,0))
        
    def atualizar(self):
        proximo_estado = self.nome_inicial
        screen = self.tela
        self.titulo.desenhar()
        self.botao_menu.desenhar()
        if self.botao_menu.get_click():
            proximo_estado = 'menu'

        if self.nome_inicial == 'selecaov1':
            self.jogador1.desenhar()
            self.botao_f1.desenhar()
            self.botao_f2.desenhar()
            self.botao_f3.desenhar()
            self.botao_f4.desenhar()
            self.botao_f5.desenhar()
            self.botao_f6.desenhar()
            if self.botao_f1.get_click():
                utils.fighter_1 = Guerreiro(1, False,PLAYER1_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
                proximo_estado = 'selecaov2'
            if self.botao_f2.get_click():
                utils.fighter_1 = Mago(1, False,PLAYER1_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
                proximo_estado = 'selecaov2'
            if self.botao_f3.get_click():
                utils.fighter_1 = Cavaleiro(1, False, PLAYER1_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
                proximo_estado = 'selecaov2'
            if self.botao_f4.get_click():
                utils.fighter_1 = Robo(1, False, PLAYER1_INICIAL_POSITION, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], screen)
                proximo_estado = 'selecaov2'
            if self.botao_f5.get_click():
                utils.fighter_1 = Paladino(1, False, PLAYER1_INICIAL_POSITION, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], screen)
                proximo_estado = 'selecaov2'
            if self.botao_f6.get_click():
                utils.fighter_1 = Deusa(1, False,PLAYER1_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, caracters_status[5], screen)
                proximo_estado = 'selecaov2'
            if self.botao_menu.get_click():
                proximo_estado = 'menu'
            
        elif self.nome_inicial == 'selecaov2':
            utils.vs_background = random.randint(0,5)
            self.jogador2.desenhar()
            self.botao2_f1.desenhar()
            self.botao2_f2.desenhar()
            self.botao2_f3.desenhar()
            self.botao2_f4.desenhar()
            self.botao2_f5.desenhar()
            self.botao2_f6.desenhar()
            if self.botao2_f1.get_click():
                utils.fighter_2 = Guerreiro(2, True,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
                proximo_estado = 'batalha'
            if self.botao2_f2.get_click():
                utils.fighter_2 = Mago(2, True,PLAYER2_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
                proximo_estado = 'batalha'
            if self.botao2_f3.get_click():
                utils.fighter_2 = Cavaleiro(2, True, PLAYER2_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
                proximo_estado = 'batalha'
            if self.botao2_f4.get_click():
                utils.fighter_2 = Robo(2, True, PLAYER2_INICIAL_POSITION, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], screen)
                proximo_estado = 'batalha'
            if self.botao2_f5.get_click():
                utils.fighter_2 = Paladino(2, True, PLAYER2_INICIAL_POSITION, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], screen)
                proximo_estado = 'batalha'
            if self.botao2_f6.get_click():
                utils.fighter_2 = Deusa(2, True,PLAYER2_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, caracters_status[5], screen)
                proximo_estado = 'batalha'
        elif self.nome_inicial == 'selecaod':
            self.botao_f1.desenhar()
            self.botao_f2.desenhar()
            self.botao_f3.desenhar()
            self.botao_f4.desenhar()
            self.botao_f5.desenhar()
            self.botao_f6.desenhar()
            if self.botao_f1.get_click():
                utils.fighter_1 = Guerreiro(1, False,PLAYER1_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
                proximo_estado = 'batalha'
            if self.botao_f2.get_click():
                utils.fighter_1 = Mago(1, False,PLAYER1_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
                proximo_estado = 'batalha'
            if self.botao_f3.get_click():
                utils.fighter_1 = Cavaleiro(1, False, PLAYER1_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
                proximo_estado = 'batalha'
            if self.botao_f4.get_click():
                utils.fighter_1 = Robo(1, False, PLAYER1_INICIAL_POSITION, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], screen)
                proximo_estado = 'batalha'
            if self.botao_f5.get_click():
                utils.fighter_1 = Paladino(1, False, PLAYER1_INICIAL_POSITION, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], screen)
                proximo_estado = 'batalha'
            if self.botao_f6.get_click():
                utils.fighter_1 = Deusa(1, False,PLAYER1_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, caracters_status[5], screen)
                proximo_estado = 'batalha'
            
            
            if utils.desafio_rota == 1:
                utils.inimigo1 = Bot_guerreiro(2, True,PLAYER2_INICIAL_POSITION, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], screen)
                utils.inimigo2 = Bot_mago(2, True,PLAYER2_INICIAL_POSITION, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], screen)
                utils.inimigo3 = Bot_cavaleiro(2, True, PLAYER2_INICIAL_POSITION, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], screen)
                utils.inimigo4 = Bot_robo(2, True, PLAYER2_INICIAL_POSITION, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], screen)
                utils.inimigo5 = Bot_paladino(2, True, PLAYER2_INICIAL_POSITION, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], screen)
                utils.inimigo6 = Bot_deusa(2, True,PLAYER2_INICIAL_POSITION, PLAYER6_DATA, player6_sheet, GODDESS_ANIMATION_STEPS, staff_fx, goddess_boss, screen)
       

            utils.inimigos = [
                    utils.inimigo1,
                    utils.inimigo2,
                    utils.inimigo3,
                    utils.inimigo4,
                    utils.inimigo5,
                    utils.inimigo6
                ]
            utils.fighter_2 = utils.inimigos[0]
        return proximo_estado
    

class Batalha:
    def __init__(self, tela):
        self.tela = tela
        self.estado = 'batalha'
        self.over = False
        self.tempo_morte = 0
        self.duracao_contador = 5000
        self.batalha_done = False
        self.texto_vitoria = Texto(tela, 'Vitoria', 550, 50, 'blue', 20, fonte)
        self.texto_vitoria2 = Texto(tela, 'Vitoria', 550, 50, 'red', 20, fonte)
        self.texto_derrota = Texto(tela, 'Derrota', 550, 50, 'red', 20, fonte)

    def atualizar(self):
        
        if utils.desafio_level == 0:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()
        elif utils.desafio_level == 1:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()

        elif utils.desafio_level == 2:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()

        elif utils.desafio_level == 3:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()

        elif utils.desafio_level == 4:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()

        elif utils.desafio_level == 5:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()

        elif utils.desafio_level == 6:
            if not utils.fighter_1.alive or not utils.fighter_2.alive:
                if not self.over:
                    self.tempo_morte = pygame.time.get_ticks()
                    self.over = True
                else:
                    if pygame.time.get_ticks() - self.tempo_morte > self.duracao_contador:
                        self.batalha_done = True
                        if not utils.fighter_1.alive:
                            utils.fighter_2.num_vitorias += 1
                        elif not utils.fighter_2.alive:
                            utils.fighter_1.num_vitorias += 1
                        self.resetar_batalha()
                        if utils.fighter_1.num_vitorias > 1 or utils.fighter_2.num_vitorias > 1:
                            self.estado = 'menu'



        return self.estado
    

    def draw_health_bar(self, health, x, y):
        ratio = health / 100
        pygame.draw.rect(self.tela, 'white', (x - 2,y - 2, 405, 35))
        pygame.draw.rect(self.tela, 'red', (x,y, 400, 30))
        pygame.draw.rect(self.tela, 'green', (x,y, 400 * ratio, 30))

    
        
    def resetar_batalha(self):
        self.estado = 'batalha'
        self.batalha_done = False


        if utils.desafio_level < 1:
            if utils.fighter_1.num_vitorias > 1 or utils.fighter_2.num_vitorias > 1:
                utils.fighter_1.num_vitorias = 0
                utils.fighter_2.num_vitorias = 0
                self.batalha_done = True
                self.estado = 'menu'
        else:
            if utils.fighter_1.num_vitorias > 1:
                utils.fighter_1.num_vitorias = 0
                utils.fighter_2.num_vitorias = 0
                if utils.desafio_level < 6:
                    utils.desafio_level += 1
                else:
                    utils.fighter_1.num_vitorias = 0
                    utils.fighter_2.num_vitorias = 0
                    self.batalha_done = True
                    self.estado = 'menu'
            elif utils.fighter_2.num_vitorias > 1:
                utils.fighter_1.num_vitorias = 0
                utils.fighter_2.num_vitorias = 0
                self.batalha_done = True
                self.estado = 'menu'
            print(utils.desafio_level)
            utils.fighter_2 = utils.inimigos[utils.desafio_level - 1]

        self.over = False
        self.tempo_morte = 0
        utils.fighter_1.alive = True
        utils.fighter_1.health = 100
        utils.fighter_2.alive = True
        utils.fighter_2.health = 100
        utils.fighter_1.rect.x = PLAYER1_INICIAL_POSITION[0]          
        utils.fighter_1.rect.y = PLAYER1_INICIAL_POSITION[1] 
        utils.fighter_2.rect.x = PLAYER2_INICIAL_POSITION[0]         
        utils.fighter_2.rect.y = PLAYER2_INICIAL_POSITION[1] 
        utils.fighter_1.ult_points = 0
        utils.fighter_2.ult_points = 0   
        utils.fighter_1.ulted = False
        utils.fighter_2.ulted = False
        utils.fighter_1.ult_lastcall = 0
        utils.fighter_2.ult_lastcall = 0
        utils.intro_count = 3
        utils.last_count_update = pygame.time.get_ticks()   
        utils.fighter_1.target = utils.fighter_2
        utils.fighter_2.target = utils.fighter_1
        




    def desenhar_texto(self):
        if utils.desafio_level == 0:
            if utils.fighter_1.alive:
                self.texto_vitoria.desenhar()
            else:
                self.texto_vitoria2.desenhar()
        else:
            if utils.fighter_1.alive:
                self.texto_vitoria.desenhar()
            else:
                self.texto_derrota.desenhar()