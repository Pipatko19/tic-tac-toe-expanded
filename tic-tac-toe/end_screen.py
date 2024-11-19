import ttkbootstrap as ttk

class EndScreen(ttk.Toplevel):
    def __init__(self, style: ttk.Style, ending_text='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(background='#ADD8E6')
        style.configure('TLabel', background='#ADD8E6')
        style.configure('Action.TButton', font=(20, 'garamond'))
        frm_main = ttk.Frame(master=self, style='Main.TFrame')
        frm_main.pack(padx=20, pady=20)
        
        lbl_congratulations = ttk.Label(master=frm_main, text=ending_text, anchor='center')
        lbl_congratulations.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        frm_reset_border = ttk.Frame(master=frm_main,style='Border.TFrame')
        frm_reset_border.grid(row=1, column=0, pady=5)
        self.btn_reset = ttk.Button(master=frm_reset_border, text='Replay', style='Action.PRIMARY.TButton')
        self.btn_reset.pack(padx=2, pady=2, ipadx=20)
        
        frm_exit_border = ttk.Frame(master=frm_main, style='Border.TFrame')
        frm_exit_border.grid(row=1, column=1, pady=5)
        self.btn_exit = ttk.Button(master=frm_exit_border, text='Exit', style='Action.SECONDARY.TButton')
        self.btn_exit.pack(padx=2, pady=2, ipadx=20)
        
if __name__ == '__main__':
    app = ttk.Window()
    screen = EndScreen('s', master=app, ending_text='Congratulations!')
    app.mainloop()