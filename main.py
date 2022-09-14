from tkinter import *
from time import strftime

root = Tk()
root.title('Digital Clock')
root.geometry("600x130")


# display_time() function will display the current time in 12-hour clock format
def display_time():
    current_time = strftime('%I:%M:%S %p')
    lblTime.config(text=current_time)
    lblTime.after(1000, display_time)


# Label for Time
lblTime = Label(root, text='Time', font=('Arial', 60), bg='white', fg='blue')
lblTime.pack()

display_time()

root.mainloop()
