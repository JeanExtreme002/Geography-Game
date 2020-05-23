import json
import os


def get_info():

    """
    Retorna as informações do jogo.
    """

    with open(os.path.join("data", "game_info.txt"), encoding = "utf-8") as file:
        return file.read()  


def get_questions():

    """
    Retorna as questões do jogo.
    """

    with open(os.path.join("data", "game_questions.json"), encoding = "utf-8-sig") as file:
        return json.loads(file.read())


def get_rules():

    """
    Retorna as regras do jogo.
    """

    with open(os.path.join("data", "game_rules.txt"), encoding = "utf-8") as file:
        return file.read()