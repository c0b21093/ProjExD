import tkinter as tk
import maze_maker


def key_down(event):
    global key
    key = event.keysym
    #print(key)


def key_up(event):
    global key
    key = ""


def main_proc():
    delta = {
        
        ""     : [0,  0], 
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    global mx, my
    global cx, cy

    if maze_list[my+delta[key][1]][mx+delta[key][0]] == 0:
        mx, my = mx+delta[key][0], my+delta[key][1] 
        cx, cy = mx*100+50, my*100+50
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科トン")
    root.geometry("1500x900")

    canv = tk.Canvas(root, background="#000", width=1500, height=900)
    canv.pack()

    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canv, maze_list)

    img = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canv.create_image(cx, cy, image=img, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    
    root.mainloop()