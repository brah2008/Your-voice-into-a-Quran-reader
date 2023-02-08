import speech_recognition as sr
from gtts import gTTS
import os

def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ar-SA")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def text_to_speech(text):
    if text is None:
        return
    tts = gTTS(text=text, lang='ar-SA')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

text = voice_to_text()
text_to_speech(text)
