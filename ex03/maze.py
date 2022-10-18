import tkinter as tk

root = tk.Tk()
root.title("迷える工科トン")
root.geometry("1500x900")

canvas = tk.Canvas(root, background="#000", width=1500, height=900)
canvas.pack()

root.mainloop()