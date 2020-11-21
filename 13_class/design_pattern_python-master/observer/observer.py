# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import time


class AbstractObserver(metaclass=ABCMeta):

    """ observer abstract class """
    @abstractmethod
    def update(self, ganerator):
        pass

class DegitObserver(AbstractObserver):

    def update(self, generator):
        print('DigitObservser: {}'.format(
            generator.get_number()
        ))
        time.sleep(0.1)

class GraphObserver(AbstractObserver):

    def update(self, generator):
        count = generator.get_number()
        for _ in range(count):
            print('*', end='')
        print()
        time.sleep(0.1)
