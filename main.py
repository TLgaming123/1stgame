import pygame
import os

WIDTH, HEIGHT = 1280, 720

ITEM_WIDTH, ITEM_HEIGHT = (2/45) * WIDTH, 0.08 * HEIGHT

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BOB_IDLE_IMAGE = pygame.image.load(os.path.join('Assets', 'Characters', 'Bob', 'Bob_Idle.png'))

BOB_IDLE = pygame.transform.scale(BOB_IDLE_IMAGE, (ITEM_WIDTH, ITEM_HEIGHT))

BOB_NEUTRAL_IMAGE = pygame.image.load(os.path.join('Assets', 'Characters', 'Bob', 'Bob_Neutral.png'))

BOB_NEUTRAL = pygame.transform.scale(BOB_NEUTRAL_IMAGE, (ITEM_WIDTH, ITEM_HEIGHT))

BOB_RUN1_IMAGE = pygame.image.load(os.path.join('Assets', 'Characters', 'Bob', 'Bob_Run1.png'))

BOB_RUN1 = pygame.transform.scale(BOB_RUN1_IMAGE, (ITEM_WIDTH, ITEM_HEIGHT))

BOB_RUN2_IMAGE = pygame.image.load(os.path.join('Assets', 'Characters', 'Bob', 'Bob_Run2.png'))

BOB_RUN2 = pygame.transform.scale(BOB_RUN1_IMAGE, (ITEM_WIDTH, ITEM_HEIGHT))

pygame.display.set_caption("Game")

FPS = 60

SKY = (94, 191, 252)

TRANSITION_NIGHT = True

TRANSITION_DAY = False

FACING = 1

FRAMES_RIGHT = 0

FRAMES_LEFT = 0

def Load_Bob(FACING, BOB_IDLE, BOB_NEUTRAL, BOB_RUN1, BOB_RUN2, FRAMES_RIGHT, FRAMES_LEFT):
    if pygame.key.get_pressed()[pygame.K_d]:
        print("blsa")
    if pygame.key.get_pressed()[pygame.K_a]:
        print("blsa")
    else:
        if FACING == 1:
            WINDOW.blit(BOB_IDLE, (WIDTH // 2 - (ITEM_WIDTH // 2), HEIGHT - (3 * ITEM_HEIGHT)))
        elif FACING == 0:
            BOB_IDLE = pygame.transform.flip(BOB_IDLE, False, True)
            WINDOW.blit(BOB_IDLE, (WIDTH // 2 - (ITEM_WIDTH // 2), HEIGHT - (3 * ITEM_HEIGHT)))
        else:
            print("unknown direction")
     

def draw_window():
    WINDOW.fill(SKY)

    Load_Bob(FACING, BOB_IDLE, BOB_NEUTRAL, BOB_RUN1, BOB_RUN2, FRAMES_RIGHT, FRAMES_LEFT)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit

if __name__ == "__main__":
    main()