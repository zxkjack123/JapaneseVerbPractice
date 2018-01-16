# usr/bin/evn python
# -*- coding:utf-8 -*-

from nose.tools import *
from ..jvp import *

def hiragana_change_vowel_test():
    '''
    Test to change a hiragana to another vowel
    '''
    hira = Hiragana('か')
    # change vowel into 'i'
    hira.change_vowel('i')
    assert_equal(hira.hiragana, 'き')

    # change vowel into 'u'
    hira.change_vowel('u')
    assert_equal(hira.hiragana, 'く')

    # change vowel into 'e'
    hira.change_vowel('e')
    assert_equal(hira.hiragana, 'け')

    # change vowel into 'o'
    hira.change_vowel('o')
    assert_equal(hira.hiragana, 'こ')

def get_verb_type_test():
    '''
    Calculate the type of verb
    '''
    verb1 = Verb('かく', '書く', 'ます')
    verb1.get_verb_type()
    assert_equal(verb1.verb_type, 1)

    verb_s1 = Verb('きる', '切る', 'ます')
    verb_s1.get_verb_type()
    assert_equal(verb_s1.verb_type, 1)

    verb2 = Verb('みる', '見る', 'ます')
    verb2.get_verb_type()
    assert_equal(verb2.verb_type, 2)

    verb3 = Verb('くる', '来る', 'ます')
    verb3.get_verb_type()
    assert_equal(verb3.verb_type, 3)

def verb_trun_to_masu_test():
    '''
    Test convert a verb into ます形 (masu type)
    '''
    verb1 = Verb('かく', '書く', 'ます')
    verb1.get_right_answer()
    assert_equal(verb1.right_answer, ['書きます', 'かきます'])

    verb2 = Verb('みる', '見る', 'ます')
    verb2.get_right_answer()
    assert_equal(verb2.right_answer, ['見ます', 'みます'])

    verb3 = Verb('くる', '来る', 'ます')
    verb3.get_right_answer()
    assert_equal(verb3.right_answer, ['来ます', 'きます'])

def verb_turn_to_te_test():
    '''
    Test convert a verb into て形 (te type)
    '''
    verb1 = Verb('かく', '書く', 'て')
    verb1.get_right_answer()
    assert_equal(verb1.right_answer, ['書いて', 'かいて'])

    verb2 = Verb('みる', '見る', 'て')
    verb2.get_right_answer()
    assert_equal(verb2.right_answer, ['見て', 'みて'])

    verb3 = Verb('くる', '来る', 'て')
    verb3.get_right_answer()
    assert_equal(verb3.right_answer, ['来て', 'きて'])

def verb_turn_to_ta_test():
    '''
    Test convert a verb into た形 (ta type)
    '''
    verb1 = Verb('かく', '書く', 'た')
    verb1.get_right_answer()
    assert_equal(verb1.right_answer, ['書いた', 'かいた'])

    verb2 = Verb('みる', '見る', 'た')
    verb2.get_right_answer()
    assert_equal(verb2.right_answer, ['見た', 'みた'])

    verb3 = Verb('くる', '来る', 'た')
    verb3.get_right_answer()
    assert_equal(verb3.right_answer, ['来た', 'きた'])

def verb_turn_to_nai_test():
    '''
    Test convert a verb into ない形 (nai type)
    '''
    verb1 = Verb('かく', '書く', 'ない')
    verb1.get_right_answer()
    assert_equal(verb1.right_answer, ['書かない', 'かかない'])

    verb11 = Verb('うたう', '歌う', 'ない')
    verb11.get_right_answer()
    assert_equal(verb11.right_answer, ['歌わない', 'うたわない'])

    verb2 = Verb('みる', '見る', 'ない')
    verb2.get_right_answer()
    assert_equal(verb2.right_answer, ['見ない', 'みない'])

    verb3 = Verb('くる', '来る', 'ない')
    verb3.get_right_answer()
    assert_equal(verb3.right_answer, ['来ない', 'こない'])



