from pytube import YouTube
from pathlib import Path

# url array (list)
url_array = ["https://www.youtube.com/watch?v=Pjw2A3QU8Qg", 
             "https://www.youtube.com/watch?v=YanYDTGkLH8", 
             "https://www.youtube.com/watch?v=XqZsoesa55w", 
             "https://www.youtube.com/watch?v=pZw9veQ76fo"]

#change path to your desired location
path = str(Path.home())+'/Downloads'

if __name__ == "__main__":
    # Using a loop to download each video
    for value in url_array:
        yt = YouTube(value)
        file_name = yt.streams.filter(file_extension="mp4").get_by_resolution("720p").title
        file_size_mb = yt.streams.filter(file_extension="mp4").get_by_resolution("720p").filesize_mb    

        #download
        yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download(path)
        
        #print info
        print("downloaded: "+str(file_name)+"; file_size_in_mb: "+str(file_size_mb))