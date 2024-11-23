import tkinter as tk
import numpy as np
from typing import Literal
from helper_functions import increase_grid

class TttModel:
    def __init__(self) -> None:
        self._player: int = -1
        self.free: int = 1
        self.size: int = 1
        self.str_player: tk.StringVar = tk.StringVar(value='Players turn: Crosses')
        self.grid: np.ndarray = np.zeros((1, 1), dtype=np.int8)

        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, val: Literal[1, -1]):
        self._player = val
        self.str_player.set('Players turn: ' + ('Crosses' if val == -1 else 'Noughts'))
        
    def increase_size(self):
        self.size += 2

        self.grid = increase_grid(self.size, self.grid, dtype=np.int8)
        print(self.grid)
    
    def default(self) -> None:
        """Set attributes to their default state."""
        self.player = -1
        self.free = 1
        self.size = 1
        self.grid = np.zeros((1, 1), dtype=np.int8)