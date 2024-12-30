import tkinter as tk
import numpy as np
from typing import Literal
from PIL import Image

from helper_functions import increase_grid
from images import create_cross_image, create_nought_image, create_single_colored

class TttModel:
    MAX_IMG_SIZE = 700
    def __init__(self) -> None:
        self._player: int = 1
        self.free: int = 1
        self.size: int = 1
        self.str_player: tk.StringVar = tk.StringVar(value='Players turn: Crosses')
        self.grid: np.ndarray = np.zeros((1, 1), dtype=np.int8)
        
        self.cross_img = create_cross_image(TttModel.MAX_IMG_SIZE)
        self.nought_img = create_nought_image(TttModel.MAX_IMG_SIZE)
        self.available_img = create_single_colored(TttModel.MAX_IMG_SIZE, rgba=(255, 255, 255, 50))
        self.empty_img = create_single_colored(TttModel.MAX_IMG_SIZE)

        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, val: Literal[1, -1]):
        self._player = val
        self.str_player.set('Players turn: ' + ('Crosses' if val == 1 else 'Noughts'))
        
    def increase_size(self):
        self.size += 2
        self.free = self.size ** 2 - (self.size - 2) ** 2
        self.grid = increase_grid(self.size, self.grid, dtype=np.int8)
        print(self.grid)
    
    def default(self) -> None:
        """Set attributes to their default state."""
        self.player = -1
        self.free = 1
        self.size = 1
        self.grid = np.zeros((1, 1), dtype=np.int8)
        self.resize_images(1)
    
    def resize_images(self, buttons_per_row: int):
        """Resizes the images to keep the same size when increasing buttons"""
        side = (TttModel.MAX_IMG_SIZE // buttons_per_row) - 10
        new_size = (side, side)
        self.cross_img = self.cross_img.resize(new_size, Image.LANCZOS)
        self.nought_img = self.nought_img.resize(new_size, Image.LANCZOS)
        self.available_img = self.available_img.resize(new_size, Image.LANCZOS)
        self.empty_img = self.empty_img.resize(new_size, Image.LANCZOS)