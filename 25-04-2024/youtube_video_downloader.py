from pytube import YouTube
from pytube.exceptions import PytubeError
import os

entered_url = input("Enter the URL you want to download: ")
yt = YouTube(entered_url)

streams_with_audio = yt.streams.filter(file_extension='mp4', audio_codec='mp4a.40.2')
print("Available Videos with Audio:")
for st in streams_with_audio:
    print(st)

tag_id = int(input("\nEnter the id of the stream you want to download: "))
stream = yt.streams.get_by_itag(tag_id)

download_path = "G:/Jobi Development/Videos"  # Default download path
if int(input("Do you want to specify a custom path? (1 for yes, 0 for no): ")):
    download_path = input("Enter the path where you want to save the video (e.g., /path/to/save): ")

try:
    stream.download(output_path=download_path)
    print("Download completed successfully!")
except PytubeError as e:
    print(f"An error occurred: {e}")
    print("Retrying the download...")
    # Retry the download
    stream.download()

# https://www.youtube.com/live/2v1lOWe6Uf0?si=Pzv4C-VWRUt81Gsn
# https://youtu.be/uaV05FSOY14?si=Uw7j0pnJVIWL6Onb