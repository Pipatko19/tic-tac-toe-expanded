import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
from typing import Literal
import numpy as np
from images import create_single_colored, create_cross_image, create_nought_image


class TttView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(style='TFrame')
        
        style = ttk.Style()
        style.configure('.', background = '#ADD8E6')
        style.configure('Game.TButton', background='navy')
        style.map('Game.TButton', background=[('disabled', 'navy')], bordercolor=[('disabled', 'green')])
        style.configure('Reset.TButton', font=('garamond', 12, 'bold'), foreground='#FFF8DC')
        style.configure('Grid.TFrame', background='blue')
        style.configure('TLabel', font=('garamond', 20, 'bold'), background= '#ADD8E6')
        style.configure('TFrame', background= '#ADD8E6')
        
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
        
        self.lbl_player = ttk.Label(master=self, text='placeholder')
        self.lbl_player.grid(column=0, row=1)
        
        self.btn_reset = ttk.Button(master=self, text='reset', style='Reset.TButton')
        self.btn_reset.grid(column=0, row=2, ipadx=40, pady=10)

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

    def end_message(self, winner):
        print(Messagebox.retrycancel(f'{winner} won! good job mate', title='winner!'))

    def update_cell(self, y, x, player: Literal[0, 1]):
        cur_node = self.cells[y, x]

        match player:
            case 0: 
                cur_node['image'] = self.cross_img
            case 1:
                cur_node['image'] = self.nought_img
            case 2:
                cur_node['image'] = self.empty_img
        cur_node['state'] = 'disabled'
        
if __name__ == '__main__':
    app = ttk.Window()
    app.config(background='#ADD8E6')
    app.title('Tic tac toe')
    app.minsize(450, 450)
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    app.mainloop()