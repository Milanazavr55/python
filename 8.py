'''
from tkinter import *

def sss():
    newText = txt.get()
    lbl.configure(text = ("Ээээ" + newText))
    
window = Tk()
window.title("vsemprivetchovamnado!!")
window.geometry('700x500')

lbl = Label(window, text = "Чо надо", font=("Arial Bold", 50))
lbl.pack()

btn = Button(window, text = "Ничо", command = sss)
btn.pack()

txt = Entry(window, width = 10)
txt.focus()
txt.pack()

window.mainloop()
'''
from tkinter import *


def sss():
    txtv = int(txt1.get())
    txtv1 = int(txt2.get())
    lbl.configure(text = (txtv + txtv1))
    
def ddd():
    txtv = int(txt1.get())
    txtv1 = int(txt2.get())
    lbl.configure(text = (txtv - txtv1))
 
def fff():
    txtv = int(txt1.get())
    txtv1 = int(txt2.get())
    lbl.configure(text = (txtv * txtv1))
    
def ggg():
    txtv = int(txt1.get())
    txtv1 = int(txt2.get())
    lbl.configure(text = (txtv / txtv1))
    
window = Tk()
window.title("Калькулятор")
window.geometry('380x520')


lbl = Label(window, text = "", font=("Arial Bold", 40))
lbl.place(x=150, y=50)

btn = Button(window, text = "+", command = sss, width = 10, height = 5)
btn.place(x=298, y=432)

btn = Button(window, text = "-", command = ddd, width = 10, height = 5)
btn.place(x=298, y=350)

btn = Button(window, text = "*", command = fff, width = 10, height = 5)
btn.place(x=298, y=264)

btn = Button(window, text = "/", command = ggg, width = 10, height = 5)
btn.place(x=298, y=186)

    
txt1 = Entry(window, width = 30)
txt1.place(x=100, y=160)


txt2 = Entry(window, width = 30)
txt2.focus()
txt2.place(x=100, y=186)


window.mainloop()