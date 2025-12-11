import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho, fonte):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        self.fonte = fonte
        self.imagemTexto = self.fonte.render(self.texto, True, self.cor)
        

    def desenhar(self):
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizar_texto(self, novo_texto):
        self.imagemTexto = self.fonte.render(novo_texto, True, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, corTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, corTexto, tamanho, pygame.font.Font('./assets/fonts/turok.ttf', 40))
        self.posicao = (x, y)
        self.corFundo = corFundo
        self.tamanho = tamanho
        self.rect = 0
    def desenhar(self):
        self.rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        pygame.draw.rect(self.tela, self.corFundo, self.rect)
        self.texto.desenhar()
    def get_click(self):
        posicaoMouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        if rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False