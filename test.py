import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Create the main application window
app = ttk.Window()
app.title("Button Border Color Example")
app.geometry("300x200")

# Create a custom style for the button
style = ttk.Style()
style.configure("Custom.TButton", borderwidth=20)

# Map the border color for the disabled state
style.map("Custom.TButton", 
          bordercolor=[("disabled", "red")],  # Change to your desired color
          foreground=[("disabled", "gray")],  # Optional: Change text color too
          background=[("disabled", "#f0f0f0")])  # Optional: Change background

# Create the button using the custom style
button = ttk.Button(app, text="Disabled Button", style="Custom.TButton")
button.pack(pady=20)

# Disable the button to see the effect
button.state(["disabled"])

app.mainloop()
