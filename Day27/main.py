#Utilizing the tkinter module in Python to experiment with building program with a GUI
import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=2, row=2)
print(input.get())


#Always has to be at the end of a program
window.mainloop()
