from src.dataloader import get_info, get_rules
from src.tools.util import create_image, create_text
from tkinter import Button, Text


class MainScreen(object):
    
    """
    Classe para gerar a tela inicial do programa.
    """

    def __init__(self, window):

        self.__window = window

        self.__canvas = window.get_canvas()
        self.__canvas.delete("all")


    def __create_button_start(self, command, width = 10, bg = "orange", fg = "white", font = ("Impact", 30)):

        """
        Cria botão para iniciar o jogo na barra lateral.
        """

        button = Button(
            self.__window, text = "Iniciar", width = width, bg = bg, fg = fg, 
            font = font, relief = "ridge", bd = 10, command = command
            )
        self.__canvas.create_window(150, self.__window.height - 100, window = button)


    def __create_info_field(self, main_color, title_fg = "orange", title_font = ("Impact", 40)):

        """
        Cria campo com todas as informações sobre o jogo.
        """

        # Cria título do campo.
        create_text(self.__canvas, "Sobre:", 390, 100, fill = title_fg, border = 1, font = title_font)
        
        # Cria texto para colocar as informações do jogo.
        info = Text(
            self.__window, width = 61, height = 10, font = ("Arial", 15), 
            bg = main_color, fg = "white", bd = 0
            )

        # Insere as informações no texto e cria o elemento no canvas.
        info.insert(0.0, get_info())
        self.__canvas.create_window(660, 250, window = info)


    def __create_rules_field(self, main_color, title_fg = "orange", title_font = ("Impact", 40)):

        """
        Cria campo com todas as regras do jogo.
        """

        # Cria título do campo.
        create_text(self.__canvas, "Regras:", 408, 400, fill = title_fg, border = 1, font = title_font)
        
        # Cria texto para colocar as regras do jogo.
        rules = Text(
            self.__window, width = 61, height = 6, font = ("Arial", 15), 
            bg = main_color, fg = "white", bd = 0
            )

        # Insere as regras do jogo no texto e cria o elemento no canvas.
        rules.insert(0.0, get_rules())
        self.__canvas.create_window(660, 500, window = rules)


    def __create_sidebar(self, sidebar_color, images):

        """
        Cria uma barra lateral com a logo do jogo, uma imagem extra e um botão para iniciar o jogo.
        """

        # Cria o background da barra lateral.
        self.__canvas.create_rectangle(0, 0, 300, self.__window.height, fill = sidebar_color, outline = "black")

        # Cria a imagem da logo do jogo.
        if len(images) > 0: 
            create_image(self.__canvas, images[0], 150, 100, resize = (300, 156))

        # Coloca no canvas uma imagem extra.
        if len(images) > 1: 
            create_image(self.__canvas, images[1], 150, 320, resize = (155, 220))


    def build(self, main_color, sidebar_color, start_function, images):

        """
        Constrói a janela.
        """

        self.__create_sidebar(sidebar_color, images)
        self.__create_button_start(start_function)
        self.__create_info_field(main_color)
        self.__create_rules_field(main_color)

