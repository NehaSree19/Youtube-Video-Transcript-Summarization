#Installing Transformers and YouTubeTranscriptApi.
!pip install -q transformers
!pip install -q youtube_transcript_api

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

#The youtube url which needs to be summarized.
youtube_video = "https://www.youtube.com/watch?v=A4OmtyaBHFE"

video_id = youtube_video.split("=")[1]

video_id #prints the video's ID.

from IPython.display import YouTubeVideo
YouTubeVideo(video_id)

# Prints the videos transcript using the video ID.
YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

#Prints the transcript based on start, duration and the text.
transcript[0:5] 

#prints the length of the result of the text extracted from the audio. 
result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))

#Preprocessing of Text
import nltk
nltk.download("punkt")
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
text = result
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print("Tokens without stopwords:",tokens_without_sw)
print("Stopwords are:",stopwords.words('english'))

summarizer = pipeline('summarization')

# Summarization of Text.
num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("input text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  print("Summarized text\n"+out)
  summarized_text.append(out)
#print(summarized_text)

#printing the length of summarized text.
len(str(summarized_text))

#Printing the summarized text.
str(summarized_text)
