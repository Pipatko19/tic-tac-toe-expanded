import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox
import numpy as np
from images import create_empty

class TttView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        style = ttk.Style()
        style.configure('Game.TButton', background='navy')
        style.map('Game.TButton', background=[('disabled', 'navy')])
        style.configure('Grid.TFrame', background='blue')

        style.configure('TLabel', font=('garamond', 20, 'bold'))
        
        frm_cell_grid = ttk.Frame(master= self, style='Grid.TFrame')
        frm_cell_grid.grid(column=0, row=0, sticky='news')
        
        self.cells: np.ndarray[ttk.Button]= np.empty((3, 3), dtype=ttk.Button)
        self.empty_image = create_empty(100)
        for y in range(3):
            for x in range(3):
                btn_cell = ttk.Button(master=frm_cell_grid, image=self.empty_image, style='Game.TButton')
                self.cells[y, x] = btn_cell
                btn_cell.grid(row=y, column=x, sticky='news', ipadx=0, ipady=0)
        
        frm_cell_grid.columnconfigure((0, 1, 2), weight=1, minsize=120)
        frm_cell_grid.rowconfigure((0, 1, 2), weight=1, minsize=120)
        
        self.lbl_player = ttk.Label(master=self, text='placeholder')
        self.lbl_player.grid(column=0, row=1)

        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

    def end_message(self, winner):
        print(Messagebox.retrycancel(f'{winner} won! good job mate', title='winner!'))

                
if __name__ == '__main__':
    app = ttk.Window()
    app.title('Tic tac toe')
    app.minsize(450, 450)
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    app.mainloop()