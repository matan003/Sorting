# import and init pygame
import pygame
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort

import draw_information

pygame.init()

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
	draw_info = draw_information.DrawInformation(800, 600, lst)
	sorting = False
	ascending = True

	sorting_algorithm = bubble_sort
	sorting_algorithm_name = "Bubble sort"
	sorting_algorithm_generator = None

	print(draw_info.height)

	while run:
		clock.tick(30)

		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False

		else:
			draw_info.draw(sorting_algorithm_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			if event.type != pygame.KEYDOWN:
				continue
				
			if event.key == pygame.K_r:
				sorting = False
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
			
			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			elif event.key == pygame.K_i and not sorting:
				sorting_algorithm = insertion_sort
				sorting_algorithm_name = "Insertion Sort"
			elif event.key == pygame.K_b and not sorting:
				sorting_algorithm = bubble_sort
				sorting_algorithm_name = "Bubble Sort"
			elif event.key == pygame.K_s and not sorting:
				sorting_algorithm = selection_sort
				sorting_algorithm_name = "Selection Sort"

	pygame.quit()

if __name__ == "__main__":
	main()