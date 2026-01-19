import pygame 
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS, PLAYER_INVINIBILITY_TIMER
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from score import Score


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Score()
    
    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                if player.invincibility_timer <= 0:  # Only damage if NOT invincible
                    log_event("player_hit")
                    player.lives -= 1
                    player.invincibility_timer = PLAYER_INVINIBILITY_TIMER  # Activate invincibility
                    score.subtract_score(25)  # Lose points
                    asteroid.kill()  # Destroy the asteroid
                    if player.lives <= 0:
                        log_event("player_died")
                        text_surface = font.render(f"Game over! Score: {score.get_score()}", True, "white")
                        screen.blit(text_surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                        pygame.display.flip()
                        waiting = True
                        while waiting:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return
                                if event.type == pygame.KEYDOWN:
                                    return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score.add_score(10)
        for thing in drawable:
            thing.draw(screen)
        text_surface = font.render(f"Score: {score.get_score()}", True, "white")
        screen.blit(text_surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 25))
        text_surface = font.render(f"Lives: {player.lives}", True, "white")
        screen.blit(text_surface, (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()