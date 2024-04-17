from flask import Flask, jsonify, request, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='static')

# Configure generativeai with Google API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_summary', methods=['GET'])
def get_summary():
    youtube_link = request.args.get('youtube_link')
    video_id = youtube_link.split("=")[1]

    try:
        transcript_text = extract_transcript_details(video_id)
        prompt = """You are a YouTube video summarizer tasked with analyzing a transcript and creating a comprehensive summary. 
                    Your summary should provide a concise overview of the video's content, capturing the main ideas within 250 words. 
                    Start by introducing the video and its key topics in a brief overview, ensuring it does not exceed 150 words. 
                    Highlight the primary points discussed in the video in a structured manner. 
                    Then, delve into the key insights presented, emphasizing any noteworthy information that users should be aware of. 
                    Conclude your summary with a final remark or key takeaway to wrap up the main ideas discussed in the video. 
                    Please provide the summary below in a coherent paragraph format.
                    Do not make use of asterisks.
                """ 

        summary = generate_gemini_content(transcript_text, prompt)
        
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_transcript_details(video_id):
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = " ".join([i["text"] for i in transcript_text])
    return transcript

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)

