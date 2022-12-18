from pytube import YouTube

youtube = YouTube('https://www.youtube.com/watch?v=p4kVWCSzfK4&list=RDtPxSX2g_VMU&index=4')

youtube.streams.get_highest_resolution().download()