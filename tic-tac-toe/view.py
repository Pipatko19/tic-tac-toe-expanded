import ttkbootstrap as ttk
from typing import Literal
import numpy as np
from images import create_single_colored, create_cross_image, create_nought_image
from style import apply_style
from end_screen import EndScreen

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
        
        frm_cell_grid = ttk.Frame(master= self, style='Grid.TFrame')
        frm_cell_grid.grid(column=0, row=0, sticky='news')
        
        self.cells: np.ndarray[ttk.Button]= np.empty((3, 3), dtype=ttk.Button)

        for y in range(3):
            for x in range(3):
                btn_cell = ttk.Button(master=frm_cell_grid, image=self.available_img, style='Game.TButton')
                self.cells[y, x] = btn_cell
                btn_cell.grid(row=y, column=x, sticky='news', ipadx=0, ipady=0)
        
        frm_cell_grid.columnconfigure((0, 1, 2), weight=1, minsize=120)
        frm_cell_grid.rowconfigure((0, 1, 2), weight=1, minsize=120)
        
        self.lbl_player = ttk.Label(master=self, text='placeholder', style='Turn.TLabel')
        self.lbl_player.grid(column=0, row=1)
        
        frm_reset_border = ttk.Frame(master=self,style='Border.TFrame')
        frm_reset_border.grid(column=0, row=2)
        
        self.btn_reset = ttk.Button(master=frm_reset_border, text='reset', style='Reset.TButton')
        self.btn_reset.pack(padx=2, pady=2, ipadx=20)

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

    def update_cell(self, y, x, player: Literal[0, 1], disable=True):
        cur_node = self.cells[y, x]

        match player:
            case 0: 
                cur_node['image'] = self.cross_img
            case 1:
                cur_node['image'] = self.nought_img
            case 2:
                cur_node['image'] = self.empty_img
        cur_node['state'] = 'disabled'
        
    def default(self):
        """Set the view to it's default state"""
        for cell in self.cells.flat:
            cell['image'] = self.available_img
            cell['state'] = 'enabled'
    
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