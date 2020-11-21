# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import random


class AbstractNumberGenerator(metaclass=ABCMeta):
    """generate number abstract class """

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self):
        for o in self.__observers:
            o.update(self)



    @abstractmethod
    def get_number(self) -> int:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass


class RandomNumberGenerator(AbstractNumberGenerator):
    """ generate number class """

    def __init__(self):
        super(RandomNumberGenerator, self).__init__()
        self.number = 0

    def get_number(self):
        return self.number

    def execute(self):
        for _ in range(20):
            self.number = random.randint(0, 49)
            self.notify_observer()
