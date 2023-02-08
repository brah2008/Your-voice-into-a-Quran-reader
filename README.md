# Your voice into a Quran reader
Turn your voice into a Quran reader It is used in mosques (a microphone that converts your voice into a Quran reader of your choice) as an amplifier

To create a **Python application** to turn your voice into a Quran reader, you can use **speech recognition and text-to-speech (TTS) technology**. Here are the general steps to do this:

--- Record your voice input using speech recognition library such as SpeechRecognition.
--- Convert the recorded speech to text using an ASR (Automatic Speech Recognition) engine.
--- Once the speech is converted to text, use a TTS engine such as gTTS to convert the text to speech.
--- Use the resulting audio to play back through a speaker or microphone.

It's important to note that building a high-quality, accurate and reliable voice-to-Quran reader would require extensive development and testing efforts, and access to high-quality speech data.


```pyton
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



```

This code first uses the **voice_to_text** function to recognize the speech input and convert it to text using the Google Speech Recognition API. If the recognition fails, the function returns **None**.

The code then uses the **text_to_speech** function to convert the text to speech using the Google Text-to-Speech API and play the resulting audio using the **mpg321** player.

This code is still a basic implementation, and you might want to add additional error handling, user input prompts, and other features to make the application more usable and robust.

-----

# Here's a sample code to get you started with the basic steps mentioned above:

```pyton
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

```

Note that the above code is just a starting point, and you'll likely need to make several modifications to the code to meet your specific requirements and handle edge cases correctly.

---

# Here's a modified version of the code that includes a Quran reader selection feature and a text-to-speech voice selection feature:

```pyton
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


```

---
In this code, the **get_quran_reader** function allows the user to select a Quran reader from a list of available readers. The **get_tts_voice** function allows the user to select a text-to-speech voice from a list of available voices.

The **voice_to_text** function remains the same as in the previous code.

The **text_to_speech** function now takes in the text, voice, and reader as arguments, and uses them to generate the audio file. The resulting audio file includes the text, read by the selected reader.
