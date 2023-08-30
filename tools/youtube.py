import argparse
from pytube import YouTube
from unidecode import unidecode

def download_youtube(video_url, save_directory):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(save_directory)
    except:
        print("Failed to download video")

    print("video was downloaded successfully")
    
def getTitle(video_url):
    video = YouTube(video_url)
    return video.title