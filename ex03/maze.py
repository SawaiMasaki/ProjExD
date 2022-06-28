import tkinter

global key

def key_down(event):
    key = event.keysym

def key_up():
    key = ""

def main_proc():
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("tori", cx, cy)        

if __name__ == "__main__":
    global cx, cy
    root = tkinter.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    key = ""

    canvas = tkinter.Canvas(root, width=1500, height=900, bg="black")
    canvas.place(x=0, y=0)

    

    tori = tkinter.PhotoImage(file="fig/5.jpg")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.mainloop()
