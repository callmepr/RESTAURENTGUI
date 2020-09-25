from tkinter import *
import time
import random

root=Tk()
root.geometry("1350x625")
root.title("RESTAURENT GUI")
root.configure(background="#DB9343")


label=Label(root, font=( 'aria' ,25, 'bold' ),text="PRAJAPATI'S RESTAURENT",anchor=W)
label.grid(row=0,column=1,padx=20,columnspan=2)
#---time---#
localtime=time.asctime(time.localtime(time.time()))
label_time=Label(root, font=( 'Times' ,25, 'bold' ),text=localtime,bg="yellow")
label_time.grid(row=2,column=1,padx=20,pady=10,columnspan=3)


text_input=StringVar()
operator =""

f1=Frame(root,width=400,height=700)
f1.grid(row=4,column=1)

h = Frame(root ,width = 400,height=700)
h.grid(row=4,column=4,padx=10)

e=Entry(h, font=( 'aria' ,25, 'bold' ),textvariable=text_input,insertwidth=7,bd=10)
e.grid(ipadx=10,columnspan=3)

#----all  fun ----#
def exit():
    root.destroy()

def button_click(number):
    global operator
    # operator=e.get()
    operator=operator+str(number)
    text_input.set(operator)

def button_equal():
    global operator
    f_sum=str(eval(operator))
    text_input.set(f_sum)
    operator = ""

def button_clear():
    global operator
    text_input.set("")
    operator=""

def Ref():
    x=random.randint(10000,90001)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))

    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)

    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)

    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)

    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


#---all buttons---#
button_1=Button(h,text="1",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(1)) 
button_3=Button(h,text="3",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(3)) 
button_4=Button(h,text="4",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(4)) 
button_2=Button(h,text="2",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(2)) 
button_5=Button(h,text="5",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(5)) 
button_6=Button(h,text="6",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(6)) 
button_7=Button(h,text="7",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(7)) 
button_8=Button(h,text="8",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(8)) 
button_9=Button(h,text="9",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(9)) 
button_0=Button(h,text="0",padx=40,pady=20,bg="#DA3358",command=lambda :button_click(0))
button_add=Button(h,text="+",padx=39,pady=20,bg="#DA3358",command=lambda: button_click("+")) 
button_substract=Button(h,text="-",padx=40,pady=20,bg="#DA3358",command=lambda: button_click("-")) 
button_divide=Button(h,text="/",padx=40,pady=20,bg="#DA3358",command=lambda: button_click("/")) 
button_multiply=Button(h,text="*",padx=40,pady=20,bg="#DA3358",command=lambda: button_click("*")) 
button_equal=Button(h,text="=",padx=91,pady=20,bg="#DA3358",command=button_equal) 
button_clear=Button(h,text="Clear",padx=81,pady=20,bg="#DA3358",command=button_clear)
status = Label(h,font=('aria', 15, 'bold'),width = 24, text="-BY  RUPESH PRAJAPATI",bd=2,relief=SUNKEN)
status.grid(row=11,columnspan=3,pady=2)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=exit)
btnexit.grid(row=7, column=3)


#----button positions---#
button_1.grid(row=9,column=0)
button_2.grid(row=9,column=1)
button_3.grid(row=9,column=2)

button_4.grid(row=8,column=0)
button_6.grid(row=8,column=2)
button_5.grid(row=8,column=1)

button_7.grid(row=7,column=0)
button_8.grid(row=7,column=1)
button_9.grid(row=7,column=2)

button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)
button_substract.grid(row=5,column=0)
button_add.grid(row=6,column=0) 

button_0.grid(row=10,column=0)
button_clear.grid(row=10,column=1,columnspan=2,pady=1)
button_equal.grid(row=6,column=1,pady=1,columnspan=2,ipadx=9) 


#-menu for food--#
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----another window for pricelist---#
def price():
    ano = Tk()
    ano.geometry("490x230")
    ano.title("Price List")
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(ano, font=('aria', 15,'bold'), text="------------", fg="white")
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="PRICE", fg="black")
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue")
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="25", fg="steel blue")
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue")
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="40", fg="steel blue")
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue")
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="35", fg="steel blue")
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue")
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="50", fg="steel blue")
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="30", fg="steel blue")
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue")
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(ano, font=('aria', 15, 'bold'), text="35", fg="steel blue")
    lblinfo.grid(row=6, column=3)

    ano.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)




root.mainloop()