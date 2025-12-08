import pygame
from fighter import Fighter
pygame.init()

class Cavaleiro(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.count_yknock_back = 0
        self.yknock_back = status['yknock_back']
        self.last_att_2 = 0
        self.att2_specialcoldown = 900
        self.animation_steps = animation_steps
        self.sprite_sheet = sprite_sheet
        self.invisible = False
        self.hab1_cooldown = 4500
        self.last_hab1 = 0
        self.hab2_cooldown = 15000
        self.hab2_duration = 4000
        self.last_hab2 = 0
        self.old_sprite = 0
        self.old_scale = data[1]
        self.ult_points = 0
        self.last_ult = 0
        self.ult_duration = 7000
        self.ulted = False




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
                self.count_yknock_back = self.yknock_back
                target.jump = True
                target.hit = True

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


        if pygame.time.get_ticks() - self.last_hab2 > self.hab2_duration:
            if self.invisible:
                self.invisible = False
                self.animation_list = self.load_images(self.old_sprite, self.animation_steps)

        if self.count_yknock_back > 0:
            self.target.rect.y -= 50 - self.target.knock_resistence / 2
            self.count_yknock_back -= 1

        if self.ulted:
            self.ult_points = 0
            if pygame.time.get_ticks() - self.last_ult > self.ult_duration:
                self.ulted = False
                self.image_scale = self.old_scale
                self.offset[0] /= 1.05
                self.offset[1] /= 1
                self.animation_list = self.load_images(self.sprite_sheet, self.animation_steps)
                new_height = self.rect.height / 1.16
                self.rect = pygame.Rect((self.rect.x, self.rect.y, self.rect.width, new_height))
                self.speed = 9
                self.defesa = 2
                self.jump_high = 35
                self.dano1 = 6
                self.dano2 = 9
                self.attack_animation_cooldown_1 = 50
                self.attack_animation_cooldown_2 = 55
                self.knock_back = 4.2
                self.max_att_coldown_1 = 35
                self.att2_specialcoldown = 900
      
        self.animar()


    def attack2(self):
        if self.attack_coldown == 0 and pygame.time.get_ticks() - self.last_att_2 > self.att2_specialcoldown:
            # execute attack
            self.attcking = True
            self.attack_type = 2
            self.last_att_2 = pygame.time.get_ticks()
   

    def check_colision(self):
        
        if self.rect.colliderect(self.target.rect):
            if pygame.time.get_ticks() - self.last_damage > self.damage_cooldown:
                self.target.health -= self.dano
                self.life -= 2
                self.target.speed = self.newspeed
                self.last_damage = pygame.time.get_ticks()
        else:
            self.target.speed = self.oldspeed

    def hab1(self):
        if pygame.time.get_ticks() - self.last_hab1 > self.hab1_cooldown:
            self.last_hab1 = pygame.time.get_ticks()
            if self.flip:
                self.rect.x = 50
            else: 
                self.rect.x = 1250


    def hab2(self):
        if not self.invisible:
            self.old_sprite = self.sprite_sheet
            self.invisible_sheet = pygame.image.load('./assets/images/knight/Sprites/invisible_knight.png').convert_alpha()
        if pygame.time.get_ticks() - self.last_hab2 > self.hab2_cooldown and not self.ulted:
            self.last_hab2 = pygame.time.get_ticks()
            self.animation_list = self.load_images(self.invisible_sheet, self.animation_steps)
            self.invisible = True
        
    def ult(self):
        if self.ult_points >= self.ult_min and not self.invisible:
            self.last_ult = pygame.time.get_ticks()
            self.ult_points -= self.ult_min
            self.image_scale *= 1.16
            self.offset[0] *= 1.05
            self.offset[1] *= 1
            self.animation_list = self.load_images(self.sprite_sheet, self.animation_steps)
            new_height = self.rect.height * 1.16
            self.rect = pygame.Rect((self.rect.x, self.rect.y, self.rect.width, new_height))
            self.speed = 7
            self.defesa = 3
            self.jump_high = 25
            self.dano1 = 8
            self.dano2 = 13
            self.attack_animation_cooldown_1 = 65
            self.attack_animation_cooldown_2 = 70
            self.ulted = True
            self.knock_back = 5.5
            self.max_att_coldown_1 = 50
            self.att2_specialcoldown = 1000
            if self.health <= 90:
                self.health += 10
            elif self.health < 100:
                self.health += 100 - self.health
            
                
            

            

            

    # def draw(self):
    #     img = pygame.transform.flip(self.image, self.flip, False)
    #     bottom_height = 5
    #     bottom_rect = pygame.Rect(
    #         self.rect.x,
    #         self.rect.bottom + bottom_height,
    #         self.rect.width - 10,
    #         bottom_height
    #     )
    #     if not self.invisible:
    #         if self.player == 1:
    #             pygame.draw.rect(self.screen, 'blue', bottom_rect)
    #             #pygame.draw.rect(self.screen, 'red', self.rect) # desenha hitbox para debug
    #         else:
    #             pygame.draw.rect(self.screen, 'red', bottom_rect)
    #         self.screen.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1]* self.image_scale)))