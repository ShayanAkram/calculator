from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root,width=45,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 10)

def clearEntry():
    e.delete(0,END)

def click_button(number):
    current = e.get()
    clearEntry()
    e.insert(0,str(current)+str(number))

def addition():
    first_num = e.get()
    global f_num
    global f_name
    f_name = "add"
    f_num = int(first_num)
    clearEntry()

def subtraction():
    first_num = e.get()
    global f_num
    global f_name
    f_name = "sub"
    f_num = int(first_num)
    clearEntry()

def multiply():
    first_num = e.get()
    global f_num
    global f_name
    f_name = "mul"
    f_num = int(first_num)
    clearEntry()

def divide():
    first_num = e.get()
    global f_num
    global f_name
    f_name = "div"
    f_num = int(first_num)
    clearEntry()


def answer():
    secondNumber = e.get()
    clearEntry()
    if(f_name == "add"):
        e.insert(0,f_num+int(secondNumber))
    elif(f_name == "sub"):
    	e.insert(0,f_num-int(secondNumber))
    elif(f_name == "mul"):
    	e.insert(0,f_num*int(secondNumber))
    else:
    	e.insert(0,f_num/int(secondNumber))	

	    

b1 = Button(root,text = "0",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(0))
b2 = Button(root,text = "1",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(1))
b3 = Button(root,text = "2",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(2))
b4 = Button(root,text = "3",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(3))
b5 = Button(root,text = "4",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(4))
b6 = Button(root,text = "5",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(5))
b7 = Button(root,text = "6",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(6))
b8 = Button(root,text = "7",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(7))
b9 = Button(root,text = "8",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(8))
b10 = Button(root,text = "9",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: click_button(9))
button_add = Button(root,text = "+",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: addition())
button_sub = Button(root,text = "-",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: subtraction())
button_mul = Button(root,text = "*",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: multiply())
button_div = Button(root,text = "/",bg = "black",padx = 10,pady = 10,fg = "white",command = lambda: divide())
button_equal = Button(root,text = "=",bg = "black",padx = 30,pady = 10,fg = "white",command = lambda: answer())
button_clear = Button(root,text = "clear",bg = "black",padx = 30,pady = 10,fg = "white",command = lambda: clearEntry())


b1.grid(row = 4,column = 0,padx = 4,pady = 4)
b2.grid(row = 3,column = 2,padx = 4,pady = 4)
b3.grid(row = 3,column = 1,padx = 4,pady = 4)
b4.grid(row = 3,column = 0,padx = 4,pady = 4)
b5.grid(row = 2,column = 2,padx = 4,pady = 4)
b6.grid(row = 2,column = 1,padx = 4,pady = 4)
b7.grid(row = 2,column = 0,padx = 4,pady = 4)
b8.grid(row = 1,column = 2,padx = 4,pady = 4)
b9.grid(row = 1,column = 1,padx = 4,pady = 4)
b10.grid(row = 1,column = 0,padx = 4,pady = 4)


button_add.grid(row = 4,column = 3,padx = 4,pady = 4)
button_sub.grid(row = 3,column = 3,padx = 4,pady = 4)
button_mul.grid(row = 2,column = 3,padx = 4,pady = 4)
button_div.grid(row = 1,column = 3,padx = 4,pady = 4)
button_equal.grid(row = 5,column = 1,columnspan = 2,padx = 4,pady = 4)
button_clear.grid(row = 4,column = 1,columnspan = 2,padx = 4,pady = 4)

root.mainloop()