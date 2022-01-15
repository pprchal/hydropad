from project.engines.engine import AbstractEngine
from config import config
import mido

class MIDIEngine(AbstractEngine):
    def __init__(self):
        self.outport = mido.open_output(config.midi_channel())
        print(f'MIDI Engine initialized: {config.midi_channel()}')

    def executeCommand(self, splits):
        if len(splits) == 3:
            command = splits[2].upper()
            self.command(command, 1)
        elif len(splits) == 4:
            command = splits[2].upper()
            param = splits[3].upper()
            self.command(command, param)

    def command(self, name, param):
        msg = mido.Message('control_change', channel=0, control=122, value=int(param), time=0)
        self.outport.send(msg)
        ## self.client.send_message(cmd, int(param))
