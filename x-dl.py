import streamlit as st
import os
import subprocess
from datetime import datetime

def download_video_as_mp3(url, path, custom_name=None):
    if not url.strip():
        return "No URL provided.", False
    if not path.strip():
        path = os.getcwd()
    # Set a default custom name if none provided, using .mp3 extension
    if not custom_name:
        custom_name = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    else:
        custom_name += ".mp3"
    try:
        # Prepare command to download as MP3
        output_path = os.path.join(path, custom_name)
        command = f"youtube-dl --extract-audio --audio-format mp3 -o '{output_path}' {url}"
        subprocess.run(command, shell=True, check=True)
        return f"Download completed successfully. Audio saved as {output_path}", True
    except subprocess.CalledProcessError as e:
        return str(e), False

# Streamlit interface
st.title("Download Audio as MP3")

url = st.text_input("Enter the video URL:")
path = st.text_input("Enter the path to save the audio (leave empty for current directory):")
custom_name = st.text_input("Enter a custom name for the audio file (optional, without extension):")

if st.button("Download Audio"):
    message, success = download_video_as_mp3(url, path, custom_name)
    if success:
        st.success(message)
    else:
        st.error(message)
