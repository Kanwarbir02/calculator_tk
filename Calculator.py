from tkinter import *

root= Tk()

root.title("Calculator")

e=Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

# global f_num

def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def click_clear():
    e.delete(0,END)

def adder():    
    global f_num
    f_num = e.get()
    e.delete(0, END)
    global operator
    operator="add"

def subtract():    
    global f_num
    f_num = e.get()
    e.delete(0, END)
    global operator
    operator="subtract" 

def multiply():    
    global f_num
    f_num = e.get()
    e.delete(0, END)
    global operator
    operator="multiply"

def divide():    
    global f_num
    f_num = e.get()
    e.delete(0, END)
    global operator
    operator="divide"

def equalbtn():
    sec_num= e.get()
    e.delete(0, END)
    if(operator=="add"):
        e.insert(0, int(f_num) + int(sec_num))
    if(operator=="subtract"):
        e.insert(0, int(f_num) - int(sec_num))
    if(operator=="multiply"):
        e.insert(0, int(f_num) * int(sec_num))
    if(operator=="divide"):
        e.insert(0, int(f_num) / int(sec_num))               

button1= Button(root, text="1", width=10, height=5, command=lambda: buttonclick(1))
button2= Button(root, text="2", width=10, height=5, command=lambda: buttonclick(2))
button3= Button(root, text="3", width=10, height=5, command=lambda: buttonclick(3))
button4= Button(root, text="4", width=10, height=5, command=lambda: buttonclick(4))
button5= Button(root, text="5", width=10, height=5, command=lambda: buttonclick(5))
button6= Button(root, text="6", width=10, height=5, command=lambda: buttonclick(6))
button7= Button(root, text="7", width=10, height=5, command=lambda: buttonclick(7))
button8= Button(root, text="8", width=10, height=5, command=lambda: buttonclick(8))
button9= Button(root, text="9", width=10, height=5, command=lambda: buttonclick(9))
button0= Button(root, text="0", width=10, height=5, command=lambda: buttonclick(0))
buttonadd= Button(root, text="+", width=10, height=5, command=adder)
buttonsub= Button(root, text="-", width=10, height=5, command=subtract)
buttonpro= Button(root, text="x", width=10, height=5, command=multiply)
buttondiv= Button(root, text="/", width=10, height=5, command=divide)
buttoneq= Button(root, text="=", width=22, height=5, command=equalbtn)
buttonclr= Button(root, text="Clear", width=22, height=5, command=click_clear)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4, column=0)
buttoneq.grid(row=4, column=1, columnspan=2)

buttonadd.grid(row=5, column=0)
buttonclr.grid(row=5, column=1, columnspan=2)

buttonsub.grid(row=6, column=0)
buttonpro.grid(row=6, column=1)
buttondiv.grid(row=6, column=2)

root.mainloop()