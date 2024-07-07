import tkinter as tk
import time
import threading 

def update_clock():
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%A')
    day_label.config(text=current_day)
    clock_label.config(text=current_time)
    window.after(1000, update_clock)

window = tk.Tk()
window.title("Zenark (beta)")
window.geometry("400x300")
window.configure(bg='#e2eafc') 

window.iconbitmap('zenark/zenarkicon.ico')


clock_label = tk.Label(window, font=('calibri', 40, 'bold'), background='#e2eafc', foreground='#abc4ff')
clock_label.pack(anchor='center')

day_label = tk.Label(window, font=('calibri', 20, 'bold'), bg="#e2eafc", fg='#c1d3fe')
day_label.pack()


update_clock()
window.mainloop()