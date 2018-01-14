# usr/bin/evn python
# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, \
    BooleanProperty
from kivy.graphics import Color

class JapaneseVerbPractice(Widget):
    jvp_question = ObjectProperty(None)
    jvp_check = ObjectProperty(None)
    jvp_error = ObjectProperty(None)
    jvp_answer = ObjectProperty(None)
    total_question_number = NumericProperty(None)
    question_id = NumericProperty(0)
    initial_flag = BooleanProperty(True)

    def initial(self):
        self.jvp_initial.text = 'How many verbs do you want to practice?'
        self.jvp_answer.focus = True

    def generate_question(self):
        if self.question_id < self.total_question_number:
            self.question_id += 1
            self.jvp_question.text = ''.join([str(self.question_id), '/',
                                               str(self.total_question_number)])
            self.jvp_answer.text = ''
            #self.jvp_answer.focus = True
        else:
            self.jvp_question.text = ''
            self.jvp_initial.text = 'All quiz finished, wrong verbs are stored'
            return

    def check_answer(self):
        if self.initial_flag:
            self.total_question_number = int(self.jvp_answer.text)
            self.initial_flag = False
            self.jvp_initial.text = 'Move curse into input box to start quiz!'
            #self.refresh()
        else:
            answer_flag = False
            if answer_flag:
                self.jvp_check.text = 'O'
            else:
                self.jvp_check.text = 'X'
                self.show_error()

    def show_error(self):
        self.jvp_error.text = 'Right answer: X'

    def get_text(self):
        self.check_answer()

    def refresh(self):
        self.jvp_initial.text = ''
        self.generate_question()
        #self.jvp_answer.focus = True

class JVPApp(App):
    def build(self):
        jvp = JapaneseVerbPractice()
        jvp.initial()
        return jvp

if __name__ == '__main__':
    JVPApp().run()
