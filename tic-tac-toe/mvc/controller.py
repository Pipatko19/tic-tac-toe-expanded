from mvc.view import TttView
from mvc.model import TttModel
import numpy as np
from ttkbootstrap.dialogs.dialogs import Messagebox


class TttController:
    def __init__(self, view: TttView, model: TttModel) -> None:
        self.view = view
        self.model = model
        
        self.view.cells[0, 0].config(command=lambda x=0, y=0: self.on_click(0, 0))

        self.view.lbl_player.config(textvariable=model.str_player)
        self.view.btn_reset.config(command=self.reset)
        self.view.btn_expand.config(command=self.expand)
    
    
    def on_click(self, x: int, y: int):
        """Controls player alternations"""
        print(f'Current position: {x}.{y}!')
        self.model.free -= 1
        
        #update player
        print('Current Player:', self.model.str_player.get())
        self.model.player = self.model.player * (-1)
        
        self.view.update_img(self.model.player, y=y, x=x)
        
        self.model.grid[y, x] = 1 if self.model.player == 1 else -1
        
        if self.check_winning(x, y):
            for idx, val in np.ndenumerate(self.model.grid):
                if val == 0:
                    self.view.update_img(2, y=idx[0], x=idx[1])
            winner = 'Noughts' if self.model.player == 1 else 'Crosses'
            self.end_window = self.view.create_end_screen(ending_text=f'Player {winner} Won. Good Job Mate!')
            self.end_window.btn_reset.config(command=self.reset)
            
    
    def check_winning(self, x: int, y: int):
        grid = self.model.grid
        
        row = abs(np.sum(grid[y, :]))
        column = abs(np.sum(grid[:, x]))
        main_diag = abs(np.sum(np.diag(grid, x - y)))
        anti_diag = abs(np.sum(np.diag(np.fliplr(grid), (grid.shape[1] - x - 1) - y)))
        
        return any(line == 3 for line in (row, column, main_diag, anti_diag))
        
    def reset(self):
        if hasattr(self, 'end_window'):
            self.end_window.destroy()
        self.model.default()
        self.view.default()
        self.view.cells[0, 0].config(command=lambda x=0, y=0: self.on_click(0, 0))
        print('Board has been restarted!')
    
    def expand(self):
        self.view.destroy_cells()
        self.model.increase_size()
        self.view.add_cells(self.model.size, self.model.grid)
        for idx, cell in np.ndenumerate(self.view.cells):
            cell.config(command=lambda x=idx[1], y=idx[0]: self.on_click(x, y))
            

        
    def handle_ending_input(self, msg: str):
        print(msg)
        print(type(msg))
        if msg == 'retry':
            self.reset()