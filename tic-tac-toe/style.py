from ttkbootstrap import Style

def apply_style(style: Style):
    style.configure('.', background = '#ADD8E6')
    style.configure('Game.TButton', background='navy')
    style.map('Game.TButton',
              background=[('disabled', 'navy')], 
              bordercolor=[('disabled', 'green')])
    style.configure('Reset.TButton', font=('garamond', 12, 'bold'), foreground='#FFF8DC')
    style.configure('Grid.TFrame', background='blue')
    style.configure('TLabel', font=('garamond', 20, 'bold'))
    style.configure('Turn.TLabel', background= '#ADD8E6')
    style.configure('TFrame', background= '#ADD8E6')
    style.configure('Border.TFrame', background='black')