from tkinter import *
window = Tk()
window.title("Miles Convertor")
window.minsize(width = 300,height = 300)
window.config(padx = 50 , pady = 50)

#Label
my_label = Label(text =" is equal to")
my_label.grid(column =2 , row = 1)

#Input
input = Entry(width = 10)
input.grid(column =4 , row = 0)

#ANSWER AS RESULT
answer = Label(text= 0)
answer.grid(column =4 , row = 1)

#KM
km = Label(text = "km")
km.grid(column =5 , row = 1)

#MILES
miles =Label(text = "miles")
miles.grid(column =5 , row = 0)

def convertor():
    data = float(input.get())
    result =round(data * 1.6)
    answer.config(text = f"{result}")


#BUTTON
button = Button(text = "calculate",command = convertor)
button.grid(column = 4, rows = 4)











window.mainloop()