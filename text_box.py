import pygame
import sys
pygame.init()

def text_box():
    def ind(s):
        table = str.maketrans({str(i):chr(0x2080 + i) for i in range(10)})
        return s.translate(table)

    # pygame.init() will initialize all
    # imported module

      
    clock = pygame.time.Clock()
      
    # it will display on screen
    screen = pygame.display.set_mode([600, 500])
      
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    global user_text
    user_text = ''
      
    # create rectangle
    input_rect = pygame.Rect(200, 200, 450, 32)
      
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
      
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
      
    active = False


    class bouton_ind:
        def __init__(self):
            self.im=pygame.draw.rect(screen, (50,30,80), pygame.Rect(100, 10, 600, 600),  width=20)
        def affiche(self):
            font2 = pygame.font.SysFont(None, 90)
            img2 = font2.render("""Indice""", True,(93,68,122))
            self.im=pygame.draw.rect(screen, (0,0,0), pygame.Rect(80, 0, 200, 80),  width=10)
            screen.blit(img2,(90,10))
        def clicked(self,event,user_text):
            if event.button == 1: # 1= clique gauche
                if self.im.collidepoint(event.pos):
                    a=user_text
                    user_text=ind(a)
                    boucle[0]=False
            return user_text

    class bouton_nor:
        def __init__(self):
            self.im=pygame.draw.rect(screen, (50,30,80), pygame.Rect(100, 10, 600, 600),  width=20)
        def affiche(self):
            font2 = pygame.font.SysFont(None, 90)
            img2 = font2.render("""Normal""", True,(93,68,122))
            self.im=pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 0, 250, 80),  width=10)
            screen.blit(img2,(310,10))
        def clicked(self,event):
            if event.button == 1: # 1= clique gauche
                if self.im.collidepoint(event.pos):
                    boucle[0]=False

                    
    bouton_indice=bouton_ind()
    bouton_normal=bouton_nor()


    global boucle
    boucle=[True]
    while boucle[0]:
        for event in pygame.event.get():
      
          # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                user_text=bouton_indice.clicked(event,user_text)
                bouton_normal.clicked(event)
      
            if event.type == pygame.KEYDOWN:
      
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
      
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
      
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
                    #print(eval(user_text))
        # it will set background color of screen
        screen.fill((255, 255, 255))
      
        if active:
            color = color_active
        else:
            color = color_passive
              
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
      
        text_surface = base_font.render(user_text, True, (255, 255, 255))
          
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
          
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
          
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        bouton_indice.affiche()
        bouton_normal.affiche()
        pygame.display.flip()
    pygame.display.quit()
    return user_text
