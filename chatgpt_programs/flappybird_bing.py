import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((288, 512))
bird_surface = pygame.image.load('bird.png').convert_alpha()
bird_surface = pygame.transform.scale(bird_surface, (50, 50))  # Resize to 50x50 pixels
bird_rect = bird_surface.get_rect(center = (100,512))

bg_surface = pygame.image.load('background.png').convert()
# Game Variables
gravity = 0.25
bird_movement = 0
bird_rect = bird_surface.get_rect(center = (100,512))

floor_surface = pygame.image.load('floor.png').convert()
floor_x_pos = 0

pipe_surface = pygame.image.load('pipe.png').convert()
pipe_height = [200, 300, 400]

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird


def draw_bird():
    screen.blit(bird_surface,bird_rect)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False

    return True

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def main():
    clock = pygame.time.Clock()
    game_active = True 
    bird_movement = 0 
    pipe_list = []
    floor_x_pos = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 12
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100,512)
                    bird_movement = 0

        screen.blit(bg_surface,(0,0))

        if game_active:
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird,bird_rect)
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # Add this line at the beginning of your main function
            SPAWNPIPE = pygame.USEREVENT
            pygame.time.set_timer(SPAWNPIPE, 1200)  # Creates a new pipe every 1.2 seconds

            # Then in your game loop, add this condition
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())

            

        # Floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -576:
            floor_x_pos = 0

        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()
