#Utilizing the tkinter module in Python to experiment with building program with a GUI
import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()


#Always has to be at the end of a program
window.mainloop()
