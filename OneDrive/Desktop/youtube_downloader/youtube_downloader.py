# youtube_downloader.py
# This script downloads a YouTube video using the pytubefix library.
# It demonstrates:
# - Importing modules and using external libraries
# - Reading user input with the input() function
# - Instantiating classes and calling methods
# - Using callbacks to monitor progress

# Import the necessary classes and functions from pytubefix.
from pytubefix.cli import on_progress
from pytubefix import YouTube

# Prompt the user for the YouTube URL.
# The input() function reads a line from the user and returns it as a string.
url = input("Enter YouTube URL: ")

# Create a YouTube object.
# The YouTube class handles retrieving video details and streams.
# The parameters used:
#   - url: The video URL provided by the user.
#   - use_oauth=True and allow_oauth_cache=True: These options enable OAuth authentication.
#     (For many cases, you can omit these if OAuth isn’t required, but here we include them to show how parameters work.)
#   - on_progress_callback=on_progress: This function is called periodically to show download progress.
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

# Print the title of the video to confirm that the YouTube object is working.
print("Downloading:", yt.title)

# Get the highest resolution progressive stream available.
# Progressive streams contain both video and audio.
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory.
# The download() method saves the file locally.
stream.download()