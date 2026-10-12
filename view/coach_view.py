import tkinter as tk
from tkinter import ttk

from fontTools.ttLib.tables.grUtils import entries

#Main Window
window = tk.Tk()
window.title("Coach Information")
window.geometry("420x420")
window.configure(bg="#f0f2f5")
window.resizable(False, False)

# Title
title = tk.Label(
    window,
    text="Coach Information",
    font=("Arial", 18, "bold"),
    bg="#f0f2f5",
    fg="#263238"
)
title.pack(pady=20)

#Main Frame
main_frame = tk.Frame(window, bg="white",padx=25, pady=20)
main_frame.pack(padx=25, fill="both", expand=True)

#Person Attributes
fields = [
    "Name:",
    "Age:",
    "Phone:",
    "BMI:"
]
entries = {}

for row, field in enumerate(fields):
    label = tk.Label(
        main_frame,
        text=field,
        font=("Arial", 11),
        bg="white",
        fg="#263238"
    )
    label.grid(row=row, column=0, sticky="w", pady=10)

    entry = tk.Entry(
        main_frame,
        font=("Arial", 11),
        width=22
    )
    entry.grid(row=row, column=1, pady=10)

    entries[field] = entry

#Coach Method
assign_button = ttk.Button(
    main_frame,
    text="Assign Workout"
)
assign_button.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)

window.mainloop()
