import tkinter as tk

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coherebot")
        self.root.config(bg="#2f3030")
        self.root.geometry("950x700")
        self.root.resizable(False)

        sidebar = tk.Frame(self.root, bg="#0c0c0d", width=200)
        sidebar.pack(side="left", fill="y")


        responses_text = tk.Text(self.root, width=52, height=20, font=("Courier New", 16), bg="#2f3030", bd=0)
        responses_text.place(x=242, y=90)
        responses_text.insert(tk.END, "Hello World")
        #responses_text.config(state="disabled")

        self.message_text = tk.Text(self.root, width=85, height=5, pady=5, bd=1, bg="#434445")
        self.message_text.place(x=233, y=550)

    def run(self):
        self.root.mainloop()

c = MainView()
c.run()
