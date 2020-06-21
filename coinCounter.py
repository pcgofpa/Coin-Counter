import tkinter as tk
from tkinter import *

#Variables
HEIGHT = 200
WIDTH = 700

def calculate():
    q=int(quarterInput.get())
    d=int(dimeInput.get())
    n=int(nickelInput.get())
    p=int(pennyInput.get())
    qValue=float(q*0.25)
    dValue=float(d*0.10)
    nValue=float(n*0.05)
    pValue=float(p*0.01)
    lblQValue=tk.Label(frame, text="${:,.2f}".format(qValue))
    lblQValue.grid(row=1,column=5)
    lblDValue=tk.Label(frame, text="${:,.2f}".format(dValue))
    lblDValue.grid(row = 2, column = 5)
    lblNValue=tk.Label(frame, text="${:,.2f}".format(nValue))
    lblNValue.grid(row=3, column = 5)
    lblPValue=tk.Label(frame, text="${:,.2f}".format(pValue))
    lblPValue.grid(row=4, column = 5)
    totalCoins = int(q+d+n+p)
    lblTotalCoins=tk.Label(frame, text=totalCoins)
    lblTotalCoins.grid(row = 5, column = 2)
    coinValue=float(qValue+dValue+nValue+pValue)
    lblCoinValue=tk.Label(frame, text="${:,.2f}".format(coinValue))
    lblCoinValue.grid(row=5, column=5)

    
coinCounter = tk.Tk()

canvas = tk.Canvas(coinCounter, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(coinCounter, bg="green")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



#label frame displays information
label1 = tk.Label(frame, text = "Coins")
label2 = tk.Label(frame, text = "Please enter how many coins" "\n you have in this column!")
label3 = tk.Label(frame, text = "Your totals for each coin" "\n will be displayed in this column!")
label4 = tk.Label(frame, text = "Quarters")
label6 = tk.Label(frame, text = "Dimes")
label8 = tk.Label(frame, text = "Nickels")
label10 = tk.Label(frame, text="Pennies")
totalLabel=tk.Label(frame, text="Totals: ")


#Entries
v=IntVar()
a=IntVar()
b=IntVar()
c=IntVar()
quarterInput=tk.Entry(frame, text=v, bg="White")
dimeInput=tk.Entry(frame, text=a, bg="White")
nickelInput=tk.Entry(frame, text=b, bg="White")
pennyInput=tk.Entry(frame, text=c, bg="White")
v.set(0)
a.set(0)
b.set(0)
c.set(0)
#Buttons
calculateButton = tk.Button(frame, text="Calculate", command=calculate)
exitButton = tk.Button(frame, text="Exit", bg= "red", command=coinCounter.destroy)

# GUI Layout
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 2)
label3.grid(row = 0, column = 5)
label4.grid(row = 1, column = 0)
quarterInput.grid(row = 1, column = 2)
label6.grid(row = 2, column = 0)
dimeInput.grid(row = 2, column = 2)
label8.grid(row = 3, column = 0)
nickelInput.grid(row = 3, column = 2)
label10.grid(row = 4, column = 0)
pennyInput.grid(row = 4, column = 2)
totalLabel.grid(row = 5, column = 0)
calculateButton.grid(row = 6, column = 2)
exitButton.grid(row = 6, column = 5)




coinCounter.mainloop()
