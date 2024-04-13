# Download X Spaces

This Streamlit application enables users to download audio from video streams as MP3 files using `youtube-dl`. It provides a simple web interface to input the video URL, specify the directory for saving the downloaded file, and set a custom name for the output file.

## Prerequisites

- **Python**: You need Python 3.6 or higher.
- **Streamlit**: This app uses Streamlit to run the web interface.
- **youtube-dl**: For downloading videos.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/jairodriguez/download-x-spaces.git
cd download-x-spaces
```

### 2. Install Dependencies

Install the required Python libraries using:

```bash
pip install streamlit youtube-dl
```

## Running the Application

To run the app, navigate to the directory containing the script and execute:

```bash
streamlit run x-dl.py
```

Replace `x-dl.py` with the name of your Python script if different.

## How to Use the App

1. **Start the App**: Run the command above to start the Streamlit app. Your default web browser will open to the local server address (typically `http://localhost:8501`).
2. **Enter Video URL**: Input the full URL of the video you wish to download as an MP3 in the provided text field.
3. **Specify Save Directory**: Enter the directory path where you want the MP3 file saved. If you leave this field empty, the file will be saved in the current directory of the script.
4. **Custom Name (Optional)**: Provide a custom name for the output file without the extension. If left blank, the file name will default to `audio_YYYYMMDDHHMMSS.mp3`, with the timestamp of download.
5. **Download Audio**: Click the "Download Audio" button. If the URL is valid and accessible, `youtube-dl` will process the video and extract the audio as an MP3 file.

## Finding the X Space URL Using Chrome Developer Tools

If you need to manually find the X Spaces download URL, you can use the Chrome Developer Tools. This tool allows you to inspect network traffic on a webpage to locate streaming media URLs. Follow these steps to capture the M3U8 file URL:

### 1. Open the X Space Web Page

- Launch Google Chrome.
- Navigate to the web page.

### 2. Access Chrome Developer Tools

- Right-click anywhere on the page and select `Inspect`, or press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac) to open the Developer Tools.

### 3. Use the Network Tab

- Click on the `Network` tab in the Developer Tools.
- There is a search bar at the top of the Network tab; enter `playlist` into the filter textbox.

### 4. Start the X Space

- Begin playing the Space on X.com if it doesn’t start automatically. 

### 5. Identify the M3U8 File

- Look for a network request that ends with `.m3u8` AND contains "playlist" in its name. This file is the HLS (HTTP Live Streaming) playlist file.
- Click on the name of the request to view more details.

### 6. Copy the playlist URL

- In the headers or response details of the selected `.m3u8` request, locate the full request URL, which is the direct link to the M3U8 playlist.
- Right-click the URL and select `Copy link address` to copy the URL to your clipboard.

### 7. Use the URL in the Streamlit App

- Paste the copied M3U8 URL into the Streamlit app's URL input field to proceed with downloading the audio as described in the app instructions.

## Running the Application


## Troubleshooting

If you encounter errors related to `youtube-dl` or permissions issues, ensure that `youtube-dl` is up-to-date and that you have write permissions to the specified directory.

## Contributing

Contributions to enhance this app are welcome! Fork the project, make your changes, and submit a pull request.

---

