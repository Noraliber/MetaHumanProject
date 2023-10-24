from flask import Flask, render_template, request
import openai
import os
import uuid

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/transcribe", methods=['POST'])
def transcribe():
    file = request.files["file"]
    recording_file = f"{uuid.uuid4()}.wav"
    recording_path = f"Enregistrements/{recording_file}"
    os.makedirs(os.path.dirname(recording_path), exist_ok=True)
    file.save(recording_path)
    audio_file = open(recording_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript


@app.route("/ask", methods=['POST'])
def ask():
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
