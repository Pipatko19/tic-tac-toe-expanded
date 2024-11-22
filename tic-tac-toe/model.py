import tkinter as tk
import numpy as np
from typing import Literal

class TttModel:
    def __init__(self) -> None:
        self._player: int = 0
        self.free: int = 9
        self.str_player: tk.StringVar = tk.StringVar(value='Players turn: Crosses')
        self.grid = np.zeros((3, 3), dtype=np.int8)

        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, val: Literal[0, 1]):
        self._player = val
        self.str_player.set('Players turn: ' + ('Crosses' if val == 0 else 'Noughts'))

    
    def default(self) -> None:
        """Set attributes to their default state."""
        self.player = 0
        self.free = 9
        self.grid = np.zeros((3, 3), dtype=np.int8)