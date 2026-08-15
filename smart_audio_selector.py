import os
import re

class AudioSelector:
    def __init__(self, audio_directory, mode="manual"):
        self.audio_directory = audio_directory
        self.mode = mode  # Default mode is manual selection


    # List all audio files in the specified directory
    def list_audio_files(self):
        if os.path.exists(self.audio_directory):
            audio_files = [f for f in os.listdir(self.audio_directory) if f.endswith('.mp3') or f.endswith('.wav')]
            return audio_files
        else:
            print(f"Audio directory not found: {self.audio_directory}")
            return []

    # Get the full path of the selected audio file
    def get_audio_file_path(self, file_name):
        file_path = os.path.join(self.audio_directory, file_name)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"Audio file not found: {file_path}")
            return None

    # Clean and extract keywords from a given text
    def get_clean_keywords(self, text):
        # Remove special characters and convert to lowercase
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text).lower()
        # Replace multiple spaces with a single space
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        # Split into individual keywords and return as a list
        keywords = cleaned_text.split(' ')
        return keywords    

    # Get the best matching audio file based on user prompt and available audio files
    def get_best_match(self, user_prompt, audio_files=None):

        if audio_files is None:
            audio_files = []
            print("No audio files available for matching.")
            return None  

        # Calculate matching score based on the number of matching keywords
        prompt_keywords = set(self.get_clean_keywords(user_prompt))
        print(f"Keywords from user prompt: {prompt_keywords}")
        best_match = None
        best_score = 0    

        # Iterate through the audio files and calculate the matching score
        for file in audio_files:
            file_keywords = set(self.get_clean_keywords(file))
            print(f"Keywords from audio file '{file}': {file_keywords}")
            score = len(prompt_keywords.intersection(file_keywords))
            print(f"Matching score for '{file}': {score}")
            if score > best_score:
                best_score = score
                best_match = file    

        # Return the best matching audio file if found, otherwise return None
        if best_match:
            selected_file = self.get_audio_file_path(best_match)
            print(f"Selected audio file based on matching score: {selected_file}")
            return selected_file
        else:
            print("No matching audio files found based on the provided keywords.")
            return None    


    # Method to select music based on the specified mode (auto or manual)
    def music_selector(self):

        # If the mode is set to "auto", prompt the user for a description and find the best match
        if self.mode == "auto":
            user_prompt = input("Enter a description of the music you want to listen to: ")
            audio_files = self.list_audio_files()
            selected_file = self.get_best_match(user_prompt, audio_files)
            if selected_file:
                print(f"Selected audio file: {selected_file}")
                return selected_file
            else:
                print("No suitable audio file found based on your description.")
                return None

        # If the mode is set to "manual", list available audio files and allow the user to select one
        else: 
            audio_files = self.list_audio_files()
            if not audio_files:
                print("No audio files available for selection.")
                return None
            print("Available audio files:")
            for idx, file in enumerate(audio_files):
                print(f"{idx + 1}. {file}")
            selection = input("Select an audio file by number: ")
            if selection.isdigit() and 1 <= int(selection) <= len(audio_files):
                selected_file = self.get_audio_file_path(audio_files[int(selection) - 1])
                if selected_file:
                    print(f"Selected audio file: {selected_file}")
                    return selected_file
            else:
                print("Invalid selection.")
                return None
        
    