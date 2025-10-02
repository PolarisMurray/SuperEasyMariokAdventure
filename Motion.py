import pygame

# 1.init Pygame
pygame.init()

# window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D 瑪利歐 - 專案一")

# COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# character photo
try:
    player_image = pygame.image.load('mario.png').convert_alpha()
    player_image = pygame.transform.scale(player_image, (50, 50)) 
except pygame.error as e:
    print("錯誤：找不到 mario.png 圖片，請確認檔案是否存在。")
    player_image = pygame.Surface((50, 50))
    player_image.fill(WHITE) 


player_x = 50
player_y = 500
player_speed = 5
