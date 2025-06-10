import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0
		self.score = 0
		self.max_speed = 300
		self.thrust_power = 400
		self.friction = 0.95

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]


	def draw(self, screen):
		pygame.draw.polygon(screen, "yellow", self.triangle(), 2)


	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt


	def update(self, dt):
		self.acceleration = pygame.Vector2(0, 0)
		self.shoot_timer -= dt
		self.wrap_around_screen()
		keys = pygame.key.get_pressed()


		if keys[pygame.K_w]:
			thrust_direction = pygame.Vector2(0, 1).rotate(self.rotation)
			self.acceleration = thrust_direction * self.thrust_power
		elif keys[pygame.K_s]:
			thrust_direction = pygame.Vector2(0, -1).rotate(self.rotation)  # Reverse
			self.acceleration = thrust_direction * self.thrust_power


		if keys[pygame.K_a]:
			self.rotation -= PLAYER_TURN_SPEED * dt
		if keys[pygame.K_d]:
			self.rotation += PLAYER_TURN_SPEED * dt
		if keys[pygame.K_SPACE]:
			self.shoot()

		self.velocity += self.acceleration * dt

		if not (keys[pygame.K_w] or keys[pygame.K_s]):
			self.velocity *= self.friction

		if self.velocity.length() > self.max_speed:
			self.velocity.scale_to_length(self.max_speed)

		self.position += self.velocity * dt


	def shoot(self):
		if self.shoot_timer > 0:
			return
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

	def current_score(self, asteroid):
		if asteroid.radius >= 50:
			self.score += 20
		elif asteroid.radius >= 30:
			self.score += 40
		else:
			self.score += 80

	def get_score(self):
		return self.score

	def player_spawn(self):
		return Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

