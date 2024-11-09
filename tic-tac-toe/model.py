import tkinter as tk

class TttModel:
    def __init__(self) -> None:
        self._player = 0
        self.str_player: tk.StringVar = tk.StringVar(value='Players turn: Crosses')
        self.nought_img = None
        self.cross_img = None
        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, val):
        self._player = val
        self.str_player.set('Players turn: ' + ('Crosses' if val == 0 else 'Noughts'))
