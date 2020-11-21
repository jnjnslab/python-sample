# -*- coding: utf-8 -*-


def main():
    field_a = 5
    s1 = Singleton.get_instance(field_a)
    print(s1)
    s2 = Singleton.get_instance(field_a)
    print(s2)
    # print(s1 == s2)

    # print(s1._field_a)
    # print(s2._field_a)


class Singleton:
    _unique_instance = None

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls, field_a: int)->object:
        if not cls._unique_instance:
            # cls._unique_instance = cls()
            cls._unique_instance = cls.__internal_new__()
            cls._unique_instance.field_a = field_a

        return cls._unique_instance


if __name__ == "__main__":
    main()
