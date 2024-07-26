import tkinter as tk
from tkinter import PhotoImage
import time
import threading 


# Function that defines the functioning of the clock
def update_clock():
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%A')
    day_label.config(text=current_day)
    clock_label.config(text=current_time)
    window.after(1000, update_clock)


# Function that defines the long running task
def long_running_task():
    for i in range(5):
        print(f'Long-running task: Step {i+1}')
        time.sleep(2)
        print('long-running task completed')



# Function that defines starting long running task
def start_long_running_task():
    task_thread = threading.Thread(target=long_running_task)
    task_thread.start()


window = tk.Tk()
window.title("Zenark (beta)")
window.geometry("400x300")
window.configure(bg='#e2eafc') 
window.iconbitmap('zenark/resourses/zenark_titlebar_icon.ico')

# Taskbar icon setup
icon_image = PhotoImage(file='zenark/resourses/zenark_desktop_icon.pgm')
window.iconphoto(True, icon_image)


clock_label = tk.Label(window, font=('calibri', 40, 'bold'), background='#e2eafc', foreground='#abc4ff')
clock_label.pack(anchor='center')

day_label = tk.Label(window, font=('calibri', 20, 'bold'), bg="#e2eafc", fg='#c1d3fe')
day_label.pack()


update_clock()
window.mainloop()