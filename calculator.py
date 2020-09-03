from tkinter import *

root=Tk()
root.title("Simple Calculator")
inp=Entry(width=50,borderwidth=4)
inp.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click_num(number):
    #inp.delete(0,END)
    current=inp.get()
    inp.delete(0,END)
    inp.insert(0,str(current)+str(number))
    return

def clear_field():
    inp.delete(0,END)
def add():
    first_num=inp.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    inp.delete(0,END)
def button_eq():
    second_num=inp.get()
    inp.delete(0,END)
    if math == "addition":
        inp.insert(0,f_num+int(second_num))
    if math == "subtraction":
        inp.insert(0,f_num-int(second_num))
    if math == "multiplication":
        inp.insert(0,f_num*int(second_num))
    if math == "division":
        inp.insert(0,f_num/int(second_num))            
    
def subtract():
    first_num=inp.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_num)
    inp.delete(0,END)
    return

def multiply():
    first_num=inp.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    inp.delete(0,END)
    return 

def divide():
    first_num=inp.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    inp.delete(0,END)
    return



button_1=Button(root,text="1",padx=40,pady=20,command=lambda:click_num(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:click_num(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:click_num(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:click_num(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:click_num(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:click_num(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:click_num(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:click_num(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:click_num(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:click_num(0))
buttton_add=Button(root,text="+",padx=40,pady=20,command=add)
button_clear=Button(root,text="C",padx=40,pady=20,command=clear_field)
button_equ=Button(root,text="=",padx=55,pady=20,command=button_eq)

buttton_sub=Button(root,text="-",padx=40,pady=20,command=subtract)
buttton_mul=Button(root,text="*",padx=40,pady=20,command=multiply)
buttton_div=Button(root,text="/",padx=40,pady=20,command=divide)

#disply button using grid
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
buttton_add.grid(row=4,column=1)

button_clear.grid(row=4,column=2)
button_equ.grid(row=6,column=1,columnspan=1)
buttton_sub.grid(row=5,column=0)
buttton_mul.grid(row=5,column=1)
buttton_div.grid(row=5,column=2)
root.mainloop()