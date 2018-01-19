# usr/bin/evn python
# -*- coding:utf-8 -*-

import os
from sys import version_info
import numpy as np
import pandas as pd
import random
import csv

hiragana_array = np.array([
    ['あ', 'い', 'う', 'え', 'お'],
    ['か', 'き', 'く', 'け', 'こ'],
    ['さ', 'し', 'す', 'せ', 'そ'],
    ['た', 'ち', 'つ', 'て', 'と'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ま', 'み', 'む', 'め', 'も'],
    ['や', 'い', 'ゆ', 'え', 'よ'],
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['わ', 'い', 'う', 'え', 'を'],
    ['が', 'ぎ', 'ぐ', 'げ', 'ご'],
    ['ざ', 'じ', 'ず', 'ぜ', 'ぞ'],
    ['だ', 'ぢ', 'づ', 'で', 'ど'],
    ['ば', 'び', 'ぶ', 'べ', 'ぼ'],
    ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']
])

hiragana_table = pd.DataFrame(hiragana_array, index=['a', 'k', 's', 't', 'n', \
                                                     'h', 'm', 'y', 'r', 'w', \
                                                     'g', 'z', 'd', 'b', 'p'],
                              columns=['a', 'i', 'u', 'e', 'o'])

speacial_v1 = ('帰る', '滑る', '入る', '切る', '知る', '要る', '走る', '減る')

class Hiragana(object):
    '''
    Class hiranaga
    '''
    def __init__(self, hiragana):
        self.hiragana = hiragana
        self.vowel = None
        self.consonant = None

    def get_vowel(self):
        '''
        Get the vowel of the hiragana
        '''
        self.vowel = None
        if self.hiragana in list(hiragana_table['a']):
            self.vowel = 'あ'
        if self.hiragana in list(hiragana_table['i']):
            self.vowel = 'い'
        if self.hiragana in list(hiragana_table['u']):
            self.vowel = 'う'
        if self.hiragana in list(hiragana_table['e']):
            self.vowel = 'え'
        if self.hiragana in list(hiragana_table['o']):
            self.vowel = 'お'
        if self.vowel == None:
            errormessage = ''.join(['hiragana: ', self.hiragana, ' not found!'])
            raise ValueError(errormessage)

    def get_consonant(self):
        self.consonant = None
        if self.hiragana in ('い', 'う', 'え'):
            self.consonant = 'a'
        else:
            for index in hiragana_table.index.values:
                if self.hiragana in list(hiragana_table.loc[index, :]):
                    self.consonant = index
        if self.consonant == None:
            raise ValueError('Something wrong')

    def change_vowel(self, vowel):
        self.get_consonant()
        self.hiragana = hiragana_table.loc[self.consonant, vowel]


class Verb(object):
    '''
    Class Verb
    '''
    def __init__(self, verb_base, verb_kanji, verb_form):
        self.level = None
        self.verb_base = verb_base
        self.verb_form = verb_form
        if verb_kanji == 'None':
            self.verb_kanji = None
        else:
            self.verb_kanji = verb_kanji
        self.verb_type = None
        self.right_answer = []
        self.error_flag = False
        self.user_answer = None
        if self.verb_kanji != None and isinstance(self.verb_kanji, str):
            self.has_kanji = True
        else:
            self.has_kanji = False

    def __str__(self):
        '''
        Print the verb base, form  and right answer
        '''
        message = None
        verb_content = ''
        if self.has_kanji:
            verb_content = self.verb_kanji + ' (' + self.verb_base + ')'
        else:
            verb_content = self.verb_base
        right_answer = '[]'
        if self.right_answer != None:
            right_answer = '['
            for i, answer in enumerate(self.right_answer):
                if i == 0:
                    right_answer = ' '.join([right_answer, answer])
                else:
                    right_answer = ' '.join([right_answer, 'or', answer])
            right_answer = ''.join([right_answer, ']'])
        message = ''.join(['verb: ', verb_content, \
                           ', required form: ', self.verb_form, \
                           ', right answer: ', right_answer])
        return message

    def get_right_answer(self):
        '''
        Get the right_answer according to the base and form
        '''
        self.get_verb_type()
        if self.verb_form == 'ます':
            self.turn_to_masu()
            return
        if self.verb_form == 'て':
            self.turn_to_te()
            return
        if self.verb_form == 'た':
            self.turn_to_ta()
            return
        if self.verb_form == 'ない':
            self.turn_to_nai()
            return
        if self.verb_form == '意志':
            self.turn_to_yizhi()
            return
        raise ValueError('Unsupported form')

    def turn_to_masu(self):
        '''
        Turn a verb into ます形 (masu type)
        '''
        if self.verb_type == 1:
            last_hira = self.verb_base[-3:]
            hira = Hiragana(last_hira)
            hira.change_vowel('i')
            hira_answer = self.verb_base[0:-3] + hira.hiragana + 'ます'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + hira.hiragana + 'ます'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 2:
            hira_answer = self.verb_base[0:-3] + 'ます'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + 'ます'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 3:
            last_second_hira = self.verb_base[-6:-3]
            hira = Hiragana(last_second_hira)
            hira.change_vowel('i')
            hira_answer = hira.hiragana + 'ます'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3]+ 'ます'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)

    def turn_to_te(self):
        '''
        Turn the verb into て形 (te type)
        '''
        if self.verb_type == 1:
            append_item = ''
            if self.verb_base[-3:] in ('う', 'つ', 'る'):
                append_item = 'って'
            if self.verb_base[-3:] in ('ぶ', 'む', 'ぬ'):
                append_item = 'んで'
            if self.verb_base[-3:] == 'く':
                append_item = 'いて'
            if self.verb_base[-3:] == 'ぐ':
                append_item = 'いで'
            if self.verb_base[-3:] == 'す':
                append_item = 'して'

            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + append_item
                if self.verb_kanji == '行く':
                    kanji_answer = '行って'
                self.right_answer.append(kanji_answer)
            hira_answer = self.verb_base[0:-3] + append_item
            if self.verb_base == 'いく':
                hira_answer = 'いって'
            self.right_answer.append(hira_answer)

        if self.verb_type == 2:
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + 'て'
                self.right_answer.append(kanji_answer)
            hira_answer = self.verb_base[0:-3] + 'て'
            self.right_answer.append(hira_answer)

        if self.verb_type == 3:
            if self.verb_base == 'くる':
                self.right_answer.append('来て')
                self.right_answer.append('きて')
            if self.verb_base == 'する':
                self.right_answer.append('して')

    def turn_to_ta(self):
        '''
        Turn a verb into た形 (ta type)
        '''
        if self.verb_type == 1:
            append_item = ''
            if self.verb_base[-3:] in ('う', 'つ', 'る'):
                append_item = 'った'
            if self.verb_base[-3:] in ('ぶ', 'む', 'ぬ'):
                append_item = 'んだ'
            if self.verb_base[-3:] == 'く':
                append_item = 'いた'
            if self.verb_base[-3:] == 'ぐ':
                append_item = 'いだ'
            if self.verb_base[-3:] == 'す':
                append_item = 'した'

            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + append_item
                if self.verb_kanji == '行く':
                    kanji_answer = '行った'
                self.right_answer.append(kanji_answer)
            hira_answer = self.verb_base[0:-3] + append_item
            if self.verb_base == 'いく':
                hira_answer = 'いった'
            self.right_answer.append(hira_answer)

        if self.verb_type == 2:
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + 'た'
                self.right_answer.append(kanji_answer)
            hira_answer = self.verb_base[0:-3] + 'た'
            self.right_answer.append(hira_answer)

        if self.verb_type == 3:
            if self.verb_base == 'くる':
                self.right_answer.append('来た')
                self.right_answer.append('きた')
            if self.verb_base == 'する':
                self.right_answer.append('した')

    def turn_to_nai(self):
        '''
        Turn a verb into ない形 (nai type)
        '''
        if self.verb_type == 1:
            last_hira = self.verb_base[-3:]
            hira = Hiragana(last_hira)
            hira.change_vowel('a')
            if hira.hiragana == 'あ':
                hira.hiragana = 'わ'
            hira_answer = self.verb_base[0:-3] + hira.hiragana + 'ない'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + hira.hiragana + 'ない'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 2:
            hira_answer = self.verb_base[0:-3] + 'ない'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + 'ない'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 3:
            if self.verb_base == 'くる':
                self.right_answer.append('来ない')
                self.right_answer.append('こない')
            if self.verb_base == 'する':
                self.right_answer.append('しない')

    def turn_to_yizhi(self):
        '''
        Turn a verb into 意志形
        '''
        if self.verb_type == 1:
            last_hira = self.verb_base[-3:]
            hira = Hiragana(last_hira)
            hira.change_vowel('o')
            hira_answer = self.verb_base[0:-3] + hira.hiragana + 'う'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + hira.hiragana + 'う'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 2:
            hira_answer = self.verb_base[0:-3] + 'よう'
            if self.has_kanji:
                kanji_answer = self.verb_kanji[0:-3] + 'よう'
                self.right_answer.append(kanji_answer)
            self.right_answer.append(hira_answer)
        if self.verb_type == 3:
            if self.verb_base == 'くる':
                self.right_answer.append('来よう')
                self.right_answer.append('こよう')
            if self.verb_base == 'する':
                self.right_answer.append('しよう')

    def get_verb_type(self):
        '''
        Calculate the verb type
        1: 动1, v1
        2: 动2, v2
        3: 动3, v3
        '''
        if self.verb_base in ('する', 'くる'):
            self.verb_type = 3
        else:
            last_hira = self.verb_base[-3:]
            if last_hira != 'る':
                self.verb_type = 1
            else:
                last_2nd_hira = self.verb_base[-6:-3]
                hira = Hiragana(last_2nd_hira)
                hira.get_vowel()
                if hira.vowel in ('う', 'あ', 'お' ):
                    self.verb_type = 1
                else:
                    if self.verb_kanji in speacial_v1:
                        self.verb_type = 1
                    else:
                        self.verb_type = 2

    def check_answer(self):
        '''
        Check the user_answer with the right_answer, and set the error flag
        '''
        if self.user_answer in self.right_answer:
            self.error_flag = False
        else:
            self.error_flag = True
            right_answer = '[]'
            if self.right_answer:
                right_answer = '['
                for i, answer in enumerate(self.right_answer):
                    if i == 0:
                        right_answer = ' '.join([right_answer, answer])
                    else:
                        right_answer = ' '.join([right_answer, 'or', answer])
                right_answer = ''.join([right_answer, ']'])
            errormessage = ''.join(['Wrong answer! Correct answer: ', right_answer])
            print errormessage

    def get_user_answer(self):
        '''
        Give the quiz information, and then get the user answer
        '''
        if self.has_kanji:
            message = ''.join(['\nPlease enter the ', self.verb_form, '形 of ',\
                               self.verb_kanji, ' (', self.verb_base, '): '])
        else:
            message = ''.join(['\nPlease enter the ', self.verb_form, '形 of ',\
                               self.verb_base, ': '])
        self.user_answer = get_input(message)


class Practice(object):
    '''
    Class Practice
    '''

    def __init__(self):
        self.total_quiz_number = 0
        self.verbs = []
        self.verbs_base_avail = None
        self.verbs_kanji_avail = None
        self.verbs_form_avail = None
        self.verbs_error = None
        self.current_quiz_number = 0
        self.practice_history = None
        self.initial()

    def initial(self):
        '''
        Initial the quiz
        '''
        self.read_verb_lib()
        self.read_form_lib()
        self.load_practice_history()

    def load_practice_history(self):
        '''
        Load practice history. If there isn't a history, set up one
        '''
        total_verbs_base = len(self.verbs_base_avail)
        total_verbs_form = len(self.verbs_form_avail)
        total_avail_verbs_number = total_verbs_base * total_verbs_form
        # check whether the file exist
        history_file = 'practice_history.csv'
        history_exist = os.path.isfile(history_file)
        if history_exist:
            practice_history = pd.read_csv(history_file, index_col=0)
            # all available in practice history?
            for i in range(total_verbs_base):
                if self.verbs_base_avail[i] not in \
                        set(practice_history['verb_base'].tolist()):
                    # add the verb
                    for form in set(practice_history['verb_form'].tolist()):
                        practice_history = practice_history.append(
                            {'verb_base': self.verbs_base_avail[i],
                             'verb_kanji': self.verbs_kanji_avail[i],
                             'verb_form' : form,
                             'sample_time': 0,
                             'error_time': 0,
                             'right_time': 0,
                             'continue_error_time': 0,
                             'continue_right_time': 0,
                             'relative_weight': 3.0}, ignore_index=True)
            for form in self.verbs_form_avail:
                if form not in set(practice_history['verb_form'].tolist()):
                    # add the form
                    for j in range(total_verbs_base):
                        practice_history = practice_history.append(
                            {'verb_base': self.verbs_base_avail[j],
                             'verb_kanji': self.verbs_kanji_avail[j],
                             'verb_form' : form,
                             'sample_time': 0,
                             'error_time': 0,
                             'right_time': 0,
                             'continue_error_time': 0,
                             'continue_right_time': 0,
                             'relative_weight': 3.0}, ignore_index=True)
            self.practice_history = practice_history
            #print self.practice_history
        else:
            # initial the practice history
            history_array = np.empty(shape=(total_avail_verbs_number, 9),
                                     dtype=object)
            # set up the dictionary of the verbs
            for i in range(total_verbs_base):
                for j in range(total_verbs_form):
                    verb = Verb(self.verbs_base_avail[i],
                                self.verbs_kanji_avail[i],
                                self.verbs_form_avail[j])
                    history_array[i*total_verbs_form + j] = \
                        [verb.verb_base, verb.verb_kanji, verb.verb_form, 0, \
                         0, 0, 0, 0, 1.0]
            # put the data into dataframe
            self.practice_history = pd.DataFrame(data=history_array,
                                                 columns = ['verb_base',
                                                            'verb_kanji',
                                                            'verb_form',
                                                            'sample_time',
                                                            'error_time',
                                                            'right_time',
                                                            'continue_error_time',
                                                            'continue_right_time',
                                                            'relative_weight'])

    def sample_verb(self):
        '''
        Choose a verb according to the sample history
        '''
        index = biased_verb_sample(self.practice_history['relative_weight'].tolist())
        verb_base = self.practice_history.loc[index, 'verb_base']
        verb_kanji = self.practice_history.loc[index, 'verb_kanji']
        verb_form = self.practice_history.loc[index, 'verb_form']
        verb = Verb(verb_base, verb_kanji, verb_form)
        self.verbs.append(verb)
        return verb

    def read_verb_lib(self):
        '''
        Read the verbs lib, choose verb from that
        '''
        self.verbs_base_avail = []
        self.verbs_kanji_avail = []
        with open('Japanese_verb_base.jvp') as f:
            for line in f:
                if line.strip():
                    line = line.strip()
                    verb_base_kanji = line.split()
                    self.verbs_base_avail.append(verb_base_kanji[0])
                    self.verbs_kanji_avail.append(verb_base_kanji[1])

    def read_form_lib(self):
        '''
        Read the form lib
        '''
        self.verbs_form_avail = []
        with open('Japanese_verb_form.jvp') as f:
            for line in f:
                if line.strip():
                    verb_form = line.strip()
                    self.verbs_form_avail.append(verb_form)

    def perform_quiz(self):
        '''
        Perform quiz
        Give quiz info, ask user input answer
        Check answer and record
        '''
        total_quiz_number_help_info = 'How many verb do you want to practice? \
Please enter a int number: '
        input_string = get_input(total_quiz_number_help_info)
        input_string = input_string.strip()
        self.total_quiz_number = int(input_string)
        for i in range(self.total_quiz_number):
            verb = self.sample_verb()
            verb.get_user_answer()
            verb.get_right_answer()
            verb.check_answer()
            self.record(verb)

    def record(self, verb):
        '''
        Record the practice history, include sample_time, error_time,
        right_time, continue_error_time, continue_right_time,
        relative_weight
        '''
        # Find the index of the verb
        index = self.find_verb_in_practice_history(verb)
        self.practice_history.loc[index, 'sample_time'] += 1
        if verb.error_flag:
            self.practice_history.loc[index, 'error_time'] += 1
            self.practice_history.loc[index, 'continue_error_time'] += 1
            self.practice_history.loc[index, 'continue_right_time'] = 0
        else:
            self.practice_history.loc[index, 'right_time'] += 1
            self.practice_history.loc[index, 'continue_right_time'] += 1
            if self.practice_history.loc[index, 'continue_right_time'] > 5:
                self.practice_history.loc[index, 'continue_right_time'] = 0
                self.practice_history.loc[index, 'error_time'] = 0
            self.practice_history.loc[index, 'continue_error_time'] = 0
        # calculate the relative weight
        # relative_weight = [1 +(5*continue_error_time) + (3*error_time)] /
        #                   [ 1 + sample_time + right_time + 2*continue_right_time]
        self.practice_history.loc[index, 'relative_weight'] = \
            (1.0 + self.practice_history.loc[index, 'error_time'] * 3.0 +
             self.practice_history.loc[index, 'continue_error_time'] * 5.0) / \
            (1.0 + self.practice_history.loc[index, 'sample_time'] +
             self.practice_history.loc[index, 'right_time'] +
             self.practice_history.loc[index, 'continue_right_time'] * 2)
        self.practice_history.to_csv('practice_history.csv')

    def find_verb_in_practice_history(self, verb):
        '''
        Find the verb in the practice history
        return the index number
        '''
        found_index = []
        verb_index = self.practice_history.verb_base[
            self.practice_history.verb_base == verb.verb_base].index.tolist()
        form_index = self.practice_history.verb_form[
            self.practice_history.verb_form == verb.verb_form].index.tolist()
        kanji_index = self.practice_history.verb_kanji[
            self.practice_history.verb_kanji == verb.verb_kanji].index.tolist()
        if verb.has_kanji:
            found_index = list(set.intersection(set(verb_index), set(form_index),
                                                set(kanji_index)))
        else:
            base_form_index = list(set.intersection(set(verb_index), set(form_index)))
            for index in base_form_index:
                if not isinstance(self.practice_history.verb_kanji[index], str):
                    found_index.append(index)

        if len(found_index) == 1:
            index = found_index[0]
            return index
        else:
            if verb.has_kanji:
                errormessage = ''.join(['Found more than one verb:', verb.verb_base,
                                        verb.verb_kanji, '的', verb.verb_form,
                                        '形 in practice_history!'])
            else:
                errormessage = ''.join(['Found more than one verb:', verb.verb_base,
                                        '的', verb.verb_form,
                                        '形 in practice_history!'])
            print found_index
            raise ValueError(errormessage)
            return -1


# Random-number sampling using the Walker-Vose alias method,
# Copyright: Joachim Wuttke, Forschungszentrum Juelich GmbH (2013)
# M. D. Vose, IEEE T. Software Eng. 17, 972 (1991)
# A. J. Walker, Electronics Letters 10, 127 (1974); ACM TOMS 3, 253 (1977)
class AliasTable(object):
    '''
    Class AliasTable
    '''
    def __init__(self, pdf):
        self.p = pdf[:]
        self.alias = None
        self.prob = None
        self.calc_alias()

    def calc_alias(self):
        n = len(self.p)
        self.prob = [0.0] * n
        self.alias = [0] * n
        small = [0.0] * n
        large = [0.0] * n
        for i in range(n):
            self.p[i] *= n

         # Set separate index lists for small and large probabilities:
        n_s, n_l = 0, 0
        for i in range(n-1, -1, -1):
            if self.p[i] < 1:
                small[n_s] = i
                n_s += 1
            else:
               large[n_l] = i
               n_l += 1

        # Work through index lists
        while n_s and n_l:
            n_s -= 1
            a = small[n_s]
            n_l -= 1
            g = large[n_l]
            self.prob[a] = self.p[a]
            self.alias[a] = g
            self.p[g] = self.p[g] + self.p[a] - 1
            if self.p[g] < 1:
                small[n_s] = g
                n_s += 1
            else:
                large[n_l] = g
                n_l += 1

        while n_l:
            n_l -= 1
            self.prob[large[n_l]] = 1

        while n_s:
          # can only happen through numeric instability
            n_s -= 1
            self.prob[small[n_s] ] = 1;

    def sample_pdf(self):
        rand1 = random.random()
        rand2 = random.random()
        i = int(len(self.p) * rand1)
        if rand2 < self.prob[i]:
            return i
        else:
            return self.alias[i]

def get_input(info):
    '''
    Get information from terminal input
    '''
    reponse = None
    py3 = version_info[0] > 3
    if py3:
        response = input(info)
    else:
        response = raw_input(info)
    return response

def biased_verb_sample(p):
    '''
    Uniformly sample a entity from a list
    '''
    # normalize p
    sum_p = 0.0
    for i in range(len(p)):
        sum_p += p[i]
    for i in range(len(p)):
        p[i] = p[i] / sum_p
    at = AliasTable(p)
    index = at.sample_pdf()
    #index = int(random.random() * len(l))
    return index

if __name__ == '__main__':
    practice = Practice()
    practice.perform_quiz()
