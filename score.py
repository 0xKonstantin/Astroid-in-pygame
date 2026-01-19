import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0

    def add_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score

    def subtract_score(self, amount):
        self.score -= amount