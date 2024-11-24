from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import PhotoImage

def create_nought_image(size: int) -> Image.Image:
    """create a blue circle."""
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((size // 15, size // 15, size - (size // 15), size - (size // 15)), outline="blue", width=20)
    return img

def create_cross_image(size: int) -> Image.Image:
    """create a red cross."""
    img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.line((size // 15, size // 15, size - (size // 15), size - (size // 15)), fill="red", width=20)
    draw.line((size // 15, size - (size // 15), size - (size // 15), size // 15), fill="red", width=20)
    (10, size - 10, size - 10, 10)
    return img

def create_single_colored(size: int, rgba: tuple[int] =(255, 255, 255, 0)) -> Image.Image:
    img = Image.new("RGBA", (size, size), rgba)
    return img


if __name__ == '__main__':
    print(type(create_nought_image(20)))