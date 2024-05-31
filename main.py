from pytube import YouTube

def get_video_url():
    url = input("Enter the URL of the YouTube video you want to download: ")
    return url

def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading '{yt.title}'...")
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = get_video_url()
    download_video(url)

if __name__ == "__main__":
    main()
