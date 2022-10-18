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
    global cx, cy

    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20

    print(cx,cy)    
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)


def make_maze(15, 9):
    


if __name__ == "__main__":

    global cx
    global cy

    root = tk.Tk()
    root.title("迷える工科トン")
    root.geometry("1500x900")

    canvas = tk.Canvas(root, background="#000", width=1500, height=900)
    canvas.pack()

    img = tk.PhotoImage(file="fig/0.png")
    cx = 300
    cy = 400

    canvas.create_image(cx, cy, image=img, tag="tori")
    
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()

    

