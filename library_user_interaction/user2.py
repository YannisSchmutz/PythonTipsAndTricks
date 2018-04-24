#!/usr/bin/python3

from myLibrary2 import Base


class ValidTest(Base):
    def bar(self):
        return 'bar'


class InvalidTest(Base):
    def not_bar(self):
        return 'not_bar'