from flask import Flask, render_template
import openai
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/transcribe", methods=['POST'])
def transcribe():
    audio_file= open("/workspace/Enregistrement.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript

@app.route("/ask", methods=['POST'])
def ask():
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
