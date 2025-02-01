import pygame
import random

#Initialize Pygame
pygame.init()

#Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) #Food colour
GREEN = (0, 255, 0) #Snake colour
BLUE = (0, 0, 255) #Background colour
GRAY = (128, 128, 128) #F=Gray for the border/other UI elements

#Screen dimensions
width = 600
height = 400

#Create the screen object
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#Snake and food block size
block_size = 20

#Clock object to control the speed of the snake
clock = pygame.time.Clock()

#Font for game over
font_style = pygame.font.SysFont("bahnschrift", 25)

#Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

#Function to display the score or game over message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/6, height/3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_list = []
    length_of_snake = 1

    # Randomly position the food
    foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", WHITE)
            pygame.display.update()

            # Check for user input to quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check if the snake hits the wall
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Draw the food
        pygame.draw.rect(screen, RED, [foodx, foody, block_size, block_size])

        # Draw the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        #Check if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(10) #Control the speed of the game

    pygame.quit()
    quit()

#Start the game
gameLoop()