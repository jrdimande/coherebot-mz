import tkinter as tk
from src.core.speech_recognition import SpeechRecognizer
from src.core.text_to_speech import TextToSpeech
from src.core.cohere_service import CohereClient
from tkinter import PhotoImage
import threading

class VoiceConversation:
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)
        self.root.title("Coherebot")
        self.root.config(bg="#b4a1ff")
        self.root.geometry("950x700")
        self.root.resizable(False, False)
        self.cohere_client = CohereClient()
        self.sr = SpeechRecognizer()
        self.tts = TextToSpeech()

        # Listening image
        self.listening_img = PhotoImage(file="../assets/images/listening.png")
        self.listening_label = tk.Label(self.root, image=self.listening_img, bg="#b4a1ff")
        self.listening_label.place(x=425, y=200)

        # Close window button
        self.close_img = PhotoImage(file="../assets/images/close_window.png")
        self.close_btn = tk.Button(self.root, image=self.close_img, bd=0, command=self.close_window)
        self.close_btn.place(x=650, y=500)

        # Mic image and button
        self.mic_img = PhotoImage(file="../assets/images/microfone1.png")
        self.mic_btn = tk.Button(self.root, image=self.mic_img, bd=0, command=self.listen_and_speak)
        self.mic_btn.place(x=250, y=500)

    # Send voice message function
    def listen_voice(self):
        threading.Thread(target=self.listen_and_speak).start()

    def listen_and_speak(self):
        text = self.sr.listen()
        response = self.cohere_client.get_response(text)
        self.tts.speak(response)

    # Close window function
    def close_window(self):
        self.root.destroy()



