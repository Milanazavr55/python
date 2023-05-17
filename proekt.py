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

def h1():
    txt2.insert(END, 1)

def h2():
    txt2.insert(END, 2)

def h3():
    txt2.insert(END, 3)

def h4():
    txt2.insert(END, 4)
    
def h5():
    txt2.insert(END, 5)
    
def h6():
    txt2.insert(END, 6)
    
def h7():
    txt2.insert(END, 7)
    
def h8():
    txt2.insert(END, 8)
    
def h9():
    txt2.insert(END, 9)
    
def h0():
    txt2.insert(END, 0)
    

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
window.geometry('380x548')


lbl = Label(window, text = "", font=("Arial Bold", 40))
lbl.place(x=150, y=50)

btn = Button(window, text = "+", command = sss, width = 9, height = 2)
btn.place(x=294, y=220)

btn = Button(window, text = "-", command = ddd, width = 9, height = 2)
btn.place(x=294, y=300)

btn = Button(window, text = "*", command = fff, width = 9, height = 2)
btn.place(x=294, y=380)

btn = Button(window, text = "/", command = ggg, width = 9, height = 2)
btn.place(x=294, y=450)



btn = Button(window, text = "=", command = ggg, width = 21, height = 2)
btn.place(x=102, y=450)



btn = Button(window, text = "1", command = h1, width = 9, height = 2)
btn.place(x=198, y=380)

btn = Button(window, text = "2", command = h2, width = 9, height = 2)
btn.place(x=102, y=380)

btn = Button(window, text = "3", command = h3, width = 9, height = 2)
btn.place(x=6, y=380)

btn = Button(window, text = "4", command = h4, width = 9, height = 2)
btn.place(x=6, y=300)

btn = Button(window, text = "5", command = h5, width = 9, height = 2)
btn.place(x=102, y=300)

btn = Button(window, text = "6", command = h6, width = 9, height = 2)
btn.place(x=198, y=300)

btn = Button(window, text = "7", command = h7, width = 9, height = 2)
btn.place(x=6, y=220)

btn = Button(window, text = "8", command = h8, width = 9, height = 2)
btn.place(x=102, y=220)

btn = Button(window, text = "9", command = h9, width = 9, height = 2)
btn.place(x=198, y=220)

btn = Button(window, text = "0", command = h0, width = 9, height = 2)
btn.place(x=6, y=450)



txt2 = Entry(window, width = 22)
txt2.focus()
txt2.place(x=100, y=130)


window.mainloop()