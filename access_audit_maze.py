import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Access Audit Maze - Malware Edition")

# Load the malware character image and scale it
malware_image = pygame.image.load('malware.png')  # Ensure 'malware.png' is in the same folder
malware_image = pygame.transform.scale(malware_image, (30, 30))

# Define initial position and speed for the malware character
malware_x, malware_y = 50, 50
malware_speed = 5

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black as the background
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get pressed keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        malware_x -= malware_speed
    if keys[pygame.K_RIGHT]:
        malware_x += malware_speed
    if keys[pygame.K_UP]:
        malware_y -= malware_speed
    if keys[pygame.K_DOWN]:
        malware_y += malware_speed

    # Draw the malware character
    screen.blit(malware_image, (malware_x, malware_y))
    
    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Set frame rate to 30 FPS

# Quit Pygame
pygame.quit()
