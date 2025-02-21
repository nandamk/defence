import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starship Defense")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Starship class
class Starship:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 60
        self.speed = 5
        
    def draw(self):
        # Draw colorful starship
        pygame.draw.polygon(screen, BLUE, [(self.x, self.y + self.height),
                                         (self.x + self.width, self.y + self.height),
                                         (self.x + self.width // 2, self.y)])
        pygame.draw.rect(screen, RED, (self.x + 10, self.y + 10, 20, 20))
        
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

# Rocket class
class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.radius = 5
        
    def move(self):
        self.y -= self.speed
        
    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

# Alien classes (10 different types)
class Alien:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 30)
        self.y = random.randint(-150, -50)
        self.speed = random.uniform(1, 3)
        self.type = random.randint(1, 10)
        self.size = random.randint(20, 40)
    
    def move(self):
        self.y += self.speed
    
    def draw(self):
        if self.type == 1:  # Circle
            pygame.draw.circle(screen, RED, (self.x, self.y), self.size // 2)
        elif self.type == 2:  # Square
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))
        elif self.type == 3:  # Triangle
            pygame.draw.polygon(screen, PURPLE, [(self.x, self.y + self.size),
                                               (self.x + self.size, self.y + self.size),
                                               (self.x + self.size // 2, self.y)])
        elif self.type == 4:  # Diamond
            pygame.draw.polygon(screen, CYAN, [(self.x + self.size // 2, self.y),
                                             (self.x + self.size, self.y + self.size // 2),
                                             (self.x + self.size // 2, self.y + self.size),
                                             (self.x, self.y + self.size // 2)])
        elif self.type == 5:  # Pentagon
            points = []
            for i in range(5):
                angle = 2 * math.pi * i / 5
                points.append((self.x + self.size // 2 * math.cos(angle) + self.size // 2,
                             self.y + self.size // 2 * math.sin(angle) + self.size // 2))
            pygame.draw.polygon(screen, YELLOW, points)
        elif self.type == 6:  # Star
            points = []
            for i in range(10):
                angle = 2 * math.pi * i / 10
                radius = self.size // 2 if i % 2 == 0 else self.size // 4
                points.append((self.x + radius * math.cos(angle) + self.size // 2,
                             self.y + radius * math.sin(angle) + self.size // 2))
            pygame.draw.polygon(screen, BLUE, points)
        elif self.type == 7:  # Hexagon
            points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                points.append((self.x + self.size // 2 * math.cos(angle) + self.size // 2,
                             self.y + self.size // 2 * math.sin(angle) + self.size // 2))
            pygame.draw.polygon(screen, RED, points)
        elif self.type == 8:  # Octagon
            points = []
            for i in range(8):
                angle = 2 * math.pi * i / 8
                points.append((self.x + self.size // 2 * math.cos(angle) + self.size // 2,
                             self.y + self.size // 2 * math.sin(angle) + self.size // 2))
            pygame.draw.polygon(screen, GREEN, points)
        elif self.type == 9:  # Cross
            pygame.draw.rect(screen, PURPLE, (self.x, self.y + self.size // 4, self.size, self.size // 2))
            pygame.draw.rect(screen, PURPLE, (self.x + self.size // 4, self.y, self.size // 2, self.size))
        elif self.type == 10:  # Ring
            pygame.draw.circle(screen, CYAN, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)
            pygame.draw.circle(screen, BLACK, (self.x + self.size // 2, self.y + self.size // 2), self.size // 3)

# Create star background
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Game objects
player = Starship()
rockets = []
aliens = []
score = 0
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Main game loop
running = True
alien_spawn_timer = 0

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire multiple rockets (3 at a time)
                rockets.append(Rocket(player.x + player.width // 2 - 10, player.y))
                rockets.append(Rocket(player.x + player.width // 2, player.y))
                rockets.append(Rocket(player.x + player.width // 2 + 10, player.y))

    # Move starship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Spawn aliens
    alien_spawn_timer += 1
    if alien_spawn_timer >= 30:  # Spawn every 30 frames
        aliens.append(Alien())
        alien_spawn_timer = 0

    # Update game objects
    # Move rockets
    for rocket in rockets[:]:
        rocket.move()
        if rocket.y < 0:
            rockets.remove(rocket)

    # Move aliens
    for alien in aliens[:]:
        alien.move()
        if alien.y > HEIGHT:
            aliens.remove(alien)

    # Collision detection
    for rocket in rockets[:]:
        for alien in aliens[:]:
            alien_rect = pygame.Rect(alien.x, alien.y, alien.size, alien.size)
            if alien_rect.collidepoint(rocket.x, rocket.y):
                rockets.remove(rocket)
                aliens.remove(alien)
                score += 10
                break

    # Check if aliens hit player
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    for alien in aliens[:]:
        alien_rect = pygame.Rect(alien.x, alien.y, alien.size, alien.size)
        if player_rect.colliderect(alien_rect):
            running = False

    # Draw everything
    screen.fill(BLACK)
    
    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)

    # Draw game objects
    player.draw()
    for rocket in rockets:
        rocket.draw()
    for alien in aliens:
        alien.draw()

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
