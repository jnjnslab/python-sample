# -*- coding: utf-8 -*-

from generator import RandomNumberGenerator
from observer import DegitObserver, GraphObserver

def main():
    generator = RandomNumberGenerator()

    degit_observer = DegitObserver()
    graph_observer = GraphObserver()

    generator.add_observer(degit_observer)
    generator.add_observer(graph_observer)

    generator.execute()

if __name__ == '__main__':
    main()
