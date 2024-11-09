from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import PhotoImage

def create_nought_image(size):
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((size // 15, size // 15, size - (size // 15), size - (size // 15)), outline="blue", width=20)
    return ImageTk.PhotoImage(img)

def create_cross_image(size):
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.line((size // 15, size // 15, size - (size // 15), size - (size // 15)), fill="red", width=20)
    draw.line((size // 15, size - (size // 15), size - (size // 15), size // 15), fill="red", width=20)
    (10, size - 10, size - 10, 10)
    return ImageTk.PhotoImage(img)

if __name__ == '__main__':
    app = tk.Tk()
    app.geometry('200x200')
    img = create_nought_image(400)
    img2 = create_cross_image(400)
    label = tk.Label(image=img)
    label.pack()
    label2 = tk.Label(image=img2)
    label2.pack()
    app.mainloop()