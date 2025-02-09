import pygame
import random

#Initialize Pygame
pygame.init()

#Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Ball Game")

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)

#Game variables
player_width = 100  
player_height = 20
player_x = (WIDTH  - player_width) // 2
player_y = HEIGHT - player_height - 50
player_speed = 7

ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = -ball_radius
ball_speed = 5

score = 0
font = pygame.font.SysFont('comic sans ma', 30)

#Set up the clock
clock = pygame.time.Clock()

#Function to draw the player (basket)
def draw_player(x, y):
    pygame.draw.rect(screen, PURPLE, (x, y, player_width, player_height))

#Function to draw the ball
def draw_ball(x, y):
    pygame.draw.circle(screen, BLUE, (x, y), ball_radius)

#Function to display the score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

#Main Loop
running = True
while running:
    screen.fill(BLACK)

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get the keys pressed
    keys = pygame.key.get_pressed()

    #Update player position
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    #Update ball position
    ball_y += ball_speed

    #If the ball reaches the bottom, reset it and update the score
    if ball_y > HEIGHT + ball_radius:
        ball_y = -ball_radius
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    #Check for collision with the player
    if (player_x < ball_x < player_x + player_width) and (player_y < ball_y < player_y + player_height):
        score += 1
        ball_y = -ball_radius
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    #Draw everything
    draw_player(player_x, player_y)
    draw_ball(ball_x, ball_y)
    display_score(score)

    #Update the display
    pygame.display.update()

    #Control frame rate
    clock.tick(60)

#Quit Pygame
pygame.quit()