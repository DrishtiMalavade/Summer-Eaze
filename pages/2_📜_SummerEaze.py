import streamlit as st
from dotenv import load_dotenv
import time
load_dotenv() 
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KE")) #Create a .env file and store the key there 
st.set_page_config(page_icon="pages/favicon.png")
st.title(":scroll: Summereaze") 

#col1, col2 = st.columns([1,9])

#with col1:
#   st.image("imagee.png", width = 50)

#with col2:
#  st.header("Summereaze")


prompt = """You are a YouTube video summarizer. Please analyze the transcript and provide a concise summary of the key points discussed in the video. Organize the summary in a note format with headings and bullet points. Ensure the main ideas are captured within 250 words.

**Video Summary:**

1. **Introduction:**
   - Brief overview of the video content. it should not exceed more than 150 words,make sure t cover important points and what all is discussed

2. **Main Points:**
   - Highlight the primary topics discussed in the video. Make it in a bullet format.

3. **Key Insights:**
   - Summarize any insightful information presented. Any noteworthy thing which should be known by the user and also anything important which was mentioned in the video.

4. **Conclusion:**
   - Provide a concluding remark or key takeaway.

Please provide the summary below:
"""


#def live_record():


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro") #Select model accordingly
    response=model.generate_content(prompt+transcript_text)
    return response.text

youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get The Summary"):
    transcript_text=extract_transcript_details(youtube_link)

    

    if transcript_text:
        
 
        summary=generate_gemini_content(transcript_text,prompt)
        st.write(summary)

    


