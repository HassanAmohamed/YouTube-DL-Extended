import os  # For operating system interactions (folder creation)


# Upgrade pytube to the latest version to avoid compatibility issues
os.system('cmd /c "pip install --upgrade pytube"')

import pytube  # Main library for YouTube video downloads

# Display the installed pytube version for debugging/verification
print(f"Using pytube version: {pytube.__version__}")

# Prompt user to input the YouTube video URL
url = input("Please enter the video link: ")

try:
    # Create a YouTube object with the provided URL
    youtube = pytube.YouTube(url)

    # Select the highest resolution stream available
    video = youtube.streams.get_highest_resolution()

    # Display the video title to confirm correct selection
    print(f"Video Name: {youtube.title}")

    # Define download folder and create it if it doesn't exist
    download_folder = "Downloaded"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)  # Create folder if missing

    # Download the video to the specified folder
    video.download(download_folder)
    print("Download completed!")

except pytube.exceptions.PytubeError as e:
    # Handle pytube-specific errors (e.g., age-restricted videos, invalid URLs)
    print(f"Pytube error: {e}")
except Exception as e:
    # Catch-all for other unexpected errors (network issues, permissions, etc.)
    print(f"An error occurred: {e}")