import pygame

pygame.init()

class Button:
	name = None
	text = None
	rect = None

	def __init__(self, name):
		self.name = name