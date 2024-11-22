import ttkbootstrap as ttk
from view import TttView
from controller import TttController
from model import TttModel

if __name__ == '__main__':
    app = ttk.Window()
    app.configure(background='#ADD8E6')
    app.title('Tic tac toe')
    app.minsize(450, 450)
    view = TttView(master=app)
    view.pack(padx=20, pady=20)
    model = TttModel()
    controller = TttController(view, model)
    app.mainloop()