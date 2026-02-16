import pygame

print('Setup Start')
pygame.init()
print('Setup end')
window = pygame.display.set_mode(size=(750, 580))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('Quintting...')
            Pygame.quit()  # Close window
            quit()  # end pygame
