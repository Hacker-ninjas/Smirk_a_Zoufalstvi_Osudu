import pygame, sys

pygame.init()

# nastavení okna hry, obrázků pohybu postavy a pozadí hry
win = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)  # velikost okna
pygame.display.set_caption("Smirk a Zoufalství Osudu")   # název okna
icon = pygame.image.load("ico.png")    # ikona programu
pygame.display.set_icon(icon)   # nastavení ikony
walkRight = [pygame.image.load("graphic/smirk/R1.png"), pygame.image.load("graphic/smirk/R2.png"), pygame.image.load("graphic/smirk/R3.png")]  # seznam obrázků chůze doprava, načtení obrázků z jiné složky -> pygame.image.load("nazev_slozky/R9.png")
walkLeft = [pygame.image.load("graphic/smirk/L1.png"), pygame.image.load("graphic/smirk/L2.png"), pygame.image.load("graphic/smirk/L3.png")]    # seznam obrázků chůze doleva
walkUp = [pygame.image.load("graphic/smirk/U1.png"), pygame.image.load("graphic/smirk/U2.png"), pygame.image.load("graphic/smirk/U3.png")]
walkDown = [pygame.image.load("graphic/smirk/D1.png"), pygame.image.load("graphic/smirk/D2.png"), pygame.image.load("graphic/smirk/D3.png")]
bg = pygame.image.load("graphic/texture_grass.png")    # obrázek pozadí
char = pygame.image.load("graphic/smirk/D2.png")    # výchozí obrázek postavy

clock = pygame.time.Clock() # framerate hry

x = 50  # výchozí bod na ose x
y = 400  # výchozí bod na ose y
width = 16  # šířka postavy
height = 16 # výška postavy
vel = 5    # počet bodů posunu
left = False    # proměnná pohybu doleva
right = False   # proměnná pohybu doprava
up = False # proměnná pohybu nahoru
down = False # proměnná pohybu dolů
walkCount = 0   # počet snímků pohybu

def redrawGameWindow(): # funkce překreslení okna při pohybu postavy
    global walkCount    # aby změna v této proměnné byla vidět i mimo funkci
    win.blit(bg, (0, 0)) # vyplnění okna obrázkem bg od souřadnice 0, 0
    
    if walkCount + 1 >= 9: # pohyb doprava a doleva má 3 obrázků a každý se bude zobrazovat 3 snímky -> 3 * 3 = 9
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif up:
        win.blit(walkUp[walkCount//3], (x,y))
        walkCount += 1
    elif down:
        win.blit(walkDown[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update() # obnovení displeje

# hlavní smyčka hry
run = True
while run:
    clock.tick(21)   # framerate v FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # po kliknutí na X přeruší smyčku a zavře okno
            run = False

    keys = pygame.key.get_pressed() # definice pohybu postavy po obrazovce. Souřadnice jsou od 0,0 vlevo nahoře po 1024,768 vpravo dole. 
    if keys [pygame.K_LEFT] and x > vel:  # pohyb doleva a ošetření uníku mimo obrazovku
        x -= vel    # pohyb doleva odečítá na ose x rychlostí vel
        left = True
        right = False
        up = False
        down = False
    elif keys [pygame.K_RIGHT] and x < 1024 - width - vel:   # pohyb doprava a ošetření uníku mimo obrazovku. (šiřka okna - šířka objektu - body posunu)
        x += vel    # pohyb doprava přičítá na ose x rychlostí vel
        right = True
        left = False
        up = False
        down = False
    elif keys [pygame.K_UP] and y > vel: # pohyb nahoru
        y -= vel
        up = True
        right = False
        left = False
        down = False
    elif keys [pygame.K_DOWN] and y < 768 - width - vel:    # pohyb dolů
        y += vel
        down = True
        up = False
        left = False
        right = False
    else:   # pokud se nehýbeme
        right = False
        left = False
        up = False
        down = False
        walkCount = 0
      
    redrawGameWindow()  # volání funkce překreslení okna
    


pygame.guit()