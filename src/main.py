# import and init pygame
import pygame
import random
pygame.init()

# information needed to draw the grid
class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	GREY = 128, 128, 128
	BACKGROUND_COLOR = WHITE

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting algorithm visualizer")
		self.set_list(lst)

	def set_list(self, lst)

# set up the drawing window
screen = pygame.display.set_mode([500, 500])

# run until quit
running = True
while running:

	# quit if user presses exit button
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# fill the background with white color
	screen.fill((255, 255, 255))

	# draw a square in the center
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(250, 250, 50, 50))

	#update display
	pygame.display.update()

# quit
pygame.quit()