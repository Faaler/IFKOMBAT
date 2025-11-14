import pygame 
from fighter import Fighter
pygame.init()
pygame.display.set_mode((1,1))
class Guerreiro(Fighter):
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        super().__init__(player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen)
        self.hab2_cooldown = 5000
        self.last_hab2 = 0


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


    def hab2(self):
        if pygame.time.get_ticks() -  self.last_hab2 > self.hab2_cooldown:
            pass
