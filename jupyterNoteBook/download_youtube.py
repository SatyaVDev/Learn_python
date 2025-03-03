import ssl
from pytube import YouTube

# Disable SSL verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Callback function to display download progress


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print(f"Downloading: {percent:.2f}%")


def download_youtube_video(video_url):
    try:
        # Initialize the YouTube object with the URL
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        print(stream)

        # Start downloading the video
        stream.download()

        # Print success message with the video title
        print(f"Video '{yt.title}' has been successfully downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get the URL from the user
video_url = 'https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=684s'

# Download the video
download_youtube_video(video_url)
