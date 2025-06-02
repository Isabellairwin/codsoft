import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password:\n{password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number")
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.resizable(False, False)
tk.Label(root, text="Password Generator", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Enter desired password length:").pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12), wraplength=300)
result_label.pack(pady=10)
root.mainloop()
