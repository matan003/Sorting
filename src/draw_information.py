# information needed to draw the grid
import pygame

pygame.init()

class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('calibri', 20)
	LARGE_FONT = pygame.font.SysFont('calibri', 30)
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
		self.block_height = int((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

	def draw(self, algorithm_name, ascending):
		self.window.fill(self.BACKGROUND_COLOR)

		title = self.LARGE_FONT.render(f"{algorithm_name} - {'Ascending' if ascending else 'Descending'}", 1, self.GREEN)
		self.window.blit(title, (self.width/2 - title.get_width()/2, 5))

		controls = self.FONT.render("R - Reset | SPACE - Start sorting | A - Ascending | D - Descending", 1, self.BLACK)
		self.window.blit(controls, (self.width/2 - controls.get_width()/2, 45))

		sorting = self.FONT.render("I - Insertion sort | B - Bubble sort", 1, self.BLACK)
		self.window.blit(sorting, (self.width/2 - sorting.get_width()/2, 75))
		
		self.draw_list()
		pygame.display.update()

	def draw_list(self, color_positions={}, clear_bg=False):
		if clear_bg:
			clear_rect = (self.SIDE_PAD//2, self.TOP_PAD, self.width - self.SIDE_PAD, self.height - self.TOP_PAD)
			pygame.draw.rect(self.window, self.BACKGROUND_COLOR, clear_rect)

		for i, val in enumerate(self.lst):
			x = self.start_x + i * self.block_width
			y = self.height - (val - self.min_val) * self.block_height

			color = self.GRADIENTS[i % 3]

			if i in color_positions:
				color = color_positions[i]

			#print(self.block_height)
			pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height)) # fix this
		
		if clear_bg:
			pygame.display.update()