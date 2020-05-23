from src.tools.util import create_image, create_text
from tkinter import Button, Text


class QuizScreen(object):

    """
    Classe para lidar com a interface do programa durante jogo.
    """

    def __init__(self, window):

        self.__window = window

        self.__canvas = window.get_canvas()
        self.__canvas.delete("all")


    def __create_next_button(self, button_bg = "orange", button_fg = "white"):

        """
        Cria botão para ir para a próxima questão.
        """

        self.__next_button = Button(
            self.__window, width = 10, height = 1, text = "Avançar", bg = button_bg, fg = button_fg, 
            font = ("Impact", 30), relief = "ridge", bd = 10, command = self.__set_next
            )

        self.__next = False


    def __create_question_field(self, main_color):

        """
        Cria campo para inserir as questões.
        """


        # Cria texto para inserir as questões.
        self.__question_text = Text(
            self.__window, width = 50, height = 10, font = ("Arial", 15), 
            bg = main_color, fg = "white", bd = 0
            )

        # Coloca o objeto no canvas.
        self.__canvas.create_window(720, 230, window = self.__question_text, tag = "question")


    def __create_question_number(self, number = 1, title_color = "orange", title_font = ("Impact", 40)): 

        """
        Cria texto para informar o número da questão.
        """

        self.__canvas.delete("question_number")

        create_text(
            self.__canvas, "%iª Questão:" % number, 560, 50, fill = title_color, 
            border = 1, font = title_font, tag = "question_number"
            )


    def __create_sidebar(self, sidebar_color, logo, btn_bg = "orange", btn_fg = "white", btn_font = ("Arial", 14)):

        """
        Cria uma barra lateral a logo e com os botões para o jogador escolher a opção correta.
        """

        # Cria o background da barra lateral com a imagem da logo do jogo.
        self.__canvas.create_rectangle(0, 0, 400, self.__window.height, fill = sidebar_color, outline = "black")
        create_image(self.__canvas, logo, 200, 100, resize = (300, 156))

        # Espaçamento entre os botões e lista de botões.
        button_spacing = 70
        self.__buttons = []

        # Cria cinco botões na barra lateral.
        for button_id in range(5):

            # Cria botão da barra lateral.
            button = Button(
                self.__window, width = 32, height = 1, bg = btn_bg, fg = btn_fg, 
                font = btn_font, relief = "ridge", bd = 10
                )

            # Cria um atributo para guardar a cor original do botão.
            button.original_color = btn_bg

            # Configura o método a ser chamado após o jogador ter apertado este botão.
            button.configure(command = lambda btn = button: self.__set_choice(btn))

            # Coloca o botão dentro do canvas.
            self.__canvas.create_window(
                200, 240 + (button_spacing * button_id), 
                window = button, tag = "sidebar_button_%i" % button_id
                )

            # Adiciona o botão à lista de botões.
            self.__buttons.append(button)


    def __set_choice(self, button):

        """
        Define a escolha do usuário.
        """

        self.__choice = button


    def __set_next(self):

        """
        Informa que o usuário pediu pela próxima questão.
        """

        self.__next = True


    def build(self, main_color, sidebar_color, logo_image):

        """
        Constrói a janela.
        """

        self.__create_sidebar(sidebar_color, logo_image)
        self.__create_question_number()
        self.__create_question_field(main_color)
        self.__create_next_button()


    def create_timer(self, sec, total = 0):

        """
        Cria um timer para mostrar ao jogador quanto tempo lhe resta.
        """

        # Apaga o último texto do timer.
        self.__canvas.delete("timer")

        # Se o tempo for igual a zero, será informado que o tempo esgotou.
        if sec == 0:
            text, font, fill = "Tempo Esgotado !!", ("Impact", 50), "red"
            return create_text(self.__canvas, text, 700, 380, tag = "timer", font = font, fill = fill, border = 2)

        # Se o tempo for menor, o texto não será criado.
        elif sec < 0: return None

        # Obtém o tempo restante em porcentagem.
        percent = 100 / total * sec

        # Define as cores do texto com base na porcentagem.
        if percent >= 60: 
            fill = "green2"

        elif percent >= 25: 
            fill = "yellow"

        else: 
            fill = "red"

        # Cria o texto do timer.
        create_text(self.__canvas, sec, 700, 520, fill = fill, border = 2, tag = "timer", font = ("Impact", 70))


    def get_choice(self):

        """
        Retorna a escolha do usuário.
        """

        return self.__choice


    def hide_next_button(self):

        """
        Remove o next_button do canvas.
        """

        self.__canvas.delete("next_button")
        self.__next = False


    def is_next(self):

        """
        Retorna um booleano informando se o usuário pediu pela próxima questão.
        """

        return self.__next


    def show_next_button(self):

        """
        Cria o next_button no canvas.
        """

        self.__canvas.create_window(720, 500, window = self.__next_button, tag = "next_button")


    def update_buttons(self, texts):

        """
        Atualiza o texto de cada botão de opção da barra lateral.
        """

        self.__choice = None

        for i in range(5):
            self.__buttons[i]["text"] = texts[i]
            self.__buttons[i]["bg"] = self.__buttons[i].original_color


    def update_question(self, question, question_number):

        """
        Atualiza o texto da questão.
        """

        self.__create_question_number(question_number)
        self.__question_text.delete(0.0, "end")
        self.__question_text.insert(0.0, question)

