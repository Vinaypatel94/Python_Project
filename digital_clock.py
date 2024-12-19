import tkinter as tk  #use gui base .
from time import strftime #  use current time and date

root =tk.Tk()  # set root windows
root.title("Digital clock") # set title
def time():
   string=strftime("%H:%M:%S:%p\n %D" )
   lebel.config(text=string)
   lebel.after(1000,time) # continues update time 

lebel=tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='white')
lebel.pack(anchor="center")

time()
root.mainloop()

