import tkinter as tk

iskl = 200

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)
    update_font_size()

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
        update_font_size()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        update_font_size()

def clear():
    entry.delete(0, tk.END)
    update_font_size()

def toggle_sign():
    current = entry.get()
    if current.startswith('-'):
        entry.delete(0, tk.END)
        entry.insert(0, current[1:])
    else:
        entry.delete(0, tk.END)
        entry.insert(0, '-' + current)
    update_font_size()

def percentage():
    try:
        current = entry.get()
        result = float(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, result)
        update_font_size()
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        update_font_size()

def update_font_size():
    current_length = len(entry.get())
    font_size = iskl

    if current_length > 10:
        font_size = iskl
    elif current_length > 7:
        font_size = iskl + 10
    elif current_length > 4:
        font_size = iskl + 20
    else:
        font_size = iskl + 30

    entry.config(font=("Helvetica", font_size))

root = tk.Tk()
root.title("Apple calc")
root.geometry("500x700")
root.configure(bg="black")

entry = tk.Entry(root, width=16, font=("Helvetica", iskl), borderwidth=2, relief="solid", justify="right", bd=5, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=30, pady=20, sticky="ew")

buttons = [
    ("AC", 1, 0), ("+/-", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("🖩", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3),
]

def create_button(text, row, col, color, command, size=6):
    button = tk.Button(root, text=text, font=("Helvetica", 18), relief="solid", command=command, bg=color, fg="white", bd=0, highlightthickness=0, padx=20, pady=20, borderwidth=5)
    
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    
    button.config(width=size, height=size)
    button["bd"] = 0
    button.config(highlightthickness=0)
    button.config(relief="flat")
    
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(col, weight=1)
    
    return button

for (text, row, col) in buttons:
    if text == "AC":
        create_button(text, row, col, "#d3d3d3", clear, size=8)
    elif text == "+/-":
        create_button(text, row, col, "#d3d3d3", toggle_sign, size=8)
    elif text == "%":
        create_button(text, row, col, "#d3d3d3", percentage, size=8)
    elif text in ("/", "*", "-", "+"):
        create_button(text, row, col, "#ff8c00", lambda t=text: button_click(t), size=8)
    elif text == "=":
        create_button(text, row, col, "#ff8c00", calculate, size=8)
    elif text == "🖩":
        create_button(text, row, col, "#d3d3d3", lambda: entry.delete(len(entry.get())-1, tk.END), size=8)
    else:
        create_button(text, row, col, "#333333", lambda t=text: button_click(t), size=8)

for i in range(6):
    root.grid_rowconfigure(i, weight=1, minsize=60)

for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=60)

root.mainloop()
