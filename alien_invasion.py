import pygame
from pygame.sprite import Group

import game_functions
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("飞机大战")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_functions.update_screen(ai_settings, screen, ship, bullets)


run_game()
