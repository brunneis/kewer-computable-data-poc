#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kewer import Kernel, Drawer


class WordCount(Kernel):
    def setup(self):
        self.wordcount = dict()

    def add_word_occurrence(self, word):
        if word in self.wordcount:
            self.wordcount[word] += 1
            return
        self.wordcount[word] = 1

    def transform(self, value):
        tweet = value['body']
        for word in tweet.split():
            if len(word) <= Drawer.MAX_KEY_LENGTH:
                self.add_word_occurrence(word)

    def finish(self):
        drawer = Drawer()
        sorted_wordcount = sorted(((v, k) for k, v in self.wordcount.items()), reverse=True)

        compartment_counter = 0
        for value, key in sorted_wordcount:
            if compartment_counter == 100:
                break
            drawer.add_compartment(key, value)
            compartment_counter += 1
        return drawer