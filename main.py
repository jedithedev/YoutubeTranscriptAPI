from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
import uvicorn

app = FastAPI()


@app.get('/transcriptfull/')
def transcriptfull(link):
    link = link
    video_id = link.split('?v=')[1].split('&')[0]

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    return fetched_transcript

@app.get('/transcript/')
def transcript(link):
    link = link
    video_id = link.split('?v=')[1].split('&')[0]

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    final = ''
    for i in fetched_transcript:
        final = final + i.text + ' '
    return final

uvicorn.run(app=app, port=7998)