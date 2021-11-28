import time
from config import config
from pythonosc import udp_client


class OSC:
    def __init__(self):
        self.client = udp_client.SimpleUDPClient(config.osc_ip(), config.osc_port())

    
    def command(self, name, param):
        cmd = '/Hydrogen/' + name
        print(cmd + "param: " + str(param))
        self.client.send_message(cmd, int(param))



# /Hydrogen/STRIP_VOLUME_ABSOLUTE/
# /Hydrogen/PAN_ABSOLUTE/
# /Hydrogen/FILTER_CUTOFF_LEVEL_ABSOLUTE/
# /Hydrogen/STRIP_MUTE_TOGGLE/
# /Hydrogen/STRIP_SOLO_TOGGLE/
# /Hydrogen/PLAY
# /Hydrogen/PLAY_STOP_TOGGLE
# /Hydrogen/PLAY_PAUSE_TOGGLE
# /Hydrogen/STOP
# /Hydrogen/PAUSE
# /Hydrogen/RECORD_READY
# /Hydrogen/RECORD_STROBE
# /Hydrogen/RECORD_STROBE_TOGGLE
# /Hydrogen/RECORD_EXIT
# /Hydrogen/MUTE
# /Hydrogen/MUTE_TOGGLE
# /Hydrogen/UNMUTE
# /Hydrogen/NEXT_BAR
# /Hydrogen/PREVIOUS_BAR
# /Hydrogen/BPM_INCR
# /Hydrogen/BPM_DECR
# /Hydrogen/MASTER_VOLUME_ABSOLUTE
# /Hydrogen/MASTER_VOLUME_RELATIVE
# /Hydrogen/STRIP_VOLUME_RELATIVE
# /Hydrogen/SELECT_NEXT_PATTERN
# /Hydrogen/SELECT_NEXT_PATTERN_PROMPTLY
# /Hydrogen/SELECT_AND_PLAY_NEXT_PATTERN
# /Hydrogen/BEATCOUNTER
# /Hydrogen/TAP_TEMPO
# /Hydrogen/PLAYLIST_SONG
# /Hydrogen/PLAYLIST_NEXT_SONG
# /Hydrogen/PLAYLIST_PREV_SONG
# /Hydrogen/TOGGLE_METRONOME
# /Hydrogen/SELECT_INSTRUMENT
# /Hydrogen/UNDO_ACTION
# /Hydrogen/REDO_ACTION
