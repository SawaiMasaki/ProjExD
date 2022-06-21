import tkinter as tk
import tkinter.messagebox as tkm

#ボタンがクリックされた時の処理
def button_click(event):
    btn = event.widget
    txt = btn["text"]   #ボタンの文字
    #tkm.showinfo(txt, f"{txt}のボタンがクリックされました")
    if txt == "=":      # ＝が押された時の処理
        fl = entry.get()
        ans = eval(fl)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)

    elif txt == "C":    #クリアの処理
        fl = entry.get()
        entry.delete(0, tk.END)

    else:               # ＝以外の処理
        entry.insert(tk.END, f"{txt}")

#全体の動き
if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x600")

    symbol = ["", "**", "%", "C", "*", "-", "+"]
    
    r = 1
    c = 0
    for i, num in enumerate(["","**", "%", "C", 7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", "00", 0, ".", "="]):
        button = tk.Button(root, 
                            font=("Times New Roman", 30),
                            text= f"{num}",
                            command=button_click,
                            bg="white",
                            width=4,
                            height=2)
        if num in symbol:
            button = tk.Button(root, 
                            font=("Times New Roman", 30),
                            text= f"{num}",
                            command=button_click,
                            width=4,
                            height=2)

        elif num == "=":
            button = tk.Button(root, 
                            font=("Times New Roman", 30),
                            text= f"{num}",
                            command=button_click,
                            bg="#87cefa",
                            width=4,
                            height=2)                    

        button.bind("<1>", button_click)              
        button.grid(row=r, column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0

    entry = tk.Entry(justify= "right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, columnspan=5)    

    root.mainloop()



    #button0 = tk.Button(root, font=("Times New Roman", 30),text="0", command=button_click, width=4, height=2)
    #button1 = tk.Button(root, font=("Times New Roman", 30),text="1", command=button_click, width=4, height=2)
    #button2 = tk.Button(root, font=("Times New Roman", 30),text="2", command=button_click, width=4, height=2)
    #button3 = tk.Button(root, font=("Times New Roman", 30),text="3", command=button_click, width=4, height=2)
    #button4 = tk.Button(root, font=("Times New Roman", 30),text="4", command=button_click, width=4, height=2)
    #button5 = tk.Button(root, font=("Times New Roman", 30),text="5", command=button_click, width=4, height=2)
    #button6 = tk.Button(root, font=("Times New Roman", 30),text="6", command=button_click, width=4, height=2)
    #button7 = tk.Button(root, font=("Times New Roman", 30),text="7", command=button_click, width=4, height=2)
    #button8 = tk.Button(root, font=("Times New Roman", 30),text="8", command=button_click, width=4, height=2)
    #button9 = tk.Button(root, font=("Times New Roman", 30),text="9", command=button_click, width=4, height=2)

    #button0.bind("<1>", button_click)
    #button1.bind("<1>", button_click)
    #button2.bind("<1>", button_click)
    #button3.bind("<1>", button_click)
    #button4.bind("<1>", button_click)
    #button5.bind("<1>", button_click)
    #button6.bind("<1>", button_click)
    #button7.bind("<1>", button_click)
    #button8.bind("<1>", button_click)
    #button9.bind("<1>", button_click)

    #button0.grid(row=3, column=0)
    #button1.grid(row=2, column=2)
    #button2.grid(row=2, column=1)
    #button3.grid(row=2, column=0)
    #button4.grid(row=1, column=2)
    #button5.grid(row=1, column=1)
    #button6.grid(row=1, column=0)
    #button7.grid(row=0, column=2)
    #button8.grid(row=0, column=1)
    #button9.grid(row=0, column=0)