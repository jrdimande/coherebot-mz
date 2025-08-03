import tkinter as tk
from src.core.cohere_service import CohereClient

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coherebot")
        self.root.config(bg="white")
        self.root.geometry("950x700")
        self.root.resizable(False, False)
        self.cohere_client = CohereClient()

        sidebar = tk.Frame(self.root, bg="#b4a1ff", width=200)
        sidebar.pack(side="left", fill="y")


        self.responses_text = tk.Text(self.root, width=52, height=20, font=("Courier New", 12), bg="white", fg="black", bd=0)
        self.responses_text.place(x=280, y=90)
        self.responses_text.insert(tk.END, "Hello World")
        #responses_text.config(state="disabled")

        self.message_text = tk.Text(self.root, width=75, height=5, pady=5, bd=1, bg="#f3f2f7", fg="black", font=("Arial", 12))
        self.message_text.place(x=233, y=550)

        self.message_text.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.message_text.get("1.0", tk.END).strip()
        self.message_text.delete("1.0", tk.END)
        response = self.cohere_client.get_response(message)
        self.responses_text.delete("1.0", tk.END)
        self.responses_text.insert(tk.END, response)




    def run(self):
        self.root.mainloop()

c = MainView()
c.run()
