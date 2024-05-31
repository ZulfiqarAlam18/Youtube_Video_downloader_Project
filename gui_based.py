import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if not save_path:
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        status_label.config(text=f"Downloaded '{yt.title}' successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

app = tk.Tk()
app.title("YouTube Video Downloader")

tk.Label(app, text="Enter YouTube URL:").pack()
url_entry = tk.Entry(app, width=50)
url_entry.pack()

tk.Button(app, text="Download", command=download_video).pack()
status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
