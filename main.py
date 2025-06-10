import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion


def main():
	pygame.init()
	pygame.font.init()

	background = pygame.image.load("screen.png")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Explosion.containers = (updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	Player.containers = (updatable, drawable)
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


	score_font = pygame.font.Font("/home/kai/workspace/github.com/hermanvadym/asteroid/cour.ttf", 32)


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	dt = 0
	life_number = 3


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				if life_number == 1:
					print("Game over!")
					print(f"Your final score: {player.get_score()}.")
					sys.exit()

				elif life_number > 1:
					life_number -= 1
					player.kill()
					player = player.player_spawn()

			for shot in shots:
				if asteroid.collides_with(shot):
					explosion = Explosion(asteroid.position.x, asteroid.position.y)
					player.current_score(asteroid)
					shot.kill()
					asteroid.split()


		text_surface = score_font.render(f"SCORE: {player.get_score()}", False, (255, 255, 255))
		life_text = score_font.render(f"LIFE: {life_number}", False, (255, 255, 255))

		screen.blit(background, (0,0))
		screen.blit(text_surface, (40,30))
		screen.blit(life_text, (40, 70))

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()


		# limit the framerate to 60 FPS	
		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
