from view import TttView
from model import TttModel
from images import create_cross_image, create_nought_image
import numpy as np

class TttController:
    def __init__(self, view: TttView, model: TttModel) -> None:
        self.view = view
        self.model = model
        
        self.model.cross_img = create_cross_image(100)
        self.model.nought_img = create_nought_image(100)
        
        for idx, cell in np.ndenumerate(self.view.cells):
            cell.config(command=lambda x=idx[1], y=idx[0]: self.on_click(x, y))
        
        self.view.lbl_player.config(textvariable=model.str_player)
    
    
    def on_click(self, x, y):
        print(f'Current position: {x}.{y}!')
        cur_node = self.view.cells[y, x]
        if self.model.player == 0: cur_node['image'] = self.model.cross_img
        else: cur_node['image'] = self.model.nought_img
        self.model.player = (self.model.player + 1) % 2
        cur_node['state'] = 'disabled'
        print('Current Player:', self.model.str_player.get())