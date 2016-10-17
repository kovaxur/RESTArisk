import configparser
import os

class Settings:
    config = None
    def __init__(self):
        pass

    @classmethod
    def initConfig(cls):
        cls.config = configparser.ConfigParser()
        cls.config.read("RESTArisk/settings.ini")


    @classmethod
    def getConfigValue(cls,section,key):
        return cls.config.get(section,key)