🎥 PyTube Video Downloader
A lightweight Python script to download YouTube videos in the highest resolution with just one click.

✨ Features
✅ Simple & Fast – Download videos with a single command.
✅ Highest Resolution – Automatically fetches the best available quality.
✅ Auto-Upgrade – Ensures pytube is always up-to-date.
✅ Organized Downloads – Saves videos to a dedicated Downloaded folder.
✅ Error Handling – Catches invalid URLs, age restrictions, and network issues.

⚙️ Installation
Clone the repository:

bash

git clone https://github.com/HassanAmohamed/YouTube-DL-Extended.git
Navigate to the project directory:

bash

cd PyTube-Downloader
Install dependencies (only pytube required):

bash

pip install pytube
🚀 Usage
Run the script:

bash

python youtube_downloader.py
Paste the YouTube video URL when prompted:

Copy
Please enter the video link: https://youtu.be/example
Done! The video saves to the Downloaded folder.

Example Output:

plaintext
Copy
Using pytube version: 15.0.0
Video Name: "How to Build a Rocket in 10 Minutes"
Download completed!
🛠 How It Works
Upgrades pytube to avoid compatibility issues.

Fetches video metadata (title, streams) using the YouTube API.

Selects the highest resolution stream available.

Downloads the video to a local Downloaded folder (auto-created if missing).

🌟 Code Highlights
python
Copy
# Auto-upgrade pytube for reliability
os.system('cmd /c "pip install --upgrade pytube"')

# Download highest resolution stream
video = youtube.streams.get_highest_resolution()
video.download("Downloaded")
🚨 Error Handling
The script catches:

Invalid URLs

Age-restricted videos

Network errors

Permission issues

Example error message:

plaintext
Copy
Pytube error: Video is age-restricted and requires login.
📂 Folder Structure
Copy
PyTube-Downloader/
├── youtube_downloader.py  # Main script
└── Downloaded/            # Default save location
    ├── video1.mp4
    └── video2.mp4
🤝 Contributing
PRs welcome! To improve:

Add progress bars

Support playlists

Add GUI (Tkinter/PyQt)

📜 License
MIT © Sona

🔗 Similar Projects
yt-dlp – Advanced YouTube downloader

pytube – Underlying library used