import os
import tempfile
from flask import Flask, request, render_template, send_file, jsonify
from pydub import AudioSegment
import whisper

app = Flask(__name__)

# Load the Whisper model once at the start of the app
model = whisper.load_model("small")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    audio_file = request.files['audio_file']
    
    # Save the audio file temporarily
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    audio_file.save(temp_audio_file.name)

    # Convert audio to mono and 16000Hz, and extract the first 60 seconds
    try:
        sound = AudioSegment.from_file(temp_audio_file.name)
        sound = sound.set_channels(1)  # Set to mono
        sound = sound.set_frame_rate(16000)  # Set to 16000Hz

        # Extract the first 60 seconds
        excerpt = sound[:60000]

        # Export excerpt to temporary wav file
        temp_excerpt_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        excerpt.export(temp_excerpt_file.name, format="wav")

        # Transcribe the audio using Whisper
        result = model.transcribe(temp_excerpt_file.name)
        transcription = result["text"]

        # Clean up temporary files
        os.remove(temp_audio_file.name)
        os.remove(temp_excerpt_file.name)

        # Return transcription as JSON
        return jsonify({"transcription": transcription})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/play_audio/<filename>')
def play_audio(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
