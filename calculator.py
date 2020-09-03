from tkinter import *
import tkinter.messagebox as tmsg


def matched(str):
    '''function for checking balanced parenthesis'''
    li=[]
    for i in str:
        if i=='(':
            li.append(i)
        elif i==')'and len(li)!=0:
            li.pop()
        elif len(li)==0 and i==")":
            return False
    if len(li)==0:
        return True
    return False


def click(event):
    '''function which gets executed when any button gets clicked'''
    global scValue
    text=event.widget.cget("text")  # this cget function is used to get the text from a widget
    #print(text)
    if text =="=":
        if scValue.get()=="":
            value=""
        elif scValue.get().isdigit():
            value=int(scValue.get())
        else:
            if matched(scValue.get()):
                value=eval(screen.get())
            else:
                tmsg.showerror("Invalid Expression","Correct your expression")
                value=scValue.get()

        scValue.set(value)
        screen.update()
    elif text=="C":
        scValue.set("")
        screen.update()

    else:
        scValue.set(scValue.get()+text)
        screen.update()

root=Tk()
root.geometry("470x730")
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")

scValue=StringVar()
scValue.set("")
screen=Entry(root,textvariable=scValue,font="lucida 38 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(root,bg="black")
f.pack()
b=Button(f,text="7",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="9",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 30 bold",bg="indianred",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f=Frame(root,bg="black")
f.pack()
b=Button(f,text="4",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=7)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=7)
b.bind("<Button-1>",click)
b=Button(f,text="6",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=7)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 32 bold",bg="indianred",padx=18,pady=10)
b.pack(side=LEFT,padx=13,pady=7)
b.bind("<Button-1>",click)

f=Frame(root,bg="black")
f.pack()
b=Button(f,text="1",font="lucida 30 bold",padx=19,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="3",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 32 bold",bg="indianred",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f=Frame(root,bg="black")
f.pack()
b=Button(f,text="0",font="lucida 30 bold",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 30 bold",bg="cyan",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="C",font="lucida 30 bold",bg="brown1",padx=18,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 31 bold",bg="indianred",padx=19,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f=Frame(root,bg="black")
f.pack()
b=Button(f,text="00",font="lucida 23 bold",padx=18,pady=15)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 33 bold",padx=20,pady=8)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="(",font="lucida 30 bold",padx=21,bg="indianred",pady=10)
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text=")",font="lucida 31 bold",bg="indianred",padx=21,pady=10)
b.pack(side=LEFT,padx=10,pady=10)
statusBar=Label(root,text=u"\u00a9"+"Pankaj Kumar 2020",relief=SUNKEN,anchor=W,bg="gray",padx=20)
statusBar.pack(side=BOTTOM,fill=X)
b.bind("<Button-1>",click)

root.mainloop()