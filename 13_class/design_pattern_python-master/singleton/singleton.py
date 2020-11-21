# -*- coding: utf-8 -*-


# class Singleton:
#     """ クラスのインスタンスが一つしか
#     生成されないこと保証するための仕組みの
#     デザインパターン

#     アプリケーション全体で、
#     絶対に１つにしないといけない
#     仕組みの実装に使用される。
#     """

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls, *args, **kwargs)

#         return cls._instance


class SingletonType(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(
                SingletonType, cls
            ).__call__(*args, **kwargs)

        return cls._instance


class TestClass(object):
    pass


class Singleton(object):
    __metaclass__ = SingletonType


obj = Singleton()

print(isinstance(TestClass, type))
print(obj)
