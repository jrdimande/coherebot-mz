import pyttsx3
from src.config.settings import VOLUME, SPEECH_RATE, VOICE

class TextToSpeech:
    def __init__(self, voice_name=VOICE, rate=SPEECH_RATE, volume=VOLUME):
        self.engine = pyttsx3.init()
        self.set_voice(voice_name)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def set_voice(self, voice_name):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if voice_name.lower() in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
