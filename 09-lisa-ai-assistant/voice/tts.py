import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 185)   # faster = youthful
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
for v in voices:
    if "female" in v.name.lower():
        engine.setProperty("voice", v.id)
        break

def speak(text: str):
    engine.say(text)
    engine.runAndWait()
