import time
import random
import os

def flappy_bird():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    height = 10
    bird_y = height // 2
    gravity = 1
    jump = -2

    obstacles = []

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')

        # Check for user input
        key = input("Press Enter to jump, or 'q' to quit: ")
        if key == 'q':
            break
        elif key == '':
            bird_y += jump
        else:
            bird_y += gravity

        # Draw bird
        print('\n' * bird_y + '^')

        # Generate obstacles
        if random.randint(0, 5) == 0:
            obstacle_height = random.randint(1, height - 2)
            obstacles.append([obstacle_height])

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle[0] -= 1
            print(' ' * obstacle[0] + '|')

        obstacles = [obs for obs in obstacles if obs[0] > 0]

        # Check for collisions
        if bird_y >= height - 1 or bird_y <= 0:
            break

        for obstacle in obstacles:
            if obstacle[0] == 1 and bird_y != obstacle[0]:
                break
        else:
            continue
        break

        time.sleep(0.1)

flappy_bird()
