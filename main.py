import pygame

pygame.init()

screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)

class Menu:
    def __init__(self):
        self.global_font = pygame.font.Font(None, 74)
        self.label = self.global_font.render("Наркомир", True, (0, 0, 0))
        self.start_btn = None
        self.option_btn = None
        self.quit_btn = None
        self.donat_btn = None
    
    def blit_text(self):
        text_width = self.label.get_width()
        text_height = self.label.get_height()
        
        screen.blit(self.label, ((WIDTH - text_width) // 2, (HEIGHT - text_height) // 2))


running = True
menu = Menu()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((136, 136, 136))
    menu.blit_text()
    
    pygame.display.flip()
            
pygame.quit()
