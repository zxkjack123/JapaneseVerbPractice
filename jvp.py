# usr/bin/evn python
# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class JapaneseVerbPractice(Widget):
    pass


class JVPApp(App):
    def build(self):
        return JapaneseVerbPractice()

textinput = TextInput(text='Hello world')

if __name__ == '__main__':
    JVPApp().run()
