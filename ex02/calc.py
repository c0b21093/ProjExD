import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("otamesi")
root.geometry("300x500")

'''
label = tk.Label(root,
                text = "raberu",
                font = ("Ricty Diminished", 20)
                )
label.pack()

tkm.showwarning("Warning", "Are you kidding me!?")
'''

button9 = tk.Button(root,
                    text = "9",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button8 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button7 = tk.Button(root,
                    text = "7",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button6 = tk.Button(root,
                    text = "6",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button5 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button4 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button3 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button2 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button1 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)
button0 = tk.Button(root,
                    text = "8",
                    font = ("Times New Roman", 30),
                    width = 4,
                    height = 2)

button9.grid(row = 0, column = 0)
button8.grid(row = 0, column = 1)
button7.grid(row = 0, column = 2)
button6.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button4.grid(row = 1, column = 2)
button3.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button1.grid(row = 2, column = 2)
button0.grid(row = 3, column = 0)

'''
entry = tk.Entry(root, width=30)
entry.insert(tk.END, "pass")
entry.pack()
'''

root.mainloop()