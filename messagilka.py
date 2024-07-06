#hi! this morning i woke up and out of nowhere got this idea to try and make dialogues/messageboxes
#using classes in Python. so here it is, my unexpected brainfart :)

import pygame
pygame.init()
w, h = 800, 600
says = []

class Dialogue:
    def __init__(self, actorname, text):
        self.text = text
        self.actorname = actorname

    def box(self, surface, scr_width, scr_height):
       boxa = pygame.draw.rect(surface, (0,0,0), (20, scr_height // 1.7, scr_width - 40, scr_height // 3 - 20))
       texta = pygame.font.Font(None, 36).render(f"{self.actorname}", True, (255,255,255))
       surface.blit(texta, (boxa[0] * 2, boxa[1] + 20))



def say(actorname, text):
    msg = Dialogue(actorname, text)
    says.append(msg)

window = pygame.display.set_mode((w, h))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not says:
                print("opa")
                say("misik", "mlom")
            else:
                says.clear()

    window.fill((255,255,255))
    for msg in says:
        msg.box(window, w, h)
    pygame.display.update()


