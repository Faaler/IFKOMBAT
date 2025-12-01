import pygame 
from fighter import Fighter
pygame.init()
pygame.display.set_mode((1,1))
acid_group = pygame.sprite.Group()
class Guerreiro(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.acid_exist = False
        self.case = 0
        self.ima_limite = 0
        self.oldspeed = 0
        self.has_ima = False
        self.ult_active = False
        self.acid_active = False
        self.last_ima = 0


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
                self.count_knock_back = self.knock_back * 3
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
        
      
        self.animar()
        acid_group.update()
        self.att_hab2()

    def hab1(self):
        lastcall = pygame.time.get_ticks()
        self.acid_active = True
        self.oldspeed = self.target.speed
        if self.player == 1:
            color = 'yellow'
        else:
            color = 'green'
        if not self.acid_exist and not self.jump and not self.ult_active:
            if self.flip:
                Acid(self.rect.bottom -2, self.rect.left - 180,20,color, lastcall, self.screen, self.target,self.oldspeed,2,150,10, acid_group)
            else:
                Acid(self.rect.bottom - 2, self.rect.left + 180,20,color, lastcall, self.screen, self.target,self.oldspeed,2,150,10, acid_group)

    def hab2(self):
        if pygame.time.get_ticks() - self.last_ima > 4000:
            self.last_ima = pygame.time.get_ticks()
            if self.player == 1:
                if not self.flip:
                    self.case = 1
                    self.ima_limite = ((self.target.rect.x - self.rect.x)*0.4)
                    if not self.has_ima:
                        self.oldspeed = self.target.speed
                else:
                    self.case = 2
                    self.ima_limite = ((self.rect.x - self.target.rect.x)*0.4)
                    if not self.has_ima:
                        self.oldspeed = self.target.speed
            elif self.player == 2:
                if self.flip:
                    self.case = 2
                    self.ima_limite = ((self.rect.x - self.target.rect.x)*0.4)
                    if not self.has_ima:
                        self.oldspeed = self.target.speed
                else:
                    self.case = 1
                    self.ima_limite = ((self.target.rect.x - self.rect.x)*0.4)
                    if not self.has_ima:
                        self.oldspeed = self.target.speed

                
    def att_hab2(self):
        if self.case == 1:
            if self.target.rect.x - self.rect.x > self.ima_limite:
                self.has_ima = True
                self.target.stoped = True
                self.target.rect.x -= 10
            else:
                self.target.stoped = False
                self.case = 0
                self.has_ima = False
        if self.case == 2:
            if self.rect.x - self.target.rect.x > self.ima_limite:
                self.has_ima = True
                self.target.stoped = True
                self.target.rect.x += 10
            else:
                self.target.stoped = False
                self.case = 0
                self.has_ima = False

        
    def ult(self):
        self.ult_active = True
        lastcall = pygame.time.get_ticks()
        self.oldspeed = self.target.speed
        if self.player == 1:
            color = '#B8860B'
        else:
            color = '#013220'
        if not self.jump and not self.acid_active:
            self.ult_points -= self.ult_min
            if self.flip:
                Acid(self.rect.bottom -2, self.rect.left - 180 - 600,90,color, lastcall, self.screen, self.target,self.oldspeed,1,600,15, acid_group)
            else:
                Acid(self.rect.bottom - 2, self.rect.left + 180,90,color, lastcall, self.screen, self.target,self.oldspeed,1,600,15, acid_group)

class Acid(pygame.sprite.Sprite):
    def __init__(self,y, x, life, color, criacao, screen,target,oldspeed,dano, largura,tempo_vida, groups):
        super().__init__(groups)
        self.rect = pygame.Rect((x, y, largura, 6))
        self.life = life
        self.screen = screen
        self.target = target
        self.last_damage = 0
        self.damage_cooldown = 200
        self.target.target.acid_exist = True
        self.color = color
        self.criacao = criacao
        self.oldspeed = oldspeed
        self.newspeed = oldspeed / 2
        self.dano = dano
        self.tempo_de_vida = tempo_vida * 1000

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.check_colision()
        if self.life <= 0 or pygame.time.get_ticks() - self.criacao > self.tempo_de_vida:
            self.target.target.acid_exist = False
            self.target.speed = self.oldspeed
            self.target.target.ult_active = False
            self.target.target.acid_active = False
            self.kill()
        

    def check_colision(self):
        
        if self.rect.colliderect(self.target.rect):
            if pygame.time.get_ticks() - self.last_damage > self.damage_cooldown:
                self.target.health -= self.dano
                self.life -= 2
                self.target.speed = self.newspeed
                self.last_damage = pygame.time.get_ticks()
        else:
            self.target.speed = self.oldspeed

