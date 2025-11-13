import pygame 
from fighter import Fighter
pygame.init()
pygame.display.set_mode((2,1))
ult_surf = pygame.image.load('./assets/images/ult_wizard/Nave.png').convert_alpha()
projetil_group = pygame.sprite.Group()
class Mago(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.dash_cooldown = status['dash_coldown']
        self.last_dash = 0
        self.dash = False
        

        print(f'valor herdado: {self.health}')   


    def update(self):
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
        
        # realiza animações
        animation_cooldown = 80
        self.image = self.animation_list[self.action][self.frame_index]
        #check  time since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown and self.attcking == False:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        elif self.attcking and pygame.time.get_ticks() - self.update_time > self.attack_animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()



        # check if animation has fineshed
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                # check attack is over
                if self.action == 3 or self.action == 4:
                    self.attcking = False
                    self.attack_coldown = 25
                if self.action == 5:
                    self.hit = False
                    # if player is in middle of an attack then the attack stops
                    self.attcking = False
                    self.attack_coldown = 20

        if self.dash:
            if pygame.time.get_ticks() - self.last_dash > self.dash_cooldown:
                self.dash = False
                 
        projetil_group.draw(self.screen)
        projetil_group.update()

    def attack2(self, target):
        if self.attack_coldown == 0:
            # execute attack
            self.attack_sound.play()
            self.attcking = True
            
            attackin_rect = pygame.Rect(self.rect.centerx - (self.attack_hitbox_modificator[0]* self.rect.width * self.flip), self.rect.top - (self.rect.height * self.attack_hitbox_modificator[1] - self.rect.height), self.attack_hitbox_modificator[0] * self.rect.width, self.rect.height * self.attack_hitbox_modificator[1]) 
            #pygame.draw.rect(surface, 'green', attackin_rect, attackin_rect.width)
            if attackin_rect.colliderect(target.rect):
                self.ult_points += 1
                target.health -= self.dano - target.defesa
                if self.health <= 100 - self.dano/2:
                    self.health += self.dano/2
                elif self.health < 100:
                    self.health += 100 - self.health
                target.hit = True


    def hab1(self):
        if self.dash == False:
            self.dash = True
            self.last_dash = pygame.time.get_ticks()
                
            if self.facing_direction == False:
                self.dashx = -1
            else:
                self.dashx = 1

    def ult(self):
        Projetil_ULT(ult_surf, self.rect.left, self.rect.bottom, self.facing_direction, self.target, projetil_group)
        

class Projetil_ULT(pygame.sprite.Sprite):
    def __init__(self,surf,x,y,direcao, target, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(bottomleft = (x,y))
        self.direcao = direcao
        self.target = target
        self.speed = 10
        
        

    def update(self):
        
        self.check_colision()
        if self.direcao:
            self.rect.centerx += self.speed
        else:
            self.rect.centerx -= self.speed
        if self.rect.left > 1100 or self.rect.right < 0:
            self.kill()

    def check_colision(self):
        if self.rect.colliderect(self.target.rect):
            self.target.health -= 25
            if self.target.target.health <= 95:
                self.target.target.health += 5
            elif self.target.target.health < 100:
                self.target.target.health += 100 - self.target.target.health
            self.kill()
        










