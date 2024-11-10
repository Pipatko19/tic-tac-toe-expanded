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
        
        
        self.model.grid[y, x] = 1 if self.model.player else -1
        if self.check_winning(x, y):
            self.view.end_message(self.model.str_player.get())
        
    def check_winning(self, x, y):
        grid = self.model.grid
        
        row = abs(np.sum(grid[y, :]))
        column = abs(np.sum(grid[:, x]))
        main_diag = abs(np.sum(np.diag(grid, x - y)))
        anti_diag = abs(np.sum(np.diag(np.fliplr(grid), (grid.shape[1] - x - 1) - y)))
        
        return row == 3 or column == 3 or main_diag == 3 or anti_diag == 3
        