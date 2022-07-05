import tkinter

def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)
    
if  __name__ == "__main__":
    root = tkinter.Tk()
    label = tkinter.Label(root,
            font=("Times New Roman", 80)
            )
    label.pack()
    tmr = 0
    root.after(1000, count_up)
    root.mainloop()
