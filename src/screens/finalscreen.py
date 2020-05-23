from src.tools.util import create_image, create_text


class FinalScreen(object):

    """
    Classe para gerar a tela final do jogo mostrando os resultados.
    """

    def __init__(self, window):

        self.__window = window

        self.__canvas = window.get_canvas()
        self.__canvas.delete("all")


    def build(self, score, points, time, logo, image1 = None, image2 = None):

        """
        Constrói a janela.
        """

        # Coloca a imagem da logo no canvas.
        create_image(self.__canvas, logo, self.__window.width // 2 , 100, resize = (300, 156))

        # Cria mensagem parabenizando o jogador.
        create_text(
            self.__canvas, "Parabéns por chegar ao final deste jogo!", 
            200, 250, fill = "white", border = 1, font = ("Arial", 15)
            )

        # Cria mensagem de informação.
        create_text(
            self.__canvas, "Aqui em baixo você poderá ver algumas informações do seu jogo.",
            310, 280, fill = "white", border = 1, font = ("Arial", 15)
            )

        # Cria campo para mostrar a pontuação do jogador.
        create_text(self.__canvas, "Pontuação:", 110, 340, fill = "orange", border = 1, font = ("Impact", 30))
        create_text(self.__canvas, points, 240, 345, fill = "white", border = 1, font = ("Arial", 30))

        # Cria campo para mostrar o número de acertos do jogador.
        create_text(self.__canvas, "Acertos:", 83, 390, fill = "orange", border = 1, font = ("Impact", 30))
        create_text(self.__canvas, score[0], 185, 395, fill = "white", border = 1, font = ("Arial", 30))

        # Cria campo para mostrar o número de falhas do jogador.
        create_text(self.__canvas, "Falhas:", 75, 440, fill = "orange", border = 1, font = ("Impact", 30))
        create_text(self.__canvas, score[1], 165, 445, fill = "white", border = 1, font = ("Arial", 30))

        # Cria campo para mostrar o tempo total em jogo.
        create_text(self.__canvas, "Tempo:", 76, 490, fill = "orange", border = 1, font = ("Impact", 30))
        create_text(self.__canvas, time, 200, 495, fill = "white", border = 1, font = ("Arial", 30))

        # Cria imagens extras.
        if image1: create_image(self.__canvas, image1, 850, 330)
        if image2: create_image(self.__canvas, image2, 850, 540, resize = [372, 220])

