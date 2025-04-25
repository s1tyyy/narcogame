import pygame

pygame.init()

screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)

class Menu:
    def __init__(self):
        self.global_font = pygame.font.Font(None, 74)
        self.label = self.global_font.render("Наркомир", True, (0, 0, 0))
        
        self.text_width = self.label.get_width()
        self.text_height = self.label.get_height() + 200
        
        self.start_btn = pygame.Rect(WIDTH // 2 - self.text_width + 75, HEIGHT  // 2 - 25, 350, 100)
        self.start_lbl = self.global_font.render("Начать игру", True, (0, 0, 0))

        self.option_btn = pygame.Rect(WIDTH // 2 - self.text_width + 75, HEIGHT // 2 + 100, 350, 100)
        self.option_lbl = self.global_font.render("Настройки", True, (0, 0, 0))

        self.donat_btn = pygame.Rect(WIDTH // 2 - self.text_width + 75, HEIGHT // 2 + 225, 350, 100)
        self.donat_lbl = self.global_font.render("Донат", True, (0, 0, 0))

        self.quit_btn = pygame.Rect(WIDTH // 2 - self.text_width + 75, HEIGHT // 2 + 350, 350, 100)
        self.quit_lbl = self.global_font.render("Выйти", True, (0, 0, 0))
    
    def blit_text(self):
        mouse_pos = pygame.mouse.get_pos()
        buttons = [self.start_btn, self.option_btn, self.donat_btn, self.quit_btn]
        
        for btn in buttons:
            if btn.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "darkgray", btn)
            else:
                pygame.draw.rect(screen, "lightgray", btn)
                
        
        screen.blit(self.label, ((WIDTH - self.text_width) // 2, (HEIGHT - self.text_height) // 2))
        screen.blit(self.start_lbl, (self.start_btn.x + 20, self.start_btn.y + 25))
        screen.blit(self.option_lbl, (self.option_btn.x + 40, self.option_btn.y + 25))
        screen.blit(self.donat_lbl, (self.donat_btn.x + 90, self.donat_btn.y + 25))
        screen.blit(self.quit_lbl, (self.quit_btn.x + 90, self.quit_btn.y + 25))

        #screen.blit(self.start_lbl, ((WIDTH - self.text_w) // 2, (HEIGHT - self.text_h) // 2))

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
