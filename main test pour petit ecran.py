import pygame
pygame.init()
import time


taille_ecran="petit" #taille_ecran="petit" ou taille_ecran="grand" selon la taille de l'écran.

taille=["petit"]

Lsym=[]
Lsym_primo=[]
xshift=130
yshift=129
alpha_glob=255

def text_box_save():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([600, 500])

    base_font = pygame.font.Font(None, 32)
    global save_fich
    save_fich = ''

    input_rect = pygame.Rect(300, 200, 450, 32)
    
    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    
    font25 = pygame.font.SysFont(None, 40)
    img_t_normal = font25.render("""Nom fich save:""", True,(93,68,122))
    screen.blit(img_t_normal,(10,250))

    class bouton_nor:
        def __init__(self):
            self.im=pygame.draw.rect(screen, (50,30,80), pygame.Rect(100, 10, 600, 600),  width=20)
        def affiche(self):
            font2 = pygame.font.SysFont(None, 90)
            img2 = font2.render("""GO""", True,(93,68,122))
            self.im=pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 0, 120, 80),  width=10)
            screen.blit(img2,(310,10))
        def clicked(self,event):
            if event.button == 1: # 1= clique gauche
                if self.im.collidepoint(event.pos):
                    boucle[0]=False

    bouton_normal=bouton_nor()

    global boucle
    boucle=[True]
    while boucle[0]:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False


                bouton_normal.clicked(event)
      
            if event.type == pygame.KEYDOWN:
                if active:
          
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        save_fich = save_fich[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        save_fich += event.unicode
                    #print(eval(user_text))
        # it will set background color of screen
        screen.fill((255, 255, 255))
      
        if active:
            color = color_active
        else:
            color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)
      
        text_surface = base_font.render(save_fich, True, (255, 255, 255))
          
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        screen.blit(img_t_normal,(10,205))
          
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10) 
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        bouton_normal.affiche()

        pygame.display.flip()
    pygame.display.quit()
    return save_fich





def text_box():

    # pygame.init() will initialize all
    # imported module

      
    clock = pygame.time.Clock()
      
    # it will display on screen
    screen = pygame.display.set_mode([600, 500])
      
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    global user_text
    user_text = ''

    global user_text_ind
    user_text_ind = ''
      
    # create rectangle
    input_rect = pygame.Rect(200, 200, 450, 32)
    input_rect2 = pygame.Rect(200, 400, 450, 32)
    
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
      
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
      
    active = False
    active2 = False
    
    font25 = pygame.font.SysFont(None, 40)
    img_t_normal = font25.render("""Normal:""", True,(93,68,122))
    screen.blit(img_t_normal,(10,250))

    font25 = pygame.font.SysFont(None, 40)
    img_t_normal2 = font25.render("""Indice:""", True,(93,68,122))
    screen.blit(img_t_normal2,(10,450))

    class bouton_nor:
        def __init__(self):
            self.im=pygame.draw.rect(screen, (50,30,80), pygame.Rect(100, 10, 600, 600),  width=20)
        def affiche(self):
            font2 = pygame.font.SysFont(None, 90)
            img2 = font2.render("""GO""", True,(93,68,122))
            self.im=pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 0, 120, 80),  width=10)
            screen.blit(img2,(310,10))
        def clicked(self,event):
            if event.button == 1: # 1= clique gauche
                if self.im.collidepoint(event.pos):
                    boucle[0]=False

    bouton_normal=bouton_nor()

    class bouton_omega:
        def __init__(self):
            self.im=pygame.draw.rect(screen, (50,30,80), pygame.Rect(100, 10, 100, 600),  width=20)
        def affiche(self):
            font2 = pygame.font.SysFont(None, 40)
            img2 = font2.render("""ajoute le Ohm a la fin du texte""", True,(93,68,122))
            self.im=pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 90, 420, 50),  width=10)
            screen.blit(img2,(100,100))
        def clicked(self,event):
            if event.button == 1: # 1= clique gauche
                if self.im.collidepoint(event.pos):
                    
                    boucle[0]=False
                    Omega[0]=True
                    

    bouton_ohm=bouton_omega()

    global boucle
    boucle=[True]
    Omega=[False]
    while boucle[0]:
        for event in pygame.event.get():
      
          # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                    active2=False
                elif input_rect2.collidepoint(event.pos):
                    active2=True
                    active = False
                else:
                    active = False
                    active2=False

                bouton_normal.clicked(event)
                bouton_ohm.clicked(event)
      
            if event.type == pygame.KEYDOWN:
                if active:
          
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode
                if active2:
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        user_text_ind = user_text_ind[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text_ind += event.unicode
                    #print(eval(user_text))
        # it will set background color of screen
        screen.fill((255, 255, 255))
      
        if active:
            color = color_active
        else:
            color = color_passive

        if active2:
            color2 =color_active
        else:
            color2 = color_passive              
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
        
        pygame.draw.rect(screen, color2, input_rect2)
        
      
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        text_surface2 = base_font.render(user_text_ind, True, (255, 255, 255))
          
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        screen.blit(text_surface2, (input_rect2.x+5, input_rect2.y+5))
        
        screen.blit(img_t_normal,(10,205))
        screen.blit(img_t_normal2,(10,405))
          
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        input_rect2.w = max(100, text_surface2.get_width()+10)  
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        bouton_normal.affiche()
        bouton_ohm.affiche()

        #######
        #######
        #######
        ####### 2eme barre
        #######
        #######
        #######
        #######
        
        pygame.display.flip()
    return user_text,user_text_ind,Omega[0]


def save():
    save_file=text_box_save()
    if taille_ecran=="grand":
        grand_ecran()
    if taille_ecran=="petit":
        petit_ecran()
    actualize_all()
    print("mareeeee")
    rect = pygame.Rect(100, 100, 1260, 740)
    sub = fen.subsurface(rect)
    pygame.image.save(sub,"circuit_final\\"+save_file+".png")



    
def petit_ecran():
    taille[0]="petit"
    global fen
    largeur = 1200
    hauteur = 640
    fen = pygame.display.set_mode((largeur, hauteur))
    global fond1
    fond1 = pygame.image.load("symbole_necessaires\\fond_blanc.png").convert()
    fen.blit(fond1, (0,0))
    global fond2
    fond2 = pygame.image.load("symbole_necessaires\\fond_moyen.png").convert()
    fond2.set_alpha(alpha_glob)
    fen.blit(fond2, (100,100))
    
    lampe = pygame.image.load("symbole_necessaires\\lampe.png").convert_alpha()
    #lampe = pygame.transform.scale(lampe, (129, 69))
    fen.blit(lampe, pos_carreau_petit_objet(0,0))

    font = pygame.font.SysFont(None, 30)
    color = (120, 0, 255)
    global img
    img = font.render("""Clic gauche pour placer et choisir. """, True, color)
    img=pygame.transform.rotate(img, 90)
    global img2
    img2 = font.render("""Clic droit pour annuler ou suprimmer.""", True, color)
    img2=pygame.transform.rotate(img2, 90)
    fen.blit(img, (1200, 250))
    global img3
    img3 = font.render("""Clic Molette pour faire tourner le symbole.""", True, color)
    img3=pygame.transform.rotate(img3, 90)
    fen.blit(img, (1200, 250))

    
def moyen_avec_traits():
    taille[0]="moyen"
    global fen
    largeur = 1160
    hauteur = 840
    fen = pygame.display.set_mode((largeur, hauteur))
    fond = pygame.image.load("symbole_necessaires\\fond_moyen.png").convert()
    fen.blit(fond, (0,0))

def grand_ecran():
    taille[0]="petit"
    global fen
    largeur = 1360
    hauteur = 840
    fen = pygame.display.set_mode((largeur, hauteur))
    global fond1
    fond1 = pygame.image.load("symbole_necessaires\\fond_blanc.png").convert()
    fen.blit(fond1, (0,0))
    global fond2
    fond2 = pygame.image.load("symbole_necessaires\\fond_petit.png").convert()
    fond2.set_alpha(alpha_glob)
    fen.blit(fond2, (100,100))
    
    lampe = pygame.image.load("symbole_necessaires\\lampe.png").convert_alpha()
    #lampe = pygame.transform.scale(lampe, (129, 69))
    fen.blit(lampe, pos_carreau_petit_objet(0,0))

    font = pygame.font.SysFont(None, 30)
    color = (120, 0, 255)
    global img
    img = font.render("""Clic gauche pour placer et choisir. """, True, color)
    img=pygame.transform.rotate(img, 90)
    global img2
    img2 = font.render("""Clic droit pour annuler ou suprimmer.""", True, color)
    img2=pygame.transform.rotate(img2, 90)
    fen.blit(img, (1200, 250))
    global img3
    img3 = font.render("""Clic Molette pour faire tourner le symbole.""", True, color)
    img3=pygame.transform.rotate(img3, 90)
    fen.blit(img, (1200, 250))

def changement_fond(choix):
    global fond2
    if choix=="blanc":
        fond2 = pygame.image.load("symbole_necessaires\\fond_blanc.png").convert()
    if choix=="carreau":
        fond2 = pygame.image.load("symbole_necessaires\\fond_petit.png").convert()



    
    
def pos_carreau_petit_objet(pixelx,pixely):
    x=int(xshift)+ int(pixelx/56)*56
    y=int(yshift)+ int(pixely/56)*56
    #print(x,y)
    return (x,y)


def pos_carreau_fil(pixelx,pixely):
    x=int(xshift+14)+ int(pixelx/28)*28
    y=int(yshift+13)+ int(pixely/28)*28

    return (x,y)

def pos_carreau_text(pixelx,pixely,rotate):
    #print(rotate)
    r=rotate*90
    if r==0%360:
        x=int(xshift)+ int(pixelx/28)*28
        y=int(yshift+32)+ int(pixely/28)*28
    if r==90%360:
        x=int(xshift+30)+ int(pixelx/28)*28
        y=int(yshift+55)+ int(pixely/28)*28
    if r==180%360:
        x=int(xshift)+ int(pixelx/28)*28
        y=int(yshift+25)+ int(pixely/28)*28
    if r==270%360:
        x=int(xshift+20)+ int(pixelx/28)*28
        y=int(yshift+55)+ int(pixely/28)*28
    return (x,y)

def pos_carreau_buzzer(pixelx,pixely,rotate):
    r=rotate*90
    if r==0%360:
        x=int(xshift+0)+ int(pixelx/56)*56
        y=int(yshift+29)+ int(pixely/56)*56
    if r==90%360:
        x=int(xshift+29)+ int(pixelx/56)*56
        y=int(yshift+50)+ int(pixely/56)*56
    if r==180%360:
        x=int(xshift-7)+ int(pixelx/56)*56
        y=int(yshift+27)+ int(pixely/56)*56
    if r==270%360:
        x=int(xshift+26)+ int(pixelx/56)*56
        y=int(yshift+56)+ int(pixely/56)*56
    return (x,y)





if taille_ecran=="grand":
    grand_ecran()
if taille_ecran=="petit":
    petit_ecran()

pygame.image.save(fen,"save.png")

class bouton_save:
    def __init__(self):
        self.im=pygame.draw.rect(fen, (50,30,80), pygame.Rect(1150, 10, 200, 80),  width=20)
    def affiche(self):
        font2 = pygame.font.SysFont(None, 90)
        img2 = font2.render("""SAVE""", True,(50,30,80))
        pygame.draw.rect(fen, (70,120,80), pygame.Rect(1130, 0, 200, 80),  width=10)
        fen.blit(img2,self.im)
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.im.collidepoint(event.pos):
                save()
                
bouton_sauvegarder=bouton_save()

class symbole_primordial:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.x=x
        self.y=y
        self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(56,28))
        self.clic=self.image.get_rect()
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)
        
        
    def actualize(self):
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)

    def generate(self,nrotate=0):
        Lsym.append(symbole(self.nom,0,0))
        Lsym[-1].nrotate=nrotate
        Lsym[-1].rotate(nrotate)
        go=1
        while go:    
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        go=0
                    if event.button == 3:
                        go=0
                        del(Lsym[-1])
                if event.type==pygame.MOUSEMOTION:
                    #print(pygame.mouse.get_pos())
                    Lsym[-1].x=pygame.mouse.get_pos()[0]-xshift
                    Lsym[-1].y=pygame.mouse.get_pos()[1]-yshift
                    actualize_all()
                    time.sleep(0.001)
                
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                self.generate()
                    
class buzzer_primordial:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.x=x
        self.y=y
        self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(56,28))
        self.clic=self.image.get_rect()
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)
        
        
    def actualize(self):
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)

    def generate(self,nrotate=0):
        Lsym.append(buzzer(self.nom,0,0))
        Lsym[-1].nrotate=nrotate
        Lsym[-1].rotate(nrotate)
        go=1
        while go:    
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        go=0
                    if event.button == 3:
                        go=0
                        del(Lsym[-1])
                if event.type==pygame.MOUSEMOTION:
                    #print(pygame.mouse.get_pos())
                    Lsym[-1].x=pygame.mouse.get_pos()[0]-xshift
                    Lsym[-1].y=pygame.mouse.get_pos()[1]-yshift
                    actualize_all()
                    time.sleep(0.001)
                
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                self.generate()

Lsym_primo.append(buzzer_primordial("buzzer",0,150))

class buzzer:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.nrotate=0
        self.x=x
        self.y=y
        (x2,y2)=pos_carreau_petit_objet(x,y)
        self.x_grid=x2
        self.y_grid=y2
        self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        self.clic=self.image.get_rect()
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)

    def rotate(self,n=1):
        self.image=pygame.transform.rotate(self.image, n*90)
        self.clic=self.image.get_rect()
        #self.clic=pygame.transform.rotate(self.clic, 90)
        
    def actualize(self):
        (self.x_grid,self.y_grid)=pos_carreau_buzzer(self.x,self.y,self.nrotate)
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)

    def clicked(self,event):
        a=pygame.key.get_pressed()
        if event.button == 1 and not a[pygame.K_LCTRL]: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                    #print("ayaaaa")
                    return "moove"
            
        if event.button == 3:
            if self.clic.collidepoint(event.pos):
                #print("a")
                return "delete"
        if event.button == 2 or (event.button == 1 and a[pygame.K_LCTRL]) :

            if self.clic.collidepoint(event.pos):
                self.nrotate+=1
                self.nrotate=self.nrotate%4
                self.rotate()
        return 1
    


Lsym_primo.append(symbole_primordial("interrupteur1",0,0))
Lsym_primo.append(symbole_primordial("interrupteur2",0,30))
Lsym_primo.append(symbole_primordial("interrupteur3",0,60))
Lsym_primo.append(symbole_primordial("interrupteur4",00,90))



Lsym_primo.append(symbole_primordial("pile",60,0))
Lsym_primo.append(symbole_primordial("pile2",60,30))

Lsym_primo.append(symbole_primordial("gene1",120,0))
Lsym_primo.append(symbole_primordial("gene2",120,30))
Lsym_primo.append(symbole_primordial("gene3",120,60))


Lsym_primo.append(symbole_primordial("lampe",180,0))
Lsym_primo.append(symbole_primordial("lampe2",180,30))
Lsym_primo.append(symbole_primordial("Moteur",180,60))

Lsym_primo.append(symbole_primordial("Resistance",240,0))
Lsym_primo.append(symbole_primordial("Resistance2",240,30))
Lsym_primo.append(symbole_primordial("photoresistance",240,60))

Lsym_primo.append(symbole_primordial("LED",300,0))
Lsym_primo.append(symbole_primordial("Diode",300,30))

Lsym_primo.append(symbole_primordial("ohmmetre",360,0))
Lsym_primo.append(symbole_primordial("voltmetre",360,30))
Lsym_primo.append(symbole_primordial("amperemetre",360,60))

Lsym_primo.append(symbole_primordial("bobine",420,0))
Lsym_primo.append(symbole_primordial("condensateur",420,30))


Lf_primo=[]

class fils_primo:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.x=x
        self.y=y
        self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(self.image.get_width()/2,self.image.get_height()/2))
        self.clic=self.image.get_rect()
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)
    def actualize(self):
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)

    def generate(self):
        Lf.append(fils(self.nom,0,0))
        go=1
        while go:    
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        go=0
                    if event.button == 3:
                        go=0
                        del(Lf[-1])
                if event.type==pygame.MOUSEMOTION:
                    #print(pygame.mouse.get_pos())
                    Lf[-1].x=pygame.mouse.get_pos()[0]-xshift-14
                    Lf[-1].y=pygame.mouse.get_pos()[1]-yshift-14
                    actualize_all()
                    time.sleep(0.001)
                
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                self.generate()

Lf_primo.append(fils_primo("C1",600,0))
Lf_primo.append(fils_primo("C3",600,60))

Lf_primo.append(fils_primo("C2",660,0))
Lf_primo.append(fils_primo("C4",660,60))

Lf_primo.append(fils_primo("BG", 700,0))
Lf_primo.append(fils_primo("BD", 740,0))

Lf_primo.append(fils_primo("BH", 780,0))
Lf_primo.append(fils_primo("BB", 780,60))

Lf_primo.append(fils_primo("t1v", 880,0))
Lf_primo.append(fils_primo("t2v", 900,0))
Lf_primo.append(fils_primo("t3v", 930,0))

Lf_primo.append(fils_primo("t1h",960,0))
Lf_primo.append(fils_primo("t2h",960,30))
Lf_primo.append(fils_primo("t3h",960,60))

Lf_primo.append(fils_primo("trait_rouge",990,0))
Lf_primo.append(fils_primo("trait_vert",1020,0))

Lf_primo.append(fils_primo("trait_vert_vert",880,30))
Lf_primo.append(fils_primo("trait_rouge_vert",880,60))

Lf_primo.append(fils_primo("noeud",1070,0))
Lf_primo.append(fils_primo("noeud_rouge",1070,20))
Lf_primo.append(fils_primo("noeud_vert",1070,40))
Lf_primo.append(fils_primo("noeud_bleu",1070,60))

Lf_primo.append(fils_primo("courant1",540,0))
Lf_primo.append(fils_primo("courant2",540,30))
Lf_primo.append(fils_primo("courant3",540,60))
Lf_primo.append(fils_primo("courant4",540,90))


Lf=[]
class fils:

    def __init__(self, nom,x,y):
        self.nom=nom
        
        self.x=x
        self.y=y
        (x2,y2)=pos_carreau_petit_objet(x,y)
        self.x_grid=x2
        self.y_grid=y2
        self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        self.clic=self.image.get_rect()
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)
        
        
    def actualize(self):
        (self.x_grid,self.y_grid)=pos_carreau_fil(self.x,self.y)
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)

    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                    #print("ayaaaa")
                    return "moove"

        if event.button == 3:
            if self.clic.collidepoint(event.pos):
                #print("a")
                return "delete"
        return 1

    

class symbole:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.nrotate=0
        self.x=x
        self.y=y
        (x2,y2)=pos_carreau_petit_objet(x,y)
        self.x_grid=x2
        self.y_grid=y2
        if taille[0]=="grand":
            self.image=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
        if taille[0]=="petit":
            im_temp=pygame.image.load("symbole_necessaires\\"+nom+".png").convert_alpha()
            self.image=pygame.transform.scale(im_temp,(92,47))
        self.clic=self.image.get_rect()
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)

    def rotate(self,n=1):
        self.image=pygame.transform.rotate(self.image, n*90)
        self.clic=self.image.get_rect()
        #self.clic=pygame.transform.rotate(self.clic, 90)
        
    def actualize(self):
        (self.x_grid,self.y_grid)=pos_carreau_petit_objet(self.x,self.y)
        self.clic.x=self.x_grid
        self.clic.y=self.y_grid
        fen.blit(self.image,self.clic)

    def clicked(self,event):
        a=pygame.key.get_pressed()
        if event.button == 1 and not a[pygame.K_LCTRL]: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                    #print("ayaaaa")
                    return "moove"
            
        if event.button == 3:
            if self.clic.collidepoint(event.pos):
                #print("a")
                return "delete"
        if event.button == 2 or (event.button == 1 and a[pygame.K_LCTRL]) :

            if self.clic.collidepoint(event.pos):
                self.nrotate+=1
                self.rotate()
        return 1
Lsym.append(symbole("lampe",0,0))
#fond = pygame.image.load("fond_blanc.png").convert()
#fen.blit(fond, (0,0))

Ltext=[]

class text_primo:
    def __init__(self, nom,x,y):
        self.nom=nom
        self.x=x
        self.y=y
        font2 = pygame.font.SysFont(None, 90)
        self.image=font2.render("""T""", True, (0,0,0))
        #self.image=pygame.transform.scale(self.image,(56,28))
        self.clic=self.image.get_rect()
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)
        
        
    def actualize(self):
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)

    def generate(self,nrotate=0,le_text=0,le_text_ind='',omega=False):
        if le_text==0:
            le_text,le_text_ind,omega=text_box()
        if taille_ecran=="grand":
            grand_ecran()
        if taille_ecran=="petit":
            petit_ecran()
        
        Ltext.append(text(le_text,le_text_ind,omega,0,0))
        Ltext[-1].nrotate=nrotate
        Ltext[-1].rotate(nrotate)
        go=1
        while go:    
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        go=0
                    if event.button == 3:
                        go=0
                        del(Ltext[-1])
                if event.type==pygame.MOUSEMOTION:
                    #print(pygame.mouse.get_pos())
                    Ltext[-1].x=pygame.mouse.get_pos()[0]-xshift
                    Ltext[-1].y=pygame.mouse.get_pos()[1]-yshift
                    actualize_all()
                    time.sleep(0.001)
                
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                self.generate()


Ltext_primo=[]
Ltext_primo.append(text_primo("bo",20,320))




                
class text:
    def __init__(self, nom,text_ind,omega,x,y):
        self.omega=omega
        self.nom=nom
        self.nrotate=0
        self.x=x
        self.y=y
        self.text_ind=text_ind
        if taille[0]=="grand":
            font21=pygame.font.SysFont(None, 70)
            self.image1=font21.render(nom, True, (0,0,0))
            font278=pygame.font.SysFont(None, 42)
            self.image2=font278.render(text_ind, True, (0,0,0))
            self.image3=pygame.image.load("symbole_necessaires\\omega.png").convert_alpha()
        if taille[0]=="petit":
            font21=pygame.font.SysFont(None, 58)
            self.image1=font21.render(nom, True, (0,0,0))
            font278=pygame.font.SysFont(None, 34)
            self.image2=font278.render(text_ind, True, (0,0,0))
            im_temp=pygame.image.load("symbole_necessaires\\omega.png").convert_alpha()
            self.image3=pygame.transform.scale(im_temp,(35,35))
        
        (x2,y2)=pos_carreau_text(x,y,0)
        self.x_grid=x2
        self.y_grid=y2
        if omega:
            self.image=pygame.Surface((self.image1.get_width()+self.image2.get_width()+self.image3.get_width(),int(self.image1.get_height()*1.3)+self.image3.get_height()), pygame.SRCALPHA)
            self.image.blit(self.image1,(0,0))
            self.image.blit(self.image2,(self.image1.get_width(),30))
            self.image.blit(self.image3,(self.image1.get_width()+self.image2.get_width(),0))
        else:
            self.image=pygame.Surface((self.image1.get_width()+self.image2.get_width(),int(self.image1.get_height()*1.3)), pygame.SRCALPHA)
            self.image.blit(self.image1,(0,0))
            self.image.blit(self.image2,(self.image1.get_width(),30))
        self.clic=self.image.get_rect()
        self.clic.center=self.x_grid,self.y_grid

        
        fen.blit(self.image,self.clic)

    def rotate(self,n=1):
        self.image=pygame.transform.rotate(self.image, n*90)
        self.clic=self.image.get_rect()
        
        
    def actualize(self):
        (self.x_grid,self.y_grid)=pos_carreau_text(self.x,self.y,self.nrotate)
        self.clic.center=self.x_grid,self.y_grid
        fen.blit(self.image,self.clic)
        

    def clicked(self,event):
        a=pygame.key.get_pressed()
        if event.button == 1 and not a[pygame.K_LCTRL]: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                    #print("ayaaaa")
                    return "moove"
            
        if event.button == 3:
            if self.clic.collidepoint(event.pos):
                #print("a")
                return "delete"
        if event.button == 2 or (event.button == 1 and a[pygame.K_LCTRL]) :
            if self.clic.collidepoint(event.pos):
                self.nrotate+=1
                self.nrotate=self.nrotate%4
                self.rotate()
                return "tourne"
        return 1



class changement_fond:
    def __init__(self, alpha,x,y):
        self.alpha=alpha
        
        self.x=x
        self.y=y
        font2 = pygame.font.SysFont(None, 30)
        self.image=font2.render("""Fond"""+str(alpha), True, (0,0,0))
        #self.image=pygame.transform.scale(self.image,(56,28))
        self.clic=self.image.get_rect()
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)
        
        
    def actualize(self):
        self.clic.x=self.x
        self.clic.y=self.y
        fen.blit(self.image,self.clic)

    def change_fond(self):
        global fond2
        fond2.set_alpha(self.alpha)
        global alpha_glob
        alpha_glob=self.alpha

                
    def clicked(self,event):
        if event.button == 1: # 1= clique gauche
            if self.clic.collidepoint(event.pos):
                self.change_fond()


L_c_fond=[]
L_c_fond.append(changement_fond(0,0,200))
L_c_fond.append(changement_fond(120,0,220))
L_c_fond.append(changement_fond(255,0,240))


def actualize_all(sf=True):
    fen.blit(fond1, (0,0))
    fen.blit(fond2, (100,100))
        
    fen.blit(img, (10, 450))
    fen.blit(img2, (30, 450))
    fen.blit(img3, (50, 400))
    bouton_sauvegarder.affiche()
    for i in Lsym:
        i.actualize()
    for i in Lsym_primo:
        i.actualize()
    for i in Lf:
        i.actualize()
    for i in Lf_primo:
        i.actualize()
    for i in Ltext_primo:
        i.actualize()
    for i in Ltext:
        i.actualize()
    for i in L_c_fond:
        i.actualize()
    pygame.display.update()

def main():    
    continuer = True
    while continuer :
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                continuer = False
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                #grand_avec_traits()
                a=1
                b=1
                j=0
                nbrotate=0
                #symboles
                for i in range(len(Lsym)):
                    a=Lsym[i].clicked(evenement)
                    if a=="delete":
                        #print("aaaaa")
                        b=a
                        j=i
                    if a=="moove":
                        b=a
                        j=i
                        nbrotate=Lsym[i].nrotate
                    #print(evenement.pos) #coordonnées du clique
                    #print(evenement.button) # numéro du bouton
                #print(a)
                if b=="delete":
                    del(Lsym[j])
                if b=="moove":
                    namet=Lsym[j].nom
                    del(Lsym[j])
                    for i in Lsym_primo:
                        if i.nom==namet:
                            #print("bugy")
                            i.generate(nbrotate)
                for i in range(len(Lsym_primo)):
                    Lsym_primo[i].clicked(evenement)
                for i in range(len(L_c_fond)):
                    L_c_fond[i].clicked(evenement)
                
                #fils
                a=1
                b=1
                j=0

                
                for i in range(len(Lf)):
                    a=Lf[i].clicked(evenement)
                    if a=="delete":
                        #print("aaaaa")
                        b=a
                        j=i
                    if a=="moove":
                        b=a
                        j=i
                    #print(evenement.pos) #coordonnées du clique
                    #print(evenement.button) # numéro du bouton
                #print(a)
                if b=="delete":
                    del(Lf[j])
                if b=="moove":
                    namet=Lf[j].nom
                    del(Lf[j])
                    for i in Lf_primo:
                        if i.nom==namet:
                            #print("bugy")
                            i.generate()
                            
                a=1
                b=1
                j=0


                for i in range(len(Ltext)):
                    a=Ltext[i].clicked(evenement)
                    if a=="delete":
                        #print("aaaaa")
                        b=a
                        j=i
                    if a=="moove":
                        b=a
                        j=i
                    if a=="tourne":
                        b=a
                        j=i
                    #print(evenement.pos) #coordonnées du clique
                    #print(evenement.button) # numéro du bouton
                #print(a)
                if b=="delete":
                    del(Ltext[j])
                if b=="moove":
                    omegat=Ltext[j].omega
                    namet=Ltext[j].nom
                    t_ind=Ltext[j].text_ind
                    nbrotate=Ltext[i].nrotate
                    del(Ltext[j])
                    Ltext_primo[0].generate(nrotate=nbrotate,le_text=namet,le_text_ind=t_ind,omega=omegat)
                            
                for i in range(len(Lf_primo)):
                    Lf_primo[i].clicked(evenement)
                for i in range(len(Ltext_primo)):
                    Ltext_primo[i].clicked(evenement)
                    
                bouton_sauvegarder.clicked(evenement)

                    
        actualize_all()
        pygame.display.update()
main()

pygame.display.quit()
