import tkinter
import customtkinter as tk
import time
import threading




def update_clock():
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%A')
    day_label.configure(text=current_day)
    clock_label.configure(text=current_time)
    app.after(1000,update_clock)


def long_running_task():
    pass

def start_long_running_task():
    pass


app = tk.CTk()
app.title('Zenark')
app.geometry('400x300')


frame = tk.CTkFrame(app, fg_color='#d8dee9')
frame.pack(fill=tk.BOTH, expand=True)

clock_label = tk.CTkLabel(frame, 
                        font=('calibri',40,'bold'),
                        bg_color='#4c566a',
                        fg_color='#d8dee9')
clock_label.pack(anchor='center')


day_label = tk.CTkLabel(frame,
                        font=('calibri',20,'bold'),
                        bg_color='#4c566a',
                        fg_color='#d8dee9')


update_clock()

if __name__ == '__main__':
  app.mainloop()










