import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Channel



url = "https://www.youtube.com/watch?v=Yh5gcLG6C3Q"  # <-- Change the URL to your desired YouTube video



download_dir = r"C:/Users/admin/Desktop"  # Change the path to your desired download location
os.makedirs(download_dir, exist_ok=True)

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

stream = yt.streams.get_highest_resolution()
if stream is None:
    raise RuntimeError("No stream found.")
stream.download(output_path=download_dir)
print(f"Saved to: {download_dir}")
print(f"Downloading: {yt.title}")
print("Download completed!")

# --- Un-comment this code underneath to save subtitles to a document ---
#yt = YouTube(url)
#caption = yt.captions['a.en']
#caption.save_captions("captions.txt")