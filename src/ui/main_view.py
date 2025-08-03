import tkinter as tk

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coherebot")
        self.root.config(bg="grey")
        self.root.geometry("950x700")

        sidebar = tk.Frame(self.root, bg="black", width=200)
        sidebar.pack(side="left", fill="y")


        responses_text = tk.Text(self.root, width=90, height=30)
        responses_text.place(x=214, y=90)

        self.message_text = tk.Text(self.root, width=90, height=5, pady=5, bd=3)
        self.message_text.place(x=213, y=550)

    def run(self):
        self.root.mainloop()

c = MainView()
c.run()
