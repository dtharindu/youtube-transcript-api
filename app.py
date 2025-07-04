from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/transcript")
def get_transcript():
    video_id = request.args.get("video_id")
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return jsonify(transcript)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)