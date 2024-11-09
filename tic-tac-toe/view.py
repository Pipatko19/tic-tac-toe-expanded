import ttkbootstrap as ttk
import numpy as np

class TttView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        style = ttk.Style()
        style.configure('Game.TButton', width= 0, background='navy')
        style.map('Game.TButton', background=[('disabled', 'navy')])
        style.configure('Grid.TFrame', background='blue')

        style.configure('TLabel', font=('garamond', 20, 'bold'))
        
        frm_cell_grid = ttk.Frame(master= self, style='Grid.TFrame')
        frm_cell_grid.grid(column=0, row=0)
        
        self.cells: np.ndarray[ttk.Button]= np.empty((3, 3), dtype=ttk.Button)
        for y in range(3):
            for x in range(3):
                btn_cell = ttk.Button(master=frm_cell_grid, style='Game.TButton')
                self.cells[y, x] = btn_cell
                btn_cell.grid(row=y, column=x, ipadx=55, ipady=50, padx=5, pady=5)
        
        frm_cell_grid.columnconfigure((0, 1, 2), weight=1, minsize=50)
        frm_cell_grid.rowconfigure((0, 1, 2), weight=1, minsize=50)
        
        self.lbl_player = ttk.Label(master=self, text='placeholder')
        self.lbl_player.grid(column=0, row=1)

                
if __name__ == '__main__':
    app = ttk.Window()
    app.title('Tic tac toe')
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    app.mainloop()