from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage


class noPacMan(App):
    def build(self):
        matrix = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        layout = GridLayout(cols=len(matrix[0]))
        for row in matrix:
            for point in row:
                if point == 1:
                    image = AsyncImage(source='./images/neon.png')
                    layout.add_widget(image)
                else:
                    image = AsyncImage(source='./images/black.png')
                    layout.add_widget(image)
        return layout


window = noPacMan()
window.run()
