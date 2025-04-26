import pygame
from main_menu import Menu
import cfg

pygame.init()
pygame.mixer.init()

screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)
clock = pygame.time.Clock()

running = True
menu = Menu(WIDTH, HEIGHT)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if menu.basic_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.option_btn.collidepoint(event.pos):
                    menu.basic_menu = False
                    menu.option_menu_flg = True
                    
        elif menu.option_menu_flg:
            menu.volume_slider.handle_event(event)
            menu.basic_volume = menu.volume_slider.value
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.option_back.collidepoint(event.pos):
                    menu.basic_menu = True
                    menu.option_menu_flg = False
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.quit_btn.collidepoint(event.pos):
                running = False
                    
    screen.fill((136, 136, 136))
    menu.blit_text(screen)
    
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()
