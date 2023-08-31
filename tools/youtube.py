from pytube import YouTube
from unidecode import unidecode

def download_youtube(video_url, save_directory):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(save_directory)
        return 1 # Success
    except:
        return 0 # Fail
        
def get_title(video_url):
    video = YouTube(video_url)
    return video.title