import tkinter
import maze_maker


def key_down(event):
    global key
    key = event.keysym
    main_proc()

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my

    if key == "Up" and maze[my-1][mx] == 0:
        my -= 1
    elif key == "Down" and maze[my+1][mx] == 0:
        my += 1
    elif key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    elif key == "Right" and maze[my][mx+1] == 0:
        mx += 1

    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    #root.after(100, main_proc)        

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")

    key = ""

    canvas = tkinter.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze)

    tori = tkinter.PhotoImage(file="fig/9.png")

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50

    canvas.create_image(cx, cy, image=tori, tag="tori")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.mainloop()
