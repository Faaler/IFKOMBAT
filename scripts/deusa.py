import pygame
from pygame import mixer
import random
from fighter import Fighter
from mago import Mago
from guerreiro import Guerreiro
from cavaleiro import Cavaleiro
from robo import Robo
from paladino import Paladino
import utils
pygame.init()
pygame.display.set_mode((1,1))
fliying_sheet = pygame.image.load('./assets/images/goddess/Sprites/flight.png').convert_alpha()
clock = pygame.time.Clock()

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








class Deusa(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.vulneravel = False
        self.vulneravel_duration = 2000
        self.last_vulneravel = 0
        self.old_defence = 0
        self.hab1_cooldown = 10000
        self.hab1_last_call = 0
        self.flying = False
        self.flight_cooldown = 5000
        self.last_flight = 0
        self.animation_steps = animation_steps
        self.sprite_sheet = sprite_sheet
        self.transformed = False
        self.ulting = False
        self.ulted = False
        self.frame_ult = 10
        self.ult_animation_cooldown = 110
        self.ult_duration = 15000
        self.ult_lastcall = 0
        self.ult_points = 0
        self.clone = 0
        self.old_position = [0,0]
        self.me = 0
        self.old_knock = 0

        


    def animar(self):
          # realiza animações
        animation_cooldown = 80
        self.image = self.animation_list[self.action][self.frame_index]
        #check  time since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown and self.attcking == False and self.ulting == False:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        elif self.ulting:
            if pygame.time.get_ticks() - self.update_time > self.ult_animation_cooldown:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == self.frame_ult:
                    self.execute_ult(self.target)
                    if self.frame_index >= len(self.animation_list[self.action]):
                        self.ulting = False
        elif self.attack_type == 1:
            if self.attcking and pygame.time.get_ticks() - self.update_time > self.attack_animation_cooldown_1:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == self.frame_att1:
                    self.execute_attack(self.target)
                    if self.frame_index >= len(self.animation_list[self.action]):
                        self.attack_type = 0
        elif self.attack_type == 2:
            if self.attcking and pygame.time.get_ticks() - self.update_time > self.attack_animation_cooldown_2:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == self.frame_att2:
                    self.execute_attack(self.target)
                    if self.frame_index >= len(self.animation_list[self.action]):
                        self.attack_type = 0
        


       

        



        # check if animation has fineshed
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                # check attack is over
                if self.action == 3: # ataque 1
                    self.attcking = False
                    self.attack_coldown = self.max_att_coldown_1
                if self.action == 4: # ataque 2
                    self.attcking = False
                    self.attack_coldown = self.max_att_coldown_2
                if self.action == 5:
                    self.hit = False
                if self.action == 7:
                    self.ulting = False



    def execute_attack(self, target):
        self.attack_sound.play()
        if self.attack_type == 1:
            if not self.flip:
                attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y - ((self.attack_hitbox_modificator_1[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_1[0],
                    self.rect.height * self.attack_hitbox_modificator_1[1]
                )
            else:
                attack_rect = pygame.Rect(
                    self.rect.left - self.rect.width * self.attack_hitbox_modificator_1[0],
                    self.rect.y - ((self.attack_hitbox_modificator_1[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_1[0],
                    self.rect.height * self.attack_hitbox_modificator_1[1]
            )
            if attack_rect.colliderect(target.rect):
                self.ult_points += 1
                target.health -= self.dano1 - target.defesa
                self.count_knock_back = self.knock_back
                target.hit = True


        elif self.attack_type == 2:
            if not self.flip:
                attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y - ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
                )
            else:
                attack_rect = pygame.Rect(
                    self.rect.left - self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.y - ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
            )
            if attack_rect.colliderect(target.rect):
                self.ult_points += 1
                target.health -= self.dano2 - target.defesa
                self.count_knock_back = self.knock_back
                target.jump = True
                target.hit = True
                if not self.vulneravel:
                    self.vulneravel = True
                    self.last_vulneravel = pygame.time.get_ticks()
                    self.old_defence = target.defesa


    def update(self):
        if self.hit:
            self.attcking = False
            self.attack_type = 0
            self.attack_coldown = 5


        #check player action
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)
        elif self.hit:
            self.update_action(5)
        elif self.attcking:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
                
        elif self.jump:
            self.update_action(2)
        elif self.running:
            self.update_action(1)
        elif self.ulting:
            self.update_action(6)
        else:
            self.update_action(0)
        
        if self.vulneravel:
            self.target.defesa = 0
            if pygame.time.get_ticks() - self.last_vulneravel > self.vulneravel_duration:
                self.vulneravel = False
                self.target.defesa = self.old_defence

        if self.flying:
            if self.rect.y < 200:
                self.vel_y = 0
            if pygame.time.get_ticks() - self.last_flight > 1800 or not self.alive or not self.target.alive:
                self.flying = False
                self.animation_list = self.load_images(self.sprite_sheet, self.animation_steps)
                self.speed = self.old_speed
                self.jump = True
                
        self.animar()

        if self.ulted:
            self.health = self.clone.health
            self.ult_points = self.clone.ult_points
            self.num_vitorias = self.clone.num_vitorias
            if pygame.time.get_ticks() - self.ult_lastcall > self.ult_duration or not self.target.alive or not self.alive:
                utils.existis_goddess = 0
                if self.player == 1:
                    utils.fighter_1 = self.me
                else:
                    utils.fighter_2 = self.me
                self.ulted = False
                self.transformed = False
                self.rect.x = self.clone.rect.x
                self.rect.y = self.clone.rect.y
                self.target.target = self.me

        if self.ulting:
            self.target.knock_back = 0
            if self.hit:
                self.count_knock_back = 6
                self.target.health -= 1
                




    def move(self, screen_width, screen_height, target):
        if not self.get_target:
            self.target = target
            self.get_target = True
        self.screen_height = screen_height
        self.screen_width = screen_width
        if self.stoped:
            SPEED = 0
        else:
            SPEED = self.speed
        GRAVIDADE = 2
        dx = 0
        dy = 0
        self.running = False
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
            self.get_knock_back(target)


        # get key pressed
        key = pygame.key.get_pressed()
        pressed_keys = pygame.key.get_just_pressed()



        if self.attcking == False and self.alive and not self.transformed and not self.ulting:
            #check player 1 controls
             # movimento
            if self.player == 1:
                if key[pygame.K_a]:
                    if not self.flip:
                        self.facing_direction = not self.facing_direction
                    
                    
                    dx = -SPEED
                    self.running = True
                elif key[pygame.K_d]:
                    if self.flip:
                        self.facing_direction = not self.facing_direction
                    dx = SPEED   
                    self.running = True

                # pulo
                if key[pygame.K_w] and self.jump == False and not self.flying:
                    self.vel_y = - self.jump_high
                    self.jump = True
                # attacks
                if key[pygame.K_c] and not self.flying:
                    self.attack1()
                    
                    
                
                if key[pygame.K_v] and not self.flying:
                    self.attack2()
                    
                    
                     
                if pressed_keys[pygame.K_g] and not self.repressed and not self.flying:
                    self.hab1()
                if pressed_keys[pygame.K_h] and not self.repressed and not self.flying:
                    self.hab2()
                if pressed_keys[pygame.K_j] and not self.repressed and not self.flying:
                    if self.ult_points >= self.ult_min:
                        self.ult()
                        

                
                    
           
            
            else:
                #check player 2 controls
                # movimento
                if self.player == 2:
                    if key[pygame.K_LEFT]:
                        if not self.flip:
                            self.facing_direction = not self.facing_direction
                        dx = -SPEED
                        self.running = True
                    elif key[pygame.K_RIGHT]:
                        if self.flip:
                            self.facing_direction = not self.facing_direction
                        dx = SPEED   
                        self.running = True
                    # pulo
                if key[pygame.K_UP] and self.jump == False and not self.flying:
                    self.vel_y = - self.jump_high
                    self.jump = True
                # attacks
                if key[pygame.K_KP_1] and not self.flying:
                    self.attack1()
                    self.attack_type = 1
                
                if key[pygame.K_KP_2] and not self.flying:
                    self.attack2()
                    self.attack_type = 2
                if pressed_keys[pygame.K_KP_4] and not self.repressed and not self.flying:
                    self.hab1()
                if pressed_keys[pygame.K_KP_5] and not self.repressed and not self.flying:
                    self.hab2()
                if pressed_keys[pygame.K_KP_6] and not self.repressed and not self.flying:
                    if self.ult_points >= self.ult_min:
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

    def hab1(self):
        if pygame.time.get_ticks() - self.hab1_last_call > self.hab1_cooldown:
            self.hab1_last_call = pygame.time.get_ticks()
            if not self.flip:
                attack_rect = pygame.Rect(
                            self.rect.right,
                            self.rect.y + 50,
                            self.rect.width + 150,
                            self.rect.height/3 
                        )
            else:
                attack_rect = pygame.Rect(
                            self.rect.left - (self.rect.width+60),
                            self.rect.y +50,
                            self.rect.width + 150,
                            self.rect.height/3
                    )
            pygame.draw.rect(self.screen, 'lightblue', attack_rect)
            if attack_rect.colliderect(self.target.rect):
                    pontos_roubados = self.target.ult_points // 2
                    self.ult_points += pontos_roubados
                    self.target.ult_points -= pontos_roubados
    
    def hab2(self):
        if pygame.time.get_ticks() - self.last_flight > self.flight_cooldown:
            self.flying = True
            self.last_flight = pygame.time.get_ticks()
            self.vel_y -= 30
            self.old_speed = self.speed
            self.speed = 14
            self.jump = False
            self.animation_list = self.load_images(fliying_sheet, self.animation_steps)

    def ult(self):
        if self.ult_points >= self.ult_min:
            self.ult_lastcall = pygame.time.get_ticks()
            self.ult_points -= self.ult_min
            self.old_position = [self.rect.x, self.rect.y]
            self.old_knock = self.target.knock_back
            self.ulting = True
            self.me = self.target.target
            if self.flying:
                self.flying = False
                self.speed = self.old_speed

    def execute_ult(self, target):
        self.transformed = True
        self.rect.y = 3000
        self.ulted = True
        self.target.knock_back = self.old_knock
        esc1 = random.randint(1,5)
        if esc1 == 1:
            self.clone = Guerreiro(self.player, self.flip,self.old_position, PLAYER1_DATA, player1_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, caracters_status[0], self.screen)
        elif esc1 == 2:
            self.clone = Mago(self.player, self.flip,self.old_position, PLAYER2_DATA, player2_sheet, WIZARD_ANIMATION_STEPS, staff_fx, caracters_status[1], self.screen)
        elif esc1 == 3:
            self.clone = Cavaleiro(self.player, self.flip, self.old_position, PLAYER3_DATA, player3_sheet, KNIGHT_ANIMATION_STEPS, sword_fx, caracters_status[2], self.screen)
        elif esc1 == 4:
            self.clone = Robo(self.player, self.flip, self.old_position, PLAYER4_DATA, player4_sheet, ROBOT_ANIMATION_STEPS, staff_fx, caracters_status[3], self.screen)
        elif esc1 == 5:
            self.clone = Paladino(self.player, self.flip, self.old_position, PLAYER5_DATA, player5_sheet, PALADINE_ANIMATION_STEPS, staff_fx, caracters_status[4], self.screen)
        self.clone.num_vitorias = self.num_vitorias
        self.clone.ult_min = 30000
        if self.health < 85:
            self.health += 15
        else:
            self.clone.health = 100
        self.clone.ult_points = self.ult_points
        self.clone.health = self.health
        if self.player == 1:
            utils.fighter_1 = self.clone
        else:
            utils.fighter_2 = self.clone
        utils.existis_goddess = self.me
        utils.existis_goddess.y = 3000
        self.target.target = self.clone
