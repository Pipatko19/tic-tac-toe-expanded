import tkinter as tk
import ttkbootstrap as ttk

def on_button_click():
    print("Button clicked!")

root = ttk.Window(themename="simplex")

# Create a custom style for the button
style = ttk.Style()
style.configure("SquareButton.TButton", width=10, padding=20)

# Create a square button using the custom style
button = ttk.Button(root, text="Click Me", style="SquareButton.TButton", command=on_button_click)
button.pack(padx=10, pady=10)

root.mainloop()