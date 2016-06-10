
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
fondo1= pygame.image.load("fondo1.png").convert()


class Pared(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__( self )
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def update(self):
        pass




class Item(pygame.sprite.Sprite):

    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__( self )
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect_colision = self.rect.inflate(-30, -10)
        self.delay = 0
        self.se_puede_comer = True
        self.rect.topleft = pos
    
    def update(self):
        pass

    def update_desaparecer(self):
        self.delay -= 1
        if self.delay < 1:
            self.kill()


    def comer(self):
        self.delay = 30
        self.update = self.update_desaparecer
        self.se_puede_comer = False





class Mapa:
    def __init__(self, archivo): 

       
        self.grupo = pygame.sprite.RenderUpdates()
        self.items = pygame.sprite.RenderUpdates()

        self.h=pygame.image.load('h.png').convert_alpha()
        self.v=pygame.image.load('v.png').convert_alpha()
        self.sd=pygame.image.load('sd.png').convert_alpha()
        self.id=pygame.image.load('id.png').convert_alpha()
        self.ii=pygame.image.load('ii.png').convert_alpha()
        self.si=pygame.image.load('si.png').convert_alpha()
        self.q=pygame.image.load('Sprite/vida.png').convert_alpha() 
        self.a=pygame.image.load('Sprite/llave.png').convert_alpha()
        self.m=pygame.image.load('Sprite/medicina.png').convert_alpha() 
        self.p=pygame.image.load('Sprite/municion.png').convert_alpha()
        self.n=pygame.image.load('Sprite/municion2.png').convert_alpha()
        self.x=pygame.image.load('Sprite/municion3.png').convert_alpha()
        self.z=pygame.image.load('Sprite/polvora.png').convert_alpha()
        self.c=pygame.image.load('Sprite/prueba.png').convert_alpha()
        self.pr=pygame.image.load('Sprite/prueba2.png').convert_alpha()   
        
        
        
        
        archivo = open(archivo)
        self.textoMapa = archivo.readlines()
        archivo.close()
        
        
        fila = -1
        for linea in self.textoMapa:
            fila += 1
            columna = -1
            for c in linea:
                columna += 1
                
 
                
                x,y = self.aPixel(fila,columna)
                
            
                
                if c == '-':
                    self.grupo.add(Pared(self.h, (x,y)))
                elif c == '|':
                    self.grupo.add(Pared(self.v, (x,y)))
                elif c == '7':
                    self.grupo.add(Pared(self.sd, (x,y)))
                elif c == 'J':
                    self.grupo.add(Pared(self.id, (x,y)))
                elif c == 'L':
                    self.grupo.add(Pared(self.ii, (x,y)))
                elif c == 'T':
                    self.grupo.add(Pared(self.si, (x,y)))
                elif c == 'k':
                    self.items.add(Item(self.q, (x,y)))
                elif c == 'A':
                    self.items.add(Item(self.a, (x,y)))
                elif c == 'M':
                    self.items.add(Item(self.m, (x,y)))
                elif c == 'P':
                    self.items.add(Item(self.p, (x,y))) 
                elif c == 'N':
                    self.items.add(Item(self.n, (x,y))) 
                elif c == 'X':
                    self.items.add(Item(self.x, (x,y)))
                elif c == 'Z':
                    self.items.add(Item(self.z, (x,y)))
                elif c == 'C':
                    self.items.add(Item(self.c, (x,y)))
                elif c == 'U':
                    self.items.add(Item(self.pr, (x,y)))                            
              
 
    
    
    
    def actualizar(self, visor):
        screen.blit(fondo1,(0,0))
        self.grupo.update()
        self.grupo.draw(visor)
        self.items.update()
        self.items.draw(visor)

    
    def aPixel(self, fila, columna):
        return (columna*40, fila*40)
    

    
    def aCuadricula(self, x, y):
        return (y/40, x/40)
        




