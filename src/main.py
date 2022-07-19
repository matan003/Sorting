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

	GRADIENTS = [
		GREY,
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('comicsans', 30)
	LARGE_FONT = pygame.font.SysFont('comicsans', 40)
	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting algorithm visualizer")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

	def draw(self):
		self.window.fill(self.BACKGROUND_COLOR)
		self.draw_list()
		pygame.display.update()

	def draw_list(self):
		for i, val in enumerate(self.lst):
			x = self.start_x + i * self.block_width
			y = self.height - (val - self.min_val) * self.block_height

			color = self.GRADIENTS[i % 3]
			print(self.block_height)
			pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height)) # fix this

def generate_starting_list(n, min_val, max_val):
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst

def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInformation(800, 600, lst)
	sorting = False
	ascending = True

	print(draw_info.height)

	while run:
		clock.tick(60)

		draw_info.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			if event.type != pygame.KEYDOWN:
				continue
				
			if event.key == pygame.K_r:
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
			
			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False

	pygame.quit()

if __name__ == "__main__":
	main()