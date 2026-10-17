from tkinter import *
from tkinter import ttk

def close_app():
    win.destroy()

win = Tk()
win.geometry("770x340")
win.title("Gym Management App")
win.configure(bg="#f2f5f3")
win.wm_protocol("WM_DELETE_WINDOW", close_app)

bg_color = "#f2f5f3"
entry_bg = "#ffffff"
btn_save_bg = "#6c9a8b"
btn_reset_bg = "#a2abb2"

# Person Id
person_id = IntVar()
Label(win, text="ID", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=20)
Entry(win, textvariable=person_id, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=20)

# Name
name = StringVar()
Label(win, text="Name", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=60)
Entry(win, textvariable=name, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=60)

# Age
age = IntVar()
Label(win, text="Age", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=100)
Entry(win, textvariable=age, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=100)

# Phone
phone = IntVar()
Label(win, text="Phone", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=140)
Entry(win, textvariable=phone, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=140)

# BMI
bmi = DoubleVar()
Label(win, text="BMI", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=180)
Entry(win, textvariable=bmi, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=180)

# Class Level
class_level = StringVar()
Label(win, text="Level", bg=bg_color, fg="#2c3e50", font=("Tahoma", 9, "bold")).place(x=20, y=220)
Entry(win, textvariable=class_level, width=16, bg=entry_bg, relief="solid", bd=1).place(x=90, y=220)

# Buttons
Button(win, text="Save", width=9, bg=btn_save_bg, fg="white", font=("Tahoma", 9, "bold"), relief="flat", activebackground="#5b8274", activeforeground="white").place(x=20, y=270)
Button(win, text="Reset", width=9, bg=btn_reset_bg, fg="white", font=("Tahoma", 9, "bold"), relief="flat", activebackground="#8b959c", activeforeground="white").place(x=95, y=270)

# Table (Treeview)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", background="#d8e3dc", foreground="#2c3e50", font=("Tahoma", 9, "bold"), relief="flat")
style.configure("Treeview", background="white", fieldbackground="white", rowheight=24, font=("Tahoma", 9))
style.map("Treeview", background=[('selected', '#b1cbbd')])

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6),
    show="headings",
)

table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Age")
table.heading(4, text="Phone")
table.heading(5, text="BMI")
table.heading(6, text="Level")

table.column(1, width=40, anchor="center")
table.column(2, width=90, anchor="w")
table.column(3, width=50, anchor="center")
table.column(4, width=95, anchor="w")
table.column(5, width=60, anchor="center")
table.column(6, width=75, anchor="center")

table.place(x=230, y=20, height=270)

win.mainloop()