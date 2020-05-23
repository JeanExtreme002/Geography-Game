from tkinter import Canvas, Tk


class Window(Tk):
    
    """
    Classe para criar a interface gráfica do programa.
    """

    def __init__(self, title, geometry, canvas_color, fullscreen_key = "<Key-F11>"):

        super().__init__()

        self.width = geometry[0]
        self.height = geometry[1]
        self.__fullscreen_mode = False

        self.geometry("{}x{}".format(*geometry))
        self.resizable(False, False)
        self.title(title)

        self.focus()
        self.bind(fullscreen_key, self.fullscreen)

        self.__create_canvas(canvas_color)


    def __create_canvas(self, color):

        """
        Constrói o canvas principal do programa.
        """
        
        self.__canvas = Canvas(
            self, width = self.width, height = self.height, 
            bg = color, highlightthickness = 0
            )

        self.__canvas.images = []
        self.__canvas.pack()


    def fullscreen(self, event = None): 

        """
        Coloca a janela em modo de tela cheia.
        """

        self.__fullscreen_mode = not self.__fullscreen_mode
        self.wm_attributes("-fullscreen", self.__fullscreen_mode)


    def get_canvas(self):

        """
        Retorna o canvas principal do programa.
        """

        return self.__canvas