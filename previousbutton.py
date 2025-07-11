import pygame

class PreviousButton:
    def __init__(
        self,
        x,
        y,
        button_image,
        image_hover,
        play_music,
        played,
        paused,
        playing
    ):
        self.button_image = button_image
        self.image_hover = image_hover
        self.image = button_image
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
                if self.played == [] or len(self.played) == 1:
                    return
                self.played.pop()
                self.play_music(f"music/{self.played[-1]}")
                self.paused["value"] = False
                self.playing["song"] = self.played[-1]
                pass
