import numpy as np

from mvc.view import TttView
from mvc.model import TttModel

from helper_functions import calculate_validity

class TttController:
    def __init__(self, view: TttView, model: TttModel) -> None:
        self.view = view
        self.model = model
        
        self.view.cells[0, 0].config(command=lambda x=0, y=0: self.on_click(0, 0))

        self.view.lbl_player.config(textvariable=model.str_player)
        self.view.btn_reset.config(command=self.reset)
        #self.view.btn_expand.config(command=self.expand)
    
    
    def on_click(self, x: int, y: int):
        """Controls player alternations"""
        print(f'Current position: {x}.{y}!')
        print('Free:', self.model.free)
        self.model.free -= 1
        
        #update player
        print('Current Player:', self.model.str_player.get())
        self.model.player = self.model.player * (-1)
        
        self.view.update_button_img(self.model.player, y=y, x=x)
        
        self.model.grid[y, x] = 1 if self.model.player == 1 else -1
        
        if self.check_winning(x, y, self.model.player):
            for idx, val in np.ndenumerate(self.model.grid):
                if val == 0:
                    self.view.update_button_img(2, y=idx[0], x=idx[1])
            winner = 'Noughts' if self.model.player == 1 else 'Crosses'
            self.end_window = self.view.create_end_screen(ending_text=f'Player {winner} Won. Good Job Mate!')
            self.end_window.btn_reset.config(command=self.reset)
            
        elif self.model.free < 1:
            self.expand()
    
    def check_winning(self, x: int, y: int, player):
        """Check if there are 5 consecutive symbols."""
        grid = self.model.grid
        
        row = calculate_validity(grid[y, :], x, player)

        column = calculate_validity(grid[:, x], y, player)

        main_diag = calculate_validity(np.diag(grid, x - y), y - max(0, y - x), player)

        created_anti_diag = np.diag(np.fliplr(grid), (grid.shape[1] - x - 1) - y)
        anti_diag = calculate_validity(created_anti_diag, y - max(0, -self.model.size + 1 + x + y), player)
        
        return any((row, column, main_diag, anti_diag))
        
    def reset(self):
        """Resets the game."""
        if hasattr(self, 'end_window'):
            self.end_window.destroy()
        self.model.default()
        self.view.default()
        self.view.cells[0, 0].config(command=lambda x=0, y=0: self.on_click(0, 0))
        print('Board has been cleared!')
    
    def expand(self):
        """Increases the size of the board"""
        self.view.destroy_cells()
        self.model.increase_size()
        self.model.resize_images(self.model.size)
        self.view.create_images()
        
        self.view.add_cells(self.model.size, self.model.grid)
        for idx, cell in np.ndenumerate(self.view.cells):
            cell.config(command=lambda x=idx[1], y=idx[0]: self.on_click(x, y))
            