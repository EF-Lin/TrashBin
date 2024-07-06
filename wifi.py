import pywifi
import time


def disconnect():
    interface = pywifi.PyWiFi().interfaces()[0]
    interface.disconnect()
    if interface.status() == pywifi.const.IFACE_DISCONNECTED:
        prof = pywifi.Profile()
        prof.auth = pywifi.const.AUTH_ALG_OPEN
        print(prof.auth)


if __name__ == '__main__':
    disconnect()
