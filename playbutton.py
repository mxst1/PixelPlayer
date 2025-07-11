import pygame
from random import randint


class PlayButton:
    def __init__(
        self,
        x,
        y,
        paused_button,
        playing_button,
        paused_hover,
        playing_hover,
        queue,
        playing,
        play_music,
        resume_music,
        pause_music,
        played,
        paused,
    ):
        self.paused_button = paused_button
        self.playing_button = playing_button
        self.paused_hover = paused_hover
        self.playing_hover = playing_hover
        self.image = playing_button
        self.queue = queue
        self.playing = playing
        self.play_music = play_music
        self.resume_music = resume_music
        self.pause_music = pause_music
        self.played = played
        self.rect = self.image.get_rect(topleft=(x, y))
        self.paused = paused

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                if self.paused["value"]:
                    self.image = self.playing_hover
                else:
                    self.image = self.paused_hover
            else:
                if self.paused["value"]:
                    self.image = self.playing_button
                else:
                    self.image = self.paused_button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.paused["value"]:
                if self.rect.collidepoint(event.pos):
                    # Code to be ran once button is pressed.
                    self.image = self.playing_button
                    print(len(self.queue[0]))
                    if self.playing["song"] == "No song playing.....":
                        self.play_music(
                            f"music/{self.queue[0][randint(0, len(self.queue[0])-1)]}"
                        )
                        self.played.append(
                            self.queue[0][randint(0, len(self.queue[0]) - 1)]
                        )
                        self.playing["song"] = self.queue[0][randint(0, len(self.queue[0]) - 1)]
                    else:
                        self.resume_music()
                    self.paused["value"] = False
                    print("Now Playing!")
            else:
                if self.rect.collidepoint(event.pos):
                    self.image = self.paused_button
                    print("Paused!")
                    self.pause_music()
                    self.paused["value"] = True
