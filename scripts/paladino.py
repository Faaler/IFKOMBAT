import pygame 
from fighter import Fighter
pygame.init()
pygame.display.set_mode((2,1))

class Paladino(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.old_sprite = 0
        self.sprite_sheet = sprite_sheet
        self.animation_steps = animation_steps
        self.shielded = False
        self.hab1_cooldown = 7000
        self.last_hab1 = 0
        self.ultes = 0
        self.repress = False
        self.repress_cooldown = 15000
        self.last_repress = 0
        self.repress_duration = 5000
        self.time_repress_started = 0


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
                target.hit = True
                self.last_hab1 -= 1000
                self.last_repress -= 1000


    def update(self):
        if self.ultes > 0:
            if self.health <= 0:
                self.health = 15
                self.ultes -= 1
                self.hit = False
                self.hab1()
        
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

        if not self.alive:
                self.ultes = 0

                

        if self.shielded and self.attcking == False:
            if self.hit:
                self.last_hab1 = pygame.time.get_ticks()
                if self.target.health > (15 - self.target.defesa) and self.target.attcking or self.target.nome == 'Deusa':
                    self.target.health -= (15 - self.target.defesa)
                    self.count_knock_back = 4
                elif self.target.health > 5 and self.target.attcking or self.target.nome == 'Deusa':
                    self.target.health = 5
                    self.count_knock_back = 4
                self.shielded = False
                self.sprite_sheet = self.old_sprite
                self.animation_list = self.load_images(self.sprite_sheet, self.animation_steps)
        
            if self.target and not self.target.alive:
                    self.shielded = False
                    self.sprite_sheet = self.old_sprite
                    self.animation_list = self.load_images(self.sprite_sheet, self.animation_steps)

        if not self.shielded:
            self.defesa = 1
        if self.repress and pygame.time.get_ticks() - self.time_repress_started > self.repress_duration:
            self.target.repressed = False
            self.repress = False

        
      
        self.animar() 


    def hab1(self):
        if not self.shielded and pygame.time.get_ticks() - self.last_hab1 > self.hab1_cooldown:
            self.shielded = True
            self.defesa = 5
            self.old_sprite = self.sprite_sheet
            new_sprite = pygame.image.load("./assets/images/paladine/Sprites/shild_paladino.png").convert_alpha()
            self.animation_list = self.load_images(new_sprite, self.animation_steps)

    def hab2(self):
        if not self.repress and pygame.time.get_ticks() - self.last_repress > self.repress_cooldown:
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
            pygame.draw.rect(self.screen, 'yellow', attack_rect)
            if attack_rect.colliderect(self.target.rect):
                self.target.repressed = True
                self.repress = True
                self.last_repress = pygame.time.get_ticks()
                self.time_repress_started = pygame.time.get_ticks()


    def ult(self):
        self.ultes += 1
        self.ult_points -= self.ult_min
    
