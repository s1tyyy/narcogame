import pygame
import cfg

pygame.init()

class Slider:
    def __init__(self, x, y, width, min_value=0, max_value=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = 8
        self.min_value = min_value
        self.max_value = max_value
        self.value = 50
        self.handle_radius = 12
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, (180, 180, 180), (self.x, self.y - self.height // 2, self.width, self.height))
        handle_x = self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width
        pygame.draw.circle(surface, (255, 0, 0), (int(handle_x), self.y), self.handle_radius)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_over_handle(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x = event.pos[0]
            relative_x = max(self.x, min(mouse_x, self.x + self.width))
            percent = (relative_x - self.x) / self.width
            self.value = self.min_value + percent * (self.max_value - self.min_value)

    def is_over_handle(self, pos):
        handle_x = self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width
        handle_y = self.y
        distance = ((pos[0] - handle_x) ** 2 + (pos[1] - handle_y) ** 2) ** 0.5
        return distance <= self.handle_radius

class Menu:
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        
        self.global_font = pygame.font.Font(None, 74)
        self.label = self.global_font.render("Наркомир", True, (0, 0, 0))
        
        self.text_width = self.label.get_width()
        self.text_height = self.label.get_height() + 200
        
        self.start_btn = pygame.Rect(self.width // 2 - self.text_width + 75, self.height // 2 - 25, 350, 100)
        self.start_lbl = self.global_font.render("Начать игру", True, (0, 0, 0))

        self.option_btn = pygame.Rect(self.width // 2 - self.text_width + 75, self.height // 2 + 100, 350, 100)
        self.option_lbl = self.global_font.render("Настройки", True, (0, 0, 0))
        self.option_back = pygame.Rect(self.width// 2 - self.text_width + 75, self.height // 2 + 50, 350, 100)
        self.option_back_lbl = self.global_font.render("Вернуться", True, (0, 0, 0))
        self.option_menu_flg = False

        self.donat_btn = pygame.Rect(self.width// 2 - self.text_width + 75, self.height // 2 + 225, 350, 100)
        self.donat_lbl = self.global_font.render("Донат", True, (0, 0, 0))

        self.quit_btn = pygame.Rect(self.width// 2 - self.text_width + 75, self.height // 2 + 350, 350, 100)
        self.quit_lbl = self.global_font.render("Выйти", True, (0, 0, 0))
    
        self.basic_menu = True
        self.basic_volume = 50 

        self.volume_slider = Slider(self.width// 2 - 200, self.height // 2, 400)

    def blit_text(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        buttons = [self.start_btn, self.option_btn, self.donat_btn, self.quit_btn]
        
        if self.basic_menu:
            for btn in buttons:
                if btn.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, "darkgray", btn)
                else:
                    pygame.draw.rect(screen, "lightgray", btn)
                
            screen.blit(self.label, ((self.width - self.text_width) // 2, (self.height - self.text_height) // 2))
            screen.blit(self.start_lbl, (self.start_btn.x + 20, self.start_btn.y + 25))
            screen.blit(self.option_lbl, (self.option_btn.x + 40, self.option_btn.y + 25))
            screen.blit(self.donat_lbl, (self.donat_btn.x + 90, self.donat_btn.y + 25))
            screen.blit(self.quit_lbl, (self.quit_btn.x + 90, self.quit_btn.y + 25))
        elif self.option_menu:
            self.volume_slider.draw(screen)
            if self.option_back.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "darkgray", self.option_back)
            else:
                pygame.draw.rect(screen, "lightgray", self.option_back)
            screen.blit(self.option_back_lbl, (self.option_back.x + 45, self.option_back.y + 25))

            volume_text = self.global_font.render(f"Громкость: {int(self.volume_slider.value)}%", True, (0, 0, 0))
            screen.blit(volume_text, (self.width// 2 - volume_text.get_width() // 2, self.height // 2 - 100))

    def option_menu(self):
        self.basic_menu = False
        self.option_menu_flg = True