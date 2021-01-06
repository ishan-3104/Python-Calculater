#python calcu. using tkinter

from tkinter import *
scr = Tk()
scr.geometry("250x400+300+300")
scr.resizable(0,0)
scr.title("calculater")

data = StringVar()
val = ""
# Intermidiate variable 
a=0
operator = ""

def one_clicked():
    global val
    global data
    val = val + "1"
    data.set(val)

def two_clicked():
    global val
    global data
    val = val + "2"
    data.set(val)

def three_clicked():
    global val
    global data
    val = val + "3"
    data.set(val)

def four_clicked():
    global val
    global data
    val = val + "4"
    data.set(val)

def five_clicked():
    global val
    global data
    val = val + "5"
    data.set(val)

def six_clicked():
    global val
    global data
    val = val + "6"
    data.set(val)

def seven_clicked():
    global val
    global data
    val = val + "7"
    data.set(val)

def eight_clicked():
    global val
    global data
    val = val + "8"
    data.set(val)

def nine_clicked():
    global val
    global data
    val = val + "9"
    data.set(val)

def zero_clicked():
    global val
    global data
    val = val + "0"
    data.set(val)

def c_clicked():
    global val
    global data
    val = ""
    data.set(val)

def puls_clicked():
    global a
    global val
    global operator
    a = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def minus_clicked():
    global a
    global val
    global operator
    a = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def multiply_clicked():
    global a
    global val
    global operator
    a = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)

def divide_clicked():
    global a
    global val
    global operator
    a = int(val)
    operator = "÷"
    val = val + "÷"
    data.set(val)

def result():
    global a
    global val
    global operator
    if operator == "+":
        val_2 = val
        x = int(val_2.split("+")[1])
        val = a + x
        data.set(val)
        val = str(val)
    elif operator == "-":
        val_2 = val
        x = int(val_2.split("-")[1])
        val = a - x
        data.set(val)
        val = str(val)
    elif operator == "x":
        val_2 = val
        x = int(val_2.split("x")[1])
        val = a * x
        data.set(val)
        val = str(val)
    elif operator == "÷":
        val_2 = val
        x = int(val_2.split("÷")[1])
        if int(val_2.split("÷")[1]) != 0:
            val = float(a/x)
            data.set(val)
            val = str(val)
        else:
            val = "Cant divide by 0...!"
            data.set(val)




label = Label(scr,text="lable",anchor= SE,font=("vordana",22),textvariable = data)
label.pack(expand = True,fill="both")


row1 = Frame(scr)
row1.pack(expand = True ,fill= "both" )

b1 = Button(row1,text="1",command = one_clicked)
b1.pack(expand = True,fill="both",side=LEFT)

b2 = Button(row1,text="2",command = two_clicked)
b2.pack(expand = True,fill="both",side=LEFT)

b3 = Button(row1,text="3",command = three_clicked)
b3.pack(expand = True,fill="both",side=LEFT)

bp = Button(row1,text="+",command = puls_clicked)
bp.pack(expand = True,fill="both",side=LEFT)

row2 = Frame(scr)
row2.pack(expand= True,fill="both")
b4 = Button(row2,text="4",command = four_clicked)
b4.pack(expand = True,fill="both",side=LEFT)

b5 = Button(row2,text="5",command = five_clicked)
b5.pack(expand = True,fill="both",side=LEFT)

b6 = Button(row2,text="6",command = six_clicked)
b6.pack(expand = True,fill="both",side=LEFT)

bs = Button(row2,text="-",command = minus_clicked)
bs.pack(expand = True,fill="both",side=LEFT)


row3 = Frame(scr)
row3.pack(expand=True,fill="both")

b7 = Button(row3,text="7",command = seven_clicked)
b7.pack(expand=True,fill="both",side=LEFT)

b8 = Button(row3,text="8",command = eight_clicked)
b8.pack(expand=True,fill="both",side=LEFT)

b9 = Button(row3,text="9",command = nine_clicked)
b9.pack(expand=True,fill="both",side=LEFT)

bm = Button(row3,text="X",command = multiply_clicked)
bm.pack(expand=True,fill="both",side=LEFT)

row4 = Frame(scr)
row4.pack(expand=True,fill="both")

bc = Button(row4,text="C",command = c_clicked)
bc.pack(expand=True,fill="both",side=LEFT) 

b0 = Button(row4,text="0",command = zero_clicked)
b0.pack(expand=True,fill="both",side=LEFT) 

be = Button(row4,text="=",command = result)
be.pack(expand=True,fill="both",side=LEFT) 

bd = Button(row4,text="÷",command = divide_clicked)
bd.pack(expand=True,fill="both",side=LEFT) 

scr.mainloop()
