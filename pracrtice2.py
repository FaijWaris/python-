import pyttsx3
engine=pyttsx3.init()
engine.say("Hello, I am your text to speech engine.")
engine.runAndWait()
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(f"Available voices: {len(voices)}")

# Try different voices
if len(voices) > 0:
    engine.setProperty('voice', voices[0].id)
    
engine.setProperty('volume', 1.0)  # Max volume
engine.say("Testing audio")
engine.runAndWait()