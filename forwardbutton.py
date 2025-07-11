import pygame
from random import randint

class ForwardButton:
    def __init__(
        self,
        x,
        y,
        button_image,
        image_hover,
        queue,
        play_music,
        played,
        paused,
        playing
    ):
        self.button_image = button_image
        self.image = button_image
        self.image_hover = image_hover
        self.queue = queue
        self.play_music = play_music
        self.played = played
        self.paused = paused
        self.playing = playing
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                # Code once mouse hovers over
                self.image = self.image_hover
                pass
            else:
                self.image = self.button_image
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                # Code to be ran once button is pressed.
                rand_song = self.queue[0][randint(0, len(self.queue[0])-1)]
                self.play_music(f"music/{rand_song}")
                self.playing["song"] = rand_song
                self.played.append(rand_song)
                self.paused["value"] = False
                pass
