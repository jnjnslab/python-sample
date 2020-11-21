from abc import ABCMeta, abstractmethod

#抽象クラス
class Animal(metaclass=ABCMeta):
    #抽象メソッド
    @abstractmethod
    def sound(self):
        pass
#抽象クラスを継承する
class Cat(Animal):
    #メソッドをオーバーライドする
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("Bow")


def output(animal):
    print(animal.__class__.__name__, end=": ")
    animal.sound()

#インスタンスの生成
c = Cat()
output(c)

d = Dog()
output(d)

