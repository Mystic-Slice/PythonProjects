import pytube


url = 'https://www.youtube.com/watch?v=P5t0-X_OM5Y&t=0s'

video = pytube.YouTube(url)
'''
for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print (stream)
'''

stream = video.streams.first()
print("Downloading...")
stream.download(output_path= r"Censored\Youtube Downloader\Downloaded")
print("Done")