import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("otamesi")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

a, b = 1, 0
for i ,num in enumerate(range(9, -1, -1), 1):
    button = tk.Button( root, text = f'{num}', 
                        font = ("Times New Roman", 30),
                        width = 4, height = 2)
    button.bind("<1>", button_click)
    button.grid(row = a,column = b)
    b += 1
    if i%3 == 0:
        a += 1
        b = 0

root.mainloop()