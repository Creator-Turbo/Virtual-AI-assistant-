from flask import Flask, render_template, request, jsonify, send_file
from src.helper import voice_input, llm_model, text_to_speech

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    text = voice_input()  # Capture voice input
    response = llm_model(text)  # Get AI response
    text_to_speech(response)  # Convert to speech
    
    return jsonify({"response": response})  # Send response to frontend

@app.route("/download_audio")
def download_audio():
    return send_file("speech.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
