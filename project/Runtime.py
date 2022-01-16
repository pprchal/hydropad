from project.Config import Config
from project.engines.OSCEngine import OSCEngine
from project.engines.MIDIEngine import MIDIEngine


class Runtime():
    engine = None

    @classmethod
    def get_engine(cls):
        return cls.engine

    @classmethod
    def init_engine(cls):
        if Config.engine() == "OSC":
            cls.engine = OSCEngine()
        else:
            cls.engine = MIDIEngine()        