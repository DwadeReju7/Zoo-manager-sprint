from pytube import YouTube

def main():
    """Downloads the highest resolution video from a given YouTube URL with progress."""

    url = input("Enter YouTube URL: ")

    try:
        def progress_func(stream, chunk, bytes_remaining):
            """Displays download progress."""
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage = (bytes_downloaded / total_size) * 100
            print(f"Downloading: {percentage:.2f}%", end='\r')

        yt = YouTube(url, on_progress_callback=progress_func) #Removed OAuth, and corrected progress.

        print("Downloading:", yt.title)

        stream = yt.streams.get_highest_resolution()

        if stream:
            stream.download()
            print("\nDownload completed successfully!")
        else:
            print("No suitable stream found.")

    except Exception as e:
        print(f"An error occurred: {e}")
    #Example of a valid URL
    
print ("Example of valid URL: #https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == "__main__":
    main()