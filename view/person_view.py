import tkinter as tk

root = tk.Tk()
root.title("Gym Manager System")
root.geometry("900x650")
root.configure(bg="#F2F4F7")

person_frame = tk.Frame(
    root,
    bg="#F2F4F7",
    highlightbackground="#3984E8",
    highlightthickness=2
)
person_frame.place(relx=0.5, rely=0.5, anchor="center", width=520, height=390)

title = tk.Label(person_frame, text="Person", font=(20), bg="C9E0FF", fg="black", pady=10)
title.pack(fill="x")

from_frame= tk.Frame(person_frame, bg="#F2F4F7")
from_frame.pack(padx=25, pady=20, fill="both", expand=True)

tk.Label(
    from_frame,
    text="Name",
    font=(12),
    width=25
).grid(row=0, column=0, sticky="w", pady=8)

name_entry = tk.Entry(from_frame, font=(12), width=25)
name_entry.grid(row=0, column=1, padx=15, pady=8)









root.mainloop()
