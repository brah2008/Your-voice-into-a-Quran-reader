import speech_recognition as sr
from gtts import gTTS
import os

# Step 1: Record the voice input
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Step 2: Convert the speech to text
text = r.recognize_google(audio)

# Step 3: Convert the text to speech
tts = gTTS(text=text, lang='en')
tts.save("audio.mp3")

# Step 4: Play the audio
os.system("mpg321 audio.mp3")
