from PIL import Image, ImageTk
from pygame import mixer


def create_image(canvas, filename, x, y, resize = None, **kwargs):

    """
    Cria imagem dentro de um Canvas.
    OBS: O objeto Canvas precisa conter uma lista chamada "images".
    """

    image = Image.open(filename)
    image = image.resize(resize) if resize else image

    canvas.images.append(ImageTk.PhotoImage(image))
    canvas.create_image(x, y, image = canvas.images[-1], **kwargs)


def create_text(canvas, text, x, y, fill = "black", border = None, **kwargs):

    """
    Cria texto dentro de um Canvas, com a opção de adicionar uma borda.
    """
   
    if border:
        canvas.create_text(x - border, y, text = text, fill = "black", **kwargs)
        canvas.create_text(x + border, y, text = text, fill = "black", **kwargs)
        canvas.create_text(x, y - border, text = text, fill = "black", **kwargs)
        canvas.create_text(x, y + border, text = text, fill = "black", **kwargs)

    canvas.create_text(x, y, text = str(text), fill = fill, **kwargs)


def play_sound(filename):

    """
    Reproduzir um áudio.
    """

    mixer.music.load(filename)
    mixer.music.play()