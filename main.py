from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.graphics import Rectangle
from kivy.core.window import Window


class Player(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

        with self.canvas:
            self.player = Rectangle(source='images/player.png', pos=(self.width / 10, self.height / 10), size=(50, 50))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        pos_x = self.player.pos[0]
        pos_y = self.player.pos[1]

        if text == 'w':
            pos_y += 5
        if text == 's':
            pos_y -= 5
        if text == 'a':
            pos_x -= 5
        if text == 'd':
            pos_x += 5

        self.player.pos = (pos_x, pos_y)
        print(text)


class NoPacMan(App):
    def loadMap(self):
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
        return matrix

    def build(self):
        matrix = self.loadMap()
        layout = GridLayout(cols=len(matrix[0]))
        for row in matrix:
            for point in row:
                if point == 1:
                    image = AsyncImage(source='./images/neon.png')
                    layout.add_widget(image)
                else:
                    image = AsyncImage(source='./images/black.png')
                    layout.add_widget(image)
        layout.add_widget(Player())
        return layout


window = NoPacMan()
window.run()
