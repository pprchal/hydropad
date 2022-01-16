from project.engines.AbstractEngine import AbstractEngine
from project.Config import Config
import time
import mido

class MIDIEngine(AbstractEngine):
    midi_channel = 9

    def __init__(self):
        self.outport = mido.open_output(Config.midi_channel())
        print(f'MIDI Engine initialized: {Config.midi_channel()}')

    def handle_message(self, splits):
        note = 38
        
        if splits[1] == 'C2':
            note = 39
            
        if splits[0] == 'n':
            self.outport.send(mido.Message('note_on', channel=self.midi_channel, note=note, velocity=127, time = 200))
            time.sleep(0.2)
            self.outport.send(mido.Message('note_off', channel=self.midi_channel, note=note, velocity=0))
        elif splits[0] == 'c':
            self.outport.send(mido.Message('control_change', channel=0, control=122, value=int(splits[1]), time=0))


#  20:0   Note on                 9, note 38, velocity 127
#  20:0   Note off                9, note 38, velocity 0
