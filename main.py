# import the necessary modules
import smart_audio_selector
import audio_player
   

if __name__ == "__main__":
    audio_directory = "Smart-Audio-player-\\Music_Lib"  # Replace with your actual audio directory path

    # Initialize the AudioSelector with the desired mode ("auto" or "manual")
    selector = smart_audio_selector.AudioSelector(audio_directory, mode="auto")  # Change mode to "manual" for manual selection

    # Use the music_selector method to get the selected audio file
    audio_files = selector.music_selector()

    # If an audio file is selected, play it using the AudioPlayer
    if audio_files:
        # Initialize the AudioPlayer with the selected audio file
        player = audio_player.AudioPlayer(audio_files)
        player.play()

        # Wait for user input to stop playback
        input("Press Enter to stop playback...")
        player.stop()
