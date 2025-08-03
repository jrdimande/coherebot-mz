import speech_recognition as sr
from src.config.settings import LANGUAGE

class SpeechRecognizer:
    def __init__(self, language=LANGUAGE, microphone_index=None):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.microphone_index = microphone_index

    def listen(self):
        with sr.Microphone(device_index=self.microphone_index) as source:
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            return "ERROR"
