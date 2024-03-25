import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('300x150')

title_Label = ttk.Label(master = window, text= 'Miles to Kilometer', font = 'Arial 24 bold')
title_Label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side = 'left', padx =1)
button.pack(side ='left')
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_Label = ttk.Label(
    master = window,
    text = 'Output',
    font = ('Arial 20'),
    textvariable= output_string)
output_Label.pack (pady = 5)

window.mainloop()
