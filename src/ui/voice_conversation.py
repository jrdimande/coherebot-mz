import tkinter as tk
from src.core.speech_recognition import SpeechRecognizer
from src.core.text_to_speech import TextToSpeech
from src.core.cohere_service import CohereClient
from tkinter import PhotoImage

class VoiceConversation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coherebot")
        self.root.config(bg="#b4a1ff")
        self.root.geometry("950x700")
        self.root.resizable(False, False)
        self.cohere_client = CohereClient()
        self.sr = SpeechRecognizer()

        self.listening_img = PhotoImage(file="../assets/listening.png")
        self.listening_label = tk.Label(self.root, image=self.listening_img, bg="#b4a1ff")
        self.listening_label.place(x=425, y=200)

    def run(self):
        self.root.mainloop()


v = VoiceConversation()
v.run()
