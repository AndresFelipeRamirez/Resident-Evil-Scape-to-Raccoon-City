import pygame
from pygame.locals import *
import sys
import time
import random


pygame.init()


BLANCO = (255,255,255)
AMARILLO = (255,0,0)
tipoLetra = pygame.font.Font('Grandezza.ttf', 40)
tipoLetra2 = pygame.font.Font('Grandezza.ttf', 50)
imagenDeFondo = 'introduccion.jpg'

ancho=800
alto=600

inst1='inst1.png'
inst2='inst2.png'
pr1='pre1.jpg'
pr2='pre2.jpg'
pr3='pre3.jpg'
pr4='pre4.jpg'
pr5='pre5.jpg'
pr6='pre6.jpg'


visor = pygame.display.set_mode((800, 600))

def pausa():
   esperar = True
   while esperar:
      for evento in pygame.event.get():
          if evento.type == KEYDOWN:
              esperar = False  

def ins1():
    fondo =pygame.image.load(inst1).convert()
    visor.blit(fondo,(0,0))
    pygame.display.update()
    pausa()

def ins2():
    fondo =pygame.image.load(inst2).convert()
    visor.blit(fondo,(0,0))
    pygame.display.update()
    pausa()

        

	 	
def mostrarIntro():
   teclasPulsadas = pygame.key.get_pressed()
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Pulsa cualquier tecla para comenzar'
   texto = tipoLetra2.render(mensaje, True, AMARILLO)
   visor.blit(texto, (50,570,350,30))
   pygame.display.update()
   pausa()

def preludio():
    fondo1 =pygame.image.load(pr1).convert()
    
    fondo2 =pygame.image.load(pr2).convert()
    fondo3 =pygame.image.load(pr3).convert()
    fondo4 =pygame.image.load(pr4).convert()
    fondo5 =pygame.image.load(pr5).convert()
    fondo6 =pygame.image.load(pr6).convert()
   
    visor.blit(fondo1, (0,0))
    pygame.display.update()
    time.sleep(2)
    
    visor.blit(fondo2, (0,0))
    pygame.display.update()
    time.sleep(2)
    visor.blit(fondo3, (0,0))
    pygame.display.update()
    time.sleep(2)
    visor.blit(fondo4, (0,0))
    pygame.display.update()
    time.sleep(2)
    visor.blit(fondo5, (0,0))
    pygame.display.update()
    time.sleep(2)
    visor.blit(fondo6, (0,0))
    pygame.display.update()
    time.sleep(3)
   
    pygame.display.update()
    time.sleep(3)
    
    ins1()
    


pygame.mouse.set_visible(False)
mostrarIntro()
preludio()
time.sleep(0.75)

visor = pygame.display.set_mode((800, 600))
     
pygame.display.update()

  
