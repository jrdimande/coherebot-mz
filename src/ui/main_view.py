import tkinter as tk
from src.core.cohere_service import CohereClient
from src.core.speech_recognition import SpeechRecognizer
from tkinter import PhotoImage


class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coherebot")
        self.root.config(bg="white")
        self.root.geometry("950x700")
        self.root.resizable(False, False)
        self.cohere_client = CohereClient()
        self.sr = SpeechRecognizer()

        # Sidebar
        sidebar = tk.Frame(self.root, bg="#b4a1ff", width=200)
        sidebar.pack(side="left", fill="y")

        # Image logo
        self.logo_img = PhotoImage(file="../assets/images/cohere_logo.png")
        self.logo_btn = tk.Button(self.root, image=self.logo_img, bg="white", bd=0)
        self.logo_btn.place(x=15, y=15)

        # Text logo
        self.text_label_logo = tk.Label(self.root,
                                        text="CohereBot",
                                        bg="#b4a1ff",
                                        fg="#184a22",
                                        font=("Arial", 16, "bold"))
        self.text_label_logo.place(x=60, y=18)

        self.responses_text = tk.Text(self.root,
                                      width=52,
                                      height=20,
                                      font=("Courier New", 12, "bold"),
                                      bg="white",
                                      fg="#050505",
                                      bd=0
                                      )
        self.responses_text.place(x=280, y=90)
        self.responses_text.insert(tk.END, "Hi, how can i assist you today?")

        # Message tex
        self.message_text = tk.Text(self.root,
                                    width=75,
                                    height=5,
                                    pady=5,
                                    bd=1,
                                    bg="#f3f2f7",
                                    fg="black",
                                    font=("Arial", 12)
                                    )
        self.message_text.place(x=233, y=550)
        self.message_text.bind("<Return>", self.send_message)

        # Send message button
        self.send_message_img = PhotoImage(file="../assets/images/arrow_up.png")
        self.send_message_btn = tk.Button(self.root,
                                          image=self.send_message_img,
                                          bg="#f3f2f7",
                                          bd=0,
                                          command=self.send_message
                                          )
        self.send_message_btn.place(x=860, y=600)

        self.voice_img = PhotoImage(file="../assets/images/microfone.png")
        self.send_voice_message = tk.Button(self.root, image=self.voice_img, bd=0, command=self.listen)
        self.send_voice_message.place(x=820, y=602)

    # Send messages function
    def send_message(self, event=None):
        message = self.message_text.get("1.0", tk.END).strip()
        self.message_text.delete("1.0", tk.END)
        response = self.cohere_client.get_response(message)
        self.responses_text.delete("1.0", tk.END)
        self.responses_text.insert(tk.END, response)

    def listen(self):
        self.responses_text.insert(tk.END, "Listening...")
        message = self.sr.listen()
        response = self.cohere_client.get_response(message)
        self.responses_text.delete("1.0", tk.END)
        self.responses_text.insert(tk.END, response)


    def run(self):
        self.root.mainloop()

c = MainView()
c.run()