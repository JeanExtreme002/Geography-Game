from src import App
from src.dataloader import get_questions


buffer = 64
images_path = "images"

canvas_color = "blue"
sidebar_color = "medium blue"

window_geometry = [1024, 600]
window_title = "Geografia do Milhão"

app = App(window_title, window_geometry, images_path, buffer)
app.run(canvas_color, sidebar_color, get_questions())


