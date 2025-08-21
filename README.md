# WhisperWave: An Audio Transcription App

WhisperWave is a lightweight web application that allows you to upload an audio file and get a text transcription of the audio. This project is built using **Flask** for the backend and leverages **OpenAI's Whisper** model for highly accurate speech-to-text transcription. It also uses **Pydub** to handle audio file processing.

## ✍️ Author of the Project

* **Uppalapati Suchith Chowdary**

## 🚀 Features

* **Audio Transcription**: Transcribes a variety of audio formats (e.g., MP3, WAV) to text.
* **Simple UI**: A clean and user-friendly web interface for easy file uploads.
* **Audio Playback**: Listen to the uploaded audio directly in the browser.
* **Efficient Processing**: Uses `Pydub` to process and prepare audio for transcription.

## ⚙️ Technologies Used

* **Backend**: Flask (Python)
* **Frontend**: HTML, CSS, JavaScript
* **Transcription Model**: OpenAI Whisper
* **Audio Processing**: Pydub

## 📋 Prerequisites

To run this application, you need to have **Python 3.x** and `pip` installed.

## 📦 Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/Suchith-2002/WhisperWave.git](https://github.com/Suchith-2002/WhisperWave.git)
    cd WhisperWave
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**

    The project uses the `pydub` and `whisper` libraries. You will also need to install `ffmpeg`, as `pydub` depends on it for audio processing.

    ```bash
    pip install Flask pydub
    pip install openai-whisper
    ```

    **Install FFmpeg:**

    * **On macOS** using Homebrew:
        ```bash
        brew install ffmpeg
        ```
    * **On Windows**: Download the FFmpeg binaries from the official website and add them to your system's PATH.
    * **On Linux**:
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```

## ▶️ How to Run the App

1.  Make sure you have completed the installation steps above.
2.  Run the Flask application from your terminal:

    ```bash
    python flask_app.py
    ```

3.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 🧑‍💻 How to Use

1.  On the web page, click the **"Choose File"** button.
2.  Select an audio file from your local machine (e.g., a `.mp3` or `.wav` file).
3.  Click the **"Upload and Transcribe"** button.
4.  The transcription will appear in the **"Transcription"** section below, and the uploaded audio will be available for playback.

## 📸 Demo

* **Homepage**
* **After Uploading**

## 🤝 Contribution

Feel free to open issues or submit pull requests to improve the project. Your contributions are welcome!
