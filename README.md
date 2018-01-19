# JapaneseVerbPractice
This is a python script that helps myself practicing Japanese verb conjugation.

Japanese verbs can represent different states (tense, voice, and
politeness), they are the essential part of a sentence.

However, there are too many verbs, and different conjugation forms have
different conjugation rules. Memorizing Japanese verbs are regard as the
most challenging part for the beginners.

This script may also helpful for other Japanese beginners (especially Chinese)
to practice Japanese verb conjugation.

*Note: All conjugations are based on 基本形 (or 字典形, Dictionary-form).* 
**This script is wrote on Linux system base on Python 2.7.**

## Usage
1. Clone this repository to your local machine
2. Enter the script main directory
3. Run: python jvp.py
    * Enter answers to the questions jumped out

*Japanese input on terminal are required*

## Current available verbs and conjugation forms
The verbs come form the file: 'Japanese\_verb\_base.jvp'. Currently, this file 
contains verb form the text book "标准日本语初级上册". I will add the verbs in
other books when I learned more.

The conjugation forms (or types) come form the file: 'Japanese\_verb\_form.jvp'.
Current supported conjugation include: 基本形 -> (ます形，て形, た形, ない形，
意志形，命令形, 假定形, 可能态, 使役态, 被动态, 被动使役态).

## To do list
- [x] Add error history records. Increase the practice time of the verbs that
user made mistake.
- [  ] Find voice resources of the verbs, play the voice when the question
jumps out. Add listening practice.
