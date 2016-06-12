import pygame
from pygame.locals import *
import sys
import time
import mapa
#import q
import random


pygame.init()

BLANCO = (255,255,255)
AMARILLO = (255,0,0)
tipoLetra = pygame.font.Font('Grandezza.ttf', 40)
tipoLetra2 = pygame.font.Font('Grandezza.ttf', 50)
tipoLetra3 = pygame.font.Font('Grandezza.ttf', 100)
musica=pygame.mixer.Sound("Laber.ogg")
soundBonus=pygame.mixer.Sound("bonus.ogg")
gameoversound=pygame.mixer.Sound("gameover.ogg")
winnersouned=pygame.mixer.Sound("winner.ogg")
shootSound=pygame.mixer.Sound("shoot.ogg")
imagenDeFondo = 'introduccion.jpg'
imagenGameOver= 'GameOver.jpg'
explosion=pygame.mixer.Sound("explosion.ogg")
niv2=pygame.mixer.Sound("Level2.ogg")
presound=pygame.mixer.Sound("Intro.ogg")
imagenPerro = 'perro.png'


# Sprites del jugador:
#imagenJill = 'jill.png'
imagenItem = 'Sprite/vida.png'
ancho=800
alto=600
SegundoNivel='SegundoNivel.jpg'
inst1='inst1.png'
inst2='inst2.png'
pr1='pre1.jpg'
pr2='pre2.jpg'
pr3='pre3.jpg'
pr4='pre4.jpg'
pr5='pre5.jpg'
pr6='pre6.jpg'

pr7='a7.png'
pr8='a8.png'
pr9='a9.png'

vida1='vida1.png'
vida2='vida2.png'
vida3='vida3.png'
vida4='vida4.png'
ex3='blood.png'
visor = pygame.display.set_mode((800, 600))
global items
global sound
global vida
vida=4
items=0
sound= True

class bloque(pygame.sprite.Sprite):

		def __init__(self,archivo):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load(archivo).convert_alpha()
			self.rect=self.image.get_rect()

		def reini_pos(self):
			self.rect.y=random.randrange(-500,-20)
			self.rect.x=random.randrange(0,ancho)

		def update(self):
			self.rect.y +=1
			if self.rect.y >810:
			   self.reini_pos()


class zombiae(pygame.sprite.Sprite):
	def __init__(self,archivo):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(archivo).convert_alpha()
		self.rect=self.image.get_rect()
		self.movimiento = ["zc/zc0.png", "zc/zc1.png", "zc/zc2.png"]
		self.cont_mov = 0

	def reini_pos(self):
		self.rect.y=random.randrange(-2000,-20)
		self.rect.x=random.randrange(0,ancho)

	def update(self):
		if not(self.cont_mov == 3):
				self.image = pygame.image.load(self.movimiento[self.cont_mov])
				self.cont_mov += 1
		else:
				self.cont_mov = 0

		self.rect.y +=1
		if self.rect.y >810:
			self.reini_pos()


class jugador(pygame.sprite.Sprite):

                def __init__(self,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()
                        self.vidas=4

                def reini_pos(self):
                        self.rect.y=550
                        self.rect.x=500

                def pos(self):
                    self.rect.y=500
                    self.rect.x=550

class item(pygame.sprite.Sprite):

                def __init__(self,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()

                def reini_pos(self):
                        self.rect.y=random.randrange(-1000,-800)
                        self.rect.x=random.randrange(0,ancho)

                def update(self):
                        self.rect.y +=1
                        if self.rect.y >5000:
                            self.reini_pos()

class bala(pygame.sprite.Sprite):

                var_y=9

                def __init__(self,x,y,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()
                        self.rect.y += y
                        self.rect.x += x

                def update(self):
                        if (self.rect.top>-50):
                                self.rect.y -= self.var_y
                        else:
                                self.rect.top= -50


#nemesis

class nemesis( pygame.sprite.Sprite ):
	def __init__( self, posX, posY ):
		pygame.sprite.Sprite.__init__( self )
		self.image = pygame.image.load('nemesis/nemesis1.png')
		#self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.topleft = (posX, posY)
		self.vida = 100 #10
		self.aparecer = False # Aparece nemesis
		self.victoria = False # VICTORIA DEL JUEGO
		self.sentido = 0
		self.derrota = False # Si nemesis llega a abajo

		self.cont_animacion = 0
		self.abajo = ['nemesis/nemesis1.png', 'nemesis/nemesis2.png', 'nemesis/nemesis3.png', 'nemesis/nemesis4.png']

	def update(self):
		if self.aparecer:
			if self.rect.y >= 600 - 77:
				puntzombi()
			if self.rect.topleft[0] <= 0:
				self.sentido = 0
				self.rect.y += 10
			if self.rect.topleft[0] >= (800 - self.rect[2]):
				self.sentido = 1
				self.rect.y += 10

			if self.sentido == 0:
				self.rect.x += 3
				#self.rect.y += 1
			else:
				self.rect.x -= 3
				#self.rect.y += 1
			if not(self.cont_animacion == 4):
				self.image = pygame.image.load(self.abajo[self.cont_animacion])
				#self.rect = self.image.get_rect()
				self.cont_animacion += 1
			else:
				self.cont_animacion = 0


		#print self.pos
		#self.pos = self.rect.topleft

	def deshacer(self):
		self.rect.topleft = self.pos
		visor = pygame.display.set_mode((800, 600))
		pygame.display.set_caption('Resident Evil')

nemesis = nemesis(0,-77)

bl=pygame.sprite.Group()
tl=pygame.sprite.Group()
al=pygame.sprite.Group()
nl=pygame.sprite.Group()
#nemesis=jugador("nemesis/nemesis1.png")
jugl2=jugador("SpriteJill/Jill10.png")
modi=pygame.sprite.Group()
tl.add(jugl2)

nemesisGroup = pygame.sprite.Group()
tl.add(nemesis)

#ll=pygame.sprite.Group()

for i in range (10):
	b=bloque("Sprite/vida.png")
	b.rect.x= random.randint(10,ancho)
	b.rect.y= random.randint(-500,0)
	bl.add(b)
	tl.add(b)

for i in range (3):
        bonus=item("item.png")
        bonus.rect.x= random.randint(10,ancho)
        bonus.rect.y= random.randint(-500,0)
        modi.add(bonus)
        tl.add(bonus)


for i in range (30):
        a=zombiae("zombia.png")
        a.rect.x=random.randint(10,ancho)
        a.rect.y=random.randint(-1000,-400)
        al.add(a)
        tl.add(a)


callelvl2= 'callelvl2.png'


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





def fondojugl2():
   mega_x=500
   mega_y=550
   modificador=0
   global vida
   global items
   global sound
   vel=1
   laser= bala(-10,-10,"laser.png")
   laser2=bala(-10,-10,"laser.png")
   tl.add(laser)
   tl.add(laser2)
   f3=pygame.image.load(ex3)
   v1=pygame.image.load(vida1).convert()
   v2=pygame.image.load(vida2).convert()
   v3=pygame.image.load(vida3).convert()
   v4=pygame.image.load(vida4).convert()
   puntosjugl2=0
   fondo = pygame.image.load(callelvl2).convert()
#   jugl2=pygame.image.load(mega).convert()
   visor.blit(fondo,(0,0))
#   visor.blit(jugl2,(mega_x,mega_y))
   jugl2.rect.x=mega_x
   jugl2.rect.y=mega_y
   vector_balas = []
   tl.update()
   pygame.display.update()
   l_existe=False
   fin =False
   while not fin:
      for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               if sound == True:
                   shootSound.play()
               laser= bala(-10,-10,"laser.png")
               laser2=bala(-10,-10,"laser.png")
               vector_balas.append(laser)
               vector_balas.append(laser2)
               print "Cantidad de balas: ", len(vector_balas)
               tl.add(laser)
               tl.add(laser2)
               if modificador==1 or modificador==2 or modificador == 3:
                   laser2.rect.x=jugl2.rect.x-10
                   laser2.rect.y=jugl2.rect.y-20
                   laser.rect.x=jugl2.rect.x+25
                   laser.rect.y=jugl2.rect.y-20
               if modificador==0:
                   laser2.rect.x=-20
                   laser2.rect.y=-20
                   laser.rect.x=jugl2.rect.x+11
                   laser.rect.y=jugl2.rect.y-20
               l_existe=True

               if laser.rect.y == 0:
                   laser.rect.x = -20
               if laser2.rect.y == 0:
                   laser2.rect.x = -20


      keys= pygame.key.get_pressed()
      if keys[K_LEFT]:
          jugl2.rect.x = jugl2.rect.x - vel - 5
          if jugl2.rect.x <= (-60 ):
            jugl2.rect.x=ancho
      if keys[K_RIGHT]:
            jugl2.rect.x=jugl2.rect.x+ vel +5
            if jugl2.rect.x >= (ancho ):
               jugl2.rect.x=-60
      if keys[K_p]:
          tempx=jugl2.rect.x
          tempy=jugl2.rect.y
          jugl2.rect.x=-10
          jugl2.rect.x=-10
          pausar()
          jugl2.rect.x=tempx
          jugl2.rect.x=tempy

      if keys[K_u]and sound==True:
         sound= False
         niv2.stop()


      if keys[K_i]and sound==False:
         sound= True
         niv2.play()
	  # IMPACTO A NEMESIS
      posicion_impactox = nemesis.rect.x, nemesis.rect.x+60
      posicion_impactoy = nemesis.rect.y, nemesis.rect.y-77
      for bala_impacto in vector_balas:
		  if bala_impacto.rect.x >= posicion_impactox[0] and bala_impacto.rect.x <= posicion_impactox[1]:
			  if bala_impacto.rect.y <= posicion_impactoy[0] and bala_impacto.rect.y >= posicion_impactoy[1]:
				  vector_balas.remove(bala_impacto)
				  if not(nemesis.vida == 0):
				  	nemesis.vida -= 1
					print "VIDA: {0}".format(nemesis.vida)
				  else:
					print "GANASTE"
					nemesis.victoria = True


      #impactos_Nemesis = pygame.sprite.spritecollide(nemesis, tl, True)#laser, nemesisGroup, True)
      #for imp in impactos_Nemesis:
		#  print "si"



      lg= pygame.sprite.spritecollide(laser,al,True)
      for b in lg:
         if sound == True:
             explosion.play()
         visor.blit(f3,(b.rect.x,b.rect.y))
         pygame.display.update()
         time.sleep(0.08)
         b.reini_pos()
         laser.rect.x=-1000
         laser.rect.y=-1000
         laser2.rect.x=-1000
         laser2.rect.y=-1000


      lg2= pygame.sprite.spritecollide(laser2,al,True)
      for b in lg2:
         if sound == True:
             explosion.play()
         visor.blit(f3,(b.rect.x,b.rect.y))
         pygame.display.update()
         time.sleep(0.08)
         b.reini_pos()
         laser2.rect.x=-1000
         laser2.rect.y=-1000
         laser.rect.x=-1000
         laser.rect.y=-1000

      if vida==4:
          visor.blit(v4,(5,5))
          pygame.display.update()

      if vida==3:
          visor.blit(v3,(5,5))
          pygame.display.update()

      if vida==2:
          visor.blit(v2,(5,5))
          pygame.display.update()

      if vida==1:
          visor.blit(v1,(5,5))
          pygame.display.update()

      ag=pygame.sprite.spritecollide(jugl2,bl,True)
      for a in ag:
          puntosjugl2 +=1
          a.reini_pos()

      mo=pygame.sprite.spritecollide(jugl2,modi,True)
      for bonus in mo:
          modificador +=1
          if modificador==2:
                vel=vel+1
          if modificador ==3:
                vida= vida+1
          bonus.reini_pos()

      ty= pygame.sprite.spritecollide(jugl2,al,True)
      for a in ty:
         vida=vida-1
         if sound == True:
             explosion.play()
         visor.blit(f3,(jugl2.rect.x,550))
         pygame.display.update()
         time.sleep(0.08)
         if vida == 0:
              puntzombi()
         a.reini_pos()

      visor.blit(fondo,(0,0))
#      visor.blit(jugl2,(mega_x,mega_y))
      tl.update()
      tl.draw(visor)
     # if l_existe:
      #   laser.rect.y=laser.rect.y-4
       #  laser2.rect.y=laser.rect.y-4

      pygame.display.flip()
      #print " NEMESIS VICTORIA: ", nemesis.victoria
	  # CUANDO GANA:
      if puntosjugl2 == 10:
          items= items+puntosjugl2
          pygame.display.update
          puntosjugl2=0
          nemesis.aparecer = True
      elif nemesis.victoria:
		  puntjugador()
		  pygame.quit()
		  sys.exit()


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
    '''
    fondo2 =pygame.image.load(pr2).convert()
    fondo3 =pygame.image.load(pr3).convert()
    fondo4 =pygame.image.load(pr4).convert()
    fondo5 =pygame.image.load(pr5).convert()
    fondo6 =pygame.image.load(pr6).convert()
    '''
    '''
    fondo7 =pygame.image.load(pr7).convert()
    fondo8 =pygame.image.load(pr8).convert()
    fondo9 =pygame.image.load(pr9).convert()
    '''
    presound.play()
    visor.blit(fondo1, (0,0))
    pygame.display.update()
    time.sleep(1)
    '''
    visor.blit(fondo2, (0,0))
    pygame.display.update()
    time.sleep(1)

    visor.blit(fondo3, (0,0))
    pygame.display.update()
    time.sleep(1)
    visor.blit(fondo4, (0,0))
    pygame.display.update()
    time.sleep(1)
    visor.blit(fondo5, (0,0))
    pygame.display.update()
    time.sleep(1)
    visor.blit(fondo6, (0,0))
    pygame.display.update()
    time.sleep(1)
    '''
    '''
    visor.blit(fondo7, (0,0))
    pygame.display.update()
    time.sleep(6)
    visor.blit(fondo8, (0,0))
    pygame.display.update()
    time.sleep(6)
    presound.stop()
    visor.blit(fondo9, (0,0))
    '''
    pygame.display.update()
    time.sleep(2)
    '''
    ins1()
    '''


pygame.mouse.set_visible(False)
mostrarIntro()
preludio()
time.sleep(0.75)
musica.play()



def mostrarlvl2():
    global lvl
    lvl=2
    fondo = pygame.image.load(SegundoNivel).convert()
    visor.blit(fondo,(0,0))
    mensaje= 'Nivel 2'
    mensaje2='Pulsa una tecla para comenzar'
    texto1=tipoLetra.render(mensaje, True, AMARILLO)
    texto2=tipoLetra.render(mensaje2, True, BLANCO)
    visor.blit(texto1, (280,50,350,30))
    visor.blit(texto2, (20,550,350,30))
    pygame.display.update()
    pausa()
    ins2()
    niv2.play()


def puntzombi():
   fondo = pygame.image.load(imagenGameOver).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Game Over'
   texto = tipoLetra3.render(mensaje, True, AMARILLO)
   visor.blit(texto, (190,450,350,30))
   pygame.display.update()
   musica.stop()
   niv2.stop()
   if sound == True:
       gameoversound.play()
   pausa()
   pygame.quit()
   sys.exit()

def pausar():
   global sound
   teclasPulsadas = pygame.key.get_pressed()
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje1='Activar sonido ( i )'
   mensaje2='Desactivar sonido ( u )'
   texto1=tipoLetra2.render(mensaje1,True,AMARILLO)
   texto2=tipoLetra2.render(mensaje2, True, AMARILLO)
   visor.blit(texto2, (150,500,350,30))
   visor.blit(texto1,(190,550,350,30))
   pygame.display.update()
   pausa()


llaveflag = 0

def puntjugador():
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Puntaje'
   puntaje = str(items + 1)
	# CARGAR OTRA FUENTEEEEEEEEEEEEE
   texto = tipoLetra.render(mensaje, True, AMARILLO)
   texto1 = tipoLetra.render(puntaje, True, AMARILLO)
   musica.stop()
   niv2.stop()
   if sound == True:
       winnersouned.play()
   print "MENSAJE {0} PUNTAJE: {1}".format(mensaje, puntaje)
   visor.blit(texto, (60,550,350,30))
   visor.blit(texto1, (280,550,350,30))
   pygame.display.flip()
   pausa()


class imagenJill( pygame.sprite.Sprite ):
	def __init__( self, posX, posY ):
		pygame.sprite.Sprite.__init__( self )
		self.image = pygame.image.load('SpriteJill/Jill0.png')
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.topleft = (posX, posY)
		self.dy = 0
		self.dx = 0
		self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
		self.mleft, self.mrigth, self.up, self.down = True, True, True, True
		self.izquierda = ['SpriteJill/Jill3.png', 'SpriteJill/Jill4.png', 'SpriteJill/Jill5.png']
		self.derecha = ['SpriteJill/Jill6.png', 'SpriteJill/Jill7.png', 'SpriteJill/Jill8.png']
		self.abajo = ['SpriteJill/Jill0.png', 'SpriteJill/Jill1.png', 'SpriteJill/Jill2.png']
		self.arriba = ['SpriteJill/Jill9.png', 'SpriteJill/Jill10.png', 'SpriteJill/Jill11.png']
	def update(self):
		self.pos = self.rect.topleft
		self.rect.move_ip(self.dx,self.dy)
	def deshacer(self):
		self.rect.topleft = self.pos

#camina en circulos
class imagenPerro( pygame.sprite.Sprite ):
	def __init__( self, posX, posY ):
		pygame.sprite.Sprite.__init__( self )
		self.image = pygame.image.load('perro.png')
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		self.rect.topleft = (posX, posY)
		self.dy = 0
		self.dx = 0
		self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
		self.mleft, self.mrigth, self.up, self.down = True, True, True, True
		self.izquierda = ['PerroZombi/zombiedog4.png', 'PerroZombi/zombiedog5.png', 'PerroZombi/zombiedog6.png', 'PerroZombi/zombiedog7.png']
		self.derecha = ['PerroZombi/zombiedog8.png', 'PerroZombi/zombiedog9.png', 'PerroZombi/zombiedog10.png', 'PerroZombi/zombiedog11.png']
		self.abajo = ['PerroZombi/zombiedog0.png', 'PerroZombi/zombiedog1.png', 'PerroZombi/zombiedog2.png', 'PerroZombi/zombiedog3.png']
		self.arriba = ['PerroZombi/zombiedog12.png', 'PerroZombi/zombiedog13.png', 'PerroZombi/zombiedog14.png', 'PerroZombi/zombiedog15.png']

	def update(self):
		self.pos = self.rect.topleft
		self.rect.move_ip(self.dx,self.dy)

	def deshacer(self):
		self.rect.topleft = self.pos


visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Resident Evil')

#camino normal con movimiento
class imagenPerro2( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('perro.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.topleft = (posX, posY)

        self.dy = 0
        self.dx = 0
        self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
        self.mleft, self.mrigth, self.up, self.down = True, True, True, True
        self.izquierda = ['PerroZombi/zombiedog4.png', 'PerroZombi/zombiedog5.png', 'PerroZombi/zombiedog6.png', 'PerroZombi/zombiedog7.png']
        self.derecha = ['PerroZombi/zombiedog8.png', 'PerroZombi/zombiedog9.png', 'PerroZombi/zombiedog10.png', 'PerroZombi/zombiedog11.png']
        self.abajo = ['PerroZombi/zombiedog0.png', 'PerroZombi/zombiedog1.png', 'PerroZombi/zombiedog2.png', 'PerroZombi/zombiedog3.png']
        self.arriba = ['PerroZombi/zombiedog12.png', 'PerroZombi/zombiedog13.png', 'PerroZombi/zombiedog14.png', 'PerroZombi/zombiedog15.png']

    def update(self):

        self.pos = self.rect.topleft

        self.rect.move_ip(self.dx,self.dy)

    def deshacer(self):

        self.rect.topleft = self.pos




visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Resident Evil')

#camina normal con movimiento alterado
class imagenPerro3( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('perro.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.topleft = (posX, posY)

        self.dy = 0
        self.dx = 0
        self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
        self.mleft, self.mrigth, self.up, self.down = True, True, True, True
        self.izquierda = ['PerroZombi/zombiedog4.png', 'PerroZombi/zombiedog5.png', 'PerroZombi/zombiedog6.png', 'PerroZombi/zombiedog7.png']
        self.derecha = ['PerroZombi/zombiedog8.png', 'PerroZombi/zombiedog9.png', 'PerroZombi/zombiedog10.png', 'PerroZombi/zombiedog11.png']
        self.abajo = ['PerroZombi/zombiedog0.png', 'PerroZombi/zombiedog1.png', 'PerroZombi/zombiedog2.png', 'PerroZombi/zombiedog3.png']
        self.arriba = ['PerroZombi/zombiedog12.png', 'PerroZombi/zombiedog13.png', 'PerroZombi/zombiedog14.png', 'PerroZombi/zombiedog15.png']

    def update(self):

        self.pos = self.rect.topleft

        self.rect.move_ip(self.dx,self.dy)

    def deshacer(self):

        self.rect.topleft = self.pos




visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Resident Evil')

class imagenRata( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('Rata/rata9.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.topleft = (posX, posY)

        self.dy = 0
        self.dx = 0

        self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
        self.mleft, self.mrigth, self.up, self.down = True, True, True, True
        self.izquierda = ['Rata/rata3.png', 'Rata/rata4.png', 'Rata/rata5.png']
        self.derecha = ['Rata/rata6.png', 'Rata/rata7.png', 'Rata/rata8.png']
        self.abajo = ['Rata/rata0.png', 'Rata/rata1.png', 'Rata/rata2.png']
        self.arriba = ['Rata/rata9.png', 'Rata/rata10.png', 'Rata/rata11.png']

    def update(self):

        self.pos = self.rect.topleft

        self.rect.move_ip(self.dx,self.dy)

    def deshacer(self):

        self.rect.topleft = self.pos




visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Resident Evil')


class imagenRata1( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('Rata/rata0.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.topleft = (posX, posY)

        self.dy = 0
        self.dx = 0

        self.contizq, self.contder, self.contup, self.contdown = 0, 0, 0, 0
        self.mleft, self.mrigth, self.up, self.down = True, True, True, True
        self.izquierda = ['Rata/rata3.png', 'Rata/rata4.png', 'Rata/rata5.png']
        self.derecha = ['Rata/rata6.png', 'Rata/rata7.png', 'Rata/rata8.png']
        self.abajo = ['Rata/rata0.png', 'Rata/rata1.png', 'Rata/rata2.png']
        self.arriba = ['Rata/rata9.png', 'Rata/rata10.png', 'Rata/rata11.png']

    def update(self):

        self.pos = self.rect.topleft

        self.rect.move_ip(self.dx,self.dy)

    def deshacer(self):

        self.rect.topleft = self.pos




visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Resident Evil')



imagenJill = imagenJill(150,500)
imagenPerro= imagenPerro(50,500)
imagenPerro2= imagenPerro2(50,300)
imagenPerro3 = imagenPerro3(50,300)
imagenRata = imagenRata(144,239)
imagenRata1= imagenRata1(246,116)

grupoimagenJill = pygame.sprite.RenderUpdates(imagenJill)
grupoimagenPerro = pygame.sprite.RenderUpdates(imagenPerro)
grupoimagenPerro2 = pygame.sprite.RenderUpdates(imagenPerro2)
grupoimagenPerro3 = pygame.sprite.RenderUpdates(imagenPerro3)
grupoimagenRata = pygame.sprite.RenderUpdates(imagenRata)
grupoimagenRata1 = pygame.sprite.RenderUpdates(imagenRata1)


nivel = mapa.Mapa('mapa.txt')

reloj = pygame.time.Clock()


#movimientos nivel 1

while True:

    reloj.tick(60)



    for evento in pygame.event.get():
        if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
            pygame.quit()
            sys.exit()



    if imagenPerro.rect.right > 800:
        puntzombi()
        pygame.quit()
        sys.exit()


    teclasPulsadas = pygame.key.get_pressed()


    if imagenPerro.rect.top > 40 and imagenPerro.rect.left < 50:
		imagenPerro.image = pygame.image.load(imagenPerro.arriba[imagenPerro.contup])
		imagenPerro.dy=-3
		imagenPerro.dx=0
		imagenPerro.contup += 1
		if imagenPerro.contup == 4:
			imagenPerro.contup = 0
    elif imagenPerro.rect.left <710 and imagenPerro.rect.top <50:
		imagenPerro.image = pygame.image.load(imagenPerro.derecha[imagenPerro.contder])
		imagenPerro.dx=3
		imagenPerro.dy=0
		imagenPerro.contder += 1
		if imagenPerro.contder == 4:
			imagenPerro.contder = 0
    elif imagenPerro.rect.top < 520:
		imagenPerro.image = pygame.image.load(imagenPerro.abajo[imagenPerro.contdown])
		imagenPerro.dy=3
		imagenPerro.dx=0
		imagenPerro.contdown += 1
		if imagenPerro.contdown == 4:
			imagenPerro.contdown = 0
    else:
		imagenPerro.image = pygame.image.load(imagenPerro.izquierda[imagenPerro.contizq])
		imagenPerro.dy=0
		imagenPerro.dx=-3
		imagenPerro.contizq += 1
		if imagenPerro.contizq == 4:
			imagenPerro.contizq = 0

    if imagenPerro.rect.top >249 and imagenPerro.rect.left > 200 and imagenPerro.rect.left < 330 and imagenPerro.rect.top <390  :
		imagenPerro.image = pygame.image.load(imagenPerro.abajo[imagenPerro.contdown])
		imagenPerro.dy=3
		imagenPerro.dx=0
		imagenPerro.contdown += 1
		if imagenPerro.contdown == 4:
			imagenPerro.contdown = 0
    elif imagenPerro.rect.top < 400 and imagenPerro.rect.left > 150 and imagenPerro.rect.top > 340 and imagenPerro.rect.left < 700:
		imagenPerro.image = pygame.image.load(imagenPerro.derecha[imagenPerro.contder])
		imagenPerro.dy=0
		imagenPerro.dx=3
		imagenPerro.contder += 1
		if imagenPerro.contder == 4:
			imagenPerro.contder = 0
    elif imagenPerro.rect.top < 470 and imagenPerro.rect.top > 339 and imagenPerro.rect.left > 201  :
		imagenPerro.image = pygame.image.load(imagenPerro.abajo[imagenPerro.contdown])
		imagenPerro.dy=3
		imagenPerro.dx=0
		imagenPerro.contdown += 1
		if imagenPerro.contdown == 4:
			imagenPerro.contdown = 0






    if imagenPerro2.rect.right > 800:
        puntzombi()
        pygame.quit()
        sys.exit()


    teclasPulsadas = pygame.key.get_pressed()



    if imagenPerro2.rect.top > 40 and imagenPerro2.rect.left < 50:
		imagenPerro2.image = pygame.image.load(imagenPerro2.arriba[imagenPerro2.contup])
		imagenPerro2.dy=-2
		imagenPerro2.dx=0
		imagenPerro2.contup += 1
		if imagenPerro2.contup == 4:
			imagenPerro2.contup = 0
    elif imagenPerro2.rect.left <500 and imagenPerro2.rect.top <50:
		imagenPerro2.image = pygame.image.load(imagenPerro2.derecha[imagenPerro2.contder])
		imagenPerro2.dx=2
		imagenPerro2.dy=0
		imagenPerro2.contder += 1
		if imagenPerro2.contder == 4:
			imagenPerro2.contder = 0
    elif imagenPerro2.rect.top < 250:
		imagenPerro2.image = pygame.image.load(imagenPerro2.abajo[imagenPerro2.contdown])
		imagenPerro2.dy=2
		imagenPerro2.dx=0
		imagenPerro2.contdown += 1
		if imagenPerro2.contdown == 4:
			imagenPerro2.contdown = 0
    else:
		imagenPerro2.image = pygame.image.load(imagenPerro2.izquierda[imagenPerro2.contizq])
		imagenPerro2.dy=0
		imagenPerro2.dx=-2
		imagenPerro2.contizq += 1
		if imagenPerro2.contizq == 4:
			imagenPerro2.contizq = 0

    if imagenPerro2.rect.top >249 and imagenPerro2.rect.left > 200 and imagenPerro2.rect.left < 330 and imagenPerro2.rect.top <390  :
		imagenPerro2.image = pygame.image.load(imagenPerro2.abajo[imagenPerro2.contdown])
		imagenPerro2.dy=2
		imagenPerro2.dx=0
		imagenPerro2.contdown += 1
		if imagenPerro2.contdown == 4:
			imagenPerro2.contdown = 0
    elif imagenPerro2.rect.top < 400 and imagenPerro2.rect.left > 150 and imagenPerro2.rect.top > 340 and imagenPerro2.rect.left < 700:
		imagenPerro2.image = pygame.image.load(imagenPerro2.derecha[imagenPerro2.contder])
		imagenPerro2.dy=0
		imagenPerro2.dx=2
		imagenPerro2.contder += 1
		if imagenPerro2.contder == 4:
			imagenPerro2.contder = 0
    elif imagenPerro2.rect.top < 470 and imagenPerro2.rect.top > 339 and imagenPerro2.rect.left > 201  :
		imagenPerro2.image = pygame.image.load(imagenPerro2.abajo[imagenPerro2.contdown])
		imagenPerro2.dy=2
		imagenPerro2.dx=0
		imagenPerro2.contdown += 1
		if imagenPerro2.contdown == 4:
			imagenPerro2.contdown = 0



    if imagenPerro3.rect.right > 800:
        puntzombi()
        pygame.quit()
        sys.exit()


    teclasPulsadas = pygame.key.get_pressed()



    if imagenPerro3.rect.top > 45 and imagenPerro3.rect.left < 55:
      imagenPerro3.image = pygame.image.load(imagenPerro3.arriba[imagenPerro3.contup])
      imagenPerro3.dy=-1
      imagenPerro3.dx=0
      imagenPerro3.contup += 1
      if imagenPerro3.contup == 4:
        imagenPerro3.contup = 0
    elif imagenPerro3.rect.left <505 and imagenPerro3.rect.top <55:
		imagenPerro3.image = pygame.image.load(imagenPerro3.derecha[imagenPerro3.contder])
		imagenPerro3.dx=1
		imagenPerro3.dy=0
		imagenPerro3.contder += 1
		if imagenPerro3.contder == 4:
			imagenPerro3.contder = 0
    elif imagenPerro3.rect.top < 255:
		imagenPerro3.image = pygame.image.load(imagenPerro3.abajo[imagenPerro3.contdown])
		imagenPerro3.dy=1
		imagenPerro3.dx=0
		imagenPerro3.contdown += 1
		if imagenPerro3.contdown == 4:
			imagenPerro3.contdown = 0
    else:
		imagenPerro3.image = pygame.image.load(imagenPerro3.izquierda[imagenPerro3.contizq])
		imagenPerro3.dy=0
		imagenPerro3.dx=-1
		imagenPerro3.contizq += 1
		if imagenPerro3.contizq == 4:
			imagenPerro3.contizq = 0

    if imagenPerro3.rect.top >254 and imagenPerro3.rect.left > 204 and imagenPerro3.rect.left < 334 and imagenPerro3.rect.top <394  :
		imagenPerro3.image = pygame.image.load(imagenPerro3.abajo[imagenPerro3.contdown])
		imagenPerro3.dy=1
		imagenPerro3.dx=0
		imagenPerro3.contdown += 1
		if imagenPerro3.contdown == 4:
			imagenPerro3.contdown = 0
    elif imagenPerro3.rect.top < 404 and imagenPerro3.rect.left > 154 and imagenPerro3.rect.top > 344 and imagenPerro3.rect.left < 704:
		imagenPerro3.image = pygame.image.load(imagenPerro3.derecha[imagenPerro3.contder])
		imagenPerro3.dy=0
		imagenPerro3.dx=1
		imagenPerro3.contder += 1
		if imagenPerro3.contder == 4:
			imagenPerro3.contder = 0
    elif imagenPerro3.rect.top < 474 and imagenPerro3.rect.top > 344 and imagenPerro3.rect.left > 206:
		imagenPerro3.image = pygame.image.load(imagenPerro3.abajo[imagenPerro3.contdown])
		imagenPerro3.dy=1
		imagenPerro3.dx=0
		imagenPerro3.contdown += 1
		if imagenPerro3.contdown == 4:
			imagenPerro3.contdown = 0


    if imagenRata.rect.right > 800:
        puntzombi()
        pygame.quit()
        sys.exit()


    teclasPulsadas = pygame.key.get_pressed()


    if imagenRata.rect.top > 100 and imagenRata.rect.left < 144:
        imagenRata.image = pygame.image.load(imagenRata.arriba[imagenRata.contup])
        imagenRata.dy=-1
        imagenRata.dx=0
        imagenRata.contup += 1
        if imagenRata.contup == 3:
          imagenRata.contup = 0

    elif imagenRata.rect.left <255 and imagenRata.rect.top <116:
      imagenRata.image = pygame.image.load(imagenRata.derecha[imagenRata.contder])
      imagenRata.dx=1
      imagenRata.dy=0
      imagenRata.contder += 1
      if imagenRata.contder == 3:
        imagenRata.contder = 0

    elif imagenRata.rect.top < 250:
      imagenRata.image = pygame.image.load(imagenRata.abajo[imagenRata.contdown])
      imagenRata.dy=1
      imagenRata.dx=0
      imagenRata.contdown += 1
      if imagenRata.contdown == 3:
        imagenRata.contdown = 0
    else:
      imagenRata.image = pygame.image.load(imagenRata.izquierda[imagenRata.contizq])
      imagenRata.dy=0
      imagenRata.dx=-1
      imagenRata.contizq += 1
      if imagenRata.contizq == 3:
        imagenRata.contizq = 0

    if imagenRata.rect.top >250 and imagenRata.rect.left > 200 and imagenRata.rect.left < 330 and imagenRata.rect.top <390:
      imagenRata.image = pygame.image.load(imagenRata.abajo[imagenRata.contdown])
      imagenRata.dy=1
      imagenRata.dx=0
      imagenRata.contdown += 1
      if imagenRata.contdown == 3:
        imagenRata.contdown = 0
    elif imagenRata.rect.top < 400 and imagenRata.rect.left > 150 and imagenRata.rect.top > 340 and imagenRata.rect.left < 700:
      imagenRata.image = pygame.image.load(imagenRata.derecha[imagenRata.contder])
      imagenRata.dy=0
      imagenRata.dx=1
      imagenRata.contder += 1
      if imagenRata.contder == 3:
        imagenRata.contder = 0
    elif imagenRata.rect.top < 470 and imagenRata.rect.top > 339 and imagenRata.rect.left > 201:
      imagenRata.image = pygame.image.load(imagenRata.abajo[imagenRata.contdown])
      imagenRata.dy=1
      imagenRata.dx=0
      imagenRata.contdown += 1
      if imagenRata.contdown == 3:
        imagenRata.contdown = 0


    if imagenRata1.rect.right > 800:
        puntzombi()
        pygame.quit()
        sys.exit()


    teclasPulsadas = pygame.key.get_pressed()


    if imagenRata1.rect.top > 100 and imagenRata1.rect.left < 144:
        imagenRata1.image = pygame.image.load(imagenRata1.arriba[imagenRata1.contup])
        imagenRata1.dy=-1
        imagenRata1.dx=0
        imagenRata1.contup += 1
        if imagenRata1.contup == 3:
          imagenRata1.contup = 0

    elif imagenRata1.rect.left <255 and imagenRata1.rect.top <116:
      imagenRata1.image = pygame.image.load(imagenRata1.derecha[imagenRata1.contder])
      imagenRata1.dx=1
      imagenRata1.dy=0
      imagenRata1.contder += 1
      if imagenRata1.contder == 3:
        imagenRata1.contder = 0

    elif imagenRata1.rect.top < 250:
      imagenRata1.image = pygame.image.load(imagenRata1.abajo[imagenRata1.contdown])
      imagenRata1.dy=1
      imagenRata1.dx=0
      imagenRata1.contdown += 1
      if imagenRata1.contdown == 3:
        imagenRata1.contdown = 0
    else:
      imagenRata1.image = pygame.image.load(imagenRata1.izquierda[imagenRata1.contizq])
      imagenRata1.dy=0
      imagenRata1.dx=-1
      imagenRata1.contizq += 1
      if imagenRata1.contizq == 3:
        imagenRata1.contizq = 0

    if imagenRata1.rect.top >250 and imagenRata1.rect.left > 200 and imagenRata1.rect.left < 330 and imagenRata1.rect.top <700:
      imagenRata1.image = pygame.image.load(imagenRata1.abajo[imagenRata1.contdown])
      imagenRata1.dy=1
      imagenRata1.dx=0
      imagenRata1.contdown += 1
      if imagenRata1.contdown == 3:
        imagenRata1.contdown = 0
    elif imagenRata1.rect.top < 400 and imagenRata1.rect.left > 150 and imagenRata1.rect.top > 340 and imagenRata1.rect.left < 700:
      imagenRata1.image = pygame.image.load(imagenRata1.derecha[imagenRata1.contder])
      imagenRata1.dy=0
      imagenRata1.dx=1
      imagenRata1.contder += 1
      if imagenRata1.contder == 3:
        imagenRata1.contder = 0
    elif imagenRata1.rect.top < 470 and imagenRata1.rect.top > 339 and imagenRata1.rect.left > 201:
      imagenRata1.image = pygame.image.load(imagenRata1.abajo[imagenRata1.contdown])
      imagenRata1.dy=1
      imagenRata1.dx=0
      imagenRata1.contdown += 1
      if imagenRata1.contdown == 3:
        imagenRata1.contdown = 0



    if imagenJill.rect.right > 800:
      puntjugador()
      mostrarlvl2()
      fondojugl2()



    teclasPulsadas = pygame.key.get_pressed()



    if teclasPulsadas[K_LEFT]:
		imagenJill.image = pygame.image.load(imagenJill.izquierda[imagenJill.contizq])
		imagenJill.dx = -3
		imagenJill.contizq += 1
		if imagenJill.contizq == 3:
			imagenJill.contizq = 0

    elif teclasPulsadas[K_RIGHT]:
		imagenJill.image = pygame.image.load(imagenJill.derecha[imagenJill.contder])
		imagenJill.dx = 3
		imagenJill.contder += 1
		if imagenJill.contder == 3:
			imagenJill.contder = 0
    else:
        imagenJill.dx = 0

	llaveflag = 1
    if imagenJill.rect.right > 780 and llaveflag == 1:
        puntjugador()
        mostrarlvl2()
        fondojugl2()

    elif imagenJill.rect.right > 780 :
      imagenJill.image = pygame.image.load(imagenJill.izquierda[imagenJill.contizq])
      imagenJill.dx = -3
      imagenJill.contizq += 1
      if imagenJill.contizq == 3:
        imagenJill.contizq = 0

    if teclasPulsadas[K_UP]:
		imagenJill.image = pygame.image.load(imagenJill.arriba[imagenJill.contup])
		imagenJill.dy = -3
		imagenJill.contup += 1
		if imagenJill.contup == 3:
			imagenJill.contup = 0
    elif teclasPulsadas[K_DOWN]:
		imagenJill.image = pygame.image.load(imagenJill.abajo[imagenJill.contdown])
		imagenJill.dy = 3
		imagenJill.contdown += 1
		if imagenJill.contdown == 3:
			imagenJill.contdown = 0
    else:
        imagenJill.dy = 0



    grupoimagenJill.update()
    grupoimagenPerro.update()
    grupoimagenPerro2.update()
    grupoimagenPerro3.update()
    grupoimagenRata.update()
    grupoimagenRata1.update()



    if pygame.sprite.spritecollide(imagenJill, nivel.grupo, 0, pygame.sprite.collide_mask):
        imagenJill.deshacer()

    if pygame.sprite.spritecollide(imagenPerro, nivel.grupo, 0, pygame.sprite.collide_mask):
        imagenPerro.deshacer()

    if teclasPulsadas[K_p]:
       pausar()

    if teclasPulsadas[K_o]:
       ins1()

    if teclasPulsadas[K_u]and sound==True:
         sound= False
         musica.stop()


    if teclasPulsadas[K_i]and sound==False:
         sound= True
         musica.play()

    for pum in pygame.sprite.groupcollide(grupoimagenJill, nivel.items, 0, 1):
        items=items+1
        #para pasar de nivel
        if items== 9:
          llaveflag=1
        if sound == True:
            soundBonus.play()
        pass


    for pum in pygame.sprite.groupcollide(grupoimagenJill, grupoimagenPerro, 1, 0):
        puntzombi()
        pygame.quit()
        sys.exit()


    for pum in pygame.sprite.groupcollide(grupoimagenJill, grupoimagenPerro2, 1, 0):
        puntzombi()
        pygame.quit()
        sys.exit()

    for pum in pygame.sprite.groupcollide(grupoimagenJill, grupoimagenPerro3, 1, 0):
        puntzombi()
        pygame.quit()
        sys.exit()

    for pum in pygame.sprite.groupcollide(grupoimagenJill, grupoimagenRata, 1, 0):
        puntzombi()
        pygame.quit()
        sys.exit()

    for pum in pygame.sprite.groupcollide(grupoimagenJill, grupoimagenRata1, 1, 0):
        puntzombi()
        pygame.quit()
        sys.exit()


    nivel.actualizar(visor)

    #print imagenJill.pos


    grupoimagenJill.draw(visor)
    grupoimagenPerro.draw(visor)
    grupoimagenPerro2.draw(visor)
    grupoimagenPerro3.draw(visor)
    grupoimagenRata.draw(visor)
    grupoimagenRata1.draw(visor)

    pygame.display.update()
