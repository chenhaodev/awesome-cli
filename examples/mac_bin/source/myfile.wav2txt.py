import sys
import os

cmd = 'ffmpeg -i ' + sys.argv[1] + ' -f segment -segment_time 00:02:00 -c copy splitted_wav%03d.mp3'; os.system(cmd)
files = os.listdir('./'); splitted_wav_files = [file for file in files if file.startswith("splitted_wav")]
for splitted_wav_file in splitted_wav_files:
    cmd = 'whisper '+ splitted_wav_file; os.system(cmd)

'''
Example
#pip install git+https://github.com/openai/whisper.git
ffmpeg -i input.mp3 -f segment -segment_time 00:02:00 -c copy output%03d.mp3
whisper 123/output003.mp3

[00:17.800 --> 00:20.080]  For example, in the phase three,
[00:20.080 --> 00:22.520]  usually the pharmacy company needs to expand
[00:22.520 --> 00:24.200]  the disease populations.
[00:24.200 --> 00:25.680]  And some of the biomarkers,
[00:25.680 --> 00:27.840]  for example, activity maybe looks like fine,
[00:27.840 --> 00:29.560]  but however, some of the biomarkers
[00:29.560 --> 00:32.000]  may not be useful for all the populations.
'''

## version old, speech_recognition ##

'''
import speech_recognition as sr
from pydub import AudioSegment
import sys

# Create a recognizer instance
recognizer = sr.Recognizer()

# Specify the audio file path
audio_file = sys.argv[1] #"1.mp3"

# Chunk size and overlap (in milliseconds)
chunk_size = 30000  # 30 seconds
overlap = 10000  # 10 seconds

# Load the audio file
audio = AudioSegment.from_file(audio_file, format="mp3")

# Get the duration of the audio in milliseconds
audio_duration = len(audio)

start_time = 0
end_time = chunk_size

while start_time < audio_duration:
    # Adjust the end time if it exceeds the audio duration
    if end_time > audio_duration:
        end_time = audio_duration

    # Extract the chunk from the audio
    audio_chunk = audio[start_time:end_time]

    # Export the chunk as a temporary WAV file
    audio_chunk.export("temp.wav", format="wav")

    # Load the temporary WAV file
    with sr.AudioFile("temp.wav") as source:
        try:
            # Read the audio data
            audio_data = recognizer.record(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized text for chunk {start_time}-{end_time}:")
            print(text)
        except sr.UnknownValueError:
            print(f"Speech recognition could not understand audio for chunk {start_time}-{end_time}")
        except sr.RequestError as e:
            print("Could not request results from the speech recognition service: {0}".format(e))

    # Update the start and end times for the next chunk
    start_time += chunk_size - overlap
    end_time += chunk_size - overlap

# Remove the temporary WAV file
import os
os.remove("temp.wav")

'''

## END of version old, speech_recognition ##
