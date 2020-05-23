from pygame import mixer
from src.screens.finalscreen import FinalScreen
from src.screens.mainscreen import MainScreen
from src.screens.quizscreen import QuizScreen
from src.tools.timer import Timer
from src.tools.util import create_text, play_sound
from src.window import Window
import os
import random
import time


class App(object):
    
    """
    Classe principal.
    """

    def __init__(self, title, window_geometry, images_path, buffer = 1024):

        # Instância os parâmetros
        self.__title = title
        self.__window_geometry = window_geometry 
        self.__images_path = images_path   

        # Obtém o caminho de todas as imagens usadas.
        self.__coins_image = os.path.join(images_path, "coins.png")
        self.__globe_image = os.path.join(images_path, "globe.png")
        self.__logo_image = os.path.join(images_path, "logo.png")
        self.__nerd_image = os.path.join(images_path, "nerd.png")

        # Inicializa o mixer.
        mixer.init(buffer = buffer)


    def __new_question(self):

        """
        Cria uma nova questão.
        """

        # Obtém aleatóriamente o ID de uma questão e o remove da lista.
        question_id = random.choice(self.__questions)
        self.__questions.remove(question_id)

        # Obtém os dados da questão.
        question = self.__questions_data[question_id]

        # Atualiza o texto dos botões de escolhas.
        options = [question["op%i" % i] for i in range(1, 6)]
        self.__quiz_screen.update_buttons(options)

        # Instância a resposta da nova pergunta.
        self.__answer = question["answer"]

        # Coloca a nova pergunta no jogo.
        question_number = len(self.__questions_data) - len(self.__questions)
        self.__quiz_screen.update_question(question["question"], question_number)


    def __start_game(self):

        """
        Inicia o jogo.
        """

        def wait_while_callback():

            """
            Retorna um booleano verificando se o método 
            wait_while deve continuar esperando.
            """

            return self.__quiz_screen.is_next() or self.__stop


        # Cria um objeto de timer.
        timer = Timer(self.__window)

        # Constrói a janela de quiz para iniciar o jogo.
        self.__quiz_screen = QuizScreen(self.__window)
        self.__quiz_screen.build(self.__main_color, self.__sidebar_color, self.__logo_image)

        # Pontuação inicial do jogador e tempo em que o jogo começou.
        self.__score = [0, 0]
        self.__time_in_game = time.time()

        # Executa o jogo enquanto houver questões e enquanto o usuário não pedir para fechar.
        while self.__questions and not self.__stop:

            # Toca uma música para informar que apareceu uma nova questão.
            play_sound("sounds/next.mp3")

            # Esconde o botão de next.
            self.__quiz_screen.hide_next_button()

            # Cria uma nova questão no jogo.
            self.__new_question()

            # Espera um tempo em segundos que será multiplicado por 10 para que a GUI não trave. 
            for i in range(self.__time * 10):

                # Obtém a escolha do usuário.
                choice = self.__quiz_screen.get_choice()
                if choice or self.__stop: break

                # Mostra para o jogador o tempo restante e espera um tempo de 100ms.
                self.__quiz_screen.create_timer(self.__time - i // 10, self.__time)
                timer.wait(100)

            # Verifica se o usuário escolheu uma opção e depois valida a escolha.
            if choice: 
                self.__validate_answer(choice)
                self.__quiz_screen.create_timer(-1)

            # Verifica se o usuário pediu para sair.
            elif self.__stop: break

            # Se o tempo tiver acabado, uma mensagem será colocada na tela.
            else:
                play_sound("sounds/fail.mp3")
                self.__quiz_screen.create_timer(0)

            # Mostra botão de next e espera até o usuário apertar este botão.
            self.__quiz_screen.show_next_button()
            timer.wait_while(wait_while_callback)

        # Se o usuário não tiver pedido para sair, será criada uma tela final.
        if not self.__stop:

            # Obtém as informações do jogador da sessão.
            total_time = time.strftime("%M:%S", time.localtime(time.time() - self.__time_in_game))
            images = [self.__logo_image, self.__nerd_image, self.__coins_image]
            points = self.__score[0] * 10

            # Reproduz música para fim de jogo.
            play_sound("sounds/end.mp3")

            # Cria a tela final.
            finalscreen = FinalScreen(self.__window)
            finalscreen.build(self.__score, points, total_time, *images)


    def __validate_answer(self, button):

        """
        Método para validar a resposta.
        """

        if button["text"] == self.__answer:
            button["bg"] = "green"
            self.__score[0] += 1

            play_sound("sounds/correct.mp3")

        else:
            button["bg"] = "red"
            self.__score[1] += 1

            play_sound("sounds/fail.mp3")


    def run(self, canvas_color, sidebar_color, questions, time = 60): 

        """
        Inicia e constrói a parte gráfica do programa.
        """

        # Cria a janela do programa.
        self.__window = Window(self.__title, self.__window_geometry, canvas_color)
        self.__window.protocol("WM_DELETE_WINDOW", self.stop)

        # Instância os parâmetros.
        self.__main_color = canvas_color
        self.__sidebar_color = sidebar_color
        self.__questions_data = questions
        self.__questions = list(self.__questions_data)
        self.__time = time
        self.__stop = False

        # Cria uma lista com a imagem de logo e a imagem do globo.
        images = [self.__logo_image, self.__globe_image]

        # Constrói a janela principal do programa.
        main_screen = MainScreen(self.__window)
        main_screen.build(canvas_color, sidebar_color, self.__start_game, images)

        # Coloca a janela do programa em um loop infinito.
        self.__window.mainloop()


    def stop(self):

        """
        Método para encerrar o programa.
        """

        mixer.music.stop()

        self.__stop = True
        self.__window.after(150, self.__window.destroy)