import ttkbootstrap as ttk
from typing import Literal
import numpy as np
from images import create_single_colored, create_cross_image, create_nought_image
from style import apply_style
from end_screen import EndScreen
from helper_functions import increase_grid

class TttView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(style='TFrame')
        
        self.style = ttk.Style()
        apply_style(self.style)

        self.cross_img = create_cross_image(100)
        self.nought_img = create_nought_image(100)
        self.available_img = create_single_colored(100, rgba=(255, 255, 255, 50))
        self.empty_img = create_single_colored(100)
        
        self.frm_cell_grid = ttk.Frame(master= self, style='Grid.TFrame')
        self.frm_cell_grid.grid(column=0, row=0)
        
        self.cells: np.ndarray[ttk.Button]= np.empty((1, 1), dtype=ttk.Button).reshape(1, 1)
        self.add_cells(1, 0)

        
        #self.frm_cell_grid.columnconfigure((0, 1, 2), weight=1, minsize=120)
        #self.frm_cell_grid.rowconfigure((0, 1, 2), weight=1, minsize=120)
        
        self.lbl_player = ttk.Label(master=self, text='placeholder', style='Turn.TLabel')
        self.lbl_player.grid(column=0, row=1)
        
        frm_reset_border = ttk.Frame(master=self,style='Border.TFrame')
        frm_reset_border.grid(column=0, row=2)
        
        self.btn_reset = ttk.Button(master=frm_reset_border, text='reset', style='Reset.TButton')
        self.btn_reset.pack(padx=2, pady=2, ipadx=20)
        
        self.btn_expand = ttk.Button(master=self, text='EXPAND')
        self.btn_expand.grid(column=0, row=3)

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)
    
    def add_cells(self, size: int, grid_values: np.ndarray):
        self.cells = increase_grid(size, self.cells, dtype=ttk.Button)
        for y in range(size):
            for x in range(size):
                btn_cell = ttk.Button(master=self.frm_cell_grid, image=self.available_img, style='Game.TButton')

                self.cells[y, x] = btn_cell
                if len(self.cells) != 1:
                    self.update_img(grid_values[y, x], node=btn_cell)
                btn_cell.grid(row=y, column=x, sticky='news', ipadx=0, ipady=0)
    def destroy_cells(self):
        for row in self.cells:
            for widget in row:
                widget.grid_forget()
                widget.destroy()
    def update_img(self, player: Literal[0, 1, 2], node: ttk.Button = None, y= None, x = None, disable=True):
        if node is None:
            if y is None or x is None:
                raise ValueError('Reference nor coordinates were provided!')
            else:
                node = self.cells[y, x]
        match player:
            case -1:
                node['image'] = self.cross_img
            case 0: 
                node['image'] = self.available_img
                return
            case 1:
                node['image'] = self.nought_img
            case 2:
                node['image'] = self.empty_img
        node['state'] = 'disabled'
        
    def default(self):
        """Set the view to it's default state"""
        self.destroy_cells()
        self.cells: np.ndarray[ttk.Button]= np.empty((1, 1), dtype=ttk.Button).reshape(1, 1)
        self.add_cells(1, 0)
    
    def create_end_screen(self, ending_text=''):
        end_window = EndScreen(style=self.style, master=self, ending_text=ending_text)
        end_window.btn_exit.config(command=self.master.destroy)
        return end_window
    
if __name__ == '__main__':
    app = ttk.Window()
    app.config(background='#ADD8E6')
    app.title('Tic tac toe')
    app.minsize(450, 450)
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    app.mainloop()