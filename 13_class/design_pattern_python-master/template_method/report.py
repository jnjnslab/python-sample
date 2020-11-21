# -*- coding: utf-8 -*-
from template import AbstractReport


class HtmlReport(AbstractReport):

    def pprint(self):
        for text in self.text_list:
            print('<p>'+text+'</p>')

    def start(self):
        title = "<html><head>"
        title += "<title>"+self.title+"</title>"
        title += "</head><body>"
        print(title)

    def end(self):
        title = "</body></html>"
        print(title)


class PlaneTextReport(AbstractReport):
    
    def pprint(self):
        for text in self.text_list:
            print(text)

    def start(self):
        title = "**** #"+self.title+" ****"
        print(title)

    def end(self):
        pass
