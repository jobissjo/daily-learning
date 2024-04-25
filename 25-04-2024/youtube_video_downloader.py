from pytube import YouTube

entered_url = input("Enter the url you want to download..")
yt = YouTube(entered_url)

print("Available Videos with Audio")
streams_with_audio = yt.streams.filter(file_extension='mp4', audio_codec='mp4a.40.2')

for st in streams_with_audio:
    print(st)

tag_id = int(input("\nEnter the id, you want to download: "))
stream = yt.streams.get_by_itag(tag_id)
stream.download()
