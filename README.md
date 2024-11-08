# VidNotes: Transforming YouTube Videos into Detailed Notes

## Description
VidNotes is a web application built with Streamlit that allows users to transform YouTube videos into concise and informative summaries. By extracting the transcript of a video and utilizing Google Gemini Pro's generative capabilities, VidNotes provides users with detailed notes that highlight the key points of the video, making it easier to grasp essential information without watching the entire content.

## Table of Contents
- [Why Do We Need This?](#why-do-we-need-this)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)
- [Future Improvements](#future-improvements)
- [Screenshorts](#Screenshorts)

## Why Do We Need This?
In an age where video content is prevalent, it can be time-consuming to extract valuable insights from lengthy videos. VidNotes addresses this challenge by providing:
- **Time Efficiency**: Quickly obtain summaries of lengthy videos, saving hours of viewing time.
- **Enhanced Learning**: Focus on key points and important information, making it easier to retain knowledge.
- **Accessibility**: Make video content more accessible for individuals who prefer reading over watching.

## Features
- Extracts transcripts from YouTube videos.
- Generates concise summaries of the transcripts using Google Gemini Pro.
- User-friendly interface built with Streamlit.
- Supports any public YouTube video link.

## Technologies Used
- Python
- Streamlit
- NLP (Natural Language Processing)
- Google Generative API (Gemini Pro)
- YouTube Transcript API

## Prerequisites
- Python 3.7 or higher
- A Google API key with access to Google Gemini Pro.

## Installation Guide
To set up VidNotes on your local environment, follow these steps:

1. Clone the Repository
 ```
 git clone https://github.com/ayushdubey570/VidNotes.git
 ```

3. Install Required Packages
```
pip install -r requirements.txt
```

5. Set Up Environment Variables
- Create a .env file in the root directory of your project.
- Add your Google API key in the following format:

```
GOOGLE_API_KEY="your_api_key_here"
```

4. Run the Application
```
streamlit run app.py
```

6. Access the Application
```
Local URL: http://localhost:8503
```


## Screenshorts:

![project_1](https://github.com/user-attachments/assets/528cd5b4-195a-41f0-b7ee-e14bf0d191c0)
![project_2](https://github.com/user-attachments/assets/7b774a36-d57f-4fe7-87f1-d188884d785f)
![project_3](https://github.com/user-attachments/assets/7da546da-e492-4ae7-b86f-94923165fd68)

## Acknowledgments

- **[Streamlit](https://streamlit.io/)** for the interactive framework.
- **[YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)** for transcript extraction.
- **[Google Gemini](https://cloud.google.com/generative-ai)** for content generation.


## Future Improvements

The VidNotes project has the potential for various enhancements. Here are some ideas for future improvements:

1. **Multi-Language Support**:
   - Implement support for multiple languages in transcripts and summaries to make the tool accessible to a broader audience.

2. **User  Authentication**:
   - Add user authentication to allow users to save their summaries and transcripts for future reference.

3. **Export Options**:
   - Provide options to export summaries in various formats (e.g., PDF, Markdown, or Word) for easier sharing and documentation.

4. **Enhanced Summarization Techniques**:
   - Explore and integrate advanced summarization models for better accuracy and coherence in generated summaries.

5. **User  Feedback System**:
   - Implement a feedback mechanism for users to rate the summaries, which can help improve the model over time.

6. **Video Playback Integration**:
   - Add a feature to play the video alongside the summary, allowing users to reference specific parts of the video easily.

7. **Mobile Responsiveness**:
   - Optimize the application for mobile devices to improve usability on smartphones and tablets.

8. **Community Contributions**:
   - Encourage open-source contributions by providing clear guidelines for contributing to the project.

9. **Performance Enhancements**:
   - Optimize the application for faster loading times and improved performance, especially with larger videos.

10. **Documentation Improvements**:
    - Expand the documentation to include more detailed usage examples, FAQs, and troubleshooting tips.

These improvements aim to enhance user experience and broaden the functionality of the VidNotes project. Contributions and suggestions from the community are always welcome!


## Contact Information

For any inquiries, suggestions, or issues regarding the VidNotes project, please feel free to reach out:

- **Name**: Ayush Dubey
- **Email**: [ayushdubey570@gmail.com](mailto:ayushdubey570l@example.com)
- **GitHub**: [ayushdubey570 ](https://github.com/ayushdubey570)
- **LinkedIn**: [ayushdubey570](https://www.linkedin.com/in/ayushdubey570)

Appreciate your feedback and contributions!
