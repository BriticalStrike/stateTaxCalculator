from tkinter import *

states = {'alabama':1.04,'alaska':1.0,'arizona':1.056,'arkansas':1.065, 'california':1.0725,'colorado':1.029,
    'connecticut':1.0635,'delaware':1.0,'florida':1.06,'georgia':1.04,'hawaii':1.04,'idaho':1.06,'illinois':1.0625,
    'indiana':1.07,'iowa':1.06,'kansas':1.065,'louisiana':1.05,'maine':1.055,'maryland':1.06,'massachusetts':1.0625,
    'michigan':1.06,'minnesota':1.06875,'mississippi':1.07,'missouri':1.04225,'montana':1.0,'nebraska':1.055,
    'nevada':1.0685,'new hampshire':1.0,'new jersey':1.06625,'new mexico':1.05125,'new york':1.04,'north carolina':1.0475,
    'north dakota':1.05,'ohio':1.0575,'oklahoma':1.045,'oregon':1.0,'pennsylvania':1.06,'rhode island':1.07,
    'south carolina':1.06,'south dakota':1.045,'tennessee':1.07,'texas':1.0625,'utah':1.047,'vermont':1.06,'virginia':1.043,
    'washington':1.065,'west virginia':1.06,'wisconsin':1.05,'wyoming':1.04}

def new_cost():
    error_text.delete("1.0", END)
    state = e2.get().lower()
    if state in states.keys():
        tax = states[state]
    else:
        error_text.delete("1.0", END)
        error_text.insert(INSERT, "That is not a state. Try again")
    try:
        cost = float(e1.get())
        new_cost = float(cost*tax)
        t_cost.delete("1.0", END)
        t_cost.insert(END, round(new_cost, 2))
    except ValueError:
        error_text.delete("1.0", END)
        error_text.insert(INSERT, "That is not a valid cost.")

window = Tk()

window.wm_title("State Tax Calculator")

l1 = Label(window, text='Price')
l1.grid(row=0,column=0)

l2 = Label(window, text='State')
l2.grid(row=0, column=1)

l3 = Label(window, text='Cost')
l3.grid(row=0, column=2)

t_cost = Text(window, height=1, width=15)
t_cost.grid(row=1, column=2)

price_text = StringVar()
e1 = Entry(window, textvariable=price_text)
e1.grid(row=1, column=0)

state_text = StringVar()
e2 = Entry(window, textvariable = state_text)
e2.grid(row=1, column=1)

error_text = Text(window, height=1, width=35)
error_text.grid(row=2, column=0, columnspan=3)

b1 = Button(window, text='Calculate', command=new_cost)
b1.grid(row=1, column=3)

window.mainloop()