import os
import pygame

# Initialize the pygame mixer
pygame.mixer.init()

class AudioPlayer:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    # Play the audio file using pygame
    def play(self):
        if os.path.exists(self.audio_file):
            print(f"Playing audio file: {self.audio_file}")
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
        else:
            print(f"Audio file not found: {self.audio_file}")

    # Stop the audio playback
    def stop(self):
        print("Stopping audio playback.")
        pygame.mixer.music.stop()
        # Here you would add the code to stop the audio playback