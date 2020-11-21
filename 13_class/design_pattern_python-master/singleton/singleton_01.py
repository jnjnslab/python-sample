# -*- coding: utf-8 -*-


def main():
    s1 = Singleton.get_instance()
    print(s1)
    s2 = Singleton.get_instance()
    print(s2)
    print(s1 == s2)

    print(s1._field_a)
    print(s2._field_a)


class Singleton:
    __instance = None

    def __init__(self):
        self._field_a = None

        if Singleton.__instance is not None:
            raise Exception('ERROR SINGLETON')
        else:
            print('インスタンスを作成しました。')
            self._field_a = 'field_a'
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()

        return Singleton.__instance


if __name__ == "__main__":
    main()
