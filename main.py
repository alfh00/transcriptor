from moviepy.editor import VideoFileClip
from pytube import YouTube
import subprocess
import speech_recognition as sr

# # URL of the YouTube video you want to download
# video_url = "https://youtu.be/2Cm9zeCeHfs?si=Byd2KkP-CLYdFoJJ"

# # Create a YouTube object
# yt = YouTube(video_url)

# # Choose the highest resolution stream (you can customize this)
# video_stream = yt.streams.get_highest_resolution()

# # Download the video to a specific directory (you can customize this)
# output_directory = "downloaded_videos/"
# video_path = output_directory + video_stream.default_filename
# video_stream.download(output_path=output_directory)

# print("Video downloaded successfully!")

# Function to extract audio from video
# def extract_audio(video_path, output_audio_path):
#     video = VideoFileClip(video_path)
#     audio = video.audio
#     audio.write_audiofile(output_audio_path)

# # Define audio and transcript file paths
# audio_path = "output_audio.wav"
# transcript_path = "transcript.txt"

# # # Extract audio from video
# # extract_audio(video_path, audio_path)




# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Function to perform speech recognition
# def transcribe_audio(audio_path):
#     # Load the audio file
#     with sr.AudioFile(audio_path) as source:
#         try:
#             # Adjust for ambient noise and listen for audio
#             recognizer.adjust_for_ambient_noise(source)
#             audio_data = recognizer.record(source)

#             # Perform Google Web Speech recognition
#             text = recognizer.recognize_vosk(audio_data, language="fr")  # Change to "fr-FR" for French
#             return text
#         except sr.UnknownValueError:
#             return "Speech recognition could not understand the audio"
#         except sr.RequestError as e:
#             return f"Could not request results from Google Web Speech Recognition; {e}"

# # Specify the path to the audio file
# audio_path = "output_audio.wav"

# # Perform speech recognition
# transcript = transcribe_audio(audio_path)

# # Print the transcript
# print("Recognized Text:")
# print(transcript)

# # Write the transcript to a text file
# with open("output.txt", "w", encoding="utf-8") as text_file:
#     text_file.write(transcript)

# print("Transcript written to 'output.txt'")

import speech_recognition as sr
from pydub import AudioSegment

# Function to perform speech recognition chunk by chunk
def transcribe_audio_chunk_by_chunk(audio_path, chunk_duration=10):
    recognizer = sr.Recognizer()

    # Load the audio file with pydub to calculate duration
    audio = AudioSegment.from_file(audio_path)
    audio_duration_ms = len(audio)

    # Convert audio duration from milliseconds to seconds
    audio_duration_s = audio_duration_ms / 1000

    # Initialize variables
    text = ""
    chunk_start = 0

    # Open the audio file for streaming
    with sr.AudioFile(audio_path) as source:
        while chunk_start < audio_duration_s:
            # Adjust for ambient noise for each chunk
            recognizer.adjust_for_ambient_noise(source)

            # Set the audio file's start and end based on the current chunk
            chunk_end = min(chunk_start + chunk_duration, audio_duration_s)
            audio_data = recognizer.record(source, offset=chunk_start, duration=chunk_end - chunk_start)

            try:
                # Perform Google Web Speech recognition on the chunk
                chunk_text = recognizer.recognize_vosk(audio_data, language="fr")  # Adjust language as needed
                print(chunk_text)
                text += chunk_text + " "
            except sr.UnknownValueError:
                text += "[Unknown] "
            except sr.RequestError as e:
                return f"Could not request results from Google Web Speech Recognition; {e}"

            # Move to the next chunk
            chunk_start = chunk_end

    return text

# Specify the path to the audio file
audio_path = "output_audio.wav"

# Perform speech recognition chunk by chunk
transcript = transcribe_audio_chunk_by_chunk(audio_path)

# Print the transcript
print("Recognized Text:")
print(transcript)

# Write the transcript to a text file
with open("output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(transcript)

print("Transcript written to 'output.txt'")



