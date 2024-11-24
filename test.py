import ttkbootstrap as ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def create_single_colored(size: int, rgba: tuple[int] =(255, 255, 255, 0)) -> Image.Image:
    img = Image.new("RGBA", (size, size), rgba)
    return img

# Initialize the ttkbootstrap style
style = ttk.Style("flatly")  # Example theme

# Create the main window
root = ttk.Window()

# Keep a reference to the image
square_image = ImageTk.PhotoImage(create_single_colored(20))  # Ensure the image is square


# Create a square button with the image
button = ttk.Button(
    root,
    image=square_image,  # Use the square image
    style="primary.TButton",  # Use a ttkbootstrap style
    command=lambda: print("Button clicked!")
)

# Set the button dimensions if needed
button.config(width=square_image.width(), height=square_image.height())

# Place the button
button.pack(pady=20, padx=20)

# Keep the reference
root.square_image = square_image  # Store the image as an attribute of the root window

# Run the application
root.mainloop()