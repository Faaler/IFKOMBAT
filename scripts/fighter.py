import pygame


class Fighter():
    def __init__(self, player,flip,inicial_postion, data, sprite_sheet, animation_steps,sound, status, screen):
        self.inicial_position = inicial_postion
        self.screen_height = 0
        self.screen_width = 0
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 # 0 - idle, 1 - run, 2 - jump, 3 - attack, 4 - attack2, 5 - hit, 6 - death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((inicial_postion[0], inicial_postion[1], status['largura'], status['altura']))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.jump_high = status['jump_high']
        self.dashx = 0
        self.attack_type = 0
        self.attcking = False
        self.attack_coldown = 0 
        self.max_att_coldown_1 = status['attack_coldwon1']
        self.max_att_coldown_2 = status['attack_coldwon2']
        self.health = 100
        self.speed = status['speed']
        self.alive = True
        self.hit = False
        self.dano1 = status['dano1'] #status
        self.dano2 = status['dano2'] # status
        self.defesa = status['defesa'] #status
        self.facing_direction = True
        self.attack_sound = sound
        self.attack_animation_cooldown_1 = status['attack_animation_cooldown_1']
        self.attack_animation_cooldown_2 = status['attack_animation_cooldown_2']
        self.attack_hitbox_modificator_1 = status['attack_box_size_1']
        self.attack_hitbox_modificator_2 = status['attack_box_size_2']
        self.screen = screen
        self.target = 0
        self.ult_points = 0
        self.ult_min = status['ult_min']
        self.knock_back = status['knock_back']
        self.count_knock_back = 0
        self.stoped = False
        
        
        

    def load_images(self, sprite_sheet, animation_steps):
        # extraindo imagens dos spritesheets
        animation_list = []
        for y, animation in enumerate(animation_steps): # y = numero de iterações desse primeiro loop
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                scaled_temp_img = pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale))
                temp_img_list.append(scaled_temp_img)
            animation_list.append(temp_img_list)
        return animation_list

    def animar(self):
          # realiza animações
        animation_cooldown = 80
        self.image = self.animation_list[self.action][self.frame_index]
        #check  time since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown and self.attcking == False:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        elif self.attack_type == 1:
            if self.attcking and pygame.time.get_ticks() - self.update_time > self.attack_animation_cooldown_1:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == 4:
                    self.execute_attack(self.target)
                    if self.frame_index >= len(self.animation_list[self.action]):
                        self.attack_type = 0
        elif self.attack_type == 2:
            if self.attcking and pygame.time.get_ticks() - self.update_time > self.attack_animation_cooldown_2:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index == 4:
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
                    
                    

    # animation updates
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
            if not self.flip:
                target.rect.x += 50
            else: 
                target.rect.x -= 50


        # get key pressed
        key = pygame.key.get_pressed()
        pressed_keys = pygame.key.get_just_pressed()



        if self.attcking == False and self.alive:
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
                    self.attack1(target)
                    
                
                if key[pygame.K_v]:
                    self.attack2(target)
                    
                    
                     
                if pressed_keys[pygame.K_g]:
                    self.hab1()
                if pressed_keys[pygame.K_h]:
                    self.hab2()
                if pressed_keys[pygame.K_j]:
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
                    self.attack1(target)
                    self.attack_type = 1
                
                if key[pygame.K_KP_2]:
                    self.attack2(target)
                    self.attack_type = 2
                if pressed_keys[pygame.K_KP_4]:
                    self.hab1()
                if pressed_keys[pygame.K_KP_5]:
                    self.hab2()
                if pressed_keys[pygame.K_KP_6]:
                    if self.ult_points >= self.ult_min:
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
                print("MOD 1:", self.attack_hitbox_modificator_1[1])
                print("OFFSET:", (self.attack_hitbox_modificator_1[1] * self.rect.height) - self.rect.height)
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


        elif self.attack_type == 2:
            if not self.flip:
                attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y + ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
                )
            else:
                attack_rect = pygame.Rect(
                    self.rect.left - self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.y + ((self.attack_hitbox_modificator_2[1] * self.rect.height) - self.rect.height),
                    self.rect.width * self.attack_hitbox_modificator_2[0],
                    self.rect.height * self.attack_hitbox_modificator_2[1]
            )
            if attack_rect.colliderect(target.rect):
                self.ult_points += 1
                target.health -= self.dano2 - target.defesa
                target.hit = True


    # desenha hitbox para debug
        #pygame.draw.rect(self.screen, 'green', attack_rect)

        

    def attack1(self, target):
        if self.attack_coldown == 0:
            # execute attack
            self.attcking = True
            self.attack_type = 1


    def attack2(self, target):
        if self.attack_coldown == 0:
            # execute attack
            self.attcking = True
            self.attack_type = 2
            
            
    

    def hab1(self):
        print('habilidade 1')

    def hab2(self):
        print('habilidade 2')

    def ult(self):
        print('ult')

    def update_action(self, new_action):
        # check if new action is diferrent
        if new_action != self.action:
            self.action = new_action
            # update animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        img = pygame.transform.flip(self.image, self.flip, False)
        bottom_height = 5
        bottom_rect = pygame.Rect(
            self.rect.x,
            self.rect.bottom + bottom_height,
            self.rect.width - 10,
            bottom_height
        )
        if self.player == 1:
            pygame.draw.rect(self.screen, 'blue', bottom_rect)
        else:
            pygame.draw.rect(self.screen, 'red', bottom_rect)
        self.screen.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1]* self.image_scale)))
        
