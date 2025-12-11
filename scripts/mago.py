import pygame 
from fighter import Fighter
pygame.init()
pygame.display.set_mode((2,1))
ult_surf = pygame.image.load('./assets/images/ult_wizard/Nave.png').convert_alpha()
ult_surf = pygame.transform.scale(ult_surf, (90, 90))
projetil_group = pygame.sprite.Group()
class Mago(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.dash_cooldown = status['dash_coldown']
        self.last_dash = 0
        self.dash = True
        self.slow = False
        self.slow_applyed = False
        self.time_apply_slow = 0
        self.half_speed = 0
        self.small_jump = 0
        self.original_speed = 0
        self.original_jump = 0
        self.hab2_last_call = 0
        self.old_attspeed_1 = 0
        self.old_attspeed_2 = 0
        self.new_attspeed_1 = 0
        self.new_attspeed_2 = 0
        self.dash_distance = 90
        
        

           


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
        else:
            self.update_action(0)
        
        self.animar()

        if not self.dash:
            if pygame.time.get_ticks() - self.last_dash > self.dash_cooldown:
                self.dash = True

        if self.slow:
            if pygame.time.get_ticks() - self.time_apply_slow < 6000 and not self.slow_applyed:
                self.target.speed = self.half_speed
                self.target.jump_high = self.small_jump
                self.target.attack_animation_cooldown_1 = self.new_attspeed_1
                self.target.attack_animation_cooldown_2 = self.new_attspeed_2
                self.slow_applyed = True
            elif pygame.time.get_ticks() - self.time_apply_slow > 5000 :
                self.slow = False
                self.target.speed = self.original_speed
                self.target.jump_high = self.original_jump
                self.target.attack_animation_cooldown_1 = self.old_attspeed_1
                self.target.attack_animation_cooldown_2 = self.old_attspeed_2
                self.slow_applyed = False
                 
        projetil_group.draw(self.screen)
        projetil_group.update()

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
                if self.health <= 100 - self.dano2/2:
                    self.health += self.dano2/2
                elif self.health < 100:
                    self.health += 100 - self.health
                target.hit = True


    # desenha hitbox para debug
        #pygame.draw.rect(self.screen, 'green', attack_rect)
                
                
                
                
                
                
               


    def hab1(self):
        if self.dash:
            self.dash = False
            self.last_dash = pygame.time.get_ticks()
            if self.facing_direction == False:
                self.dashx = -1
            else:
                self.dashx = 1


    def hab2(self):
        if pygame.time.get_ticks() - self.hab2_last_call > 6000:
            self.half_speed = self.target.speed / 2.1
            self.small_jump = self.target.jump_high / 1.2
            self.new_attspeed_1 = self.target.attack_animation_cooldown_1 * 1.5
            self.new_attspeed_2 = self.target.attack_animation_cooldown_2 * 1.5

            self.old_attspeed_1 = self.target.attack_animation_cooldown_1
            self.old_attspeed_2 = self.target.attack_animation_cooldown_2
            self.original_speed = self.target.speed
            self.original_jump = self.target.jump_high
            self.exec_slow()
            self.hab2_last_call = pygame.time.get_ticks()

    def ult(self):
        if not self.jump:
            self.ult_points -= self.ult_min
            Projetil_ULT(ult_surf, self.rect.left, self.rect.bottom, self.target, self.screen_width, self.target.flip, projetil_group)



    def exec_slow(self):
        if not self.slow:
            if not self.flip:
                    attack_rect = pygame.Rect(
                        self.rect.right,
                        self.rect.y,
                        self.rect.width + 100,
                        self.rect.height/3 
                    )
            else:
                    attack_rect = pygame.Rect(
                        self.rect.left - (self.rect.width+60),
                        self.rect.y,
                        self.rect.width + 100,
                        self.rect.height/3
                )
            pygame.draw.rect(self.screen, 'purple', attack_rect)
            if attack_rect.colliderect(self.target.rect):
                self.slow = True
                self.time_apply_slow = pygame.time.get_ticks()
                
                
        

class Projetil_ULT(pygame.sprite.Sprite):
    def __init__(self,surf,x,y,target, screen_width, direction, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(bottomleft = (x,y))
        self.screen_width = screen_width
        self.target = target
        self.speed = 14
        self.direction = direction
        
        

    def update(self):
        
        self.check_colision()
        if self.direction:
            self.rect.centerx += self.speed
        else:
            self.image = pygame.transform.flip(self.image, self.direction, False)
            self.rect.centerx -= self.speed
        if self.rect.left > self.screen_width or self.rect.right < 0:
            self.kill()

    def check_colision(self):
        if self.rect.colliderect(self.target.rect):
            self.target.health -= 25
            self.target.hit = True
            self.target.target.count_knock_back = 3
            if self.target.target.health <= 95 and self.target.alive:
                self.target.target.health += 5
            elif self.target.target.health < 100 and self.target.alive:
                self.target.target.health += 100 - self.target.target.health
            self.kill()
        










