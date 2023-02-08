import speech_recognition as sr
from gtts import gTTS
import os

def get_quran_reader():
    readers = ["Mohammed Siddiq Al-Minshawi", "Abdullah Basfar", "Mahmoud Khalil Al-Husary"]
    print("Select a Quran reader:")
    for i, reader in enumerate(readers):
        print(f"{i + 1}. {reader}")

    selected = int(input("Enter the number of the reader: "))
    return readers[selected - 1]

def get_tts_voice():
    voices = ["ar-SA-Standard-A", "ar-SA-Standard-B", "ar-SA-Standard-C"]
    print("Select a Text-to-Speech voice:")
    for i, voice in enumerate(voices):
        print(f"{i + 1}. {voice}")

    selected = int(input("Enter the number of the voice: "))
    return voices[selected - 1]

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

def text_to_speech(text, voice, reader):
    if text is None:
        return
    tts = gTTS(text=f"{text}, read by {reader}", lang='ar-SA', voice=voice)
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

reader = get_quran_reader()
voice = get_tts_voice()
text = voice_to_text()
text_to_speech(text, voice, reader)
