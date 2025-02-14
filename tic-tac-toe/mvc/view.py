import ttkbootstrap as ttk
import numpy as np

from PIL import ImageTk
from typing import Literal

from mvc.model import TttModel
from style import apply_style
from end_screen import EndScreen
from helper_functions import increase_grid

class TttView(ttk.Frame):
    def __init__(self, model: TttModel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(style='TFrame')
        self.model = model
        self.style = ttk.Style()
        apply_style(self.style)

        self.create_images()
        
        self.frm_cell_grid = ttk.Frame(master= self, style='Grid.TFrame')
        self.frm_cell_grid.grid(column=0, row=0)
        
        self.cells: np.ndarray[ttk.Button]= np.empty((1, 1), dtype=ttk.Button).reshape(1, 1)
        self.add_cells(1, 0)
        
        self.lbl_player = ttk.Label(master=self, text='placeholder', style='Turn.TLabel')
        self.lbl_player.grid(column=0, row=1)
        
        frm_reset_border = ttk.Frame(master=self,style='Border.TFrame')
        frm_reset_border.grid(column=0, row=2)
        
        self.btn_reset = ttk.Button(master=frm_reset_border, text='reset', style='Reset.TButton')
        self.btn_reset.pack(padx=2, pady=2, ipadx=20)
        
        #self.btn_expand = ttk.Button(master=self, text='EXPAND')
        #self.btn_expand.grid(column=0, row=3)

        self.columnconfigure(0, weight=1, minsize=700)
        self.rowconfigure((0, 1, 2), weight=3, minsize=50)
        
    def add_cells(self, size: int, grid_values: np.ndarray):
        """Rewrites the board (changes its size)."""
        self.cells = increase_grid(size, self.cells, dtype=ttk.Button)
        for y in range(size):
            for x in range(size):
                btn_cell = ttk.Button(master=self.frm_cell_grid, image=self.available_img, style='Game.TButton')

                self.cells[y, x] = btn_cell
                if len(self.cells) != 1:
                    self.update_button_img(grid_values[y, x], node=btn_cell)
                btn_cell.grid(row=y, column=x, sticky='news', ipadx=0, ipady=0)
                
    def destroy_cells(self):
        """Removes all cells."""
        for row in self.cells:
            for widget in row:
                widget.grid_forget()
                widget.destroy()
                
    def update_button_img(self, player: Literal[-1, 0, 1, 2], node: ttk.Button = None, y= None, x = None, disable=True):
        """Updates the button images. Works by coordinates or reference."""
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
    
    def create_images(self):
        """Changes internal images to Tk.PhotoImage"""
        self.cross_img = ImageTk.PhotoImage(self.model.cross_img)
        self.nought_img = ImageTk.PhotoImage(self.model.nought_img)
        self.available_img = ImageTk.PhotoImage(self.model.available_img)
        self.empty_img = ImageTk.PhotoImage(self.model.empty_img)
    
    def default(self):
        """Set the view to it's default state"""
        self.destroy_cells()
        self.create_images()
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