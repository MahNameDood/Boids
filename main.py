import pygame, sys, random
import bird, predator

pygame.init()

WIDTH = 1900
HEIGHT = 1100
win_dim = (WIDTH, HEIGHT)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BOIDS !!!')
clock = pygame.time.Clock()

birds = bird.spawn_birds(300, win_dim)
predators = predator.spawn_predators(0, win_dim)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	win.fill((0,0,0))

	predators = predator.update_predators(predators, birds, win_dim)
	predator.render_predators(predators, win)

	birds = bird.update_birds(predators, birds, win_dim)
	bird.render_birds(birds, win)

	pygame.display.update()
	clock.tick(60)