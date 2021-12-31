import pygame

pygame.init()

# nastavení okna hry, obrázků pohybu postavy a pozadí hry
screen = pygame.display.set_mode((500, 500))  # velikost okna
pygame.display.set_caption("Smirk a Zoufalství Osudu")   # název okna
icon = pygame.image.load("ico.png")    # ikona programu
pygame.display.set_icon(icon)   # nastavení ikony
walkRight = [pygame.image.load("graphic/smirk/R1.png"), pygame.image.load("graphic/smirk/R2.png"), pygame.image.load("graphic/smirk/R3.png")]  # seznam obrázků chůze doprava, načtení obrázků z jiné složky -> pygame.image.load("nazev_slozky/R9.png")
walkLeft = [pygame.image.load("graphic/smirk/L1.png"), pygame.image.load("graphic/smirk/L2.png"), pygame.image.load("graphic/smirk/L3.png")]    # seznam obrázků chůze doleva
walkUp = [pygame.image.load("graphic/smirk/U1.png"), pygame.image.load("graphic/smirk/U2.png"), pygame.image.load("graphic/smirk/U3.png")]
walkDown = [pygame.image.load("graphic/smirk/D1.png"), pygame.image.load("graphic/smirk/D2.png"), pygame.image.load("graphic/smirk/D3.png")]
bg = pygame.image.load("graphic/mapa.png")    # obrázek pozadí
char = pygame.image.load("graphic/smirk/D2.png")    # výchozí obrázek postavy

clock = pygame.time.Clock() # framerate hry

class Player(object):
    # třída postavy hráče
    def __init__(self, x, y, width, height):
        # atributy třídy
        self.x = x  # výchozí bod na ose x
        self.y = y  # výchozí bod na ose y
        self.width = width  # šířka postavy
        self.height = height    # výška postavy
        self.vel = 5    # počet bodů posunu
        self.left = False   # proměnná pohybu doleva
        self.right = False  # proměnná pohybu doprava
        self.up = False # proměnná pohybu nahoru
        self.down = False   # proměnná pohybu dolů
        self.walkCount = 0  # počet snímků pohybu
    
    def draw(self,screen):
        # definice pohybu hráče
        if self.walkCount + 1 >= 9: # pohyb doprava a doleva má 3 obrázků a každý se bude zobrazovat 3 snímky -> 3 * 3 = 9
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            screen.blit(walkUp[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(walkDown[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x,self.y))

#class Enemy(object):
    # třída postavy nepřítele
  

def redrawGameWindow():
    # funkce překreslení okna při pohybu postavy
    screen.blit(bg, (0, 0)) # vyplnění okna obrázkem bg od souřadnice 0, 0
    man.draw(screen) 
    pygame.display.update() # obnovení displeje


# hlavní smyčka hry
man = Player(300, 410, 16, 16)
run = True
while run:
    clock.tick(21)   # framerate v FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # po kliknutí na X přeruší smyčku a zavře okno
            run = False

    keys = pygame.key.get_pressed() # definice pohybu postavy po obrazovce. Souřadnice jsou od 0,0 vlevo nahoře po 1024,768 vpravo dole. 
    if keys [pygame.K_LEFT] and man.x > man.vel:  # pohyb doleva a ošetření uníku mimo obrazovku
        man.x -= man.vel    # pohyb doleva odečítá na ose x rychlostí vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
    elif keys [pygame.K_RIGHT] and man.x < 1024 - man.width - man.vel:   # pohyb doprava a ošetření uníku mimo obrazovku. (šiřka okna - šířka objektu - body posunu)
        man.x += man.vel    # pohyb doprava přičítá na ose x rychlostí vel
        man.right = True
        man.left = False
        man.up = False
        man.down = False
    elif keys [pygame.K_UP] and man.y > man.vel: # pohyb nahoru
        man.y -= man.vel    # pohyb nahoru odečítá na ose y rychlostí vel
        man.up = True
        man.right = False
        man.left = False
        man.down = False
    elif keys [pygame.K_DOWN] and man.y < 768 - man.width - man.vel:    # pohyb dolů
        man.y += man.vel    # pohyb dolů přičítá na ose y rychlostí vel
        man.down = True
        man.up = False
        man.left = False
        man.right = False
    else:   # pokud se nehýbeme
        man.right = False
        man.left = False
        man.up = False
        man.down = False
        man.walkCount = 0
      
    redrawGameWindow()  # volání funkce překreslení okna
    


pygame.guit()