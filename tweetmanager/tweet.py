import time

import datetime

class tweet():

    _author = ""

    _text = ""

    _age=datetime.datetime.now()

    def __init__(self, author, text):

        self._author=author

        self._text=text

        self._age=datetime.datetime.now()

    def get_author(self):

        return self._author

    def get_text(self):

        return self._text

    def get_age(self):

        now=datetime.datetime.now()
        time = now-self._age
        time = time.seconds
        seconds = ""
        
        if ( time > 60):

            time = time/60

            seconds = str(int(time)) + "m"

            if ( time > 60):

                seconds = str(time * 1 / 60) + "H"

        else:

            seconds = str(time) + "s"

        return seconds
