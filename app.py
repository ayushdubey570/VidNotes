import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are a YouTube video summarizer. Your task is to take the provided transcript text and create a concise summary of the video, highlighting the key points. Please ensure that the summary is clear and informative, and limit it to a maximum of 500 words. Here is the transcript text for summarization"""


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

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("VidNotes: Transforming YouTube Videos into Detailed Notes")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)



# Sidebar Section
def sidebar():
    st.sidebar.header("About the Project")
    st.sidebar.markdown(
        """
        ## YouTube Video Summarizer

        This project is designed to help users quickly grasp the key points and notes from YouTube videos. By leveraging advanced natural language processing techniques, the application extracts and summarizes the content of videos in the form of text, allowing users to save time and focus on the most important information.

        ### Key Features:
        - **Video Summarization**: Automatically generates concise summaries of YouTube videos.
        - **Note-taking**: Provides users with easy-to-read notes that highlight essential points.
        - **User -Friendly Interface**: Simple and intuitive design for seamless navigation.
        - **Accessibility**: Ideal for students, professionals, and anyone looking to enhance their learning experience.

        ### How It Works:
        1. Enter the URL of the YouTube video you want to summarize.
        2. View your summarized notes, and copy for future reference.

        Start summarizing your favorite YouTube videos today!
        """
    )

    # Connect with Me Section
    st.sidebar.header("Connect with Me")
    st.sidebar.markdown(
        """
        - [GitHub](https://github.com/ayushdubey570)
        - [LinkedIn](www.linkedin.com/in/ayuhdubey570)
        - [X(Twitter)](https://x.com/ayushdubey570)
        - [Email](mailto:ayushdubey570@gmail.com)
        """
    )

# Call the sidebar function
sidebar()
