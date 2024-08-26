import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BEE_SIZE = 50
FLOWER_SIZE = 30
SPEED = 5

# Load the images
bee_image = pygame.image.load('bee.png')
bee_image = pygame.transform.scale(bee_image, (BEE_SIZE, BEE_SIZE))
flower_image = pygame.image.load('flower.png')
flower_image = pygame.transform.scale(flower_image, (FLOWER_SIZE, FLOWER_SIZE))
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the bee and flower positions
bee_x, bee_y = WIDTH / 2, HEIGHT / 2
flower_x, flower_y = random.randint(0, WIDTH - FLOWER_SIZE), random.randint(0, HEIGHT - FLOWER_SIZE)

# Set up the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the bee
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bee_y -= SPEED
    if keys[pygame.K_DOWN]:
        bee_y += SPEED
    if keys[pygame.K_LEFT]:
        bee_x -= SPEED
    if keys[pygame.K_RIGHT]:
        bee_x += SPEED

    # Check for collision with the flower
    if (bee_x + BEE_SIZE > flower_x and
        bee_x < flower_x + FLOWER_SIZE and
        bee_y + BEE_SIZE > flower_y and
        bee_y < flower_y + FLOWER_SIZE):
        score += 1
        flower_x, flower_y = random.randint(0, WIDTH - FLOWER_SIZE), random.randint(0, HEIGHT - FLOWER_SIZE)

    # Draw everything
    screen.blit(background_image, (0, 0))
    screen.blit(bee_image, (bee_x, bee_y))
    screen.blit(flower_image, (flower_x, flower_y))
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)