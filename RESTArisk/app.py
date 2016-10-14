import sys

class App:

    def __init__(self):
        sys.path.append('modules')
        print("Cica")
        from webApp import WebApp