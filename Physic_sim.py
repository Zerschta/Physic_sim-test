import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physik-Simulation")

# Farben
WHITE = (0, 0, 0)
RED = (255, 0, 0)

# Ball Klasse
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    # Methode zur Aktualisierung der Position des Balls
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Überprüfen der Kollision mit den Wänden
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.speed_y *= -1

    # Methode zum Zeichnen des Balls
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Ball erstellen
ball = Ball(WIDTH // 2, HEIGHT // 2, 20, RED, 0.1, 0.1)

# Hauptfunktion
def main():
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
           

        # Ball aktualisieren
        ball.update()

        # Ball zeichnen
        ball.draw()

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

print("Made by deiner mom")

if __name__ == "__main__":
    main()


"""

Neu Schreiben sieht kacke aus ChatGPT macht es Strange 
- ball = Ball(WIDTH // 2, HEIGHT // 2, 20, RED, 0.1, 0.1) ? 

"""