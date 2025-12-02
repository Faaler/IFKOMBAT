from fighter import Fighter
from guerreiro import Guerreiro
from mago import Mago
import pygame
import random
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
                target.rect.x += 50
            else: 
                target.rect.x -= 50

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
                    self.attack1(target)
                else:
                    self.attack2(target)


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
                target.rect.x += 50
            else: 
                target.rect.x -= 50

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
                esc = random.randint(0, 10)
                if esc < 6:
                    self.attack1(target)
                elif esc > 6 and esc < 8:
                    self.hab2()
                else:
                    self.attack2(target)


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

        # dash aleatório
        if self.dash and random.randint(0, 70) == 1:
            self.dashx = 60 if not self.flip else -60
            self.last_dash = pygame.time.get_ticks()
            self.dash = False
                            
        if self.ult_points >= 6 and random.randint(0, 150) == 1:
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
        self.ult_points = 6

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
                target.rect.x += 50
            else: 
                target.rect.x -= 50

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
                    self.attack1(target)
                else:
                    self.attack2(target)


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
                            
        if random.randint(0, 90) == 1:
            self.hab1()
            self.hab2()

        if self.ult_points >= 6 and random.randint(0, 150) == 1:
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

    

