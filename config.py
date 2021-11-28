import configparser

class config():
    @classmethod
    def osc_ip(cls):
        return conf['DEFAULT']['OscIP']

    @classmethod
    def osc_port(cls):
        return conf['DEFAULT'].getint('OscPort')

    @classmethod
    def server_name(cls):
        return conf['DEFAULT']['ServerName']

    @classmethod
    def server_port(cls):
        return conf['DEFAULT'].getint('ServerPort')

conf = configparser.ConfigParser()
conf.read('hydropad.ini')
