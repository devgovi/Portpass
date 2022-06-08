import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label




class PortpassApp(App):
    def build(self):
        return Label(text='Hello World')


if __name__ == '__main__':
    PortpassApp().run()