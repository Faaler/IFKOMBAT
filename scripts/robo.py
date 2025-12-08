import pygame 
import random
from fighter import Fighter
pygame.init()
pygame.display.set_mode((1,1))
shot_surf = pygame.image.load('./assets/images/robot/Sprites/Projectile.png').convert_alpha()
shot_group = pygame.sprite.Group()
big_projetil = pygame.image.load('./assets/images/robot/Sprites/BigProjetil.png').convert_alpha()
missil = pygame.image.load('./assets/images/robot/Sprites/missil.png').convert_alpha()
class Robo(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.knock_resistence = 40
        self.dash_distance = 40
        self.ulting = False
        self.ult_animation_cooldown = 100
        self.frame_ult = 6




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
                target.hit = True
                self.count_knock_back = self.knock_back / 2


        elif self.attack_type == 2:
            if not self.flip:
                attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y + ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
                )
                #pygame.draw.rect(self.screen, 'green', attack_rect)  
            else:
                attack_rect = pygame.Rect(
                    self.rect.left - self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.y + ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
            )
                #pygame.draw.rect(self.screen, 'green', attack_rect)  
            if attack_rect.colliderect(target.rect):
                self.ult_points += 2
                target.health -= self.dano2 - target.defesa
                target.hit = True
                self.count_knock_back = self.knock_back


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


    def update(self):
        if self.hit:
            self.attcking = False
            self.attack_type = 0
            self.attack_coldown = 5

        # if not self.enemie_knockback_geted:
        #     self.get_nock(self.target)
        #     self.enemie_knockback_geted = True
        

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
            self.update_action(7)
        else:
            self.update_action(0)
        
        shot_group.draw(self.screen)
        shot_group.update()
        
        self.animar() 


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



        if self.attcking == False and self.alive and not self.ulting:
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
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = - self.jump_high
                    self.jump = True
                # attacks
                if key[pygame.K_c]:
                    self.attack1()
                    
                
                if key[pygame.K_v]:
                    self.attack2()
                    
                    
                     
                if pressed_keys[pygame.K_g] and not self.repressed:
                    self.hab1()
                if pressed_keys[pygame.K_h] and not self.repressed:
                    self.hab2()
                if pressed_keys[pygame.K_j] and not self.repressed:
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
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = - self.jump_high
                    self.jump = True
                # attacks
                if key[pygame.K_KP_1]:
                    self.attack1()
                    self.attack_type = 1
                
                if key[pygame.K_KP_2]:
                    self.attack2()
                    self.attack_type = 2
                if pressed_keys[pygame.K_KP_4] and not self.repressed:
                    self.hab1()
                if pressed_keys[pygame.K_KP_5] and not self.repressed:
                    self.hab2()
                if pressed_keys[pygame.K_KP_6] and not self.repressed:
                    if self.ult_points >= self.ult_min:
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




    def attack2(self):
        if self.attack_coldown == 0:
            self.attcking = True
            self.attack_type = 2
            self.dashx = 1 if not self.flip else -1

    def hab1(self):
        if self.ult_points > 0:
            self.ult_points -= 1
            shot = ShotRobo(shot_surf, self.rect.centerx, self.rect.centery, self.target, self.screen_width, 30, [5, 2, self.target.flip],  shot_group)

    def hab2(self):
        if self.ult_points > 2 and not self.jump:
            self.ult_points -= 3
            if self.flip:
                spaw = 1334
            else:
                spaw = -34
            bigshot = ShotRobo(big_projetil, spaw, self.rect.bottom, self.target, self.screen_width, 2,[20, 6, self.target.flip],  shot_group)

    
    def ult(self):
        if self.ult_points >= self.ult_min:
            self.ult_points -= self.ult_min
            self.ulting = True
    def execute_ult(self, target):
        missil_shot = MissilRobo(missil, random.randint(700, 1300), -100, target, self.screen, 18, 55, shot_group)
        missil_shot = MissilRobo(missil, random.randint(100, 600), -100, target, self.screen, 18, 55, shot_group)


class ShotRobo(pygame.sprite.Sprite):
    def __init__(self,surf,x,y,target, screen_width,speed, status, groups):
        super().__init__(groups)
        self.screen = screen_width
        self.image = surf
        self.rect = self.image.get_rect(bottomleft = (x,y))
        self.speed = speed
        self.target = target
        self.dano = status[0]
        self.knock_back = status[1]
        self.direction = status[2]

    def update(self):
        
        self.check_colision()
        if self.direction:
            self.rect.centerx += self.speed
        else:
            self.rect.centerx -= self.speed
        if self.rect.left > (self.screen + 66) or self.rect.right < -66:
            self.kill()

    def check_colision(self):
        if self.rect.colliderect(self.target.rect):
            self.target.health -= (self.dano -self.target.defesa)
            self.target.hit = True
            self.target.target.count_knock_back = self.knock_back
            self.kill()

class MissilRobo(pygame.sprite.Sprite):
    def __init__(self,surf,x,y,target, screen_width,speed, dano, groups):
        super().__init__(groups)
        self.screen = screen_width
        self.image = surf
        self.rect = self.image.get_rect(bottomleft = (x,y))
        self.speed = speed
        self.target = target
        self.dano = dano
        

    def update(self):
        self.check_colision()
        self.rect.centery += self.speed
        if self.rect.top > self.screen.height:
            self.kill()

    def check_colision(self):
        if self.rect.colliderect(self.target.rect):
            self.target.health -= (self.dano - self.target.defesa)
            self.target.hit = True
            self.kill()




