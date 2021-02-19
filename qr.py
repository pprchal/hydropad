import pyqrcode

def printQR(hostName, serverPort):
    url = f'http://{hostName}:{str(serverPort)}'
    code = pyqrcode.create(url, error='L', version=27, mode='binary')
    # code.png('url.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return code.xbm(scale=5)


