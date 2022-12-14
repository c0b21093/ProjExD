
import tkinter as tk

#初期設定
root = tk.Tk()
root.title("otamesi")
root.geometry("400x620")

#ボタンを押したときの挙動に関する関数
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    entry.insert(tk.END, txt)

def calc_num(event):
    num1 = eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(tk.END, num1)

def clear_num(event):
    entry.delete(0, tk.END)

#数字ボタンの配置
a, b = 1, 0
#key = [9,8,7,c,6,5,4,"+",3,2,1,"=",0]
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
#プラスボタンの配置
plus_button = tk.Button( root, text = '+', 
                        font = ("Times New Roman", 30),
                        width = 4, height = 2)
plus_button.bind("<1>", button_click)
plus_button.grid(row = 3, column = 3)

#イコールボタンの配置
equal_button = tk.Button( root, text = '=', 
                font = ("Times New Roman", 30),
                width = 4, height = 2)
equal_button.bind("<1>", calc_num)
equal_button.grid(row = 4, column = 3)

#cボタンの配置
c_button = tk.Button( root, text = 'c', 
                font = ("Times New Roman", 30),
                width = 4, height = 2)
c_button.bind("<1>", clear_num)
c_button.grid(row = 1, column = 3)

#液晶部分の作成
entry = tk.Entry(justify="right", width = 10, font = ("Times New Roman", 40))
entry.grid(row = 0, column = 0, columnspan = 3)


root.mainloop()