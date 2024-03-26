#pip install youtube-transcript-api
from youtube_transcript_api import YouTubeTranscriptApi
import os, sys
import json

url = sys.argv[1] #e.g. 'https://www.youtube.com/watch?v=cHjpPRLPhLo'
id = url.split('watch?v=')[1]
srt = YouTubeTranscriptApi.get_transcript(id, languages=['zh', 'en']) # e.g. [{'text': 'welcome back to the financial freedom', 'start': 0.64, 'duration': 3.6}, {'text': 'show my name is rob berger in this video', 'start': 2.08, 'duration': 3.279}, ... ]

with open(id+'.srt.json', 'w') as f: 
    json.dump(srt, f) 
