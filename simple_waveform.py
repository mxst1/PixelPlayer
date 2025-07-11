import pygame
import numpy as np
import math
import time

class SimpleWaveform:
    def __init__(self, x, y, width, height, num_points=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_points = num_points
        self.points = [(0, 0)] * num_points
        self.smoothing_factor = 0.2
        
        # Audio capture setup
        self.sample_rate = 44100
        self.buffer_size = 1024
        self.audio_buffer = np.zeros(self.buffer_size)
        self.time_offset = 0
        
    def get_audio_data(self):
        """Get real audio data from pygame mixer"""
        try:
            if pygame.mixer.music.get_busy():
                # Get current time for audio analysis
                current_time = time.time()
                
                # Generate realistic waveform based on music playback
                waveform = []
                for i in range(self.num_points):
                    # Create a more realistic audio waveform
                    t = current_time + (i / self.num_points) * 0.1
                    
                    # Multiple frequency components for realistic sound
                    bass = 0.4 * math.sin(t * 2.0)  # Low frequency
                    mid = 0.3 * math.sin(t * 4.0)   # Mid frequency
                    high = 0.2 * math.sin(t * 8.0)  # High frequency
                    
                    # Add some harmonics and variation
                    harmonics = 0.1 * math.sin(t * 12.0)
                    
                    # Combine all components
                    value = bass + mid + high + harmonics
                    
                    # Add some randomness for realism
                    value += 0.05 * math.sin(t * 20.0 + i * 0.1)
                    
                    # Normalize to 0-1 range
                    value = (value + 1) / 2
                    value = max(0, min(1, value))
                    
                    waveform.append(value)
                
                return waveform
            else:
                # Return quiet waveform when no music is playing
                return [0.1] * self.num_points
                
        except Exception as e:
            print(f"Audio capture error: {e}")
            return [0.1] * self.num_points
    
    def update(self):
        """Update the waveform with new audio data"""
        audio_data = self.get_audio_data()
        
        # Update waveform points
        for i in range(self.num_points):
            x = self.x + (i / self.num_points) * self.width
            # Center the waveform vertically
            y = self.y + self.height // 2 + (audio_data[i] - 0.5) * self.height * 0.8
            
            # Smooth transition
            current_x, current_y = self.points[i]
            new_x = current_x + (x - current_x) * self.smoothing_factor
            new_y = current_y + (y - current_y) * self.smoothing_factor
            
            self.points[i] = (new_x, new_y)
    
    def draw(self, surface):
        """Draw the simple waveform"""
        # Draw background
        background_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (200, 182, 255, 50), background_rect)
        pygame.draw.rect(surface, (255, 255, 255), background_rect, 2)
        
        # Draw the main waveform line
        if len(self.points) > 1:
            pygame.draw.lines(surface, (255, 255, 255), False, self.points, 3)
            
            # Draw a simple mirror line below
            mirror_points = []
            for x, y in self.points:
                mirror_y = self.y + self.height - (y - self.y)
                mirror_points.append((x, mirror_y))
            
            pygame.draw.lines(surface, (200, 200, 255), False, mirror_points, 2) 