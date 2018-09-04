import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):

    def test_empty_story(self):
        bot = BodyOfText('')
        self.assertEqual(0, bot.num_paragraphs())

    def test_single_paragraph(self):
        bot = BodyOfText('This is a short story. It has only one paragraph.')
        self.assertEqual(1, bot.num_paragraphs())

    def test_several_paragraphs(self):
        bot = BodyOfText('''1st paragraph.
        2nd paragraph.
        3rd paragraph.''')
        self.assertEqual(3, bot.num_paragraphs())

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
