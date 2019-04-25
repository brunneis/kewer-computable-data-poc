#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kewer import Kernel, Drawer


class Count(Kernel):
    def setup(self):
        self.counter = 0

    def transform(self, value):
        self.counter += 1

    def finish(self):
        drawer = Drawer()
        drawer.add_compartment('count', self.counter)
        return drawer
