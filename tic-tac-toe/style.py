from ttkbootstrap import Style

def apply_style(style: Style):
    style.configure('.', background = '#ADD8E6')
    style.configure('TLabel', font=('garamond', 20, 'bold'))
    style.configure('TFrame', background= '#ADD8E6')
    
    style.configure('Border.TFrame', background='black')
    
    style.configure('Grid.TFrame', background='blue')
    style.configure('Game.TButton', background='navy', padding=(3, 3))
    style.map('Game.TButton',
              background=[('disabled', 'navy')], 
              bordercolor=[('disabled', 'green')])
    
    style.configure('Reset.TButton', font=('garamond', 12, 'bold'), foreground='#FFF8DC')
    style.configure('Turn.TLabel', background= '#ADD8E6')
