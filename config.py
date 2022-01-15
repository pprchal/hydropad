import configparser

class config():
    @classmethod
    def engine(cls):
        return conf['DEFAULT']['Engine']

    @classmethod
    def osc_ip(cls):
        return conf['DEFAULT']['OSC_IP']
  
    @classmethod
    def osc_port(cls):
        return conf['DEFAULT'].getint('OSC_Port')

    @classmethod
    def midi_channel(cls):
        return conf['DEFAULT']['MIDI_Port']

    @classmethod
    def server_name(cls):
        return conf['DEFAULT']['ServerName']

    @classmethod
    def server_port(cls):
        return conf['DEFAULT'].getint('ServerPort')


conf = configparser.ConfigParser()
conf.read('hydropad.ini')
