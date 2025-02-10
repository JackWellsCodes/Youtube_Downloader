from pytube import YouTube
import sys

# Ensure the script is run with a YouTube link
if len(sys.argv) < 2:
    print("Usage: python3 youtube_downloader.py <YouTube_Link>")
    sys.exit(1)

# Get the YouTube link from the command-line arguments
link = sys.argv[1]

try:
    # Create a YouTube object
    yt = YouTube(link)

    # Print video details
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video (seconds): ", yt.length)
    print("Rating: ", yt.rating)

    # Get the highest resolution stream
    print("\nDownloading...")
    yt.streams.get_highest_resolution().download()
    print("Download completed successfully!")

except Exception as e:
    print("An error occurred:", e)

