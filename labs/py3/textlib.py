class BodyOfText:
    def __init__(self, text):
        self.text = text

    def num_paragraphs(self):
        if '' == self.text:
            result = 0
        else:
            result = self.text.count('\n') + 1
        return result

    def paragraphs(self):
        if '' == self.text:
            result = []
        else:
            result = self.text.split('\n')
        return result

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
