from pytube import YouTube
from pathlib import Path

path = str(Path.home())+'/downloads'

def download_720p_mp4_videos(url: str, outpath: path):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download(outpath)

if __name__ == "__main__":
    download_720p_mp4_videos("https://www.youtube.com/watch?v=FDBqs7GOY_w", path)