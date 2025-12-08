from fighter import Fighter
from guerreiro import Guerreiro
from mago import Mago
from cavaleiro import Cavaleiro
from robo import Robo
from paladino import Paladino
from deusa import Deusa
import utils
import pygame
from pygame import mixer
import random


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 840

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

WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS = [8,8,1,8,8,3,7]
KNIGHT_ANIMATION_STEPS = [10,6,2,5,4,3,9]
ROBOT_ANIMATION_STEPS = [4, 6, 1, 6, 6, 2, 6, 6]
PALADINE_ANIMATION_STEPS = [7, 7, 1, 10, 4, 3, 5]


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
    'attack_coldwon2': 70,
    'knock_back': 2
     },
     {
     'nome': 'Paladino',
     'dano1' : 8,
     'dano2' : 12,
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
     'dano1' : 9,
     'dano2' : 12,
     'defesa': 2,
     'speed': 6.5,
     'jump_high': 30,
     'largura': 100,
     'altura': 230,
     'attack_animation_cooldown_1' : 50,
     'attack_animation_cooldown_2' : 40,
     'attack_box_size_1': [1.3, 0.8],
     'attack_box_size_2': [1.7, 1],
     'frame_att1': 7,
     'frame_att2': 10,
     'ult_min': 10,
     'attack_coldwon1': 7,
     'attack_coldwon2': 35,
     'knock_back': 1
     },
]


# uploads
bg_image = pygame.image.load('./assets/images/background/background.jpg').convert_alpha()
player1_sheet = pygame.image.load('./assets/images/warrior/Sprites/warrior.png').convert_alpha()
player2_sheet = pygame.image.load('./assets/images/wizard/Sprites/wizard.png').convert_alpha()
player3_sheet = pygame.image.load('./assets/images/knight/Sprites/knight.png').convert_alpha()
player4_sheet = pygame.image.load('./assets/images/robot/Sprites/Roobot.png').convert_alpha()
player5_sheet = pygame.image.load('./assets/images/paladine/Sprites/paladino.png').convert_alpha()





sword_fx = mixer.Sound('./assets/audio/sword.wav')
sword_fx.set_volume(0.3)
staff_fx = mixer.Sound('./assets/audio/magic.wav')
staff_fx.set_volume(0.3)








class Bot_player(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
       super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)

        
        
  

    # movimento do personagem

    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 120
        min_dist = 70
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False # Prioriza animação de ataque/idle
            
            if self.attack_coldown == 0 and not self.attcking:
                if random.randint(0, 10) < 6:
                    self.attack1()
                else:
                    self.attack2()


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 30:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       

            dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 80) == 1:
            self.vel_y = -self.jump_high
            self.jump = True
                            
                

        # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
            else:
                self.dashx += 30
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True 

        #update player position with dash
        self.rect.x += self.dashx
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy



class Bot_mago(Mago):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)

    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 120
        min_dist = 70
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False # Prioriza animação de ataque/idle
            
            if self.attack_coldown == 0 and not self.attcking and not self.repressed:
                esc = random.randint(0, 10)
                if esc < 6:
                    self.attack1()
                elif esc > 6 and esc < 8:
                    self.hab2()
                else:
                    self.attack2()


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 30:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       

            dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 70) == 1:
            self.vel_y = -self.jump_high
            self.jump = True

        # dash aleatório
        if self.dash and random.randint(0, 70) == 1 and not self.repressed:
            self.dashx = 60 if not self.flip else -60
            self.last_dash = pygame.time.get_ticks()
            self.dash = False
                            
        if self.ult_points >= self.ult_min and random.randint(0, 60) == 1 and not self.jump and not self.repressed:
            self.ult()
                

        # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
            else:
                self.dashx += 30
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True 

        #update player position with dash
        self.rect.x += self.dashx
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy
    
class Bot_guerreiro(Guerreiro):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)

    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 120
        min_dist = 70
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False # Prioriza animação de ataque/idle
            
            if self.attack_coldown == 0 and not self.attcking:
                if random.randint(0, 10) < 6:
                    self.attack1()
                else:
                    self.attack2()


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 30:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       

            dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 80) == 1:
            self.vel_y = -self.jump_high
            self.jump = True
                            
        if random.randint(0, 90) == 1 and self.jump == False and not self.repressed:
            self.hab1()
            self.hab2()

        if self.ult_points >= self.ult_min and random.randint(0, 60) == 1 and not self.jump and not self.repressed:
            self.ult()
                

        # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
            else:
                self.dashx += 30
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True 

        #update player position with dash
        self.rect.x += self.dashx
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy

    
class Bot_cavaleiro(Cavaleiro):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)



    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 130
        min_dist = 80
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False 
            
            if self.attack_coldown == 0 and not self.attcking:
                att_choice =  random.randint(0, 10)
                if att_choice < 4:
                    self.attack1()
                elif att_choice > 4 and att_choice <7:
                    self.attack2()
                else:
                    self.attack2()
                    self.attack1()


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 30 and not self.invisible:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       

            dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 80) == 1:
            self.vel_y = -self.jump_high
            self.jump = True
                            
        if random.randint(0, 90) == 1 and self.jump == False and not self.repressed:
            self.hab1()

        if random.randint(0, 30) == 1 and self.jump == False and not self.repressed and dist_abs > 600:
            self.hab2()

        if self.ult_points >= self.ult_min and random.randint(0, 60) == 1 and not self.jump and not self.repressed:
            self.ult()
                

        # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
            else:
                self.dashx += 30
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True 

        #update player position with dash
        self.rect.x += self.dashx
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy



class Bot_robo(Robo):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)

    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist2 = 300
        min_dist2 = 250
        max_dist = 100
        min_dist = 40
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False # Prioriza animação de ataque/idle
            
            if self.attack_coldown == 0 and not self.attcking:
                if random.randint(0, 10) < 6:
                    self.attack1()
        elif dist_abs < max_dist2 and dist_abs >= min_dist2:
            if random.randint(0, 10) < 6:
                self.attack2()
        


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 25:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       
            if self.alive:
                dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 150) == 1:
            self.vel_y = -self.jump_high
            self.jump = True
                            
        if random.randint(0, 500) == 1 and self.jump == False and not self.repressed:
            self.hab1()

        if random.randint(0, 700) == 1 and self.jump == False and not self.repressed:
            self.hab2()

        if self.ult_points >= self.ult_min and random.randint(0, 100) == 1 and not self.jump and not self.repressed:
            self.ult()
                

            # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
                self.rect.x -= self.dash_distance
            else:
                self.dashx += 30
                self.rect.x += self.dash_distance
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if not self.attcking and self.dashx == 0:
            if target.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True

        #update player position with dash
        
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy


class Bot_paladino(Paladino):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)



    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 140
        min_dist = 70
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False 
            
            if self.attack_coldown == 0 and not self.attcking:
                att_choice =  random.randint(0, 10)
                if att_choice < 6:
                    self.attack1()
                else:
                    self.attack2()



        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 30:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       
            if self.alive:
                dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 80) == 1:
            self.vel_y = -self.jump_high
            self.jump = True
                            
        if random.randint(0, 90) == 1 and self.jump == False and not self.repressed:
            self.hab1()

        if dist_abs < max_dist and dist_abs >= min_dist:
            if random.randint(0, 20) == 1 and self.jump == False and not self.repressed:
                self.hab2()

        if self.ult_points >= self.ult_min and random.randint(0, 60) == 1 and not self.jump and not self.repressed:
            self.ult()
                

        # aplicar gravidade
        self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
            else:
                self.dashx += 30
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True 

        #update player position with dash
        self.rect.x += self.dashx
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy

class Bot_deusa(Deusa):

    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)



    def move(self, screen_width, screen_height, target):
        self.target = target
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        
        if self.player == 1:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        elif self.player == 2:
            if not self.flip:
                self.facing_direction = True
            else:
                self.facing_direction = False
        

        if self.count_knock_back > 0:
            self.count_knock_back -= 1
            if not self.flip:
                target.rect.x += 50 - self.target.knock_resistence
            else: 
                target.rect.x -= 50 - self.target.knock_resistence

        distancia = target.rect.centerx - self.rect.centerx
        dist_abs = abs(distancia)

        max_dist = 110
        min_dist = 30
        


        if dist_abs < min_dist:
            # AFASTAR
            if not self.attcking: # Garante que ele não se afaste DURANTE um ataque
                dx = -SPEED if distancia > 0 else SPEED
            self.running = True
            
       
        elif dist_abs < max_dist and dist_abs >= min_dist: # Adicionar >= min_dist é redundante, mas ajuda na clareza.
            self.ai_move = 0
            dx = 0 # Força parada para atacar/idle
            self.running = False 
            
            if self.attack_coldown == 0 and not self.attcking and not self.flying and not self.ulting:
                att_choice =  random.randint(0, 10)
                if att_choice < 6:
                    self.attack1()
                else:
                    self.attack2()
        


        else:
            # -------------------------------
            # APENAS SE LONGE DO PLAYER
            # MOVIMENTO ALEATÓRIO FUNCIONA
            # -------------------------------
            if self.health > 40 and not self.ulting:
                if not hasattr(self, "ai_timer"):
                    self.ai_timer = 0
                    self.ai_move = 0

                self.ai_timer += 1

                if self.ai_timer >= 20:
                    self.ai_timer = 0
                    opção = random.randint(0, 10)

                    if opção < 4:
                        self.ai_move = 1
                        self.running = True
                    elif opção < 8:
                        self.ai_move = -1
                        self.running = True
                    else:
                        self.ai_move = 0
            else:
                if distancia > 0:
                    self.ai_move = 1
                else:
                    self.ai_move = -1
                self.running = True       
            if self.alive and not self.ulting:
                dx += self.ai_move * SPEED
        if dx != 0:
            self.running = True
        else:
            self.running = False


        # pulo aleatório
        if not self.jump and random.randint(0, 80) == 1 and not self.flying and not self.ulting:
            self.vel_y = -self.jump_high
            self.jump = True

        if dist_abs < max_dist and dist_abs >= min_dist:                    
            if random.randint(0, 60) == 1 and self.jump == False and not self.repressed and not self.flying:
                self.hab1()

        if random.randint(0, 110) == 1 and not self.repressed and not self.flying and not self.ulting:
                self.hab2()

        if self.ult_points >= self.ult_min and random.randint(0, 60) == 1 and not self.jump and not self.repressed and not self.flying and not self.attcking:
            self.ult()
                

        # aplicar gravidade
        if not self.flying and not self.transformed:
            self.vel_y += GRAVIDADE
        dy += self.vel_y
        
        # aplicar dash
        if self.dashx > -130 and self.dashx < 130 and self.dashx != 0:
            if self.dashx < 0:
                self.dashx -= 30
                self.rect.x -= self.dash_distance
            else:
                self.dashx += 30
                self.rect.x += self.dash_distance
        else:
            self.dashx = 0


        # verifica se o player ta na tela
        if self.rect.left + dx < 0 and not self.transformed:
            dx =  -self.rect.left
        elif self.rect.right + dx > screen_width and not self.transformed:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40 and not self.transformed:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # aplicar cooldown attack
        if self.attack_coldown > 0:
            self.attack_coldown -= 1
        
        # verifica se os player olham um pro outro
        if not self.attcking and self.dashx == 0:
            if target.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True

        #update player position with dash
        
        if self.dashx == 0:
            self.rect.x += dx
            self.rect.y += dy



    def execute_ult(self, target):
        self.transformed = True
        self.rect.y = 3000
        self.ulted = True
        self.target.knock_back = self.old_knock
        esc1 = random.randint(1,5)
        if esc1 == 1:
            self.clone = Bot_guerreiro(self.player, self.flip,self.old_position, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], self.screen)
        elif esc1 == 2:
            self.clone = Bot_mago(self.player, self.flip,self.old_position, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], self.screen)
        elif esc1 == 3:
            self.clone = Bot_cavaleiro(self.player, self.flip, self.old_position, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], self.screen)
        elif esc1 == 4:
            self.clone = Bot_robo(self.player, self.flip, self.old_position, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], self.screen)
        elif esc1 == 5:
            self.clone = Bot_paladino(self.player, self.flip, self.old_position, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], self.screen)
        self.clone.health = self.health
        self.clone.ult_min = 30000
        self.clone.ult_points = self.ult_points
        utils.fighter_2 = self.clone
        utils.existis_goddess = self.me
        utils.existis_goddess.y = 3000
        self.target.target = self.clone