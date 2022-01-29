from threading import Thread
import time
from project.engines.AbstractEngine import AbstractEngine
from project.Config import Config
from project.Queue import Queue
import mido

class MIDIProducer(Thread):
    def __init__(self, input):
        Thread.__init__(self)
        self.input = input

    # get messages from MIDI
    def run(self):
        for message in self.input:
            with Queue.cond:
                str_msg = mido.format_as_string(message)
                Queue.queue_message(str_msg)

    
class MIDIEngine(AbstractEngine):
    midi_channel = 9

    # open MIDI ports 
    def __init__(self):
        self.outport = mido.open_output(Config.midi_channel())
        self.producer_t = MIDIProducer(mido.open_input(Config.midi_channel()))
        self.producer_t.start()
        print(f'MIDI Engine initialized: {Config.midi_channel()}')

    def get_name(self):
        return "MIDI"

    # engine 
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
