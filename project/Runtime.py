from project.Config import Config
from project.engines.OSCEngine import OSCEngine
from project.engines.MIDIEngine import MIDIEngine

class Runtime():
    engines = []
    server = None

    @classmethod
    def get_engine(cls):
        return cls.engine

    @classmethod
    def init(cls):
        for engineDef in Config.engines().split(','):
            if engineDef == "OSC":
                cls.engines.append(OSCEngine())
            elif engineDef == "MIDI":
                cls.engines.append(MIDIEngine())

    @classmethod
    def handle_message_multiple(cls, split):
        for engine in  cls.engines:
            engine.handle_message(split)

    @classmethod 
    def get_server_ip(cls):
        return f"{Config.server_name()}:{Config.server_port()}"

    
