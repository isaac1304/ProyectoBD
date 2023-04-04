import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

root.title("Mi primer GUI")

label = tk.Label(root, text="Hola Mundo", font =('Calibri', 13))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial',13))
textbox.pack(padx=10)

frame =  tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn1 = tk.Button(frame, text="1", font=('Arial',18))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2= tk.Button(frame, text="2", font=('Arial',18))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(frame, text="3", font=('Arial',18))
btn3.grid(row=1,column=0, sticky=tk.W+tk.E)

btn4 = tk.Button(frame, text="4", font=('Arial',18))
btn4.grid(row=1,column=1, sticky=tk.W+tk.E)

frame.pack(fill='x')

#ROOT
root.mainloop()

