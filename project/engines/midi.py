from project.engines.engine import AbstractEngine
from config import config
import mido

class MIDIEngine(AbstractEngine):
    def __init__(self):
        self.outport = mido.open_output(config.midi_channel())
        print(f'MIDI Engine initialized: {config.midi_channel()}')

    def handleMessage(self, splits):
        if splits[1] == 'n':
            self.outport.send(mido.Message('note_on', channel=10, note=20, velocity=127, time=1))
        elif splits[0] == 'c':
            self.outport.send(mido.Message('control_change', channel=0, control=122, value=int(splits[2]), time=0))

