import pygame
from os import walk
from playbutton import PlayButton
from forwardbutton import ForwardButton
from previousbutton import PreviousButton
from simple_waveform import SimpleWaveform

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 415, 515

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font("assets/fonts/SuperPixel.ttf", 20)
pygame.display.set_caption("Pixel Player")

# Loading assets
play_button_image = pygame.image.load("assets/images/play.png").convert_alpha()
play_hover_button_image = pygame.image.load(
    "assets/images/play_hover.png"
).convert_alpha()
pause_button_image = pygame.image.load("assets/images/pause.png").convert_alpha()
pause_hover_button_image = pygame.image.load(
    "assets/images/pause_hover.png"
).convert_alpha()
forward_button_image = pygame.image.load("assets/images/next.png").convert_alpha()
forward_hover_button_image = pygame.image.load(
    "assets/images/next_hover.png"
).convert_alpha()
previous_button_image = pygame.image.load("assets/images/previous.png").convert_alpha()
previous_hover_button_image = pygame.image.load(
    "assets/images/previous_hover.png"
).convert_alpha()

# Get size to center easily
button_width, button_height = play_button_image.get_size()

# Center of application
center_x = (SCREEN_WIDTH - button_width) // 2
center_y = (SCREEN_HEIGHT - button_height) // 2

clock = pygame.time.Clock()

queue = []
playing = {"song": "No song playing....."}
played = []
paused = {"value": True}

for dirpath, dirnames, filenames in walk("music"):
    queue.append(filenames)
    break

# Load all the songs before starting the application. (Don't think this works..)
# for song in queue[0]:
#     pygame.mixer.music.load(f"music/{song}")


def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def pause_music():
    pygame.mixer.music.pause()


def resume_music():
    pygame.mixer.music.unpause()


def next_song(next_song):
    pygame.mixer.music.stop()
    play_music(next_song)
    pygame.mixer.music.play()


def previous_song(previous_song):
    pygame.mixer.music.stop()
    play_music(previous_song)
    pygame.mixer.music.play()


play_button = PlayButton(
    center_x,
    360,
    pause_button_image,
    play_button_image,
    pause_hover_button_image,
    play_hover_button_image,
    queue,
    playing,
    play_music,
    resume_music,
    pause_music,
    played,
    paused,
)

forward_button = ForwardButton(
    center_x + 135,
    360,
    forward_button_image,
    forward_hover_button_image,
    queue,
    play_music,
    played,
    paused,
    playing
)

previous_button = PreviousButton(
    center_x - 135,
    360,
    previous_button_image,
    previous_hover_button_image,
    play_music,
    played,
    paused,
    playing
)

# Create simple waveform visualizer
waveform = SimpleWaveform(20, 50, SCREEN_WIDTH - 40, 200, num_points=80)

def render_scaled_text(text, font_path, max_width, color, initial_size=20, min_size=10):
    size = initial_size
    while size >= min_size:
        font = pygame.font.Font(font_path, size)
        rendered = font.render(text, True, color)
        if rendered.get_width() <= max_width:
            return rendered
        size -= 1
    # If it never fits, return the smallest size
    return font.render(text, True, color)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        play_button.handle_mouse(event)
        forward_button.handle_mouse(event)
        previous_button.handle_mouse(event)

    clock.tick(60)
    screen.fill((200, 182, 255))
    
    # Update and draw the simple waveform
    waveform.update()
    waveform.draw(screen)
    
    app_title = font.render("Pixel Player", True, (255, 255, 255))
    song_title = render_scaled_text(
        playing["song"][0:-4],
        "assets/fonts/SuperPixel.ttf",
        SCREEN_WIDTH - 40,  # 20px padding on each side
        (255, 255, 255),
        initial_size=20,
        min_size=10
    )
    screen.blit(app_title, (110, 10))
    screen.blit(song_title, (20, 300))
    play_button.draw(screen)
    forward_button.draw(screen)
    previous_button.draw(screen)
    if not paused["value"]:
        play_button.image = pause_button_image
    pygame.display.update()
    clock.tick(60)
